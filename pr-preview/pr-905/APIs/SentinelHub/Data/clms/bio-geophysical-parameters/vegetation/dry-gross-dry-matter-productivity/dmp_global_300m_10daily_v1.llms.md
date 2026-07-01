# DMP 2014-present (raster 300 m), global, 10-daily – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/dry-matter-productivity-v1-0-300m)

Represents the overall growth rate or dry biomass increase of the vegetation and is directly related to ecosystem Net Primary Production (NPP), however with units customized for agro-statistical purposes (kg/ha/day). Every 10-days estimates are available in near real time at global scale in the spatial resolution of about 300 m from January 2014 to June 2020 based upon PROBA-V data with version 1.0 and from July 2020 onwards based upon Sentinel-3/OLCI data with version 1.1.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_DMP_300M_10DAILY_RT0&clmsSelectedPath=Dry%2FGross%20Dry%20Matter%20Productivity&clmsSelectedCollection=COPERNICUS_CLMS_DMP_300M_10DAILY_RT0) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-a952e004-9e4c-41b8-a75d-b0516bcccadc` for the BYOC collection with id `a952e004-9e4c-41b8-a75d-b0516bcccadc`.

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
|   RT0   | `a952e004-9e4c-41b8-a75d-b0516bcccadc` |
|   RT1   | `c3302784-5238-4524-ac0c-689586819b3b` |
|   RT2   | `d7c77de5-3a7b-406e-823e-253b2394707d` |
|   RT5   | `3b23589d-b748-4b8a-b7ea-59a61d9ef2e1` |
|   RT6   | `e6352a02-c52e-4258-8541-6f92ca98359c` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| DMP | Dry Matter Productivity | kg/ha/day | INT16 | 0.0-327.67 | 1/100 | 0 |
| QFLAG | Bitwise quality flag | \- | UINT8 | — | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/dry-gross-dry-matter-productivity/dmp_global_300m_10daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
