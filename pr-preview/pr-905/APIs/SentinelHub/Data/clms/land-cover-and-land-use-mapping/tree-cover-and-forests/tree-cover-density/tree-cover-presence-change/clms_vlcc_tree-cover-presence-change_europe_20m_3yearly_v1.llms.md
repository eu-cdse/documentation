# TCPC 20m 3yearly (2018-2021)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-forests-and-tree-cover)

The Copernicus High Resolution Layer Tree Cover Precense Change (TCPC) 2018-2021 raster product provides information on the change between the reference years 2018 and 2021 and consists of 4 thematic classes (unchanged areas with no tree cover / new tree cover / loss of tree cover / unchanged areas with tree cover). The class 255 = outside area is predefined by the 100m boundary layer and remains unchanged. This layer for previous reference year compraissions is called Tree Cover Change Mask (TCCM).

This dataset is provided in 20 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

The production of the high resolution forest layers was coordinated by the European Environment Agency (EEA) in the frame of the EU Copernicus programme.

Confidence layer available for the dataset.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_TREE-COVER-PRESENCE-CHANGE_EUROPE_20M_3YEARLY_V1&clmsSelectedPath=Tree%20Cover%20Presence%20Change&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_TREE-COVER-PRESENCE-CHANGE_EUROPE_20M_3YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-c1e547c2-47ec-4ce7-b87c-3057faba5ecc` for the BYOC collection with id `c1e547c2-47ec-4ce7-b87c-3057faba5ecc`.

[Check out this example request](../../../../../../../../APIs/SentinelHub/Process/Examples/BYOC.llms.md)

#### sentinelhub Python package

For using the [sentinelhub Python package](https://sentinelhub-py.readthedocs.io/en/latest/index.html), please provide the `collectionId` as follows:

``` python
byoc_collection = DataCollection.define_byoc(
    collection_id="<collectionId>"
)
```

[Check out this Jupyter Notebook example](../../../../../../../../notebook-samples/sentinelhub/cloudless_process_api.llms.md)

[Click here](../../../../../../../../APIs/SentinelHub/Byoc.llms.md) for more information about the BYOC API.

### Collection ID

| Collection | ID |
|:--:|----|
| Tree Cover Presence Change | `c1e547c2-47ec-4ce7-b87c-3057faba5ecc` |
| Tree Cover Presence Change Confidence Layer | `86fea022-0a9a-44b1-81c6-61df8d508712` |

## Date range

2018 - 2021

## Bands

Tree Cover Presence Change

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| TCPC | Tree cover extent change | 0: unchanged areas with no tree cover;1: new tree cover;2: loss of tree cover;10: unchanged areas with tree cover;255: outside area | UINT8 | 0.0-10.0 | 1 | 0 |

Tree Cover Presence Change Confidence Layer

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| TCPCCL | Confidence of tree cover change | None | UINT8 | 0.0-253.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/tree-cover-and-forests/tree-cover-density/tree-cover-presence-change/clms_vlcc_tree-cover-presence-change_europe_20m_3yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
