# DLT 10m Yearly (2018-present)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-forests-and-tree-cover)

The High Resolution Dominant Leaf Type (DLT) raster product provides a basic land cover classification with 3 thematic classes (all non-tree covered areas, broadleaved and coniferous).

This dataset is provided annually starting with 2018 in 10 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

High Resolution Layer Tree Cover and Forest product is part of the European Union’s Copernicus Land Monitoring Service. Confidence layer available for the dataset.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_DOMINANT-LEAF-TYPE_EUROPE_10M_YEARLY_V1&clmsSelectedPath=Dominant%20Leaf%20Type&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_DOMINANT-LEAF-TYPE_EUROPE_10M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-42b2ef44-5983-4bd1-9e2f-52c093c08b3d` for the BYOC collection with id `42b2ef44-5983-4bd1-9e2f-52c093c08b3d`.

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
| Dominant Leaf Type | `42b2ef44-5983-4bd1-9e2f-52c093c08b3d` |
| Dominant Leaf Type Confidence Layer | `626dc954-9177-41f3-84c9-d2119402e524` |

## Date range

2018 - present

## Bands

Dominant Leaf Type

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| DLT | Dominant leaf type classification | 0 = All non-tree covered areas, 1 = Broadleaved trees, 2 = Coniferous trees | UINT8 | 0.0-2.0 | 1 | 0 |

Dominant Leaf Type Confidence Layer

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| DLTCL | Confidence of dominant leaf type | Confidence percentage (0-100%) | UINT8 | 0.0-253.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/tree-cover-and-forests/dominant-leaf-type/dominant-leaf-type/clms_vlcc_dominant-leaf-type_europe_10m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
