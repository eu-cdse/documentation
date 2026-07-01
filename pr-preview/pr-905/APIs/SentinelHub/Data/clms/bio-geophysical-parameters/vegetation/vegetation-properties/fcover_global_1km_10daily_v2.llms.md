# FCOVER 1999-2020 (raster 1 km), global, 10-daily – version 2

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/fraction-of-green-vegetation-cover-v2-0-1km)

FCOVER corresponds to the fraction of ground covered by green vegetation. It quantifies the spatial extent of the vegetation. Every 10-days estimates are available at global scale in the spatial resolution of about 1 km covering the period from 1999 to June 2020 from SPOT/VEGETATION and PROBA-V data.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_FCOVER_1KM_10DAILY&clmsSelectedPath=Vegetation%20Properties&clmsSelectedCollection=COPERNICUS_CLMS_FCOVER_1KM_10DAILY) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-44f54dfc-a372-4a22-988b-4b054880bb2a` for the BYOC collection with id `44f54dfc-a372-4a22-988b-4b054880bb2a`.

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
|  None   | `44f54dfc-a372-4a22-988b-4b054880bb2a` |
|   RT0   | `8f6a4b38-934c-4363-ac20-8427f20760c0` |
|   RT1   | `3e88055a-b8c3-4c68-acc6-4b93509b1f14` |
|   RT2   | `80fc6bcf-bcdc-4ede-94f8-b47d096d734c` |
|   RT6   | `c58a4f07-86b9-4e62-b955-808cdc820599` |

## Date range

1999 - 2020

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FCOVER | Fraction of green vegetation cover | \- | UINT8 | 0.0-1.0 | 1/250 | 0 |
| RMSE | Uncertainty on the FCover | \- | UINT8 | 0.0-1.0 | 1/250 | 0 |
| QFLAG | Quality flag | \- | UINT16 | — | 1 | 0 |
| NOBS | Number of valid observations during the synthesis period | \- | UINT8 | 0.0-120.0 | 1 | 0 |
| LENGTH_BEFORE | Length in days of the semi-period before the dekadal date of the compositing window | \- | UINT8 | 5.0-60.0 | 1 | 0 |
| LENGTH_AFTER | Length in days of the semi-period after the dekadal date of the compositing window | \- | UINT8 | 5.0-60.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-properties/fcover_global_1km_10daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
