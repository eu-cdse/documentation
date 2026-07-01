# Examples for S3SYNL2

The requests below are written in python. To execute them you need to create an OAuth client as explained [here](../../../../APIs/SentinelHub/Overview/Authentication.llms.md#python). It is named `oauth` in these examples.

### True Color

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["B08", "B06", "B04"],
    output: {
      bands: 3,
      sampleType: "AUTO", // default value - scales the output values from [0,1] to [0,255].
    },
  }
}

function evaluatePixel(sample) {
  return [2.5 * sample.B08, 2.5 * sample.B06, 2.5 * sample.B04]
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
            "bbox": [
                8.3333,
                41.3149,
                9.7009,
                43.0568,
            ],
        },
        "data": [
            {
                "type": "sentinel-3-synergy-l2",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-04-04T00:00:00Z",
                        "to": "2020-04-05T00:00:00Z",
                    }
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [{"format": {"type": "image/png"}}],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/process/v1"
response = oauth.post(url, json=request)
```

### Normalized difference vegetation index, computed from surface reflectances

``` python
evalscript = """
//VERSION=3

function evaluatePixel(samples) {
    if (samples.dataMask == 0) return [0,0,0,0];

    var val = samples.NDVI_V10;
    if (val<-1.1) return [0,0,0,1];
else if (val<-0.2) return [0.75,0.75,0.75,1];
else if (val<-0.1) return [0.86,0.86,0.86,1];
else if (val<0) return [1,1,0.88,1];
else if (val<0.025) return [1,0.98,0.8,1];
else if (val<0.05) return [0.93,0.91,0.71,1];
else if (val<0.075) return [0.87,0.85,0.61,1];
else if (val<0.1) return [0.8,0.78,0.51,1];
else if (val<0.125) return [0.74,0.72,0.42,1];
else if (val<0.15) return [0.69,0.76,0.38,1];
else if (val<0.175) return [0.64,0.8,0.35,1];
else if (val<0.2) return [0.57,0.75,0.32,1];
else if (val<0.25) return [0.5,0.7,0.28,1];
else if (val<0.3) return [0.44,0.64,0.25,1];
else if (val<0.35) return [0.38,0.59,0.21,1];
else if (val<0.4) return [0.31,0.54,0.18,1];
else if (val<0.45) return [0.25,0.49,0.14,1];
else if (val<0.5) return [0.19,0.43,0.11,1];
else if (val<0.55) return [0.13,0.38,0.07,1];
else if (val<0.6) return [0.06,0.33,0.04,1];
else return [0,0.27,0,1];
}

function setup() {
  return {
    input: [{
      bands: [
        "NDVI_V10",
        "dataMask"
      ]
    }],
    output: {
      bands: 4
    }
  }
}
"""

request = {
    "input": {
        "bounds": {
            "properties": {"crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"},
            "bbox": [
                8.3333,
                41.3149,
                9.7009,
                43.0568,
            ],
        },
        "data": [
            {
                "type": "sentinel-3-synergy-l2",
                "dataFilter": {
                    "timeRange": {
                        "from": "2020-04-04T00:00:00Z",
                        "to": "2020-04-05T00:00:00Z",
                    }
                },
            }
        ],
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [{"format": {"type": "image/png"}}],
    },
    "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/process/v1"
response = oauth.post(url, json=request)
```
