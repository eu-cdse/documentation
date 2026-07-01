# FAPAR 2014-present (raster 300 m), global, 10-daily – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/fraction-of-absorbed-photosynthetically-active-radiation-v1-0-300m)

Quantifies the fraction of the solar radiation absorbed by live plants for photosynthesis. Every 10-days estimates are available in near real time at global scale in the spatial resolution of about 300 m from January 2014 to June 2020 based upon PROBA-V data with version 1.0 and from July 2020 onwards based upon Sentinel-3/OLCI data with version 1.1.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_FAPAR_300M_10DAILY&clmsSelectedPath=Vegetation%20Properties&clmsSelectedCollection=COPERNICUS_CLMS_FAPAR_300M_10DAILY) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-302c25ab-3d8c-4783-8123-9a231660e98a` for the BYOC collection with id `302c25ab-3d8c-4783-8123-9a231660e98a`.

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
|  None   | `302c25ab-3d8c-4783-8123-9a231660e98a` |
|   RT0   | `4dcb63e9-9527-4293-a3b8-74b763887d04` |
|   RT1   | `b4e696d6-d622-4157-871b-99b599a1f6cc` |
|   RT2   | `6492eee5-ea96-4cef-a11b-a8aaa7b6a180` |
|   RT6   | `453f68c6-f2a9-462c-8bc6-74343fc4f638` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FAPAR | Fraction of Absorbed Photosynthetically Active Radiation | \- | UINT8 | 0.0-0.94 | 1/250 | 0 |
| RMSE | RMSE on FAPAR | \- | UINT8 | 0.0-0.94 | 1/250 | 0 |
| QFLAG | Quality flag | \- | UINT8 | — | 1 | 0 |
| NOBS | Number of available valid instantaneous estimates in the compositing window | \- | UINT8 | 0.0-40.0 | 1 | 0 |
| LENGTH_BEFORE | Length in days of semi-period before D | \- | UINT8 | 15.0-210.0 | 1 | 0 |
| LENGTH_AFTER | Length in days of semi-period after D | \- | UINT8 | 0.0-60.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-properties/fapar_global_300m_10daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
