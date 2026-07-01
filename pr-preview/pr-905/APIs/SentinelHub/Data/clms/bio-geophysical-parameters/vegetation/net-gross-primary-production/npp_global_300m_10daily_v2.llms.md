# NPP 2014-present (raster 300 m), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/net-primary-production-v2-0-300m)

Provides information about the net amount of biomass, or carbon, produced by plants per unit area and time, expressed in gC/m²/day. It is equal to the difference between the Gross Primary Production (GPP), i.e. the total amount of carbon produced through photosynthesis, and the amount of energy used for plant respiration. Every 10-days, estimates are available at global scale, at a spatial resolution of ~ 300 m, from January 2014 to the present.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_NPP_GLOBAL_300M_10DAILY_V2_RT0&clmsSelectedPath=Net%2FGross%20Primary%20Production&clmsSelectedCollection=COPERNICUS_CLMS_NPP_GLOBAL_300M_10DAILY_V2_RT0) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-40fdc188-1ba7-4c62-a2f8-5d057451dcf9` for the BYOC collection with id `40fdc188-1ba7-4c62-a2f8-5d057451dcf9`.

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
|   RT0   | `40fdc188-1ba7-4c62-a2f8-5d057451dcf9` |
|   RT1   | `4c50c693-ff8f-4a44-a095-ef4dfec3e234` |
|   RT2   | `48ada5a5-b721-4181-b87b-68957e7b1c8a` |
|   RT6   | `c1390928-f7ee-4d50-af81-b0872e0aceff` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| NPP | Net Primary Production (gC/m²/day) | gC/m²/day | INT16 | 0.0-16.3835 | 1/2000 | 0 |
| QFLAG | Quality Flag on Net Primary Production | \- | UINT8 | — | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/net-gross-primary-production/npp_global_300m_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
