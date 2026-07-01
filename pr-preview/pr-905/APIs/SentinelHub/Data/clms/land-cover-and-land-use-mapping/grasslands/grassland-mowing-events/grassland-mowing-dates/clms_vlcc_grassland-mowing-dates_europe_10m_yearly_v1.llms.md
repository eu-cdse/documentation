# GRAMD 10m Yearly (2017-present) 4 Events

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-grasslands)

The High Resolution Layer Grassland Mowing Dates (GRAMD) raster product provides at pan-European level in the spatial resolution of 10 m a basic land cover classification, flagging and mapping the start date (DOY) (GRAMD) within the detected Herbaceous cover layer (temporal and permanent grassland)) with a Minimum Mapping Unit (MMU) of 0.25 ha. The GRAMD product will flag and map the dates (Day of Year) of each mowing event on temporary or permanent grassland per year, resulting in a product split in four different rasters per year.

This dataset is provided annually starting with 2017 in 10 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

High Resolution Layer Grasslands product is part of the European Union’s Copernicus Land Monitoring Service.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_GRASSLAND-MOWING-DATES_EUROPE_10M_YEARLY_V1&clmsSelectedPath=Grassland%20Mowing%20Dates&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_GRASSLAND-MOWING-DATES_EUROPE_10M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-23039406-da63-45df-8766-ccb5afce75a5` for the BYOC collection with id `23039406-da63-45df-8766-ccb5afce75a5`.

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

`23039406-da63-45df-8766-ccb5afce75a5`

## Date range

2017 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| GRAMD1 | Classification of grassland mowing dates | Day of Year (DOY) / 0: flag for no mowing detected; 65533: flag for non-herbaceous areas | UINT16 | 1.0-366.0 | 0 | 1 |
| GRAMD2 | Classification of grassland mowing dates | Day of Year (DOY) / 0: flag for no mowing detected; 65533: flag for non-herbaceous areas | UINT16 | 1.0-366.0 | 0 | 1 |
| GRAMD3 | Classification of grassland mowing dates | Day of Year (DOY) / 0: flag for no mowing detected; 65533: flag for non-herbaceous areas | UINT16 | 1.0-366.0 | 0 | 1 |
| GRAMD4 | Classification of grassland mowing dates | Day of Year (DOY) / 0: flag for no mowing detected; 65533: flag for non-herbaceous areas | UINT16 | 1.0-366.0 | 0 | 1 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/grasslands/grassland-mowing-events/grassland-mowing-dates/clms_vlcc_grassland-mowing-dates_europe_10m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
