# Tree Cover Density at 10m - Annual V1

## About

[Official documentation](https://land.copernicus.eu/en/products/global-dynamic-land-cover/tree-cover-density-2020-raster-10-m-pantropical-annual)

Provides pantropical tree cover density as projective tree cover in percent per pixel at 10 m resolution for the 2020 base year. The data are updated annually and will be available for the 2020-2026 years. The product belongs to the Copernicus Global Land Cover and Tropical Forest Mapping and Monitoring Service (LCFM) and builds upon initiatives like the REDDCopernicus, EO4SD Forest Monitoring and pan-European Vegetated Land Cover Characteristics. It advances tropical forest monitoring capabilities, ensuring alignment with international sustainability initiatives and providing critical information for analysis and monitoring of deforestation and forest degradation. Please note: this version is still in beta status, as final validation is ongoing.

[View this dataset in Copernicus Browser](https://browser.dataspace.copernicus.eu/?zoom=10&lat=19.35456&lng=-99.13651&themeId=DEFAULT-THEME&datasetId=8bd33a42-dce4-4554-9a1f-1bb248b4183d&clmsSelectedPath=Global%20Dynamic%20Land%20Cover&clmsSelectedCollection=8bd33a42-dce4-4554-9a1f-1bb248b4183d) (Click on ‘Show latest date’ after the page loads.)

## Attribution and use

The service is implemented by the Joint Research Centre (JRC) and the European Environment Agency (EEA) on behalf of the European Commission. All products are free of charge and can be used for any purpose.

## Accessing CLMS data

CLMS products are provided as Bring Your Own COG (BYOC) collections ([BYOC API](../../../../../../APIs/SentinelHub/Byoc.llms.md)) and are accessed like any other data using Sentinel Hub APIs. In all cases, a `collectionId` and a product-specific `evalscript` is needed, which can be obtained from the respective sections below.

### Data type identifier

#### API requests

For direct use of the APIs with e.g. oauthlib or cURL requests, use `byoc-<collectionId>` as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-8bd33a42-dce4-4554-9a1f-1bb248b4183d` for the BYOC collection with id `8bd33a42-dce4-4554-9a1f-1bb248b4183d`.

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

`8bd33a42-dce4-4554-9a1f-1bb248b4183d`

## Date range

2020 - 2026

## Bands

| Name | Description | Units | Source format | Range | Scaling | Offset |
|----|----|----|----|----|----|----|
| TCD10 | Tree Cover Density Map at 10m - Annual V1 | % | UINT8 | 0.0-100.0 | 1 | 0 |

## Evalscript

**[Example scripts for this product.](https://github.com/eu-cdse/sentinel-hub-custom-scripts/tree/main/clms/land-cover-and-land-use-mapping/global-dynamic-land-cover/tcd_pantropical_10m_yearly_v1)**

Use the link above to access dedicated Evalscript examples for this product in the Copernicus Data Space Ecosystem Sentinel Hub Custom Scripts repository.

An Evalscript (or “custom script”) is a piece of Javascript code which defines how the data shall be processed by Sentinel Hub and what values the service shall return. It is a required part of any [process](../../../../../../APIs/SentinelHub/Process.llms.md), [batch processing](../../../../../../APIs/SentinelHub/BatchV2.llms.md) or [OGC request](../../../../../../APIs/SentinelHub/OGC.llms.md).

Evalscripts can use any JavaScript function or language structures, along with certain [utility functions](../../../../../../APIs/SentinelHub/Evalscript/Functions.llms.md) we provide for your convenience. For running evalscripts we use the [Chrome V8](https://v8.dev/) JavaScript engine.
