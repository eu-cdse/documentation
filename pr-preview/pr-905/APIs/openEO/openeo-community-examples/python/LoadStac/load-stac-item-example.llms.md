This notebook showcases how to use your own files on openEO by creating a stac item for it.

It’s content is as follows: 1. Getting an example GTiff file from openEO 2. Creating a stac item for the file 3. Using `load_stac` to load the file into openEO

*Note: This notebook creates a stac item for a result file from openEO for the sake of demonstration. In practice, openEO creates stac items for all files it produces. You can use these results directly in `load_stac`*

## 1. Create example GTiff

First we download a simple GTiff file containing ndvi data from an openEO provider.

We calculate the NDVI from the S2 bands for the month of June 2021 and download the result as a GTiff file.  
*Note: the `temporal_extend` can be set as “2021-06” without specifying the days. More info [here](https://open-eo.github.io/openeo-python-client/data_access.html#single-string-temporal-extents).*

``` python
import openeo
import pystac
from datetime import datetime
import rasterio
import rasterio.warp
from rasterio.plot import show
```

``` python
connection = openeo.connect("openeo.dataspace.copernicus.eu").authenticate_oidc()
```

    Authenticated using refresh token.

``` python
scl = connection.load_collection(
    "SENTINEL2_L2A",
    spatial_extent={"west": 5.0, "south": 51.2, "east": 5.1, "north": 51.3},
    temporal_extent="2021-06",
    bands=["SCL"],
    max_cloud_cover=95
)
cloud_mask = scl.process(
    "to_scl_dilation_mask",
    data=scl,
    kernel1_size=17, kernel2_size=77,
    mask1_values=[2, 4, 5, 6, 7],
    mask2_values=[3, 8, 9, 10, 11],
    erosion_kernel_size=3
)
collection = connection.load_collection(
    "SENTINEL2_L2A",
    spatial_extent={"west": 5.0, "south": 51.2, "east": 5.1, "north": 51.3},
    temporal_extent="2021-06",
    bands=["B04", "B08"],
    max_cloud_cover=95
)
collection = collection.mask(cloud_mask)
collection = collection.ndvi(red="B04",nir="B08", target_band="NDVI-band").filter_bands("NDVI-band")
collection = collection.reduce_temporal("mean")
ndvi_job = collection.create_job(title="NDVI", out_format="GTiff")
ndvi_job.start_and_wait().get_results().download_file("ndvi-file.tif")
```

    0:00:00 Job 'j-240430fa4ef14b43838af02be5686907': send 'start'
    0:00:15 Job 'j-240430fa4ef14b43838af02be5686907': created (progress N/A)
    0:00:20 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:00:27 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:00:35 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:00:45 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:01:00 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:01:16 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:01:35 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:01:59 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:02:29 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:03:07 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:03:54 Job 'j-240430fa4ef14b43838af02be5686907': running (progress N/A)
    0:04:52 Job 'j-240430fa4ef14b43838af02be5686907': finished (progress N/A)

    WindowsPath('ndvi-file.tif')

``` python
with rasterio.open("ndvi-file.tiff") as src:
    show(src)
```

![](load-stac-item-example_files/figure-html/cell-5-output-1.png)

## 2. Create a STAC item

We create a STAC item for the GTiff file using pystac.

A STAC item is a JSON file that describes a geospatial dataset. It contains metadata about the dataset, such as the spatial extent, the time range, the bands, and the projection. The STAC item also contains links to the data files in assets.

It is important that the GTiff file is accessible for the openEO backend. This can be done by uploading the file to a cloud storage service like AWS S3 or Google Cloud Storage, or by storing the file in your public directory on a terrascope uservm (when using the openeo.vito.be backend).

``` python
# url to the tiff file
tiff_url = "https://artifactory.vgt.vito.be/artifactory/auxdata-public/openeo/load-stac-example/ndvi-file.tiff"

# datetime of the tiff file
# In case your data spans multiple days, you can use the datetime of the first day of the data
# When specifying a temporal range in load_stac later on, the stac item will be filteren only on this datetime
dt = datetime.fromisoformat("2021-06-01")

#desired output path for the stac item
output_path = "ndvi-example-stac-item.json"
```

Make sure the band names are set correctly in the STAC item. In this case the band name is “NDVI-band”. **These band names are required by openEO to identify the bands in the data and name them.**

The other metadata in the stac item are extracted from the GTiff file using rasterio.

``` python
with rasterio.open(tiff_url) as src:
    proj_bounds = list(src.bounds)
    left, bottom, right, top = rasterio.warp.transform_bounds(src.crs, "EPSG:4326", *src.bounds)
    item = pystac.Item(
        id="ndvi-example-stac-item",
        geometry={
            "type": "Polygon",
            "coordinates": [[
                [left, bottom],
                [right, bottom],
                [right, top],
                [left, top],
                [left, bottom]
            ]]
        },
        bbox=[left, bottom, right, top],
        datetime= dt,
        properties={ # These properties are optional, but can speed up the loading of the data.
            "proj:epsg": src.crs.to_epsg(),
            "proj:shape": src.shape, # Caveat: this is [height, width] and not [width, height] if you want to set them yourself
            "proj:bbox": proj_bounds,
        },
        stac_extensions=[
            "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
            "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
        ],
        assets={
            "ndvi": pystac.Asset(
                href=tiff_url,
                title="Normalized Difference Vegetation Index",
                extra_fields={
                    "eo:bands": [ # REQUIRED: define the bands in the eo extension for openEO to be able to load it
                        {
                            "name": "NDVI-band",
                        }
                    ],
                }
            )
        }
    )
    item.validate()
    item.save_object(dest_href=output_path, include_self_link=False)
```

Upload the resulting STAC item to a place where the openEO backend can access it. This can be a cloud storage service or a public directory on a terrascope uservm (when using the openeo.vito.be backend).

## 3. Load the STAC item in openEO as a collection

We load the STAC item in openEO as a collection using `load_stac` and download the result as a GTiff file. Instead of directly downloading, this datacube can also be further processed or merged with other datacubes.

**IMPORTANT**: Make sure the STAC item and the GTiff are accessible for the openEO backend. This can be done by uploading the STAC item to a cloud storage service like AWS S3 or Google Cloud Storage, or by storing the STAC item in your public directory on a terrascope uservm (when using the openEO.vito.be backend).

``` python
datacube = connection.load_stac("https://artifactory.vgt.vito.be/artifactory/auxdata-public/openeo/load-stac-example/ndvi-example-stac-item.json")
datacube.download("ndvi-from-stac.tiff")
```

``` python
with rasterio.open("ndvi-from-stac.tiff") as src:
    show(src)
```

![](load-stac-item-example_files/figure-html/cell-9-output-1.png)
