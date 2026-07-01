# SWS Europe (high mountains) 60m Daily V2

## About

[Official documentation](https://land.copernicus.eu/en/products/snow/high-resolution-sar-wet-snow)

The SAR Wet Snow (SWS) product provides the wet snow extent for high mountain areas with a spatial resolution of 60 m x 60 m. It is generated in near real-time for selected high mountain areas at European scale based on C-band Synthetic Aperture Radar satellite data from the Sentinel-1 constellation. It is available for the period from 2016 to the present. More information here.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_WSI_SAR-WET-SNOW_EUROPE_UTM_60M_DAILY_V2&clmsSelectedPath=Snow%20State&clmsSelectedCollection=COPERNICUS_CLMS_WSI_SAR-WET-SNOW_EUROPE_UTM_60M_DAILY_V2) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-41fc21f0-b657-4346-a4ab-aafc8cc636f2` for the BYOC collection with id `41fc21f0-b657-4346-a4ab-aafc8cc636f2`.

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

`41fc21f0-b657-4346-a4ab-aafc8cc636f2`

## Date range

2016 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| WSM | Wet Snow classification in high Mountains areas | 110: wet snow, 125: dry snow or no snow or patchy snow, 200: radar shadow or layover or foreshortening, 210: water, 220: forest, 230: urban areas, 240: non-mountain areas | UINT8 | 110.0-240.0 | 1 | 0 |
| WSM_QA | Quality layer for the wet snow classification (WSM) layer | 0: high quality, 1: medium quality, 2: low quality, 3: minimal quality, 250: masked | UINT8 | 0.0-250.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/snow/snow-state/clms_wsi_sar-wet-snow_europe_utm_60m_daily_v2)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
