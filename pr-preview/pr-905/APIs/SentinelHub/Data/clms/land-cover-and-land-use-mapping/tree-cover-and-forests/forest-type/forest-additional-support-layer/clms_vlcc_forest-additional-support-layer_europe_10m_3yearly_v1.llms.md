# FADSL 10m 3-yearly (2018-2021)

## About

[Official documentation](https://land.copernicus.eu/en/products/high-resolution-layer-forests-and-tree-cover)

The High Resolution Layer Forest Additional Support Layer (FADSL) provides information on trees under agricultural use or in urban context to be excluded from the Forest Type (FTY) product and at 10m spatial resolution. The derivation of Forest Additional Support Layer (FADSL) is based on the spatial intersection of the 10m DLT and TCD layers with CORINE Land Cover (CLC) 2018 and HRL Imperviousness Degree 2018 with 10 m spatial resolution; TCD range of 10-100%; with a MMW of 10m and no MMU (pixel base). This dataset is provided on a 3-yearly frequency in 10 meter rasters (fully conformant with the EEA reference grid) in 100 x 100 km tiles covering the EEA38 countries. High Resolution Layer Tree Cover and Forest product is part of the European Union’s Copernicus Land Monitoring Service. This dataset includes data from the French Overseas Territories (DOMs)

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=41.82019&lng=12.57866&themeId=DEFAULT-THEME&datasetId=COPERNICUS_CLMS_VLCC_FOREST-ADDITIONAL-SUPPORT-LAYER_EUROPE_10M_3YEARLY_V1&clmsSelectedPath=Forest%20Additional%20Support%20Layer&clmsSelectedCollection=COPERNICUS_CLMS_VLCC_FOREST-ADDITIONAL-SUPPORT-LAYER_EUROPE_10M_3YEARLY_V1) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-912a6eb9-12f2-4cad-a821-2c5b03dfccbb` for the BYOC collection with id `912a6eb9-12f2-4cad-a821-2c5b03dfccbb`.

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

`912a6eb9-12f2-4cad-a821-2c5b03dfccbb`

## Date range

2018 - 2021

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| FADSL | Forest Additional Support Layer over 3 years | 3: trees predominantly used for agricultural practices - broadleaved (from CLC2018); 4: trees in urban context - broadleaved and coniferous (from IMD 2018); 5: trees in urban context - broadleaved and coniferous (from CLC 2018) | UINT8 | 3.0-5.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/tree-cover-and-forests/forest-type/forest-additional-support-layer/clms_vlcc_forest-additional-support-layer_europe_10m_3yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
