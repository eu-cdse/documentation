# LWQ 2019-2024 (raster 100 m), global, 10-daily – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/water-bodies/lake-water-quality-v1-0-100m)

Provides semi-continuous observations for a large number of medium and large-sized lakes.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_LWQ_100M_10DAILY_NRT_V1&clmsSelectedPath=Lake%20Water%20Quality&clmsSelectedCollection=COPERNICUS_CLMS_LWQ_100M_10DAILY_NRT_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-8894d46b-a451-4abf-838e-292b4bcacae1` for the BYOC collection with id `8894d46b-a451-4abf-838e-292b4bcacae1`.

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

`8894d46b-a451-4abf-838e-292b4bcacae1`

## Date range

2019 - 2024

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FOBS | Number of days from the start of the sensing period until the first cloud-free observation | Days since the start of the observation period | FLOAT32 | 0.0-10.0 | 1 | 0 |
| LOBS | Number of days from the start of the sensing period until the last cloud-free observation | Days since the start of the observation period | FLOAT32 | 0.0-10.0 | 1 | 0 |
| NOBS | Number of observations | \- | INT16 | 0.0– | 1 | 0 |
| RW1375 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW1610 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW2190 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW443 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW490 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW560 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW665 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW705 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW740 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW783 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW842 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW865 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| RW945 | Fully normalised water-leaving reflectance | \- | FLOAT32 | 0.0-1.0 | 1 | 0 |
| TMEAN | Mean turbidity | NTU | FLOAT32 | 0.0– | 1 | 0 |
| TOBS | Trophic State Index | \- | FLOAT32 | 1.0-11.0 | 1 | 0 |
| TSI | Mean of total suspended matter | \- | FLOAT32 | 0.0-100.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/water-bodies/lake-water-quality/lwq-nrt_global_100m_10daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
