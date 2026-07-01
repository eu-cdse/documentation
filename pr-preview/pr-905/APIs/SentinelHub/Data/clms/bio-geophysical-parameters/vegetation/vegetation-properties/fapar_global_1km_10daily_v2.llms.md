# FAPAR 1999-2020 (raster 1 km), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/fraction-of-absorbed-photosynthetically-active-radiation-v2-0-1km)

FAPAR quantifies the fraction of the solar radiation absorbed by live plants for photosynthesis. Every 10-days estimates are available at global scale in the spatial resolution of about 1 km covering the period from 1999 to June 2020 from SPOT/VEGETATION and PROBA-V data.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_FAPAR_1KM_10DAILY&clmsSelectedPath=Vegetation%20Properties&clmsSelectedCollection=COPERNICUS_CLMS_FAPAR_1KM_10DAILY) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-288befb5-6ce6-4aae-9fb8-e6e4531216a1` for the BYOC collection with id `288befb5-6ce6-4aae-9fb8-e6e4531216a1`.

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

| Version | ID                                     |
|:-------:|----------------------------------------|
|  None   | `288befb5-6ce6-4aae-9fb8-e6e4531216a1` |
|   RT0   | `c59b1cb0-50ef-4737-a863-463c1056c66c` |
|   RT1   | `e9a0a9ec-5614-4747-bcdb-e4942d5af0b2` |
|   RT2   | `8bf7f8a0-09d5-4167-a53b-9e3f6676a488` |
|   RT6   | `990a6aca-4a63-4d47-94e2-6b948af1b603` |

## Date range

1999 - 2020

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FAPAR | Fraction of Absorbed PAR | \- | UINT8 | 0.0-0.94 | 1/250 | 0 |
| RMSE | Uncertainty on the FAPAR | \- | UINT8 | 0.0-0.94 | 1/250 | 0 |
| QFLAG | Quality flag | \- | UINT16 | — | 1 | 0 |
| NOBS | Number of valid observations during the synthesis period | \- | UINT8 | 0.0-120.0 | 1 | 0 |
| LENGTH_BEFORE | Length in days of the semi-period before the dekadal date of the compositing window | \- | UINT8 | 5.0-60.0 | 1 | 0 |
| LENGTH_AFTER | Length in days of the semi-period after the dekadal date of the compositing window | \- | UINT8 | 5.0-60.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-properties/fapar_global_1km_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
