# Usecase showcasing Regional Benchmarking service of Anomaly Identification

The openEO-based Regional Benchmarking service allows users to monitor crop growth on a specific field and compare it with similar fields in the region. This comparison helps determine if the field is performing better or worse than other fields, providing valuable insights for agricultural management.

In this example, we compared several fields within our area of interest with a similar crop type. The area of interest was derived using WFS from the DLV service, filtered by the crop type ‘Zomergerst’. However, users can use their polygons or parcels for comparison, provided they are of a similar crop type.

``` python
# importing necessary packages
import openeo
import requests
import json
import geopandas as gpd
from shapely.geometry import box
import folium
```

``` python
# Acquire more information about the service
service = "Anomaly_Detection"
namespace = "vito"

eoconn = openeo.connect("https://openeo.vito.be").authenticate_oidc()
eoconn.describe_process(service, namespace=namespace)
```

    Authenticated using refresh token.

As mentioned earlier, though, in this example, we used parcels from a WFS; these parameters are specific to them. User can use their polygons/parcels based on their requirements.

``` python
# Specific parameters
croptype = "Zomergerst"

# Bounding Box
west = 5.17
east = 5.3
south = 51.1
north = 52.246
```

``` python
# reading the json file (user can use this function if they have their features stored as json file)


def read_json_str(json_txt: str) -> dict:
    field = json.loads(json_txt)
    return field
```

## Parse the data

Here, we parsed WFS data from <https://lv.vlaanderen.be/en> to obtain parcels with their respective crop types.

``` python
# requesting data over a region for a specific crop type

url = f"https://geo.api.vlaanderen.be/Landbgebrperc/wfs?service=WFS&request=getfeature&cql_filter=LBLHFDTLT='{croptype}'&outputformat=json&typename=Lbgebrperc&SRSName=urn:x-ogc:def:crs:EPSG:4326"
req = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

wfs_request_url = (
    requests.Request("GET", url, headers={"User-Agent": "Mozilla/5.0"}).prepare().url
)
data = req.json()
```

Before proceeding, we want to ensure that the filtered data lies within the area of interest. The following cell includes a method to display the parsed data as a dataframe and on a map.

``` python
dataframe = gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:4326")
area = dataframe.to_crs(epsg=3857).area
dataframe = dataframe[area > 200]

# filter data within the bounding box
bbox = box(west, south, east, north)
dataframe = dataframe[dataframe.within(bbox)]

dataframe = dataframe.head()
# converting dataframe to geojson string
geojson_str = dataframe.to_json()

dataframe
```

|  | geometry | UIDN | OIDN | ALVID | HFDTLT | LBLHFDTLT | GEWASGROEP | PM | LBLPM |
|----|----|----|----|----|----|----|----|----|----|
| 10 | POLYGON ((5.29093 51.20048, 5.29086 51.20056, ... | 4367507 | 1523096 | 1860308032 | 322 | Zomergerst | Granen, zaden en peulvruchten |  |  |
| 44 | POLYGON ((5.18902 51.18327, 5.18902 51.18333, ... | 4701063 | 1578592 | 1968471924 | 322 | Zomergerst | Granen, zaden en peulvruchten |  |  |
| 99 | POLYGON ((5.17625 51.16141, 5.17624 51.16141, ... | 4736113 | 1401727 | 1748157137 | 322 | Zomergerst | Granen, zaden en peulvruchten |  |  |
| 140 | POLYGON ((5.29437 51.18630, 5.29466 51.18570, ... | 4720017 | 405396 | 423080654 | 322 | Zomergerst | Granen, zaden en peulvruchten |  |  |
| 145 | POLYGON ((5.24719 51.10475, 5.24698 51.10514, ... | 4721711 | 1643282 | 2077021994 | 322 | Zomergerst | Granen, zaden en peulvruchten |  |  |

``` python
# plot the polygons
map = folium.Map(tiles="OpenStreetMap", zoom_start=12, location=[51.243, 5.18])
points = folium.features.GeoJson(dataframe.to_crs("EPSG:4326").to_json())
map.add_child(points)
map.fit_bounds(map.get_bounds(), padding=(30, 30))
map
```

Make this Notebook Trusted to load map: File -\> Trust Notebook

## Apply Anomaly Detection service

``` python
# parameters mandatory for this openeo-based service
aoi = read_json_str(geojson_str)
date = ["2020-03-06", "2020-06-30"]

# accessing the openeo service
anomaly = eoconn.datacube_from_process(
    service, namespace=namespace, date=date, polygon=aoi
)
```

``` python
# synchronous download or batch process
anomaly.download("RegionalBenchmarking_AD.json")
```

The service calculates the CropSAR fAPAR curve for each field. It compares it with the regional average fAPAR curve, derived from comparable fields in the region during a given time period.

## Visualize and compare the final result

``` python
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

data_json = json.load(open("RegionalBenchmarking_AD.json", "r"))
```

``` python
figure(figsize=(18, 9), dpi=300)
for i in data_json:
    x_Axis = [key for key, value in data_json[i].items()]
    y_Axis = [value for key, value in data_json[i].items()]
    plt.plot(x_Axis, y_Axis, label=i)

ax = plt.gca()
n = 7  # Keeps every 7th label
[l.set_visible(False) for (i, l) in enumerate(ax.get_xticklabels()) if i % n != 0]
plt.xlabel("variable")
plt.xticks(rotation=90)
plt.ylabel("value")
plt.tight_layout()
plt.legend()
plt.show()
```

![](Anomaly_Detection_files/figure-html/cell-12-output-1.png)

Through the visualized curves, you can study the crop type behaviour of the field in comparison with the regional average.
