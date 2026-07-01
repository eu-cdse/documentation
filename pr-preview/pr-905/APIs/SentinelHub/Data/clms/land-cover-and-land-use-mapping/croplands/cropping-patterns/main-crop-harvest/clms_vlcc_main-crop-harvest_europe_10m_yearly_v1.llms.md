# CPMCH 10m Yearly (2017-present)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-croplands)

The High Resolution Layer Cropping Patterns - Main Crop Harvest (CPMCH) raster product provides the harvest date of the main (annual) crop expressed in days of the year (DOY). The harvest is considered as the time of removal of most of the biomass. YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-365)

This dataset is provided annually starting in 2017 with 10 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

High Resolution Layer Croplands product is part of the European Union’s Copernicus Land Monitoring Service. Confidence layer available for the dataset.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_MAIN-CROP-HARVEST_EUROPE_10M_YEARLY_V1&clmsSelectedPath=Main%20Crop%20Harvest&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_MAIN-CROP-HARVEST_EUROPE_10M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-8008322f-ebec-4a30-854a-7775778a368c` for the BYOC collection with id `8008322f-ebec-4a30-854a-7775778a368c`.

[Check out this example request](../../../../../../../../APIs/SentinelHub/Process/Examples/BYOC.llms.md)

#### sentinelhub Python package

For using the [sentinelhub Python package](https://sentinelhub-py.readthedocs.io/en/latest/index.html), please provide the `collectionId` as follows:

``` python
byoc_collection = DataCollection.define_byoc(
    collection_id="<collectionId>"
)
```

[Check out this Jupyter Notebook example](../../../../../../../../notebook-samples/sentinelhub/cloudless_process_api.llms.md)

[Click here](../../../../../../../../APIs/SentinelHub/Byoc.llms.md) for more information about the BYOC API.

### Collection ID

|             Collection             | ID                                     |
|:----------------------------------:|----------------------------------------|
|      Main Crop Harvest - 2017      | `8008322f-ebec-4a30-854a-7775778a368c` |
|      Main Crop Harvest - 2018      | `f62add8d-b87b-4f8d-a4e7-cd56752a25ad` |
|      Main Crop Harvest - 2019      | `ad5bb52f-e768-478e-b480-d71ee8e2760a` |
|      Main Crop Harvest - 2020      | `5cf01cbb-24e1-47dc-b612-48928ede66e5` |
|      Main Crop Harvest - 2021      | `061655da-2c3f-47ea-8766-934ff1b7ef6d` |
|      Main Crop Harvest - 2022      | `694ee6e1-7e04-4508-97ba-72888d56b60f` |
|      Main Crop Harvest - 2023      | `01174ebf-1a51-46c9-a7fd-85a402de7f0d` |
| Main Crop Harvest Confidence Layer | `4c522ea1-eb7a-4d07-bfd2-1523f982c50b` |

## Date range

2017 - present

## Bands

Main Crop Harvest - 2017

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 17001.0-18365.0 | 1 | 0 |

Main Crop Harvest - 2018

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 18001.0-19365.0 | 1 | 0 |

Main Crop Harvest - 2019

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 19001.0-20366.0 | 1 | 0 |

Main Crop Harvest - 2020

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 20001.0-21365.0 | 1 | 0 |

Main Crop Harvest - 2021

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 21001.0-22365.0 | 1 | 0 |

Main Crop Harvest - 2022

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 22001.0-23365.0 | 1 | 0 |

Main Crop Harvest - 2023

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCH | Main crop harvest date | YYDOY where YY = last 2 digits of the year (e.g. 19 for 2019) and DOY is the day of the year (1-366) | UINT16 | 23001.0-24366.0 | 1 | 0 |

Main Crop Harvest Confidence Layer

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CPMCHCL | Confidence of main crop harvest | Days | UINT16 | 1.0-40.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/croplands/cropping-patterns/main-crop-harvest/clms_vlcc_main-crop-harvest_europe_10m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
