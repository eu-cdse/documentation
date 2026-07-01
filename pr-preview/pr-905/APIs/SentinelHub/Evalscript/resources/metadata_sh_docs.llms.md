This user guide will show you how to work with metadata in evalscripts. We will focus on using objects [`scenes`](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Evalscript/Functions.html#scenes), [`inputMetadata`](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Evalscript/Functions.html#inputmetadata), and [`outputMetadata`](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Evalscript/Functions.html#outputmetadata). Use cases, covered with the examples below, include accessing metadata and using it in processing, passing the metadata to an output file `userdata.json`, and adding your own metadata to the file.

> **Important:** If you’re running this notebook on the [CDSE JupyterLab environment](https://jupyterhub.dataspace.copernicus.eu/), **don’t forget to select the `Sentinel Hub` kernel** to ensure all dependencies and authentication methods work correctly.

Note that metadata normally provided in raster format is available as bands in Sentinel Hub. Such metadata can be accessed and processed in evalscript in the same manner as any other input band. This is not covered in this guide, but you can find basic examples and such metadata listed in the `Data` section for each data collection e.g. [sunAzimuthAngles](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/S2L1C.html#available-bands-and-data).

Each example below begins with a description that highlights the important points of the example. All examples output also processed satellite images (average values of NDVI or band B02) but we do not display them here, since the focus is on metadata. To run the examples, you only need to have Python installed on your machine and an active Sentinel Hub account. You will always need to run the code in the chapter “Authentication” while the rest of the examples can be run independently.

## Authentication

First, we need to fetch an access token, which we will use to authenticate all Sentinel Hub requests. To do so, replace `<client_id>` and `<client_secret>` in the code snippet below with your client id and client secret, respectively and run the code. To learn how to get your client id and client secret, read this [documentation](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html#registering-oauth-client).

``` python
import matplotlib.pyplot as plt
import numpy as np
from sentinelhub import CRS, DataCollection, Geometry, MimeType, SentinelHubRequest, SHConfig

config = SHConfig()
config.sh_client_id = "<your_client_id>"
config.sh_client_secret = "<your_client_secret>"
config.sh_base_url = "https://sh.dataspace.copernicus.eu"
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
```

The access token is stored in the `oauth` object, which will be used to send all subsequent requests.

## Check which metadata is available

The metadata is stored in two objects, which we call `inputMetadata` and `scenes`. Their properties are documented [here](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Evalscript/Functions.html#inputmetadata) and [here](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Evalscript/Functions.html#scenes), respectively. However, the properties of the `scenes` object can be different depending on the selected: - mosaicking (e.g. ORBIT or TILE), - data collection (Sentinel-2 L2A, Sentinel-1, Sentinel-5p, …), - function in the evalscript (`evaluatePixel`, `preProcessScenes`, `updateOutputMetadata`).

A convenient way to check which metadata is for your request available in `scenes` is to dump (i.e. write) all properties of the object to userdata.json file. This can be achieved with the Processing API as shown in this basic [example](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Process/Examples/S2L1C.html#true-color-and-metadata-multi-part-response-geotiff-and-json). The two examples below show few more tricks that can be used to explore `scenes` object.

### Properties of scenes object and mosaicking ORBIT

This example shows: - How to access metadata when mosaicking is ORBIT using `scenes.orbits`. - How to pass metadata from `scenes` to userdata.json file using `outputMetadata.userData` in `updateOutputMetadata` function.

``` python
url = 'https://sh.dataspace.copernicus.eu'

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B02", "dataMask"],
    mosaicking: Mosaicking.ORBIT,
    output: {
      id: "default",
      bands: 1
    }
  }
}

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {
  //Average value of band B02 based on the requested scenes
  var sumOfValidSamplesB02 = 0
  var numberOfValidSamples = 0
  for (i = 0; i < samples.length; i++) {
    var sample = samples[i]
    if (sample.dataMask == 1){
        sumOfValidSamplesB02 += sample.B02
        numberOfValidSamples += 1
    }
  }
  return [sumOfValidSamplesB02 / numberOfValidSamples]
}

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
  outputMetadata.userData = {
    "inputMetadata": inputMetadata
  }
  outputMetadata.userData["orbits"] = scenes.orbits
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [13.8, 45.8, 13.9, 45.9]
    },
    "data": [{
      "type": "sentinel-2-l1c",
      "dataFilter": {
        "timeRange": {
          "from": "2020-12-01T00:00:00Z",
          "to": "2020-12-06T23:59:59Z"
        }
      }
    }]
  },
  "output": {
    "responses": [{
        "identifier": "default",
        "format": {
          "type": "image/tiff"
        }
      },
      {
        "identifier": "userdata",
        "format": {
          "type": "application/json"
        }
      }
    ]
  },
  "evalscript": evalscript
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/x-tar'
}

response = oauth.post(f"{url}/process/v1", headers=headers, json = request)
tar = tarfile.open(fileobj=io.BytesIO(response.content))
userdata = json.load(tar.extractfile(tar.getmember('userdata.json')))
userdata
```

### Properties of scenes object and mosaicking TILE

This example shows how to: - Access scenes metadata when mosaicking is TILE using `scenes.tiles` and write it to userdata.json file. - How to calculate a maximum value of band B02 and write it to userdata.json file. Note that we use a global variable `maxValueB02` so that we can assign a value to it in `evaluatePixel` function but write its value to metadata in `updateOutputMetadata` function. The advantage of this approach is that `maxValueB02` is written to metadata only once and not for each output pixel.

``` python
url = 'https://sh.dataspace.copernicus.eu'

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B02", "dataMask"],
    mosaicking: Mosaicking.TILE,
    output: {
      id: "default",
      bands: 1
    }
  }
}

var maxValueB02 = 0

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {
  //Average value of band B02 based on the requested tiles
  var sumOfValidSamplesB02 = 0
  var numberOfValidSamples = 0
  for (i = 0; i < samples.length; i++) {
    var sample = samples[i]
    if (sample.dataMask == 1){
        sumOfValidSamplesB02 += sample.B02
        numberOfValidSamples += 1
        if (sample.B02 > maxValueB02){
            maxValueB02 = sample.B02
        }
    }
  }
  return [sumOfValidSamplesB02 / numberOfValidSamples]
}

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
  outputMetadata.userData = { "tiles":  scenes.tiles }
  outputMetadata.userData.maxValueB02 = maxValueB02
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [13.8, 45.8, 13.9, 45.9]
    },
    "data": [{
      "type": "sentinel-2-l1c",
      "dataFilter": {
        "timeRange": {
          "from": "2020-12-01T00:00:00Z",
          "to": "2020-12-06T23:59:59Z"
        }
      }
    }]
  },
  "output": {
    "responses": [{
        "identifier": "default",
        "format": {
          "type": "image/tiff"
        }
      },
      {
        "identifier": "userdata",
        "format": {
          "type": "application/json"
        }
      }
    ]
  },
  "evalscript": evalscript
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/x-tar'
}

response = oauth.post(f"{url}/process/v1", headers=headers, json = request)
tar = tarfile.open(fileobj=io.BytesIO(response.content))
userdata = json.load(tar.extractfile(tar.getmember('userdata.json')))
userdata
```

## Output metadata into userdata.json file

In this example, we write several pieces of information to the userdata.json file: - A version of the software with which the data was processed. We take this information from `inputMetadata`. - Dates when the data used for processing was acquired. We take this information from `scene.tiles`. - Values set by user and used for processing, such as thresholds (e.g. `ndviThreshold`) and array of values (e.g. `notAllowedDates`). - Dates of all tiles available before we filtered out those acquired on dates given in `notAllowedDates` array. These dates are listed in `tilesPPSDates` property of userData. Note how we used a global variable `tilesPPS`: we assigned it a value in `preProcessScenes` and output it in `updateOutputMetadata` function. - Dates of all tiles available after the filtering. These dates are listed in `tilesDates` property of userData. - Description of the processing implemented in the evalscript and links to external resources.

``` python
url = 'https://sh.dataspace.copernicus.eu'

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B08", "B04", "dataMask"],
    mosaicking: Mosaicking.TILE,
    output: {
      id: "default",
      bands: 1
    }
  }
}

// User's inputs
var notAllowedDates = ["2020-12-06", "2020-12-09"]
var ndviThreshold = 0.2

var tilesPPS = []
function preProcessScenes(collections) {
  tilesPPS = collections.scenes.tiles
  collections.scenes.tiles = collections.scenes.tiles.filter(function(tile) {
    var tileDate = tile.date.split("T")[0];
    return !notAllowedDates.includes(tileDate);
  })
  return collections
}

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {

  var valid_ndvi_sum = 0
  var numberOfValidSamples = 0
  for (i = 0; i < samples.length; i++) {
    var sample = samples[i]
    if (sample.dataMask == 1){
        var ndvi = (sample.B08 - sample.B04)/(sample.B08 + sample.B04)
        if (ndvi <= ndviThreshold){
          valid_ndvi_sum += ndvi
          numberOfValidSamples += 1
        }
    }
  }

  return [valid_ndvi_sum / numberOfValidSamples]
}

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
  outputMetadata.userData = {
    "inputMetadata.serviceVersion": inputMetadata.serviceVersion
  }

  outputMetadata.userData.description = "The evalscript calculates average ndvi " +
  "in a requested time period. Data collected on notAllowedDates is excluded. " +
  "ndvi values greater than ndviThreshold are excluded. " +
  "More about ndvi: https://www.indexdatabase.de/db/i-single.php?id=58."

  // Extract dates for all available tiles (before filtering)
  var tilePPSDates = []
  for (i = 0; i < tilesPPS.length; i++){
    tilePPSDates.push(tilesPPS[i].date)
  }
  outputMetadata.userData.tilesPPSDates = tilePPSDates

  // Extract dates for tiles after filtering out tiles with "notAllowedDates"
  var tileDates = []
  for (i = 0; i < scenes.tiles.length; i++){
    tileDates.push(scenes.tiles[i].date)
  }
  outputMetadata.userData.tilesDates = tileDates

  outputMetadata.userData.notAllowedDates = notAllowedDates
  outputMetadata.userData.ndviThreshold = ndviThreshold
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [13.8, 45.8, 13.9, 45.9]
    },
    "data": [{
      "type": "sentinel-2-l1c",
      "dataFilter": {
        "timeRange": {
          "from": "2020-12-01T00:00:00Z",
          "to": "2020-12-15T23:59:59Z"
        }
      }
    }]
  },
  "output": {
    "responses": [{
        "identifier": "default",
        "format": {
          "type": "image/tiff"
        }
      },
      {
        "identifier": "userdata",
        "format": {
          "type": "application/json"
        }
      }
    ]
  },
  "evalscript": evalscript
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/x-tar'
}

response = oauth.post(f"{url}/process/v1", headers=headers, json = request)

tar = tarfile.open(fileobj=io.BytesIO(response.content))
userdata = json.load(tar.extractfile(tar.getmember('userdata.json')))
userdata
```

## Filter tiles based on metadata

### Satellite (S2A vs S2B)

Here we parse original tile ids to get the information with which satellite, S2A or S2B, this tile was collected. Then we filter out the tiles acquired from the satellite S2A and only process the data acquired from the satellite S2B.

``` python
url = 'https://sh.dataspace.copernicus.eu'

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B02", "dataMask"],
    mosaicking: Mosaicking.TILE,
    output: {
      id: "default",
      bands: 1
    }
  }
}

function getSatelliteFromProductId(productId) {
  textParts = productId.split("_")
  satellite = textParts[0];
  return satellite
}

// Filter by satellite
function preProcessScenes(collections) {
  collections.scenes.tiles = collections.scenes.tiles.filter(function (tile) {
      return getSatelliteFromProductId(tile.productId) == "S2B"});
  return collections;
}

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {
  outputMetadata.userData = {
    "tiles": scenes.tiles
  }

  //Average value of band B02 based on the requested tiles
  var sumOfValidSamplesB02 = 0
  var numberOfValidSamples = 0
  for (i = 0; i < samples.length; i++) {
    var sample = samples[i]
    if (sample.dataMask == 1){
        sumOfValidSamplesB02 += sample.B02
        numberOfValidSamples += 1
    }
  }
  return [sumOfValidSamplesB02 / numberOfValidSamples]
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [13.8, 45.8, 13.9, 45.9]
    },
    "data": [{
      "type": "sentinel-2-l1c",
      "dataFilter": {
        "timeRange": {
          "from": "2020-12-01T00:00:00Z",
          "to": "2020-12-06T23:59:59Z"
        }
      }
    }]
  },
  "output": {
    "responses": [{
        "identifier": "default",
        "format": {
          "type": "image/tiff"
        }
      },
      {
        "identifier": "userdata",
        "format": {
          "type": "application/json"
        }
      }
    ]
  },
  "evalscript": evalscript
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/x-tar'
}

response = oauth.request("POST", f"{url}/process/v1", headers=headers, json = request)
tar = tarfile.open(fileobj=io.BytesIO(response.content))
userdata = json.load(tar.extractfile(tar.getmember('userdata.json')))
userdata
```

### Relative orbit id

This example shows how to filter tiles based on relative orbit id. The steps are: - We parse absolute orbit id from product id, which is available in `scenes` object and looks like `'S2B_MSIL1C_20201206T100409_N0209_R122_T33TUL_20201206T111219'`. This is done with the function `getRelativeOrbitIdFromProductId`. - Once we have a relative orbit id for each tile, we use `preProcessScenes` function to select tiles from the relative orbit 122.

``` python
url = 'https://sh.dataspace.copernicus.eu'

evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B02", "dataMask"],
    mosaicking: Mosaicking.TILE,
    output: {
      id: "default",
      bands: 1
    }
  }
}

function getRelativeOrbitIdFromProductId(productId) {
  textParts = productId.split("_")
  relativeOrbitId = parseInt(textParts[4].substring(1));
  return relativeOrbitId
}

// Filter by relative orbit id
function preProcessScenes(collections) {
  var allowedRelativeOrbits = [122]
  collections.scenes.tiles = collections.scenes.tiles.filter(function(tile) {
    var relativeOrbitId = getRelativeOrbitIdFromProductId(tile.productId);
    return allowedRelativeOrbits.includes(relativeOrbitId)
  })
  return collections;
}

function evaluatePixel(samples, scenes, inputMetadata, customData, outputMetadata) {
  outputMetadata.userData = {
    "scenes": scenes.tiles
  }

  //Average value of band B02 based on the requested tiles
  var sumOfValidSamplesB02 = 0
  var numberOfValidSamples = 0
  for (i = 0; i < samples.length; i++) {
    var sample = samples[i]
    if (sample.dataMask == 1){
        sumOfValidSamplesB02 += sample.B02
        numberOfValidSamples += 1
    }
  }
  return [sumOfValidSamplesB02 / numberOfValidSamples]
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [13.8, 45.8, 13.9, 45.9]
    },
    "data": [{
      "type": "sentinel-2-l1c",
      "dataFilter": {
        "timeRange": {
          "from": "2020-12-01T00:00:00Z",
          "to": "2020-12-06T23:59:59Z"
        }
      }
    }]
  },
  "output": {
    "responses": [{
        "identifier": "default",
        "format": {
          "type": "image/tiff"
        }
      },
      {
        "identifier": "userdata",
        "format": {
          "type": "application/json"
        }
      }
    ]
  },
  "evalscript": evalscript
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/x-tar'
}

response = oauth.request("POST", f"{url}/process/v1", headers=headers, json = request)

tar = tarfile.open(fileobj=io.BytesIO(response.content))
userdata = json.load(tar.extractfile(tar.getmember('userdata.json')))
userdata
```
