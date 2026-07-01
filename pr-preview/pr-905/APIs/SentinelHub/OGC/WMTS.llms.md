# Web Mapping Tile Service

## WMTS Request

The Sentinel Hub WMTS (Web Map Tile Service) service conforms to the [WMTS standard](https://www.ogc.org/standard/wmts/). It provides access to Sentinel-2's 13 unprocessed bands (B01 through B12, with B8A following B08) as well as processed products such as true color imagery and NDVI. Access to the service is done via a custom server instance URL which will be provided to you upon registration. Provides access to the same bands product and additional informational layers as the WMS request except only one layer can be specified at once, even when only raw Sentinel-2 bands are used. As with the WMS service, WMTS is also only available via a user-preconfigured custom server instance URL.

See our OGC API [Webinar](https://www.youtube.com/watch?v=CBIlTOl2po4), which will guide you through different OGC services, including WMTS, help you understand the structure, show you how to run the requests in different environments and how they can be integrated with QGIS, ArcGIS and web applications.

The base URL for the WMTS service:

``` default
https://sh.dataspace.copernicus.eu/ogc/wmts/<INSTANCE_ID>
```

The service supports the same output formats as the WMS request and supports the standard WMTS requests `GetTile`, `GetCapabilities`. It supports WMTS version 1.0.0.

If you want to force a specific output format (e.g. float 32 or uint 16) set `sampleType` in your evalscript as explained [here](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#sampletype). Use `dataMask` band in your evalscript as explained [here](../../../APIs/SentinelHub/UserGuides/Transparency.llms.md) to make pixels transparent.

Check `GetCapabilities` for a list of supported coordinate reference systems and tile matrix sets which can be used for the TILEMATRIX and TILEMATRIXSET parameters.

## WMTS Parameters

**Standard common WMTS URL parameters** (names are case insensitive):

[TABLE]

In addition to the standard WMS URL parameters, the WMS service also supports many custom URL parameters. See [Custom service URL parameters](../../../APIs/SentinelHub/OGC/AdditionalRequestParameters.llms.md) for details.

**Standard `GetTile` request URL parameters:**

| WMTS parameter | Info |
|:---|:---|
| TILEMATRIXSET | The matrix set to be used for the output tile. Check `GetCapabilities` for a list of supported matrix sets. |
| TILEMATRIX | The matrix to be used for the output tile. Check `GetCapabilities` for a list of supported matrices. |
| TILECOL | The column index of the output tile. Check `GetCapabilities` for a list of supported matrix widths. |
| TILEROW | The row index of the output tile. Check `GetCapabilities` for a list of supported matrix heights. |
| LAYER | The preconfigured (in the instance) layer for which to generate the output tile. |
| FORMAT | The returned image format. Optional, default: "image/png", other options: "image/jpeg", "image/tiff". [Detailed information about supported values.](../../../APIs/SentinelHub/OGC/OutputFormats.llms.md) |
