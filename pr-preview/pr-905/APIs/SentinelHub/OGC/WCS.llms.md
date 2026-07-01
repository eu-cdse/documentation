# Web Coverage Service

## WCS Request

The Sentinel Hub WCS (Web Coverage Service) service conforms to the [WCS standard](https://www.ogc.org/standard/wcs/). Provides access to the same bands product and additional informational layers as the WMS service except only one layer can be specified at once, even when only raw Sentinel-2 bands are used. In addition to raster products, the WCS service can also return the vector features of the Sentinel-2 tiles' metadata. As with the WMS service, WCS is also only available via a user-preconfigured custom server instance URL.

See our OGC API [Webinar](https://www.youtube.com/watch?v=CBIlTOl2po4), which will guide you through different OGC services, including WCS, help you understand the structure, show you how to run the requests in different environments and how they can be integrated with QGIS, ArcGIS and web applications.

The base URL for the WCS service:

``` default
https://sh.dataspace.copernicus.eu/ogc/wcs/<INSTANCE_ID>
```

The service supports the same output formats as the WMS request (with addition of vector output formats, when "TILE" is selected as the COVERAGE) and supports the standard WCS requests: `GetCoverage`, `DescribeCoverage` and `GetCapabilities`. It supports WCS versions 1.0.0 and 1.1.2.

## WCS URL Parameters

**Standard common WCS URL parameters** (parameter names are case insensitive):

[TABLE]

In addition to the standard WCS URL parameters, the WCS service also supports many custom URL parameters. See [Custom service URL parameters](../../../APIs/SentinelHub/OGC/AdditionalRequestParameters.llms.md) for details.

**Standard `GetCoverage` request URL parameters:**

| WCS parameter | Info |
|:---|:---|
| COVERAGE | The preconfigured (in the instance) layer for which to generate the output image, or "TILE" to return the vector format features. |
| FORMAT | The returned image format. Optional, default: "image/png", other options: "image/jpeg", "image/tiff". [Detailed information about supported values.](../../../APIs/SentinelHub/OGC/OutputFormats.llms.md) |

**Standard `DescribeCoverage` request URL parameters:**

| WCS parameter  | Info |
|:---------------|:-----|
| Coming soon... |      |
