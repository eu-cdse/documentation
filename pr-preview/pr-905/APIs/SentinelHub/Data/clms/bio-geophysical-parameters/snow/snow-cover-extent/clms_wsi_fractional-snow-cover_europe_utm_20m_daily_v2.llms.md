# FSC Europe 20m Daily V2

## About

[Official documentation](https://land.copernicus.eu/en/products/snow/fractional-snow-cover)

The Fractional Snow Cover (FSC) product provides the fraction of the surface covered by snow at the top of canopy (FSC-TOC) and on ground (FSC-OG) per pixel as a percentage (0% – 100%). It is generated in near real-time at European scale based on optical satellite data from the Sentinel-2 constellation, with a spatial resolution of 20 m x 20 m. It is available for the period from 2016 to the present. More information here.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_WSI_FRACTIONAL-SNOW-COVER_EUROPE_UTM_20M_DAILY_V2&clmsSelectedPath=Snow%20Cover%20Extent&clmsSelectedCollection=COPERNICUS_CLMS_WSI_FRACTIONAL-SNOW-COVER_EUROPE_UTM_20M_DAILY_V2) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-2bb9974a-0eb8-484d-adf1-20cc307021b6` for the BYOC collection with id `2bb9974a-0eb8-484d-adf1-20cc307021b6`.

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

`2bb9974a-0eb8-484d-adf1-20cc307021b6`

## Date range

2016 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FSCOG | Snow fraction on-ground (%) | Fractional snow cover on ground (%): 0-100=snow fraction; 205=cloud or cloud shadow; 210=inland water | UINT8 | 0.0-100.0 | 1 | 0 |
| FSCOG_QA | Quality layer for the on-ground snow fraction (FSC OG) layer | Quality assessment for FSCOG: 0=high quality; 1=medium quality; 2=low quality; 3=minimal quality; 205=cloud or cloud shadow; 210=inland water | UINT8 | 0.0-3.0 | 1 | 0 |
| FSCTOC | Snow fraction on top of canopy (%) | Fractional snow cover top of canopy (%): 0-100=snow fraction; 205=cloud or cloud shadow; 210=inland water | UINT8 | 0.0-100.0 | 1 | 0 |
| FSCTOC_QA | Quality layer for the Top-of-canopy snow fraction (FSC TOC) layer | Quality assessment for FSCTOC: 0=high quality; 1=medium quality; 2=low quality; 3=minimal quality; 205=cloud or cloud shadow; 210=inland water | UINT8 | 0.0-3.0 | 1 | 0 |
| QAFLAGS | Quality flags | Bitmask with pixel quality flags. | UINT8 | — | 1 | 0 |
| CLD | Cloud and cloud shadow mask | Bitmask with cloud and cloud shadow masks derived from MAJA Sentinel-2 Level-2A product. | UINT8 | — | 1 | 0 |
| NDSI | Normalised Difference Snow Index (%) of detected snow areas | Normalised Difference Snow Index (%): 0-100=NDSI values for snow-covered pixels; 205=cloud or cloud shadow; 210=inland water | UINT8 | 0.0-100.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/snow/snow-cover-extent/clms_wsi_fractional-snow-cover_europe_utm_20m_daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
