# GRA 100m Yearly (2017-present)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-grasslands)

The High Resolution Layer Grassland (GRA) raster product provides a binary status layer of grassland/non-grassland mask. This grassy and non-woody vegetation baseline product includes all kinds of grasslands: managed grassland, semi-natural grassland and natural grassy vegetation. It does not include temporary grasslands, which are masked out using the corresponding Ploughing indicator (PLOUGH), indicating on the number of years since a pixel was last ploughed. In the 100 meter raster product, the number of Grassland pixels are counted and the percentages stored in each 100 meter cell. The class 255 = outside area is predefined by the 100m boundary layer and remains unchanged.

This dataset is provided annually starting in 2017 with 100 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

High Resolution Layer Grasslands product is part of the European Union’s Copernicus Land Monitoring Service.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_GRASSLAND_EUROPE_100M_YEARLY_V1&clmsSelectedPath=Grassland&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_GRASSLAND_EUROPE_100M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-f99fe8ab-0c49-4c68-acd2-1687b0e04816` for the BYOC collection with id `f99fe8ab-0c49-4c68-acd2-1687b0e04816`.

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

`f99fe8ab-0c49-4c68-acd2-1687b0e04816`

## Date range

2017 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| GRA | Grassland presence and percentage coverage | % of grassland density | UINT8 | 0.0-100.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/grasslands/grassland-and-herbaceous/grassland/clms_vlcc_grassland_europe_100m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
