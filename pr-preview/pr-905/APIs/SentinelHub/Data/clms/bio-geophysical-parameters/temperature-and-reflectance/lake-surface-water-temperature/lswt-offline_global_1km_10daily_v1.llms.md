# Lake Surface Water Temperature 2002-2012 (raster 1 km), global, 10-daily, Offline – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/temperature-and-reflectance/lake-surface-water-temperature-offline-1km)

Provides the temperature of the water at the lake surface. The LSWT observations (every 10 days) are available at global scale at spatial resolution of ~1 km and with the temporal extent from 2002 to 2012.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_LSWT_OFFLINE_1KM_10DAILY_V1&clmsSelectedPath=Lake%20Surface%20Water%20Temperature&clmsSelectedCollection=COPERNICUS_CLMS_LSWT_OFFLINE_1KM_10DAILY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-db5aea5e-a0d1-487f-adff-ad8831933208` for the BYOC collection with id `db5aea5e-a0d1-487f-adff-ad8831933208`.

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

`db5aea5e-a0d1-487f-adff-ad8831933208`

## Date range

2002 - 2012

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| LSWT | Lake surface skin temperature, weighted average over the aggregation period. | Kelvin | INT16 | -200.0-5000.0 | 0.01 | 273.15 |
| UNC | Uncertainties on LSWT | Kelvin | INT16 | 0.0-10000.0 | 0.001 | 0 |
| STDEV | Standard deviation of the LSWT observations within the aggregation time period | Kelvin | INT16 | — | 0.001 | 0 |
| NOBS | Number of LSWT observations contributing to the average | \- | INT8 | 0.0-10.0 | 1 | 0 |
| QLEVEL | Quality level | Quality flags: 0=no_data, 1=bad_data, 2=worst_quality, 3=low_quality, 4=acceptable_quality, 5=best_quality | INT8 | — | 1 | 0 |
| TOBS | Bitwise observation time | Bit flags for days 1-11 within dekad | INT16 | — | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/temperature-and-reflectance/lake-surface-water-temperature/lswt-offline_global_1km_10daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
