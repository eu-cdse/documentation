# SP S1+S2 Europe (high mountains) 60m Yearly V1

## About

[Official documentation](https://land.copernicus.eu/en/products/snow/high-resolution-snow-phenology)

The Sentinel-1 & Sentinel-2 Snow Phenology (SP S1+S2) product characterizes the timing and duration of the snow season. For each pixel and for a given hydrological year, it provides the number of days with snow cover, as well as the first and last day of the longest continuous snow period. The hydrological year starts on 1 September. The product is generated at the European scale with a spatial resolution of 60 m × 60 m, consistent with the input snow cover maps derived from optical satellite data acquired by the Sentinel-2 constellation and from C-band Synthetic Aperture Radar satellite data acquired by the Sentinel-1 constellation (Gap-filled Fractional Snow Cover - GFSC). It is available for the period from 2016 to the present and can be downloaded in multiple projections and pixel spacings. More information here.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_WSI_SNOW-PHENOLOGY-S1-S2_EUROPE_UTM_60M_YEARLY_V1&clmsSelectedPath=Snow%20Cover%20Extent&clmsSelectedCollection=COPERNICUS_CLMS_WSI_SNOW-PHENOLOGY-S1-S2_EUROPE_UTM_60M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-1896152f-75d8-4daf-9db9-987773559a2c` for the BYOC collection with id `1896152f-75d8-4daf-9db9-987773559a2c`.

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

`1896152f-75d8-4daf-9db9-987773559a2c`

## Date range

2016 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| SCD | Snow cover duration (in days) | Number of days of snow cover over the hydrological year | UINT16 | 0.0-366.0 | 1 | 0 |
| SCO | Snow cover onset date defined as the first day of the longest snow cover period | Snow cover onset date, expressed as the number of days from the beginning of the hydrological year (1st September = day 0). Note that SCO is not given when the snow cover duration SCD is less than 60 days. | UINT16 | 0.0-366.0 | 1 | 0 |
| SCM | Snow cover melt out date defined as the last day of the longest snow cover period | Snow cover melt out date, expressed as the number of days from the beginning of the hydrological year (1st September = day 0). Note that SCM is not given when the snow cover duration SCD is less than 60 days. | UINT16 | 0.0-366.0 | 1 | 0 |
| NCSO | Number of days with clear sky observations within the hydrological year | Number of days with clear sky observations used in the interpolation of the snow cover time series within the hydrological year. | UINT16 | 0.0-366.0 | 1 | 0 |
| NWSO | Number of days with Sentinel-1-based wet snow observations within the hydrological year | Number of days with Sentinel-1-based wet snow observations used in the interpolation of the snow cover time series within the hydrological year (used where Sentinel-2-based observations have gaps). | UINT16 | 0.0-366.0 | 1 | 0 |
| QAFLAGS | Quality flags | Bitmask layer with pixel quality flags. The default visualisation displays areas where the snow cover duration is less than 60 days. These correspond to pixels where bit 4 is activated. Additional information can also be visualised by selecting other bits. | UINT8 | — | 1 | 0 |
| SCD_QA | Quality layer for the snow cover duration (SCD) layer | Quality assessment for SCD: 0=high quality; 1=medium quality; 2=low quality; 3=minimal quality; 420=inland water | UINT16 | 0.0-3.0 | 1 | 0 |
| SCO_QA | Quality layer for the snow cover onset date (SCO) layer | Number of days between the estimated snow onset date and the closest snow observation date. | UINT16 | 0.0-365.0 | 1 | 0 |
| SCM_QA | Quality layer for the snow cover melt out date (SCM) layer | Number of days between the estimated snow melt out date and the closest snow observation date. | UINT16 | 0.0-365.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/bio-geophysical-parameters/snow/snow-cover-extent/clms_wsi_snow-phenology-s1-s2_europe_utm_60m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
