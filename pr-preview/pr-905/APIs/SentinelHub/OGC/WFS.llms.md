# Web Feature Service

## WFS Request

The Sentinel Hub WFS (Web Feature Service) service conforms to the [WFS standard](https://www.ogc.org/standard/wfs/). It provides access to the geometric (vector) metadata about the available data collection tiles. As with the WMS service, WFS is also only available via a user-preconfigured custom server instance URL.

See our OGC API [Webinar](https://www.youtube.com/watch?v=CBIlTOl2po4), which will guide you through different OGC services, including WFS, help you understand the structure, show you how to run the requests in different environments and how they can be integrated with QGIS, ArcGIS and web applications.

The base URL for the WFS service:

``` default
https://sh.dataspace.copernicus.eu/ogc/wfs/<INSTANCE_ID>
```

The service supports many vector formats, including GML, XML, JSON and also raw HTML and plain text. Check `GetCapabilities` for a list of all supported formats. It supports WFS version 2.0.0.

## WFS URL Parameters

**Standard common WFS URL parameters** (parameter names are case insensitive):

[TABLE]

In addition to the standard WFS URL parameters, the WFS service also supports many custom URL parameters. See [Custom service URL parameters](../../../APIs/SentinelHub/OGC/AdditionalRequestParameters.llms.md) for details.

**Standard `GetFeature` request URL parameters:**

| WFS parameter | Info |
|:---|:---|
| TYPENAMES | More information found [below](../../../APIs/SentinelHub/OGC/WFS.llms.md#typenames). |
| MAXFEATURES | The maximum number of features to be returned by a single request. Default value: 100. Valid range: 0..100. |
| BBOX | The bounding box area for which to return the features. |
| SRSNAME | The CRS in which the BBOX is specified. |
| FEATURE_OFFSET | Offset controls the starting point within the returned features. |
| OUTPUTFORMAT | The MIME format of the returned features. |

**Standard `DescribeFeatureType` request URL parameters:**

| WFS parameter | Info |
|:---|:---|
| TYPENAMES | More information found [below](../../../APIs/SentinelHub/OGC/WFS.llms.md#typenames). |
| OUTPUTFORMAT | The MIME format of the returned features. |

### Typenames

| Data collection  | TYPENAMES for services |
|:-----------------|:-----------------------|
| SENTINEL-2 L1C   | DSS1                   |
| SENTINEL-2 L2A   | DSS2                   |
| SENTINEL-1 IW    | DSS3                   |
| SENTINEL-1 EW    | DSS3                   |
| SENTINEL-1 EW SH | DSS3                   |
| SENTINEL 3 OLCI  | DSS8                   |
| SENTINEL 3 L2    | DSS22                  |
| SENTINEL 3 SLSTR | DSS9                   |
| SENTINEL 5P      | DSS7                   |
| BYOC             | byoc-\<collectionId\>  |
