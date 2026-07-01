# FAPAR 2014-present (raster 300 m), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/fraction-of-absorbed-photosynthetically-active-radiation-v2-0-300m)

Quantifies the fraction of the solar radiation absorbed by live plants for photosynthesis. Every 10-days estimates are available at global scale, in the spatial resolution of ~ 300 m, from January 2014 to the present.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_FAPAR_300M_10DAILY_V2_RT0&clmsSelectedPath=Vegetation%20Properties&clmsSelectedCollection=COPERNICUS_CLMS_FAPAR_300M_10DAILY_V2_RT0) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-0dfe26be-b9ca-4286-b624-37591ea2addf` for the BYOC collection with id `0dfe26be-b9ca-4286-b624-37591ea2addf`.

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
|   RT0   | `0dfe26be-b9ca-4286-b624-37591ea2addf` |
|   RT1   | `5e850ca5-2925-40b2-b377-d2410cb7fa21` |
|   RT2   | `98358a1f-474e-45b0-abd8-7a543cbfe1ea` |
|   RT6   | `f3d558b9-7f12-46ff-aaef-7ea0dab397ed` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FAPAR | Fraction of Absorbed Photosynthetically Active Radiation | \- | UINT8 | 0.0-0.94 | 1/250 | 0 |
| RMSE | Root Mean Square Error on FAPAR | \- | UINT8 | 0.0-0.94 | 1/250 | 0 |
| QFLAG | Bitwise quality flag | \- | UINT8 | — | 1 | 0 |
| NOBS | Number of available valid instantaneous FAPAR | \- | UINT8 | 0.0-60.0 | 1 | 0 |
| LENGTH_BEFORE | Length of the semi-period before the date \[days\] | \- | UINT8 | 0.0-210.0 | 1 | 0 |
| LENGTH_AFTER | Length of the semi-period after the date \[days\] | \- | UINT8 | 0.0-60.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-properties/fapar_global_300m_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
