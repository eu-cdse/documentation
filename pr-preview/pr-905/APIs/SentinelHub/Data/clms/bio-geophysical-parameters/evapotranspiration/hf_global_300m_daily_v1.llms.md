# Heat Flux 2025-present (raster 300 m), global, daily – version 1

## About

[Official documentation](https://land.copernicus.eu/en/products/evapotranspiration/heat-flux-2025-present-raster-300-m-global-daily-version-1)

Provides latent and sensible heat fluxes with one auxiliary information. Estimates are provided for each Sentinel-3 overpass in near real time at global scale in the spatial resolution of about 300 m from November 2025 onwards in version 1.0.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_HF_GLOBAL_300M_DAILY_V1&clmsSelectedPath=Evapotranspiration&clmsSelectedCollection=COPERNICUS_CLMS_HF_GLOBAL_300M_DAILY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-5e16244f-3357-46c8-9ddc-28d182aec8e5` for the BYOC collection with id `5e16244f-3357-46c8-9ddc-28d182aec8e5`.

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

`5e16244f-3357-46c8-9ddc-28d182aec8e5`

## Date range

2025 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| H_TSEBPT | Sensible heat flux calculated by the TSEB-PT model. Unit: W/m² | W/m² | INT16 | -100.0-1000.0 | 1 | 0 |
| LE_TSEBPT | Latent heat flux calculated by the TSEB-PT model. Unit: W/m² | W/m² | INT16 | -100.0-1000.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/evapotranspiration/hf_global_300m_daily_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
