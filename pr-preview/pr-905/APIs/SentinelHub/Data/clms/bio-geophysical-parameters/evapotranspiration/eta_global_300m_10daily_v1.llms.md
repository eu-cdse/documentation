# Evapotranspiration 2025-present (raster 300 m), global, 10-daily – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/evapotranspiration/evapotranspiration-2025-present-raster-300m-global-10-daily-version-1)

The Evapotranspiration product group provides global actual evapotranspiration (ETA) estimates at 300 m spatial resolution with a frequency of 10-daily for ET, E and T and at a daily frequency for H and LE, combining outputs from two modelling frameworks and an Ensemble model.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_ETA_GLOBAL_300M_10DAILY_V1&clmsSelectedPath=Evapotranspiration&clmsSelectedCollection=COPERNICUS_CLMS_ETA_GLOBAL_300M_10DAILY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-24fd5fde-b9db-44f1-a32b-e5dc3a0c5b9b` for the BYOC collection with id `24fd5fde-b9db-44f1-a32b-e5dc3a0c5b9b`.

[Check out this example request](../../../../../../APIs/SentinelHub/Process/Examples/BYOC.llms.md)

#### sentinelhub Python package

For using the [sentinelhub Python package](https://sentinelhub-py.readthedocs.io/en/latest/index.html), please provide the `collectionId` as follows:

``` python
byoc_collection = DataCollection.define_byoc(
    collection_id="<collectionId>"
)
```

[Check out this Jupyter Notebook example](../../../../../../notebook-samples/sentinelhub/cloudless_process_api.llms.md)

[Click here](../../../../../../APIs/SentinelHub/Byoc.llms.md) for more information about the BYOC API.

### Collection ID

`24fd5fde-b9db-44f1-a32b-e5dc3a0c5b9b`

## Date range

2025 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| GFD | Per pixel average gap-filling distance (in days) for cloudy pixels in a given dekad. Unit in days | days | UINT8 | 0.0-60.0 | 1 | 0 |
| FLAG | Per pixel annotation flag indicating quality or other limitations | \- | UINT8 | — | \- | \- |
| NOBS | Per pixel number of cloud free observations in a given dekad. | \- | UINT8 | 0.0-11.0 | 1 | 0 |
| E_STD | Per pixel standard deviation between TSEB-PT and ETLook model E. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| T_STD | Per pixel standard deviation between TSEB-PT and ETLook model T. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| ET_STD | Per pixel standard deviation between TSEB-PT and ETLook model ET. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| E_ETLOOK | Soil evaporation calculated by the ETLook model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| E_TSEBPT | Soil evaporation calculated by the TSEB-PT model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| T_ETLOOK | Canopy transpiration calculated by the ETLook model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| T_TSEBPT | Canopy transpiration calculated by the TSEB-PT model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| ET_ETLOOK | Actual evapotranspiration calculated by the ETLook model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| ET_TSEBPT | Actual evapotranspiration calculated by the TSEB-PT model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| E_ENSEMBLE | Soil evaporation calculated by the Ensemble model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| T_ENSEMBLE | Canopy transpiration calculated by the Ensemble model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |
| ET_ENSEMBLE | Actual evapotranspiration calculated by the Ensemble model. Unit: mm/day | mm/day | UINT8 | 0.0-20.0 | 1/10 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/evapotranspiration/eta_global_300m_10daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
