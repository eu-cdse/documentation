# Getting started with openEO

openEO is an open-source initiative that simplifies accessing and processing Earth Observation (EO) data.

Traditional methods involve complex steps like data discovery, download, and pre-processing, which can be time-consuming and challenging, especially when dealing with multiple datasets. openEO standardises this process, providing a unified interface for accessing and processing diverse EO datasets using familiar programming languages like Python. It leverages the concept of datacubes, which streamline the representation and manipulation of EO data, making spatiotemporal analysis more intuitive and efficient.

openEO is used in several applications across a range of EO scenarios, ranging from simple to complex workflows. However, this notebook aims to guide beginners in starting with openEO using the Python client. We’ll cover the basics, like installing it, authenticating, finding available EO data, accessing it, and performing basic analysis. We will also show you how to include some advanced custom functions.

This notebook is compiled using existing examples of openEO; therefore, we recommend exploring the available sample notebooks for more comprehensive explanations. Additionally, for a thorough understanding of various features, we suggest delving into the Eo-college course titled [Cubes&Cloud](https://eo-college.org/courses/cubes-and-clouds/), which provides step-by-step guidance and theoretical explanations. Our focus here is to help users become acquainted with the general openEO workflow.

Additionally, we recommend visiting the official [openEO Python client documentation](https://open-eo.github.io/openeo-python-client/index.html) for more detailed information on the available functions and their usage.

## Installation

The openEO Python client library is available from PyPI and can be easily installed with a tool like **pip**. However, it is pre-installed if you use Jupyter Workspace provided by the openEO platform, Copernicus Dataspace Ecosystem, Terrascope, or EOX.

``` python
!pip install openeo
```

You can find additional information on openEO installation in [this page](https://open-eo.github.io/openeo-python-client/installation.html).

``` python
import openeo
```

## Connect and Authenticate

Next, let’s set up a connection to an openEO backend using its connection URL. You can find these URLs for different backends on the [openEO hub](https://hub.openeo.org/). For this notebook, we’ll use the Copernicus Data Space Ecosystem, a cloud platform supported by the European Commission, ESA, and Copernicus. Make sure you have an [account](https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/auth?client_id=cdse-public&response_type=code&scope=openid&redirect_uri=https%3A//dataspace.copernicus.eu/account/confirmed/1) to access and process data using openEO.

When using other backends, you can register using your EduGAIN and social logins as suggested [here](https://docs.openeo.cloud/join/free_trial.html).

``` python
connection = openeo.connect(url="openeo.dataspace.copernicus.eu").authenticate_oidc()
```

    Authenticated using refresh token.

You can find additional information on Authentication on [this page](https://open-eo.github.io/openeo-python-client/auth.html).

## Data discovery and access

The Earth observation data is organised in so-called collections. You can programmatically list the collections available on a backend and their metadata using methods on the `connection` object. Furthermore, to visualise available collections and metadata in a user-friendly manner, you can also visit the [openEO hub](https://hub.openeo.org/) or explore [backend-specific openEO web editor](https://openeo.dataspace.copernicus.eu/).

### Data discovery

``` python
# Get all collection ids
connection.list_collection_ids()
```

    ['SENTINEL3_OLCI_L1B',
     'SENTINEL3_SLSTR',
     'SENTINEL_5P_L2',
     'COPERNICUS_VEGETATION_PHENOLOGY_PRODUCTIVITY_10M_SEASON1',
     'COPERNICUS_VEGETATION_PHENOLOGY_PRODUCTIVITY_10M_SEASON2',
     'COPERNICUS_PLANT_PHENOLOGY_INDEX',
     'ESA_WORLDCOVER_10M_2020_V1',
     'ESA_WORLDCOVER_10M_2021_V2',
     'COPERNICUS_VEGETATION_INDICES',
     'SENTINEL2_L1C',
     'SENTINEL2_L2A',
     'SENTINEL1_GRD',
     'COPERNICUS_30',
     'LANDSAT8_L2',
     'SENTINEL3_SYN_L2_SYN',
     'SENTINEL3_SLSTR_L2_LST']

``` python
# Get metadata of a single collection
connection.describe_collection("SENTINEL2_L2A")
```

Congrats!!!, You did your first openEO queries on the openEO Copernicus Data Space Ecosystem backend using the openEO Python client library.

### Process discovery

To proceed, it’s important to grasp the available built-in processes of openEO. We’ve already utilized a few of these processes in our earlier queries, like `list_collection_ids` and `describe_collection`.

``` python
# List all processes
connection.list_processes()
```

``` python
connection.describe_process("aggregate_temporal")
```

Find more information on these processes in [this page](https://open-eo.github.io/openeo-python-client/processes.html).

### Data access

A common task in earth observation is to apply a formula to several spectral bands to compute an ‘index’, such as NDVI, NDWI, EVI, … In this tutorial, we’ll go through a couple of steps to extract EVI (enhanced vegetation index) values and timeseries and discuss some openEO concepts along the way.

To calculate the EVI, we must determine the reflectance of the red, blue, and (near) infrared spectral components. These spectral bands are part of the well-known Sentinel-2 data set and are available on the current backend under collection ID SENTINEL2_L2A. So, let’s load this collection.

``` python
sentinel2_cube = connection.load_collection(
    "SENTINEL2_L2A",
    spatial_extent={"west": 5.14, "south": 51.17, "east": 5.17, "north": 51.19},
    temporal_extent=["2021-02-01", "2021-04-30"],
    bands=["B02", "B04", "B08"],
)
```

Here, we use the `load_collection` process that loads a collection from the current backend using its ID. The collection is loaded as a data cube restricted by spatial_extent, temporal_extent, bands, and properties.

Additionally, by filtering as early as possible (directly in `load_collection()` in this case), we ensure the backend only loads the data we are interested in for better performance and to keep the processing costs low. In this example, we filter the data based on the spatial extent, temporal extent, and bands.

Furthermore, in this example, we implemented bbox for `spatial_extent`; however, user can import their spatial files and feed them into the process as a feature collection.

Find out more about data discovery, loading and filtering at [Finding and loading data](https://open-eo.github.io/openeo-python-client/data_access.html).

## Data processing: Calculate EVI

While openEO offers a built-in process for calculating NDVI(`ndvi()`), this capability hasn’t been implemented yet for EVI or other indices. Instead, openEO provides support for most other indices through an auxiliary subpackage calle[d Awesome Spectral Indic](https://open-eo.github.io/openeo-python-client/cookbook/spectral_indices.html)es. However, users also have the option to perform band math independently, as demonstrated in this notebook. The choice between the two methods depends on user preference.

From this data cube, we can now select the individual bands using the [`DataCube.band()`](https://open-eo.github.io/openeo-python-client/api.html#openeo.rest.datacube.DataCube) method and rescale the digital number values to physical reflectances.

``` python
blue = sentinel2_cube.band("B02") * 0.0001
red = sentinel2_cube.band("B04") * 0.0001
nir = sentinel2_cube.band("B08") * 0.0001
```

We now want to compute the enhanced vegetation index and can do that directly with these band variables:

``` python
evi_cube = 2.5 * (nir - red) / (nir + 6.0 * red - 7.5 * blue + 1.0)
```

Please note that while this looks like an actual calculation, real data processing still needs to be done. At this point, the **evi_cube** object is just an abstract representation of our algorithm under construction. The mathematical operators we used here are syntactic sugar for compactly expressing this part of the algorithm.

As an illustration of this, you can also have a look at the JSON representation of the algorithm so far by simply printing them as json: `print(evi_cube.to_json())`

## Execute the process

Depending on the datacube that is created by our process graph and on the later use case, we can export the results to more suitable formats supported by openEO. You can explore the supported file formats in [this page](https://documentation.dataspace.copernicus.eu/APIs/openEO/File_formats.html).

Here, let’s download this as a GeoTIFF file. However, a GeoTIFF does not support a temporal dimension, thus, we first should eliminate it by taking the temporal maximum value for each pixel.

``` python
evi_composite = evi_cube.max_time()
```

Finally, to trigger an actual execution (on the backend), we have to explicitly send the above representation to the backend. You can do this either synchronously(simple download) or using the batch-job-based method. Most of the simple, basic openEO usage examples show synchronous downloading of results. Synchronous downloads are handy for quick experimentation on small data cubes.

This only works properly if the processing doesn’t take too long and is focused on a smaller area of interest. However, you have to use batch jobs for the heavier work (larger regions of interest, larger time series, more intensive processing). For more information on using batch-job in openEO, visit [here](https://open-eo.github.io/openeo-python-client/batch_jobs.html).

``` python
evi_composite.download("evi_composite.tiff")
```

This download command triggers the actual processing on the back-end: it sends the process graph to the back-end and waits for the result.

## Visualise the results

``` python
import rasterio
import matplotlib.pyplot as plt

img2 = rasterio.open("evi_composite.tiff").read()
plt.imshow(img2[0], vmax=1, vmin=-0.1)
plt.colorbar()
```

![](GettingStarted_files/figure-html/cell-14-output-1.png)

When we inspect the downloaded image, we observed a significant impact from cloud-related artefacts on the maximum EVI value. While incorporating a cloud mask could mitigate this issue, our primary objective in this notebook was to introduce the basic task in openEO to the openEO beginners. Thus, we recommend exploring the cloud mask in [openEO sample notebooks](https://github.com/Open-EO/openeo-community-examples/tree/main/python) for more advanced users.

As we conclude, we encourage further exploration into additional materials for those interested in:

- Applying a cloud mask to enhance the workflow. For guidance, refer to [link](https://open-eo.github.io/openeo-python-client/basics.html#applying-a-cloud-mask).
- Exploring temporal aggregation of the calculated EVI [Link](https://open-eo.github.io/openeo-python-client/basics.html#aggregated-evi-timeseries).
- Utilizing batch-job-based execution [Link](https://github.com/eu-cdse/notebook-samples/blob/main/openeo/Batch_job.ipynb).
- [Examples](https://github.com/eu-cdse/notebook-samples/blob/main/openeo/UDF.ipynb) of including self-defined functions as [user-defined-functions (UDF)](https://open-eo.github.io/openeo-python-client/udf.html) in openEO workflow.
- Learn more on [user-defined-process](https://open-eo.github.io/openeo-python-client/udp.html) to build your own library of reusable algorithms.
- [Examples](https://github.com/Open-EO/openeo-community-examples/blob/main/python/README.md) on more comprehensive EO applications, including techniques such as resampling,reduce_dimension, apply_neighborhood and many more.
