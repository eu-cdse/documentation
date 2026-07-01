# First Steps in accessing Satellite Imagery on Copernicus Data Space Ecosystem with Sentinel Hub APIs

The Sentinel Hub API is a RESTful API interface that provides access to various satellite imagery archives. It allows you to access raw satellite data, rendered images, statistical analysis, and other features.

``` python
# Utilities
import matplotlib.pyplot as plt
import pandas as pd
import getpass

from sentinelhub import (
    SHConfig,
    DataCollection,
    SentinelHubCatalog,
    SentinelHubRequest,
    SentinelHubStatistical,
    BBox,
    bbox_to_dimensions,
    CRS,
    MimeType,
    Geometry,
)

from utils import plot_image
```

## Credentials

Credentials for Sentinel Hub services (`client_id` & `client_secret`) can be obtained in your [Dashboard](https://shapps.dataspace.copernicus.eu/dashboard/#/). In the User Settings you can create a new OAuth Client to generate these credentials. For more detailed instructions, visit the relevant [documentation page](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html).

Now that you have your `client_id` & `client_secret`, it is recommended to configure a new profile in your Sentinel Hub Python package. Instructions on how to configure your Sentinel Hub Python package can be found [here](https://sentinelhub-py.readthedocs.io/en/latest/configure.html). Using these instructions you can create a profile specific to using the package for accessing Copernicus Data Space Ecosystem data collections. This is useful as changes to the the config class are usually only temporary in your notebook and by saving the configuration to your profile you won’t need to generate new credentials or overwrite/change the default profile each time you rerun or write a new Jupyter Notebook.

If you are a first time user of the Sentinel Hub Python package for Copernicus Data Space Ecosystem, you should create a profile specific to the Copernicus Data Space Ecosystem. You can do this in the following cell:

``` python
# Only run this cell if you have not created a configuration.

config = SHConfig()
# config.sh_client_id = getpass.getpass("Enter your SentinelHub client id")
# config.sh_client_secret = getpass.getpass("Enter your SentinelHub client secret")
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
config.sh_base_url = "https://sh.dataspace.copernicus.eu"
# config.save("cdse")
```

However, if you have already configured a profile in Sentinel Hub Python for the Copernicus Data Space Ecosystem, then you can run the below cell entering the profile name as a string replacing `<profile_name>`.

``` python
# config = SHConfig("profile_name")
```

## Setting an area of interest

The bounding box in `WGS84` coordinate system is `[(longitude and latitude coordinates of lower left and upper right corners)]`. You can get the bbox for a different area at the [bboxfinder](http://bboxfinder.com/) website.

All requests require a bounding box to be given as an instance of `sentinelhub.geometry.BBox` with corresponding Coordinate Reference System (`sentinelhub.constants.CRS`). In our case it is in WGS84 and we can use the predefined WGS84 coordinate reference system from `sentinelhub.constants.CRS`.

``` python
aoi_coords_wgs84 = [15.461282, 46.757161, 15.574922, 46.851514]
```

When the bounding box bounds have been defined, you can initialize the `BBox` of the area of interest. Using the `bbox_to_dimensions` utility function, you can provide the desired resolution parameter of the image in meters and obtain the output image shape.

``` python
resolution = 10
aoi_bbox = BBox(bbox=aoi_coords_wgs84, crs=CRS.WGS84)
aoi_size = bbox_to_dimensions(aoi_bbox, resolution=resolution)

print(f"Image shape at {resolution} m resolution: {aoi_size} pixels")
```

    Image shape at 10 m resolution: (860, 1054) pixels

## Catalog API

To search and discover data, you can use the Catalog API. Sentinel Hub Catalog API (or shortly “Catalog”) is an API implementing the STAC Specification, providing geospatial information for data available in Sentinel Hub. Firstly, to initialise the `SentinelHubCatalog` class we will use:

``` python
catalog = SentinelHubCatalog(config=config)
```

Now we can build the Catalog API request; to do this we use the `aoi_bbox` we defined earlier as well as `time_interval` and insert these into the request:

``` python
aoi_bbox = BBox(bbox=aoi_coords_wgs84, crs=CRS.WGS84)
time_interval = "2022-07-01", "2022-07-20"

search_iterator = catalog.search(
    DataCollection.SENTINEL2_L2A,
    bbox=aoi_bbox,
    time=time_interval,
    fields={"include": ["id", "properties.datetime"], "exclude": []},
)

results = list(search_iterator)
print("Total number of results:", len(results))

results
```

    Total number of results: 8

    [{'id': 'S2B_MSIL2A_20220719T095559_N0400_R122_T33TWM_20220719T113943.SAFE',
      'properties': {'datetime': '2022-07-19T10:07:53.062Z'}},
     {'id': 'S2B_MSIL2A_20220716T094549_N0400_R079_T33TWM_20220716T114017.SAFE',
      'properties': {'datetime': '2022-07-16T09:57:56.26Z'}},
     {'id': 'S2A_MSIL2A_20220714T100041_N0400_R122_T33TWM_20220714T175057.SAFE',
      'properties': {'datetime': '2022-07-14T10:08:00.748Z'}},
     {'id': 'S2A_MSIL2A_20220711T095041_N0400_R079_T33TWM_20220711T142927.SAFE',
      'properties': {'datetime': '2022-07-11T09:58:04.522Z'}},
     {'id': 'S2B_MSIL2A_20220709T100029_N0400_R122_T33TWM_20220709T114004.SAFE',
      'properties': {'datetime': '2022-07-09T10:07:52.974Z'}},
     {'id': 'S2B_MSIL2A_20220706T095039_N0400_R079_T33TWM_20220706T113052.SAFE',
      'properties': {'datetime': '2022-07-06T09:57:56.689Z'}},
     {'id': 'S2A_MSIL2A_20220704T100041_N0400_R122_T33TWM_20220704T141618.SAFE',
      'properties': {'datetime': '2022-07-04T10:08:01.243Z'}},
     {'id': 'S2A_MSIL2A_20220701T095041_N0400_R079_T33TWM_20220701T141709.SAFE',
      'properties': {'datetime': '2022-07-01T09:58:04.669Z'}}]

## Process API

### Example 1: True Color Image

We build the request according to the [API Reference](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/ApiReference.html), using the `SentinelHubRequest` class. Each Process API request also needs an [evalscript](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Evalscript.html). An evalscript (or “custom script”) is a piece of Javascript code which defines how the satellite data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Process.html), [batch processing](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Batch.html) or [OGC request](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/OGC.html).

The information that we specify in the `SentinelHubRequest` object is: - an evalscript, - a list of input data collections with time interval, - a format of the response, - a bounding box and its size (size or resolution). - `mosaickingOrder` (optional): in this example we have used `leastCC` which will return pixels from the least cloudy acquisition in the specified time period.

The evalscript in the example is used to select the appropriate bands. We return the RGB (B04, B03, B02) Sentinel-2 L2A bands.

The least cloudy image from the time period is downloaded. Without any additional parameters in the evalscript, the downloaded data will correspond to reflectance values in `UINT8` format (values in 0-255 range).

``` python
evalscript_true_color = """
    //VERSION=3

    function setup() {
        return {
            input: [{
                bands: ["B02", "B03", "B04"]
            }],
            output: {
                bands: 3
            }
        };
    }

    function evaluatePixel(sample) {
        return [sample.B04, sample.B03, sample.B02];
    }
"""

request_true_color = SentinelHubRequest(
    evalscript=evalscript_true_color,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A.define_from(
                name="s2l2a", service_url="https://sh.dataspace.copernicus.eu"
            ),
            time_interval=("2022-05-01", "2022-05-20"),
            other_args={"dataFilter": {"mosaickingOrder": "leastCC"}},
        )
    ],
    responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
    bbox=aoi_bbox,
    size=aoi_size,
    config=config,
)
```

The method `get_data()` will always return a list of length 1 with the available image from the requested time interval in the form of numpy arrays.

``` python
true_color_imgs = request_true_color.get_data()
```

``` python
print(
    f"Returned data is of type = {type(true_color_imgs)} and length {len(true_color_imgs)}."
)
print(
    f"Single element in the list is of type {type(true_color_imgs[-1])} and has shape {true_color_imgs[-1].shape}"
)
```

    Returned data is of type = <class 'list'> and length 1.
    Single element in the list is of type <class 'numpy.ndarray'> and has shape (1054, 860, 3)

``` python
image = true_color_imgs[0]
print(f"Image type: {image.dtype}")

# plot function
# factor 1/255 to scale between 0-1
# factor 3.5 to increase brightness
plot_image(image, factor=3.5 / 255, clip_range=(0, 1))
```

    Image type: uint8

![](introduction_to_SH_APIs_files/figure-html/cell-12-output-2.png)

### Example 2: NDVI Image

Secondly, we will also show you an example of how to calculate and visualise NDVI using the same API. NDVI is a very commonly used spectral vegetation index for vegetation monitoring, for example, monitoring crop growth and yields. As you will notice in the codeblock below, the evalscript has changed substantially: - we are only using Band 4 and Band 8 as an input into our script. - In the `evaluatePixel()` function, we calculate NDVI and visualise this using the `imgVals` array.

``` python
evalscript_ndvi = """
//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "B04",
        "B08",
        "dataMask"
      ]
    }],
    output: {
      bands: 4
    }
  }
}
  

function evaluatePixel(sample) {
    let val = (sample.B08 - sample.B04) / (sample.B08 + sample.B04);
    let imgVals = null;
    
    if (val<-1.1) imgVals = [0,0,0];
    else if (val<-0.2) imgVals = [0.75,0.75,0.75];
    else if (val<-0.1) imgVals = [0.86,0.86,0.86];
    else if (val<0) imgVals = [1,1,0.88];
    else if (val<0.025) imgVals = [1,0.98,0.8];
    else if (val<0.05) imgVals = [0.93,0.91,0.71];
    else if (val<0.075) imgVals = [0.87,0.85,0.61];
    else if (val<0.1) imgVals = [0.8,0.78,0.51];
    else if (val<0.125) imgVals = [0.74,0.72,0.42];
    else if (val<0.15) imgVals = [0.69,0.76,0.38];
    else if (val<0.175) imgVals = [0.64,0.8,0.35];
    else if (val<0.2) imgVals = [0.57,0.75,0.32];
    else if (val<0.25) imgVals = [0.5,0.7,0.28];
    else if (val<0.3) imgVals = [0.44,0.64,0.25];
    else if (val<0.35) imgVals = [0.38,0.59,0.21];
    else if (val<0.4) imgVals = [0.31,0.54,0.18];
    else if (val<0.45) imgVals = [0.25,0.49,0.14];
    else if (val<0.5) imgVals = [0.19,0.43,0.11];
    else if (val<0.55) imgVals = [0.13,0.38,0.07];
    else if (val<0.6) imgVals = [0.06,0.33,0.04];
    else imgVals = [0,0.27,0];
    
    
    imgVals.push(sample.dataMask)
    
    return imgVals
}
"""

request_ndvi_img = SentinelHubRequest(
    evalscript=evalscript_ndvi,
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L2A.define_from(
                name="s2l2a", service_url="https://sh.dataspace.copernicus.eu"
            ),
            time_interval=("2022-05-01", "2022-05-20"),
            other_args={"dataFilter": {"mosaickingOrder": "leastCC"}},
        )
    ],
    responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
    bbox=aoi_bbox,
    size=aoi_size,
    config=config,
)
```

The same method as before is used to request and then visualise the data. In the visualisation, the lighter greens indicate a higher NDVI value (vegetation, forest) and the darker greens (urban areas and water bodies) represent areas with lower NDVI values.

``` python
ndvi_img = request_ndvi_img.get_data()
```

``` python
print(
    f"Returned data is of type = {type(true_color_imgs)} and length {len(true_color_imgs)}."
)
print(
    f"Single element in the list is of type {type(true_color_imgs[-1])} and has shape {true_color_imgs[-1].shape}"
)
```

    Returned data is of type = <class 'list'> and length 1.
    Single element in the list is of type <class 'numpy.ndarray'> and has shape (1054, 860, 3)

``` python
image = ndvi_img[0]
print(f"Image type: {image.dtype}")

# plot function
plot_image(image, factor=1 / 255)
```

    Image type: uint8

![](introduction_to_SH_APIs_files/figure-html/cell-16-output-2.png)

## Statistical API

In the Process API examples, we have seen how to obtain satellite imagery. Statistical API can be used in a very similar way. The main difference is that the results of Statistical API are aggregated statistical values of satellite data instead of entire images. In many use cases, such values are all that we need. By using Statistical API we can avoid downloading and processing large amounts of satellite data.

All general rules for building evalscripts apply. However, there are some specifics when using evalscripts with the Statistical API:

- The `evaluatePixel()` function must, in addition to other output, always return a `dataMask` output. This output defines which pixels are excluded from calculations. For more details and an example, see [here](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Statistical.html).
- The default value of sampleType is `FLOAT32`.
- The output.bands parameter in the setup() function can be an array. This makes it possible to specify custom names for the output bands and different output `dataMask` for different outputs, see this [example](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Statistical/Examples.html#multiple-outputs-with-different-datamasks-multi-band-output-with-custom-bands-names-and-different-histogram-types).

### Requesting, and plotting an NDVI time series for a single field

In the example here, we will calculate NDVI for a specific field of interest and then plot the mean NDVI and standard deviation over the requested time period. First we define our evalscript:

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "B04",
        "B08",
        "dataMask"
      ]
    }],
    output: [
      {
        id: "ndvi",
        bands: 1
      },
      {
        id: "dataMask",
        bands: 1
      }]
  };
}

function evaluatePixel(samples) {
    let index = (samples.B08 - samples.B04) / (samples.B08+samples.B04);
    return {
        ndvi: [index],
        dataMask: [samples.dataMask],
    };
}

"""
```

In this example, we will compare two fields within the area we requested using Process API:

``` python
field1 = {
    "type": "Polygon",
    "coordinates": [
        [
            [15.541723001099184, 46.820368115848446],
            [15.541756949727985, 46.82037740810231],
            [15.54192669287196, 46.82008470133467],
            [15.542211861353849, 46.81964331510048],
            [15.539394125163792, 46.81905789197882],
            [15.539251540922846, 46.819805931503055],
            [15.541723001099184, 46.820368115848446],
        ]
    ],
}

field2 = {
    "type": "Polygon",
    "coordinates": [
        [
            [15.507170086710744, 46.83938135202761],
            [15.508086699688228, 46.83921879483953],
            [15.50831755036404, 46.839576420004114],
            [15.508582349668648, 46.83992939835186],
            [15.508874307876296, 46.840221997066486],
            [15.50860950857169, 46.840514594187695],
            [15.50842618597619, 46.84082112279607],
            [15.508113858591262, 46.840639992466144],
            [15.50781511065786, 46.84039384001332],
            [15.50739414766079, 46.83981328730921],
            [15.507149717533464, 46.83939064099493],
            [15.507170086710744, 46.83938135202761],
        ]
    ],
}
```

Now we have defined the evalscript and the two fields of interest, we can build the first Statistical API Request, before returning the response for the first field. In this request, as part of the payload we define some input parameters: - `time_interval` this defines the time range of our request. - `aggregation_interval` this defines the length of time each interval is. In this case, the interval is 10 days. he aggregation intervals should be at least one day long (e.g. “P5D”, “P30D”). You can only use period OR time designator not both. - `dataFilter: {maxCloudCoverage}` this is an additional argument in our request which filters out image acquisitions that have a cloud coverage percentage above 10%.

**NOTE:** If a timeRange is not divisible by an aggregationInterval, the last (“not full”) time interval will be dismissed by default (SKIP option). The user can instead set the lastIntervalBehavior to SHORTEN (shortens the last interval so that it ends at the end of the provided time range) or EXTEND (extends the last interval over the end of the provided time range so that all the intervals are of equal duration).

``` python
geometry = Geometry(geometry=field1, crs=CRS.WGS84)

request = SentinelHubStatistical(
    aggregation=SentinelHubStatistical.aggregation(
        evalscript=evalscript,
        time_interval=("2022-04-01T00:00:00Z", "2022-08-30T23:59:59Z"),
        aggregation_interval="P10D",
        size=[368.043, 834.345],
    ),
    input_data=[
        SentinelHubStatistical.input_data(
            DataCollection.SENTINEL2_L1C.define_from(
                name="s2l1c", service_url="https://sh.dataspace.copernicus.eu"
            ),
            other_args={"dataFilter": {"maxCloudCoverage": 10}},
        ),
    ],
    geometry=geometry,
    config=config,
)

response1 = request.get_data()
response1
```

    [{'data': [{'interval': {'from': '2022-04-21T00:00:00Z',
         'to': '2022-05-01T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.08167635649442673,
             'max': 0.39603960514068604,
             'mean': 0.13346635554959452,
             'stDev': 0.06778421108052068,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-05-11T00:00:00Z', 'to': '2022-05-21T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.07600757479667664,
             'max': 0.4349462389945984,
             'mean': 0.11771845381622796,
             'stDev': 0.06006468950382084,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-05-21T00:00:00Z', 'to': '2022-05-31T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.12070990353822708,
             'max': 0.22220245003700256,
             'mean': 0.1623609989287693,
             'stDev': 0.02119876493505649,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-05-31T00:00:00Z', 'to': '2022-06-10T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.30697834491729736,
             'max': 0.5585442781448364,
             'mean': 0.3871644425922805,
             'stDev': 0.036877585538162914,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-06-10T00:00:00Z', 'to': '2022-06-20T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.4932262897491455,
             'max': 0.7623130679130554,
             'mean': 0.7166323115162642,
             'stDev': 0.03632912872686905,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-06-20T00:00:00Z', 'to': '2022-06-30T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.5235322713851929,
             'max': 0.8472102880477905,
             'mean': 0.8134408265822731,
             'stDev': 0.04334495262826597,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-06-30T00:00:00Z', 'to': '2022-07-10T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.5385261178016663,
             'max': 0.8165295124053955,
             'mean': 0.7346462549343704,
             'stDev': 0.05007425808442363,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-07-10T00:00:00Z', 'to': '2022-07-20T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.48085325956344604,
             'max': 0.7764950394630432,
             'mean': 0.6345127327117525,
             'stDev': 0.037435679050829576,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-07-20T00:00:00Z', 'to': '2022-07-30T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.3827281594276428,
             'max': 0.7180401086807251,
             'mean': 0.47361417948967777,
             'stDev': 0.04486725306919478,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-07-30T00:00:00Z', 'to': '2022-08-09T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.25120440125465393,
             'max': 0.6704408526420593,
             'mean': 0.3448654317316632,
             'stDev': 0.060250767466331526,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}},
       {'interval': {'from': '2022-08-09T00:00:00Z', 'to': '2022-08-19T00:00:00Z'},
        'outputs': {'ndvi': {'bands': {'B0': {'stats': {'min': 0.24285714328289032,
             'max': 0.6134668588638306,
             'mean': 0.33002391002395726,
             'stDev': 0.05309494318283593,
             'sampleCount': 306912,
             'noDataCount': 137731}}}}}}],
      'status': 'OK'}]

However, as it is clear to see, our response is not that useful in `json` format. It’s difficult to read from a human perspective. So, let’s transform it into a `pandas` dataframe. To help us achieve this, let’s define some helper functions.

``` python
# define functions to extract statistics for all acquisition dates
def extract_stats(date, stat_data):
    d = {}
    for key, value in stat_data["outputs"].items():
        stats = value["bands"]["B0"]["stats"]
        if stats["sampleCount"] == stats["noDataCount"]:
            continue
        else:
            d["date"] = [date]
            for stat_name, stat_value in stats.items():
                if stat_name == "sampleCount" or stat_name == "noDataCount":
                    continue
                else:
                    d[f"{key}_{stat_name}"] = [stat_value]
    return pd.DataFrame(d)


def read_acquisitions_stats(stat_data):
    df_li = []
    for aq in stat_data:
        date = aq["interval"]["from"][:10]
        df_li.append(extract_stats(date, aq))
    return pd.concat(df_li)
```

``` python
result_df1 = read_acquisitions_stats(response1[0]["data"])
result_df1
```

|     | date       | ndvi_min | ndvi_max | ndvi_mean | ndvi_stDev |
|-----|------------|----------|----------|-----------|------------|
| 0   | 2022-04-21 | 0.081676 | 0.396040 | 0.133466  | 0.067784   |
| 0   | 2022-05-11 | 0.076008 | 0.434946 | 0.117718  | 0.060065   |
| 0   | 2022-05-21 | 0.120710 | 0.222202 | 0.162361  | 0.021199   |
| 0   | 2022-05-31 | 0.306978 | 0.558544 | 0.387164  | 0.036878   |
| 0   | 2022-06-10 | 0.493226 | 0.762313 | 0.716632  | 0.036329   |
| 0   | 2022-06-20 | 0.523532 | 0.847210 | 0.813441  | 0.043345   |
| 0   | 2022-06-30 | 0.538526 | 0.816530 | 0.734646  | 0.050074   |
| 0   | 2022-07-10 | 0.480853 | 0.776495 | 0.634513  | 0.037436   |
| 0   | 2022-07-20 | 0.382728 | 0.718040 | 0.473614  | 0.044867   |
| 0   | 2022-07-30 | 0.251204 | 0.670441 | 0.344865  | 0.060251   |
| 0   | 2022-08-09 | 0.242857 | 0.613467 | 0.330024  | 0.053095   |

We can take this another step further, and display the data in a time series using the Matplotlib python library:

``` python
fig_stat, ax_stat = plt.subplots(1, 1, figsize=(12, 6))
t1 = result_df1["date"]
ndvi_mean_field1 = result_df1["ndvi_mean"]
ndvi_std_field1 = result_df1["ndvi_stDev"]
ax_stat.plot(t1, ndvi_mean_field1, label="field 1 mean")
ax_stat.fill_between(
    t1,
    ndvi_mean_field1 - ndvi_std_field1,
    ndvi_mean_field1 + ndvi_std_field1,
    alpha=0.3,
    label="field 1 stDev",
)
ax_stat.tick_params(axis="x", labelrotation=30, labelsize=12)
ax_stat.tick_params(axis="y", labelsize=12)
ax_stat.set_xlabel("Date", size=15)
ax_stat.set_ylabel("NDVI/unitless", size=15)
ax_stat.legend(loc="lower right", prop={"size": 12})
ax_stat.set_title("NDVI time series", fontsize=20)
for label in ax_stat.get_xticklabels()[1::2]:
    label.set_visible(False)
```

![](introduction_to_SH_APIs_files/figure-html/cell-22-output-1.png)

### Comparing different fields

Now that we have learnt how to plot the data for the first field, let’s take this another step forward and compare the NDVI time series of the first field with the second field. We will now run the same request for our second field and then transform the response into a second Pandas dataframe.

``` python
geometry = Geometry(geometry=field2, crs=CRS.WGS84)

request = SentinelHubStatistical(
    aggregation=SentinelHubStatistical.aggregation(
        evalscript=evalscript,
        time_interval=("2022-04-01T00:00:00Z", "2022-08-30T23:59:59Z"),
        aggregation_interval="P10D",
        size=[368.043, 834.345],
    ),
    input_data=[
        SentinelHubStatistical.input_data(
            DataCollection.SENTINEL2_L1C.define_from(
                name="s2l1c", service_url="https://sh.dataspace.copernicus.eu"
            ),
            other_args={"dataFilter": {"maxCloudCoverage": 10}},
        ),
    ],
    geometry=geometry,
    config=config,
)

response2 = request.get_data()
result_df2 = read_acquisitions_stats(response2[0]["data"])
```

Now we have requested the statistics for both fields and transformed them into Pandas dataframes, let’s plot the two time series and visualise this in the same plot:

``` python
fig_stat, ax_stat = plt.subplots(1, 1, figsize=(12, 6))
t1 = result_df1["date"]
t2 = result_df1["date"]
ndvi_mean_field1 = result_df1["ndvi_mean"]
ndvi_std_field1 = result_df1["ndvi_stDev"]
ndvi_mean_field2 = result_df2["ndvi_mean"]
ndvi_std_field2 = result_df2["ndvi_stDev"]
ax_stat.plot(t1, ndvi_mean_field1, label="field 1 mean")
ax_stat.fill_between(
    t1,
    ndvi_mean_field1 - ndvi_std_field1,
    ndvi_mean_field1 + ndvi_std_field1,
    alpha=0.3,
    label="field 1 stDev",
)
ax_stat.plot(t2, ndvi_mean_field2, label="field 2 mean")
ax_stat.fill_between(
    t2,
    ndvi_mean_field2 - ndvi_std_field2,
    ndvi_mean_field2 + ndvi_std_field2,
    alpha=0.3,
    label="field 2 stDev",
)
ax_stat.tick_params(axis="x", labelrotation=30, labelsize=12)
ax_stat.tick_params(axis="y", labelsize=12)
ax_stat.set_xlabel("Date", size=15)
ax_stat.set_ylabel("NDVI/unitless", size=15)
ax_stat.legend(loc="lower right", prop={"size": 12})
ax_stat.set_title("NDVI time series", fontsize=20)
for label in ax_stat.get_xticklabels()[1::2]:
    label.set_visible(False)
```

![](introduction_to_SH_APIs_files/figure-html/cell-24-output-1.png)

## Summary

So what have we learnt in this notebook?

- How to quickly access satellite imagery though Sentinel Hub using Process API.
- Visualising NDVI derived from the satellite imagery
- Using Statistical API to produce NDVI time series for single and multiple fields.

This concludes this notebook on working with Sentinel Hub APIs to access data from the Copernicus Data Space Ecosystem. For more information you can check out the [Sentinel Hub API](https://dataspace.copernicus.eu/analyse/apis/sentinel-hub) Documentation and the [Sentinel Hub Python package](https://sentinelhub-py.readthedocs.io/en/latest/index.html) documentation too.
