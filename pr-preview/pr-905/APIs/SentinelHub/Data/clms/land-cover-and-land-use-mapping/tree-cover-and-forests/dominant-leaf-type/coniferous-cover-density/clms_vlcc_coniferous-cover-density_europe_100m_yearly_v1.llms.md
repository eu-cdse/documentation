# CCD 100m Yearly (2018-present)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-forests-and-tree-cover)

The High Resolution Layer Coniferous Cover Density (CCD) dataset provides information on the percentage of coniferous pixels at 100m spatial resolution, and is derived through aggregation of the 10m DLT for the respective reference year. Within each cell the number of coniferous pixels are counted and the percentages stored into in the 100m pixel of the CCD. The class 255 = outside area is predefined by the 100m boundary layer and remains unchanged.

This dataset is provided annually starting with 2018 in 100 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries.

High Resolution Layer Tree Cover and Forest product is part of the European Union’s Copernicus Land Monitoring Service.

This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_CONIFEROUS-COVER-DENSITY_EUROPE_100M_YEARLY_V1&clmsSelectedPath=Coniferous%20Cover%20Density&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_CONIFEROUS-COVER-DENSITY_EUROPE_100M_YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-a0edd575-c763-4c4a-a910-631df3df4506` for the BYOC collection with id `a0edd575-c763-4c4a-a910-631df3df4506`.

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

`a0edd575-c763-4c4a-a910-631df3df4506`

## Date range

2018 - present

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| CCD | Coniferous cover density (100 m) | % | UINT8 | 0.0-100.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/tree-cover-and-forests/dominant-leaf-type/coniferous-cover-density/clms_vlcc_coniferous-cover-density_europe_100m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
