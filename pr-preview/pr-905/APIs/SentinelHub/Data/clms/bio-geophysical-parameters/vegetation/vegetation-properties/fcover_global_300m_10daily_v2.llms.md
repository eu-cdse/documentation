# Fraction of Green Vegetation Cover 2014-present (raster 300 m), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/fraction-of-green-vegetation-cover-v2-0-300m)

Provides information about the fraction of ground covered by green vegetation. Every 10-days estimates are available at global scale in the spatial resolution of ~ 300 m from January 2014 to the present.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_FCOVER_GLOBAL_300M_10DAILY_V2_RT0&clmsSelectedPath=Vegetation%20Properties&clmsSelectedCollection=COPERNICUS_CLMS_FCOVER_GLOBAL_300M_10DAILY_V2_RT0) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-4fea1f4f-7438-4e19-9890-2674347a278d` for the BYOC collection with id `4fea1f4f-7438-4e19-9890-2674347a278d`.

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
|   RT0   | `4fea1f4f-7438-4e19-9890-2674347a278d` |
|   RT1   | `b5617f5b-69a0-4054-a14b-d831fd43babf` |
|   RT2   | `47f6a6cc-0a44-4561-a6dc-05433be56d07` |
|   RT6   | `23bfb3d0-a265-4e3a-8203-23e4f09de82c` |

## Date range

2014 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FCOVER | Fraction of Green Vegetation Cover | \- | UINT8 | 0.0-1.0 | 1/250 | 0 |
| RMSE | Root Mean Square Error on FCOVER | \- | UINT8 | 0.0-1.0 | 1/250 | 0 |
| NOBS | Number of available valid instantaneous FCOVER | \- | UINT8 | 0.0-60.0 | 1 | 0 |
| LBEFORE | Length of the semi-period before the date \[days\] | days | UINT8 | 0.0-210.0 | 1 | 0 |
| LAFTER | Length of the semi-period after the date \[days\] | days | UINT8 | 0.0-60.0 | 1 | 0 |
| QFLAG | Bitwise quality flag | Quality Flag on Fraction of green Vegetation Cover | UINT8 | 0.0-254.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-properties/fcover_global_300m_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
