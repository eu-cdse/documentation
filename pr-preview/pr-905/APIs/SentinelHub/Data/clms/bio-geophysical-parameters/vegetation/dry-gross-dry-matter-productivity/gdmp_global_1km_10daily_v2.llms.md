# GDMP 1999-2020 (raster 1 km), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/gross-dry-matter-productivity-v2-0-1km)

GDMP is equivalent to Gross Primary Production (GPP). Every 10-days estimates are available at global scale in the spatial resolution of about 1km and with the temporal extent from 1999 to June 2020.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_GDMP_1KM_10DAILY_V2&clmsSelectedPath=Dry%2FGross%20Dry%20Matter%20Productivity&clmsSelectedCollection=COPERNICUS_CLMS_GDMP_1KM_10DAILY_V2) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-7bf3dc12-3662-4844-ac8f-cc120710731a` for the BYOC collection with id `7bf3dc12-3662-4844-ac8f-cc120710731a`.

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
|  None   | `7bf3dc12-3662-4844-ac8f-cc120710731a` |
|   RT0   | `f35460ee-178b-404f-85d5-0349c9ec6e7c` |
|   RT1   | `c8ce04cf-5bca-41a3-b90c-8904e9655ce4` |
|   RT2   | `075d7c80-8170-4f65-b7cf-39976219e74a` |
|   RT6   | `f20cd28d-6d06-430e-8deb-5abce20a6700` |

## Date range

1999 - 2020

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| GDMP | Gross Dry Matter Productivity | kg/ha/day | INT16 | 0.0-655.34 | 1/50 | 0 |
| QFLAG | Bitwise quality flag | \- | UINT8 | — | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/dry-gross-dry-matter-productivity/gdmp_global_1km_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
