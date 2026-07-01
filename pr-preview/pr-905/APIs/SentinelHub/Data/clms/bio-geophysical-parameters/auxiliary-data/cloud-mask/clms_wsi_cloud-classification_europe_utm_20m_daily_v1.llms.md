# Sentinel-2 CC Europe 20m Daily V1

## About

[Official documentation](https://land.copernicus.eu/en/products/snow/fractional-snow-cover)

The Cloud Classification (CC) product provides information on the extent of clouds and cloud shadows derived from optical satellite data acquired by the Sentinel-2 constellation. It is generated in near real-time at European scale, with a pixel spacing of 20 m x 20 m. Cloud detection is performed at a 120m spatial resolution. It is available for the period from 2016 to the present and used to produce the CLMS High-Resolution Water, Snow and Ice datasets (HR-WSI), which rely on Sentinel-2 imagery. More information in the products documentation here.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_WSI_CLOUD-CLASSIFICATION_EUROPE_UTM_20M_DAILY_V1&clmsSelectedPath=Cloud%20Mask&clmsSelectedCollection=COPERNICUS_CLMS_WSI_CLOUD-CLASSIFICATION_EUROPE_UTM_20M_DAILY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-64d015da-e225-48d8-9643-30a453657beb` for the BYOC collection with id `64d015da-e225-48d8-9643-30a453657beb`.

[Check out this example request](../../../../../../../APIs/SentinelHub/Process/Examples/BYOC.llms.md)

#### sentinelhub Python package

For using the [sentinelhub Python package](https://sentinelhub-py.readthedocs.io/en/latest/index.html), please provide the `collectionId` as follows:

``` python
byoc_collection = DataCollection.define_byoc(
    collection_id="<collectionId>"
)
```

[Check out this Jupyter Notebook example](../../../../../../../notebook-samples/sentinelhub/cloudless_process_api.llms.md)

[Click here](../../../../../../../APIs/SentinelHub/Byoc.llms.md) for more information about the BYOC API.

### Collection ID

`64d015da-e225-48d8-9643-30a453657beb`

## Date range

2016 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CC | Cloud and cloud shadow classification of the Sentinel-2 image | Cloud classification: 0=No Data, 1=Clear, 2=Cloud Shadow, 3=Cloud | UINT8 | 0.0-3.0 | 1 | 0 |
| CC_QA | Quality layer for the cloud and cloud shadow classification (CC) layer | Quality assessment for CC layer. Indicators for defects such as missing pixels and cloudy data. | UINT8 | 0.0-255.0 | 1 | 0 |
| QAFLAGS | Quality flags | Bitmask with quality flags. Bit 0: cloud detection using single-scene threshold approach. | UINT8 | 0.0-255.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/auxiliary-data/cloud-mask/clms_wsi_cloud-classification_europe_utm_20m_daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
