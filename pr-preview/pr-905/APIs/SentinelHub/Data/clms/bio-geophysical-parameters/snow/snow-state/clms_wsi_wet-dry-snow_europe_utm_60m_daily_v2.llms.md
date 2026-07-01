# WDS Europe 60m Daily V2

## About

[Official documentation](https://land.copernicus.eu/en/products/snow/high-resolution-wet-dry-snow)

The Wet / Dry Snow (WDS) product provides information on the snow state (wet or dry) by combining Sentinel-1 radar-based wet snow maps within the snow cover extent derived from Sentinel-2 optical data. It is generated in near real-time at European scale, with a spatial resolution of 60 m x 60 m in areas where Sentinel-1 and Sentinel-2 observation tracks overlap. It is available for the period from 2016 to the present. More information here.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_WSI_WET-DRY-SNOW_EUROPE_UTM_60M_DAILY_V2&clmsSelectedPath=Snow%20State&clmsSelectedCollection=COPERNICUS_CLMS_WSI_WET-DRY-SNOW_EUROPE_UTM_60M_DAILY_V2) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-e52773f2-d35d-492d-8144-371a9e741212` for the BYOC collection with id `e52773f2-d35d-492d-8144-371a9e741212`.

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

`e52773f2-d35d-492d-8144-371a9e741212`

## Date range

2016 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| SSC | Snow State Classification | wet snow / dry snow / snow free / patchy snow cover / radar shadow / layover / foreshortening / cloud / cloud shadow / water / forest / urban area | UINT8 | 110.0-230.0 | 1 | 0 |
| SSC_QA | Quality layer for the snow state classification (SSC) layer | high quality / medium quality / low quality / minimal quality / masked | UINT8 | 0.0-250.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/snow/snow-state/clms_wsi_wet-dry-snow_europe_utm_60m_daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
