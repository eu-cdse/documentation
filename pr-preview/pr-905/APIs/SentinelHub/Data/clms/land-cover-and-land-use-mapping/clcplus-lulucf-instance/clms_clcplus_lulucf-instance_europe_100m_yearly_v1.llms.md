# CLCplus LULUCF Instance Europe 100m Yearly V1

## About

[Official documentation](https://land.copernicus.eu/en/products/clcplus-lulucf-instance)

This metadata refers to the CORINE Land Cover Plus Land Use, Land-Use Change and Forestry Instance (CLCplus LULUCF Instance), an annually updated, pan-European, spatially consistent and seamless geospatial proxy for land use reporting under the LULUCF regulation. The product is delivered as a single raster layer with a spatial resolution of 100 m, derived from multiple pan-European Copernicus Land Monitoring Service (CLMS) high resolution input datasets. The LULUCF Instance is available for the reference years 2018, 2021, 2022 and 2023, with production moving to an annual update cycle starting from the 2021 product. Each raster cell represents a dominant LULUCF land-use class, assigned according to thematic and spatial rulesets implemented during the extraction process. While each pixel corresponds primarily to one of the six main LULUCF land use categories - forest land, grassland, cropland, settlements, wetlands, and other lands - the dataset further differentiates these categories into sub classes, resulting in a total of 27 classes. This classification structure supports greenhouse gas reporting and other applications within the LULUCF sector by providing a harmonised and policy relevant representation of land use across Europe. It is crucial to understand that this product is fundamentally different from other CLMS products, as it is not based directly on satellite image classification or visual interpretation. Instead, it is produced through the combination and integration of existing CLMS data layers. Consequently, the dataset does not introduce fundamentally new information; rather, its novelty lies in the expert driven integration of multiple sources to produce a LULUCF oriented land use representation. More information here.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_CLCPLUS_LULUCF-INSTANCE_EUROPE_100M_YEARLY_V1&clmsSelectedPath=CLCplus%20LULUCF%20Instance&clmsSelectedCollection=COPERNICUS_CLMS_CLCPLUS_LULUCF-INSTANCE_EUROPE_100M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-714b4c8d-2d89-4ed8-933c-f7c8bb7a1d4b` for the BYOC collection with id `714b4c8d-2d89-4ed8-933c-f7c8bb7a1d4b`.

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

`714b4c8d-2d89-4ed8-933c-f7c8bb7a1d4b`

## Date range

2018 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| LULUCF_INSTANCE | Pan-European annual raster LULUCF dataset | \[classes\] | UINT8 | 11.0-254.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/clcplus-lulucf-instance/clms_clcplus_lulucf-instance_europe_100m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
