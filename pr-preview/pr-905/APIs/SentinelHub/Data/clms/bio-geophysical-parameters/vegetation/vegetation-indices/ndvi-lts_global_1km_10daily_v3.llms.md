# NDVI LTS 1km 10-daily V3

## About

[Official documentation](https://land.copernicus.eu/en/products/vegetation/normalised-difference-vegetation-long-term-statistics-v3-0-1km)

Provides the Long-Term Statistics of the Normalized Difference Vegetation Index. Every 10-days, minimum, median, maximum and mean are available at global scale, at a spatial resolution of ~1km over the 21-years period 1999-2019.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_NDVI_1KM_STATS_V3&clmsSelectedPath=Vegetation%20Indices&clmsSelectedCollection=COPERNICUS_CLMS_NDVI_1KM_STATS_V3) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-1b1b0b08-19c4-42b7-8ea1-bf9b43769b42` for the BYOC collection with id `1b1b0b08-19c4-42b7-8ea1-bf9b43769b42`.

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

`1b1b0b08-19c4-42b7-8ea1-bf9b43769b42`

## Date range

1999 - 2019

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| NDVI_MAX_LTS | Maximum value of Normalized Difference Vegetation Index | \- | UINT8 | -0.08-0.92 | 1/250 | -0.08 |
| NDVI_MEAN_LTS | Mean value of Normalized Difference Vegetation Index | \- | UINT8 | -0.08-0.92 | 1/250 | -0.08 |
| NDVI_MEDIAN_LTS | Median value of Normalized Difference Vegetation Index | \- | UINT8 | -0.08-0.92 | 1/250 | -0.08 |
| NDVI_MIN_LTS | Minimum value of Normalized Difference Vegetation Index | \- | UINT8 | -0.08-0.92 | 1/250 | -0.08 |
| NDVI_STDEV_LTS | Standard deviation of Normalized Difference Vegetation Index | \- | UINT8 | 0.0-1.0 | 1/250 | 0 |
| NDVI_NOBS_LTS | Number of NDVI values used to calculate the statistics | \- | UINT8 | 0.0-19.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/vegetation/vegetation-indices/ndvi-lts_global_1km_10daily_v3)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
