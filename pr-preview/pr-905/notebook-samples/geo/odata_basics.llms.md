# How to query CDSE Catalogue and download products

The following example shows how to interact with the catalogue and download EO data products for further processing. We will search for cloudless Sentinel-2 L1C products over Warsaw and create an RGB true color image form one of the products found in the catalogue.

### Import necessary Python modules

``` python
# HTTP requests
import requests

# JSON parser
import json

# XML parser
import xml.etree.ElementTree as ET

# system modules
import os
import re
import sys
import random

# data manipulation
import pandas as pd
import numpy as np

# image manipulation
import rasterio
import matplotlib.pyplot as plt
import matplotlib.image
from rasterio.windows import Window

# file manipulation
from pathlib import Path
```

#### Query the catalogue and get a list of products matching the search parameters

Refer to https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-collection-of-products

``` python
# base URL of the product catalogue
catalogue_odata_url = "https://catalogue.dataspace.copernicus.eu/odata/v1"

# search parameters
collection_name = "SENTINEL-2"
product_type = "S2MSI1C"
max_cloud_cover = 1
aoi = "POLYGON((20.888443 52.169721,21.124649 52.169721,21.124649 52.271099,20.888443 52.271099,20.888443 52.169721))"
search_period_start = "2023-06-01T00:00:00.000Z"
search_period_end = "2023-06-10T00:00:00.000Z"
```

#### Build and check the search query

``` python
search_query = f"{catalogue_odata_url}/Products?$filter=Collection/Name eq '{collection_name}' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq '{product_type}') and OData.CSC.Intersects(area=geography'SRID=4326;{aoi}') and ContentDate/Start gt {search_period_start} and ContentDate/Start lt {search_period_end}"

print(f"""\n{search_query.replace(' ', "%20")}\n""")
```


    https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'SENTINEL-2'%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'S2MSI1C')%20and%20OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((20.888443%2052.169721,21.124649%2052.169721,21.124649%2052.271099,20.888443%2052.271099,20.888443%2052.169721))')%20and%20ContentDate/Start%20gt%202023-06-01T00:00:00.000Z%20and%20ContentDate/Start%20lt%202023-06-10T00:00:00.000Z

#### Run the query and display the results

``` python
response = requests.get(search_query).json()
result = pd.DataFrame.from_dict(response["value"])

# print first 3 results
result.head(3)
```

|  | @odata.mediaContentType | Id | Name | ContentType | ContentLength | OriginDate | PublicationDate | ModificationDate | Online | EvictionDate | S3Path | Checksum | ContentDate | Footprint | GeoFootprint |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | application/octet-stream | adc9ef40-4231-446e-8265-65d85e07d743 | S2A_MSIL1C_20230606T095031_N0509_R079_T34UED_2... | application/octet-stream | 628718136 | 2023-06-06T14:45:40.192Z | 2023-06-06T14:55:34.488Z | 2023-06-07T01:31:17.153Z | True |  | /eodata/Sentinel-2/MSI/L1C/2023/06/06/S2A_MSIL... | \[{'Value': '84f6c8ca3a8dfd09b8ebdcfa9b061631',... | {'Start': '2023-06-06T09:50:31.025Z', 'End': '... | geography'SRID=4326;POLYGON ((22.4422542865043... | {'type': 'Polygon', 'coordinates': \[\[\[22.44225... |
| 1 | application/octet-stream | 7954a18c-5585-4880-a9c4-ef3bc9d8c6c6 | S2B_MSIL1C_20230601T094549_N0509_R079_T34UEC_2... | application/octet-stream | 270482371 | 2023-06-01T13:42:40.429Z | 2023-06-01T13:48:45.988Z | 2023-06-01T13:55:23.363Z | True |  | /eodata/Sentinel-2/MSI/L1C/2023/06/01/S2B_MSIL... | \[{'Value': 'de63c6f5614f01cc2b3e3265ab755fc8',... | {'Start': '2023-06-01T09:45:49.024Z', 'End': '... | geography'SRID=4326;POLYGON ((21.370763876953 ... | {'type': 'Polygon', 'coordinates': \[\[\[21.37076... |
| 2 | application/octet-stream | a0e9b43e-0638-4212-aee8-fb5cae2dffdf | S2B_MSIL1C_20230601T094549_N0509_R079_T34UDC_2... | application/octet-stream | 334240926 | 2023-06-01T13:50:41.383Z | 2023-06-01T14:00:19.601Z | 2023-06-01T14:02:33.827Z | True |  | /eodata/Sentinel-2/MSI/L1C/2023/06/01/S2B_MSIL... | \[{'Value': '5a1c9e1f6c40c2f8e13409d209d91581',... | {'Start': '2023-06-01T09:45:49.024Z', 'End': '... | geography'SRID=4326;POLYGON ((21.1416714490104... | {'type': 'Polygon', 'coordinates': \[\[\[21.14167... |

#### Add filtering by cloud coverage and repeat the query

``` python
search_query = f"{search_query} and Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value le {max_cloud_cover})"
print(f"""\n{search_query.replace(' ', "%20")}\n""")

response = requests.get(search_query).json()
result = pd.DataFrame.from_dict(response["value"])

# Print the first 3 results
result.head(3)
```


    https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'SENTINEL-2'%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'S2MSI1C')%20and%20OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((20.888443%2052.169721,21.124649%2052.169721,21.124649%2052.271099,20.888443%2052.271099,20.888443%2052.169721))')%20and%20ContentDate/Start%20gt%202023-06-01T00:00:00.000Z%20and%20ContentDate/Start%20lt%202023-06-10T00:00:00.000Z%20and%20Attributes/OData.CSC.DoubleAttribute/any(att:att/Name%20eq%20'cloudCover'%20and%20att/OData.CSC.DoubleAttribute/Value%20le%201)

|  | @odata.mediaContentType | Id | Name | ContentType | ContentLength | OriginDate | PublicationDate | ModificationDate | Online | EvictionDate | S3Path | Checksum | ContentDate | Footprint | GeoFootprint |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0 | application/octet-stream | 7954a18c-5585-4880-a9c4-ef3bc9d8c6c6 | S2B_MSIL1C_20230601T094549_N0509_R079_T34UEC_2... | application/octet-stream | 270482371 | 2023-06-01T13:42:40.429Z | 2023-06-01T13:48:45.988Z | 2023-06-01T13:55:23.363Z | True |  | /eodata/Sentinel-2/MSI/L1C/2023/06/01/S2B_MSIL... | \[{'Value': 'de63c6f5614f01cc2b3e3265ab755fc8',... | {'Start': '2023-06-01T09:45:49.024Z', 'End': '... | geography'SRID=4326;POLYGON ((21.370763876953 ... | {'type': 'Polygon', 'coordinates': \[\[\[21.37076... |
| 1 | application/octet-stream | a0e9b43e-0638-4212-aee8-fb5cae2dffdf | S2B_MSIL1C_20230601T094549_N0509_R079_T34UDC_2... | application/octet-stream | 334240926 | 2023-06-01T13:50:41.383Z | 2023-06-01T14:00:19.601Z | 2023-06-01T14:02:33.827Z | True |  | /eodata/Sentinel-2/MSI/L1C/2023/06/01/S2B_MSIL... | \[{'Value': '5a1c9e1f6c40c2f8e13409d209d91581',... | {'Start': '2023-06-01T09:45:49.024Z', 'End': '... | geography'SRID=4326;POLYGON ((21.1416714490104... | {'type': 'Polygon', 'coordinates': \[\[\[21.14167... |
| 2 | application/octet-stream | badf9949-313d-464a-869e-4c5add6eab5e | S2B_MSIL1C_20230601T094549_N0509_R079_T34UED_2... | application/octet-stream | 633935426 | 2023-06-01T13:54:41.204Z | 2023-06-01T14:05:13.794Z | 2023-06-01T14:05:31.433Z | True |  | /eodata/Sentinel-2/MSI/L1C/2023/06/01/S2B_MSIL... | \[{'Value': '76289c4e705a458eabbba4be5bb21780',... | {'Start': '2023-06-01T09:45:49.024Z', 'End': '... | geography'SRID=4326;POLYGON ((22.4484108895815... | {'type': 'Polygon', 'coordinates': \[\[\[22.44841... |

#### Authenticate your account to download files

``` python
# Provide CDSE account credentials - replace with your own data
import os

username = os.environ["CDSE_USERNAME"]
password = os.environ["CDSE_PASSWORD"]

# Get authentication token
import certifi

auth_server_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
data = {
    "client_id": "cdse-public",
    "grant_type": "password",
    "username": username,
    "password": password,
}

response = requests.post(auth_server_url, data=data, verify=True, allow_redirects=False)
access_token = json.loads(response.text)["access_token"]
```

#### Select the product and establish authenticated session

``` python
# Select identifier of the first product
product_identifier = result.iloc[0, 1]
product_name = result.iloc[0, 2]

# Establish session
session = requests.Session()
session.headers["Authorization"] = f"Bearer {access_token}"
```

#### Get manifest file

``` python
# Nodes() method lets us traverse the directory tree and retrieve single file from the product
url = f"{catalogue_odata_url}/Products({product_identifier})/Nodes({product_name})/Nodes(MTD_MSIL1C.xml)/$value"
response = session.get(url, allow_redirects=False)
while response.status_code in (301, 302, 303, 307):
    url = response.headers["Location"]
    response = session.get(url, allow_redirects=False)

file = session.get(url, verify=False, allow_redirects=True)

# Save the product in home directory
outfile = Path.home() / "MTD_MSIL1C.xml"
outfile.write_bytes(file.content)
```

    45819

#### Parse manifest file and get bands location

``` python
# Pass the path of the xml document
tree = ET.parse(str(outfile))
# get the parent tag
root = tree.getroot()

# Get the location of individual bands in Sentinel-2 granule
band_location = []
band_location.append(f"{product_name}/{root[0][0][12][0][0][1].text}.jp2".split("/"))
band_location.append(f"{product_name}/{root[0][0][12][0][0][2].text}.jp2".split("/"))
band_location.append(f"{product_name}/{root[0][0][12][0][0][3].text}.jp2".split("/"))
```

#### Download bands

``` python
# Build the url for each file using Nodes() method
bands = []
for band_file in band_location:
    url = f"{catalogue_odata_url}/Products({product_identifier})/Nodes({product_name})/Nodes({band_file[1]})/Nodes({band_file[2]})/Nodes({band_file[3]})/Nodes({band_file[4]})/$value"
    response = session.get(url, allow_redirects=False)
    while response.status_code in (301, 302, 303, 307):
        url = response.headers["Location"]
        response = session.get(url, allow_redirects=False)
    file = session.get(url, verify=False, allow_redirects=True)
    # Save the product in home directory
    outfile = Path.home() / band_file[4]
    outfile.write_bytes(file.content)
    bands.append(str(outfile))
    print("Saved:", band_file[4])
```

    Saved: T34UEC_20230601T094549_B02.jp2
    Saved: T34UEC_20230601T094549_B03.jp2
    Saved: T34UEC_20230601T094549_B04.jp2

#### Prepare cropped patch

``` python
%matplotlib inline

# Crop the images to random 1000x1000 patch
xsize, ysize = 1000, 1000
xoff, yoff, xmax, ymax = 0, 0, 0, 0
n = 2

for band_file in bands:
    full_band = rasterio.open(band_file, driver="JP2OpenJPEG")
    if xmax == 0:
        xmin, xmax = 0, full_band.width - xsize
    if ymax == 0:
        ymin, ymax = 0, full_band.height - ysize
    if xoff == 0:
        xoff, yoff = random.randint(xmin, xmax), random.randint(ymin, ymax)
    window = Window(xoff, yoff, xsize, ysize)
    transform = full_band.window_transform(window)
    profile = full_band.profile
    crs = full_band.crs
    profile.update({"height": xsize, "width": ysize, "transform": transform})
    with rasterio.open(
        f"{Path.home()}/patch_band_{n}.jp2", "w", **profile
    ) as patch_band:
        # Read the data from the window and write it to the output raster
        patch_band.write(full_band.read(window=window))
    print(f"Patch for band {n} created")
    n += 1
```

    Patch for band 2 created
    Patch for band 3 created
    Patch for band 4 created

#### Generate true color image

``` python
# Read the patch files
band2 = rasterio.open(f"{Path.home()}/patch_band_2.jp2", driver="JP2OpenJPEG")  # blue
band3 = rasterio.open(f"{Path.home()}/patch_band_3.jp2", driver="JP2OpenJPEG")  # green
band4 = rasterio.open(f"{Path.home()}/patch_band_4.jp2", driver="JP2OpenJPEG")  # red

red = band4.read(1)
green = band3.read(1)
blue = band2.read(1)

# Normalize the pixel values and apply gain
gain = 2
red_n = np.clip(red * gain / 10000, 0, 1)
green_n = np.clip(green * gain / 10000, 0, 1)
blue_n = np.clip(blue * gain / 10000, 0, 1)

# Create composite image
rgb_composite_n = np.dstack((red_n, green_n, blue_n))

# Display image
plt.imshow(rgb_composite_n)

# Save image to file
matplotlib.image.imsave(f"{Path.home()}/Sentinel2_true_color.jpeg", rgb_composite_n)
print("Saved as:", outfile)
```

    Saved as: /home/jovyan/T34UEC_20230601T094549_B04.jp2

![](odata_basics_files/figure-html/cell-13-output-2.png)

#### 

#### Explore the CDSE Documentation to learn more about the available APIs and services:

#### https://documentation.dataspace.copernicus.eu/Home.html
