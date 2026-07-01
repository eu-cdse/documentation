# GPP 2014-present (raster 300 m), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/gross-primary-production-v2-0-300m)

Provides information about the total amount of carbon compounds produced by photosynthesis of plants in an ecosystem in a given period of time, expressed in gC/m²/day. Every 10-days, estimates are available at global scale, at a spatial resolution of ~ 300 m, from January 2014 to the present.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=&clmsSelectedPath=Net%2FGross%20Primary%20Production&clmsSelectedCollection=) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-eacf6c34-a3db-4b3b-bdf9-0feba8eed996` for the BYOC collection with id `eacf6c34-a3db-4b3b-bdf9-0feba8eed996`.

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
|   RT0   | `eacf6c34-a3db-4b3b-bdf9-0feba8eed996` |
|   RT1   | `f37f3647-c076-4dc1-9b0e-3ad129521bf4` |
|   RT2   | `42d86587-3a2b-4394-8588-7d5e0238574d` |
|   RT6   | `7e2d31f2-80ef-4d9c-bd81-da59e40b0eea` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| GPP | Gross Primary Production value | gC/m²/day | INT16 | 0.0-32.767 | 1/1000 | 0 |
| QFLAG | Quality flag indicator | \- | UINT8 | — | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/net-gross-primary-production/gpp_global_300m_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
