# SWI 2007-present (raster 12.5 km), global, 10-daily – version 3

## About

[Official documentation](https://land.copernicus.eu/en/products/soil-moisture/10-daily-soil-water-index-global-v3-0-12-5-km)

Averages the daily Soil Water Index product over 10 days. The data are produced every 10 days over the globe at the spatial resolution of 0.1° and with the temporal extent from January 2007 to present.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_SWI_12_5KM_10DAILY&clmsSelectedPath=Soil%20Water%20Index&clmsSelectedCollection=COPERNICUS_CLMS_SWI_12_5KM_10DAILY) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-fe52f4cb-c1f3-4d67-b040-73704bf0f2c3` for the BYOC collection with id `fe52f4cb-c1f3-4d67-b040-73704bf0f2c3`.

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

`fe52f4cb-c1f3-4d67-b040-73704bf0f2c3`

## Date range

2007 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| QFLAG001 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG005 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG010 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG015 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG020 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG040 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG060 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| QFLAG100 | Quality flag for different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI001 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI005 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI010 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI015 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI020 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI040 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI060 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| SWI100 | Soil Water Index at different time lengths | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS001 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS005 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS010 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS015 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS020 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS040 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS060 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |
| VOBS100 | Percentage of valid observations in the 10-day synthesis period. | % | UINT8 | 0.0-100.0 | 1/2 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/soil-moisture/soil-water-index/swi_global_12.5km_10daily_v3)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
