# LSP 300m Yearly V1

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation?tab=vegetation_phenology_and_productivity_parameters)

Land Surface Phenology (LSP) is the term for land surface vegetation phenology estimated from remotely sensed data. It involves the analysis of time series of vegetation indices, which provide quantitative measures of green biomass and photosynthetic activity. LSP is an invaluable indicator in ecosystem studies and climate research.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_LSP_300M_YEARLY_V1&clmsSelectedPath=Vegetation%20Phenology%20and%20Productivity%20Parameters&clmsSelectedCollection=COPERNICUS_CLMS_LSP_300M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-3c49e431-5d28-4920-a6ef-684fc7617df6` for the BYOC collection with id `3c49e431-5d28-4920-a6ef-684fc7617df6`.

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

`3c49e431-5d28-4920-a6ef-684fc7617df6`

## Date range

2023 - 2024

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| TPROD_S2 | Provides the growing season integral computed as the time-integrated Plant Phenology Index values between the dates of the season start and end. | m2 × m-2 × day | INT16 | 0.0-2000.0 | 1 | 0 |
| LENGTH_S2 | Provides the number of days between the start and end dates of the vegetation growing season. | Day | INT16 | 0.0-730.0 | 1 | 0 |
| SOSV_S2 | Provides the value of the Plant Phenology Index at the start of the vegetation growing season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| RSLOPE_S1 | Provides the rate of change in the values of the Plant Phenology Index at the day when the vegetation growing season ends. | m2 × m-2 × day-1 | INT16 | -1000.0-1000.0 | 1/1000 | 0 |
| LENGTH_S1 | Provides the number of days between the start and end dates of the vegetation growing season. | Day | INT16 | 0.0-730.0 | 1 | 0 |
| LSLOPE_S2 | Provides the rate of change in the values of the Plant Phenology Index at the day when the vegetation growing season starts. | m2 × m-2 × day-1 | INT16 | -1000.0-1000.0 | 1/1000 | 0 |
| AMPL_S2 | Provides the difference between the maximum and minimum Plant Phenology Index values reached during the season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| QA_S2 | Indicates the quality of the global Vegetation Phenology and Productivity Parameters, in the form of a confidence level. | \- | UINT8 | — | 1 | 0 |
| SPROD_S1 | Provides the growing season integral computed as the time-integrated Plant Phenology Index values between the dates of the season start and end, minus their base level value. | m2 × m-2 × day | INT16 | 0.0-2000.0 | 1 | 0 |
| LSLOPE_S1 | Provides the rate of change in the values of the Plant Phenology Index at the day when the vegetation growing season starts. | m2 × m-2 × day-1 | INT16 | -1000.0-1000.0 | 1/1000 | 0 |
| QA_S1 | Indicates the quality of the global Vegetation Phenology and Productivity Parameters, in the form of a confidence level. | \- | UINT8 | — | 1 | 0 |
| EOSD_S2 | Provides the day of the year when the vegetation growing season ends in the time profile of the Plant Phenology Index. | Day-Of-Year | INT16 | 0.0-730.0 | 1 | 0 |
| MAXV_S2 | Provides the maximum (peak) value that the Plant Phenology Index reaches during the vegetation growing season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| MAXD_S2 | Provides the day of the year in the vegetation growing season when the maximum Plant Phenology Index value is reached. | Day-Of-Year | INT16 | 0.0-366.0 | 1 | 0 |
| MINV_S2 | Provides the average Plant Phenology Index value of the minima on left and right sides of each season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| EOSV_S2 | Provides the value of the Plant Phenology Index at the end of the vegetation growing season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| SOSD_S2 | Provides the day of the year when the vegetation growing season starts in the time profile of the Plant Phenology Index. | Day-Of-Year | INT16 | -365.0-365.0 | 1 | 0 |
| SOSD_S1 | Provides the day of the year when the vegetation growing season starts in the time profile of the Plant Phenology Index. | Day-Of-Year | INT16 | -365.0-365.0 | 1 | 0 |
| EOSD_S1 | Provides the day of the year when the vegetation growing season ends in the time profile of the Plant Phenology Index. | Day-Of-Year | INT16 | 0.0-730.0 | 1 | 0 |
| RSLOPE_S2 | Provides the rate of change in the values of the Plant Phenology Index at the day when the vegetation growing season ends. | m2 × m-2 × day-1 | INT16 | -1000.0-1000.0 | 1/1000 | 0 |
| SOSV_S1 | Provides the value of the Plant Phenology Index at the start of the vegetation growing season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| SPROD_S2 | Provides the growing season integral computed as the time-integrated Plant Phenology Index values between the dates of the season start and end, minus their base level value. | m2 × m-2 × day | INT16 | 0.0-2000.0 | 1 | 0 |
| TPROD_S1 | Provides the growing season integral computed as the time-integrated Plant Phenology Index values between the dates of the season start and end. | m2 × m-2 × day | INT16 | 0.0-2000.0 | 1 | 0 |
| MAXD_S1 | Provides the day of the year in the vegetation growing season when the maximum Plant Phenology Index value is reached. | Day-Of-Year | INT16 | 0.0-366.0 | 1 | 0 |
| MINV_S1 | Provides the average Plant Phenology Index value of the minima on left and right sides of each season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| EOSV_S1 | Provides the value of the Plant Phenology Index at the end of the vegetation growing season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1 | 0 |
| MAXV_S1 | Provides the maximum (peak) value that the Plant Phenology Index reaches during the vegetation growing season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |
| AMPL_S1 | Provides the difference between the maximum and minimum Plant Phenology Index values reached during the season. | PPI unit m2 × m-2 | INT16 | 0.0-5000.0 | 1/1000 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-phenology-and-productivity-parameters/lsp_global_300m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
