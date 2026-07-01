##### Access Sentinel-1 Level 3 Monthly Mosaics with Sentinel Hub

Sentinel-1 Level 3 Monthly Mosaics are onboarded to Sentinel Hub as a BYOC data collection. To access the data, you will need the specific pieces of information listed below, for general information about how to access BYOC collections visit our [Data BYOC page](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/Byoc.html).

**IW Mosaics**

- Data collection id: byoc-3c662330-108b-4378-8899-525fd5a225cb
- Available Bands and Data:

| Name | Description | Resolution |
|----|----|----|
| VV | VV polarization | 20 m |
| VH | VH polarization | 20 m |
| dataMask | The mask of data/no data pixels ([more](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/UserGuides/Datamask.html)) | N/A\* |

\*dataMask has no source resolution as it is calculated for each output pixel.

###### Example of requesting mosaic over Sfântu Gheorghe with Processing API request

The request below is written in Python. To execute it, you need to create an OAuth client as is explained [here](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html#python). It is named `oauth` in this example.

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["VV", "VH", "dataMask"],
    output: { bands: 3 }
  };
}

var viz = new HighlightCompressVisualizer(0, 0.8);
var gain = 0.8;


function evaluatePixel(sample) {
  if (sample.dataMask == 0) {
    return [0, 0, 0];
  }
  
  let vals = [gain * sample.VV / 0.28,
              gain * sample.VH / 0.06,
              gain * sample.VH / sample.VV / 0.49];
  
  return viz.processList(vals);
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [
          25.713501,
          45.74836,
          26.196213,
          45.965231
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2023-09-01T00:00:00Z",
            "to": "2023-09-02T23:59:59Z"
          }
        },
        "type": "byoc-3c662330-108b-4378-8899-525fd5a225cb"
      }
    ]
  },
  "output": {
    "width": 512,
    "height": 330,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/process/v1"
response = oauth.post(url, json=request)
```

**DH Mosaics**

- Data collection id: byoc-cc676fec-cb8d-4bc1-adce-1d9658da950b
- Available Bands and Data:

| Name | Description | Resolution |
|----|----|----|
| HH | HH polarization | 40 m |
| HV | HV polarization | 40 m |
| dataMask | The mask of data/no data pixels ([more](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/UserGuides/Datamask.html)) | N/A\* |

\*dataMask has no source resolution as it is calculated for each output pixel.

###### Example of requesting mosaic over Reykjavík with Processing API request

The request below is written in Python. To execute it, you need to create an OAuth client as is explained [here](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html#python). It is named `oauth` in this example.

``` python
evalscript = """
//VERSION=3
function setup() {
  return {
    input: ["HH", "HV", "dataMask"],
    output: { bands: 4 }
  };
}

var viz = new HighlightCompressVisualizer(0, 0.8);
var gain = 0.8;


function evaluatePixel(sample) {
  let vals = [gain * sample.HH / 0.28,
              gain * sample.HV / 0.06,
              gain * sample.HV / sample.HH / 0.49];
  
  let out = viz.processList(vals);
  out.push(sample.dataMask);
  return out;
}
"""

request = {
  "input": {
    "bounds": {
      "bbox": [
          -22.486267,
          63.959085,
          -19.79187,
          64.722572
      ]
    },
    "data": [
      {
        "dataFilter": {
          "timeRange": {
            "from": "2023-01-01T00:00:00Z",
            "to": "2023-01-02T23:59:59Z"
          }
        },
        "type": "byoc-cc676fec-cb8d-4bc1-adce-1d9658da950b"
      }
    ]
  },
  "output": {
    "width": 858,
    "height": 553,
    "responses": [
      {
        "identifier": "default",
        "format": {
          "type": "image/jpeg"
        }
      }
    ]
  },
  "evalscript": evalscript,
}

url = "https://sh.dataspace.copernicus.eu/process/v1"
response = oauth.post(url, json=request)
```
