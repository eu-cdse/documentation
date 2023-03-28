---
title: Examples for S3SLSTR
---

To request data using any of the request below, you will need to replace
the string `<your access token>` with your Sentinel Hub access token.
Sentinel Hub access token will look something like this:

``` default
ayJhbGciOiJSUzI1NiJ9.ayJzdWIiOiI0MmYwODZjCy1kMzI3LTRlOTMtYWMxNS00ODAwOGFiZjI0YjIiLCJhdWQiOiJlY2I1MGM1Zi1i
MWM1LTQ3ZTgtYWE4NC0zZTU4NzJlM2I2MTEiLCJqdGkiOiI5MzYxMWE4ODEyNTM4Y2M0MmU0NDJjYjUyMTY0YmJlNyIsImV4cCI6MTU1N
TQyMzk3MiwibmFtZSI6ImFuamEudnJlY2tvQHNpbmVyZ2lzZS5jb20iLCJlbWFpbCI6ImFuamEudnJlY2tvQHNpbmVyZ2lzZS5jb20iLC
JzaWQiOiIzZjVjZDVkNS04MjRiLTQ3ZjYtODgwNy0wNDMyNWY4ODQxZmQifQ.U7FPOy_2jlEOFxXSjyN5KEdBROna3-Dyec0feShIbUOY
1p9lEXdNaMmR5euiINi2RXDayX9Kr47CuSTsvq1zHFvZs1YgkFr1iH6kDuX-t_-wfWpqu5oPjoPVKZ4Rj0Ms_dxAUTQFTXR0rlbLuO-KS
gnaeLVb5iiv_qY3Ctq2XKdIRcFRQLFziFcP4yZJl-NZMlwzsiiwjakcpYpI5jSYAdU2hpZLHRzceseeZt5YfZOe5Px1kZXro9Nd0L2GPC
-qzOXw_V1saMGFa2ov8qV6Dvk92iv2SDDdGhOdII_JOf8XkK4E3g2z0EEFdWhG9F4Iky4ukNsqBPgE8LRb31s0hg
```

and can be obtained as described in the [Authentication
chapter](/APIs/SentinelHub/Overview/Authentication.md).

### False Color

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["S3", "S2", "S1"],
    output: {
      bands: 3,
      sampleType: "AUTO",
    },
  }
}

function evaluatePixel(sample) {
  return [2 * sample.S3, 2 * sample.S2, 2 * sample.S1]
}
"""

request = {
    "input": {
        "bounds": {
            "bbox": [
                8.558382,
                41.359678,
                9.579525,
                43.055688,
            ],
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/4326"
            },
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {"format": {"type": "image/png"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```

### False Color (EPSG 32632)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["S3", "S2", "S1"],
    output: {
      bands: 3,
      sampleType: "AUTO",
    },
  }
}

function evaluatePixel(sample) {
  return [2 * sample.S3, 2 * sample.S2, 2 * sample.S1]
}
"""

request = {
    "input": {
        "bounds": {
            "bbox": [
                444170,
                4574059,
                557052,
                4767386,
            ],
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/32632"
            },
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {"format": {"type": "image/png"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```

### False Color, resolution (EPSG 32632)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["S3", "S2", "S1"],
    output: {
      bands: 3,
      sampleType: "AUTO",
    },
  }
}

function evaluatePixel(sample) {
  return [2 * sample.S3, 2 * sample.S2, 2 * sample.S1]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/32632"
            },
            "bbox": [
                444170,
                4574059,
                557052,
                4767386,
            ],
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "resx": 250,
        "resy": 250,
        "responses": [
            {"format": {"type": "image/png"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```

### Thermal IR fire emission band, gradient visualizer (K)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["F1"],
    output: {
      bands: 3,
    },
  }
}

// Create a Red gradient visualiser from 274-450 K
var viz = ColorGradientVisualizer.createRedTemperature(274, 450)

function evaluatePixel(sample) {
  return viz.process(sample.F1)
}
"""

request = {
    "input": {
        "bounds": {
            "bbox": [
                -120.141,
                37.5282,
                -119.4131,
                37.8716,
            ],
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/4326"
            },
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2018-08-06T00:00:00Z",
                        "to": "2018-08-06T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {"format": {"type": "image/png"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```

### False Color and metadata (multi-part GeoTIFF and json)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["S3", "S2", "S1"],
    output: {
      id: "default",
      bands: 3,
      sampleType: "INT16", //floating point values are automatically rounded to the nearest integer by the service.
    },
    mosaicking: "TILE",
  }
}

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
  outputMetadata.userData = { scenes: scenes.tiles }
}

function evaluatePixel(sample) {
  // Return reflectance multiplied by 10000 as integers to save processing units.
  // To obtain reflectance values, simply divide the result pixel values by 10000.
  return [sample[0].S3 * 10000, sample[0].S2 * 10000, sample[0].S1 * 10000] //the values are multiplied by 10000 because output sampleType is UINT16
}
"""

request = {
    "input": {
        "bounds": {
            "bbox": [
                8.558382,
                41.359678,
                9.579525,
                43.055688,
            ],
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/4326"
            },
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {
                "identifier": "default",
                "format": {"type": "image/tiff"},
            },
            {
                "identifier": "userdata",
                "format": {
                    "type": "application/json"
                },
            },
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request, headers={"Accept": "application/tar"})
```

### NDVI as jpeg image with bouds given as polygon

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["S2", "S3"],
    output: {
      bands: 3,
    },
  }
}

function evaluatePixel(sample) {
  let NDVI = index(sample.S3, sample.S2)
  const viz = ColorGradientVisualizer.createWhiteGreen(-0.1, 1.0)
  return viz.process(NDVI)
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/32632"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            535547.7290897672,
                            4767538.771691742,
                        ],
                        [
                            542559.6872296461,
                            4744749.907737136,
                        ],
                        [
                            550448.1401370098,
                            4660606.41005859,
                        ],
                        [
                            521523.8128100095,
                            4570327.449007649,
                        ],
                        [
                            474193.0953658272,
                            4600128.271102134,
                        ],
                        [
                            461045.67385355436,
                            4630805.5879641045,
                        ],
                        [
                            453157.22094619065,
                            4698295.685060439,
                        ],
                        [
                            497858.45408791833,
                            4741243.928667196,
                        ],
                        [
                            520647.3180425246,
                            4744749.907737136,
                        ],
                        [
                            525906.2866474338,
                            4771044.750761681,
                        ],
                        [
                            525906.2866474338,
                            4771044.750761681,
                        ],
                        [
                            525906.2866474338,
                            4771044.750761681,
                        ],
                        [
                            535547.7290897672,
                            4767538.771691742,
                        ],
                    ]
                ],
            },
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {"format": {"type": "image/jpeg"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```

### NDVI image and value (multi-part response png and GeoTIFF)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: [
      {
        bands: ["S2", "S3"],
      },
    ],
    output: [
      {
        id: "default",
        bands: 1,
        sampleType: "INT16",
      },
      {
        id: "ndvi_image",
        bands: 3,
        sampleType: "AUTO",
      },
    ],
  }
}

function evaluatePixel(sample) {
  let NDVI = index(sample.S3, sample.S2)
  const viz = ColorGradientVisualizer.createWhiteGreen(-0.1, 1.0)
  return {
    default: [NDVI * 10000],
    ndvi_image: viz.process(NDVI),
  }
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/32632"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            535547.7290897672,
                            4767538.771691742,
                        ],
                        [
                            542559.6872296461,
                            4744749.907737136,
                        ],
                        [
                            550448.1401370098,
                            4660606.41005859,
                        ],
                        [
                            521523.8128100095,
                            4570327.449007649,
                        ],
                        [
                            474193.0953658272,
                            4600128.271102134,
                        ],
                        [
                            461045.67385355436,
                            4630805.5879641045,
                        ],
                        [
                            453157.22094619065,
                            4698295.685060439,
                        ],
                        [
                            497858.45408791833,
                            4741243.928667196,
                        ],
                        [
                            520647.3180425246,
                            4744749.907737136,
                        ],
                        [
                            525906.2866474338,
                            4771044.750761681,
                        ],
                        [
                            525906.2866474338,
                            4771044.750761681,
                        ],
                        [
                            525906.2866474338,
                            4771044.750761681,
                        ],
                        [
                            535547.7290897672,
                            4767538.771691742,
                        ],
                    ]
                ],
            },
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {
                "identifier": "ndvi_image",
                "format": {"type": "image/png"},
            },
            {
                "identifier": "default",
                "format": {"type": "image/tiff"},
            },
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request, headers={"Accept": "application/tar"})
```

### VNIR and SWIR bands as a GeoTIFF (EPSG 32632)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: [
      {
        bands: ["S1", "S2", "S3", "S4", "S5", "S6"],
        units: "REFLECTANCE",
      },
    ],
    output: {
      bands: 6,
      sampleType: "UINT16", //floating point values are automatically rounded to the nearest integer by the service.
    },
  }
}

function evaluatePixel(sample) {
  // Return reflectance multiplied by 10000 as integers to save processing units.
  // To obtain reflectance or BT values, simply divide the resulting pixel values by 10000.
  return [
    10000 * sample.S1,
    10000 * sample.S2,
    10000 * sample.S3,
    10000 * sample.S4,
    10000 * sample.S5,
    10000 * sample.S6,
  ]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/32632"
            },
            "bbox": [
                444170,
                4574059,
                557052,
                4767386,
            ],
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "resx": 500,
        "resy": 500,
        "responses": [
            {"format": {"type": "image/tiff"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```

### TIR bands as a GeoTIFF (EPSG 32632)

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: [
      {
        bands: ["S7", "S8", "S9", "F1", "F2"],
      },
    ],
    output: {
      bands: 5,
      sampleType: "UINT16",
    },
  }
}

function multiplyband(sample) {
  // Multiply by 100
  return 100 * sample
}

function evaluatePixel(sample) {
  // Return the bands multiplied by 100 as integers to save processing units.
  // To obtain reflectance or BT values, simply divide the resulting pixel values by 100.
  return [
    multiplyband(sample.S7),
    multiplyband(sample.S8),
    multiplyband(sample.S9),
    multiplyband(sample.F1),
    multiplyband(sample.F2),
  ]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {
                "crs": "http://www.opengis.net/def/crs/EPSG/0/32632"
            },
            "bbox": [
                444170,
                4574059,
                557052,
                4767386,
            ],
        },
        "data": [
            {
                "type": "sentinel-3-slstr",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-06-20T00:00:00Z",
                        "to": "2020-06-20T23:59:59Z",
                    },
                    "orbitDirection": "DESCENDING",
                },
            }
        ],
    },
    "output": {
        "resx": 500,
        "resy": 500,
        "responses": [
            {"format": {"type": "image/tiff"}}
        ],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/process"
response = requests.post(url, json=request)
```
