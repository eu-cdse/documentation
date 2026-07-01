# HER 10m Yearly (2017-present)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-grasslands)

The High Resolution Layer Herbaceous cover (HER) raster product provides a basic land cover classification with 2 thematic classes (temporal and permanent herbaceous / non-herbaceous). The production of the herbaceous layer is primarily based on the probability estimates obtained from the Base Vegetation Layer (BVL) which also serves to harmonize the different vegetated HRL products (Grasslands, Tree Cover and Forests, Croplands). HER is further used as input for the Grassland status layer (GRA) extracting the permanent herbaceous in combination with the Ploughing indicator (PLOUGH).

This dataset is provided annually starting in 2017 with 10 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

High Resolution Layer Grasslands product is part of the European Union’s Copernicus Land Monitoring Service.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_HERBACEOUS-COVER_EUROPE_10M_YEARLY_V1&clmsSelectedPath=Herbaceous%20Cover&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_HERBACEOUS-COVER_EUROPE_10M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-e2d6c154-b874-454e-9bb1-43d04b45a92d` for the BYOC collection with id `e2d6c154-b874-454e-9bb1-43d04b45a92d`.

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

|    Collection    | ID                                     |
|:----------------:|----------------------------------------|
| Herbaceous cover | `e2d6c154-b874-454e-9bb1-43d04b45a92d` |

## Date range

2017 - present

## Bands

Herbaceous cover

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| HER | Classification of herbaceous / non-herbaceous | Non-grassland in reference year, Permanent and temporary grassland in reference year | UINT8 | 0.0-1.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/grasslands/grassland-and-herbaceous/herbaceous-cover/clms_vlcc_herbaceous-cover_europe_10m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
