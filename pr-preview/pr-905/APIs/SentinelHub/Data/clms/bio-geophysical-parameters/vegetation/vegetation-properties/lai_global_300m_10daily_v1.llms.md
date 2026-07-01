# LAI 2014-present (raster 300 m), global, 10-daily – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/leaf-area-index-300m-v1.0)

Defined as half the total area of green elements of the canopy per unit horizontal ground area. Every 10-days estimates are available in near real time at global scale in the spatial resolution of about 300 m from January 2014 to June 2020 based upon PROBA-V data with version 1.0 and from July 2020 onwards based upon Sentinel-3/OLCI data with version 1.1.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_LAI_300M_10DAILY&clmsSelectedPath=Vegetation%20Properties&clmsSelectedCollection=COPERNICUS_CLMS_LAI_300M_10DAILY) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-b6317fa9-c341-4c7f-a81f-24615f57c868` for the BYOC collection with id `b6317fa9-c341-4c7f-a81f-24615f57c868`.

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
|  None   | `b6317fa9-c341-4c7f-a81f-24615f57c868` |
|   RT0   | `6c90d3aa-4e57-4f08-a837-23ba6df3429a` |
|   RT1   | `2cb83160-105c-4072-9fb3-51e47ddc9f1a` |
|   RT2   | `8d7a4caa-b58c-4658-9aa0-ca155b670662` |
|   RT6   | `559b2871-ddbd-41f9-8ab0-5242a454e411` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| LAI | Leaf Area Index | \- | UINT8 | 0.0-7.0 | 1/30 | 0 |
| LENGTH_BEFORE | Length in days of semi-period before D | \- | UINT8 | 15.0-210.0 | 1 | 0 |
| LENGTH_AFTER | Length in days of semi-period after D | \- | UINT8 | 0.0-60.0 | 1 | 0 |
| NOBS | Number of available valid instantaneous estimates in the compositing window | \- | UINT8 | 0.0-60.0 | 1 | 0 |
| RMSE | RMSE on LAI | \- | UINT8 | 0.0-7.0 | 1/30 | 0 |
| QFLAG | Quality Flag | \- | UINT8 | — | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-properties/lai_global_300m_10daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
