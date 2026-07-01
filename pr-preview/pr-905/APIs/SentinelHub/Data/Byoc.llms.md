# Bring Your Own COG

## About BYOC Data

Bring Your Own COG (BYOC) is data ingested by Sentinel Hub users using [BYOC API](../../../APIs/SentinelHub/Byoc.llms.md).

## Accessing data

Data is accessed using Sentinel Hub APIs, just like any other data you are used to. In all cases `collection id` is needed, which can be obtained from your [dashboard](https://shapps.dataspace.copernicus.eu/dashboard/#/byoc). You also need to access data from the correct endpoint.

### Data type identifier

Use `byoc-<collectionId>` for BYOC collections as the value of the `input.data.type` parameter in your API requests. For example, set it to `byoc-017aa0ae-33a6-45d3-8548-0f7d1041b40c` for BYOC collection with id `017aa0ae-33a6-45d3-8548-0f7d1041b40c`.

### Request resolution limit

For the limit, we take five times the median resolution of the lowest resolution overview of all tiles in the collection. If this resolution is higher than 500 meters per pixel, the limit is set at 500 meters per pixel. This is to allow for more zoomed out viewing. Note, only overviews which are at least 256 pixels in either width or height are used for this computation. Adding or removing tiles from a collection will recompute its limit.

You can see the computed resolution limit for a collection in the collection details in your dashboard. Alternatively, in the response if querying a collection using the BYOC API.

### Filtering Options

This chapter will explain the `input.data.dataFilter` object.

#### mosaickingOrder

Sets the order of overlapping tiles from which the output result is mosaicked. The tiling is defined by the user when ingesting the data in the collection.

| Value | Description | Notes |
|:---|:---|:---|
| **mostRecent** | The pixel will be selected from the tile, which the most recent `sensing time`. | In case there are more tiles available with the same `sensing time`, the one, which was created later will be used. |
| **leastRecent** | Similar to **mostRecent** but in reverse order. |  |

### Processing Options

This chapter will explain the `input.data.processing` object of the `process` API.

[TABLE]

### Available Bands and Data

Since collections contains your data this means that the available bands are the ones you have prepared. The band names to use in you evalscript are also listed in each collection in your [dashboard](https://shapps.dataspace.copernicus.eu/dashboard/#/byoc).

`dataMask` is also available. In BYOC, dataMask value equals 1 only when a pixel is contained within cover geometry of a BYOC tile and when a pixel has data at the same time. All other instances (e.g. a pixel with data outside tile's cover geometry or a pixel with no-data within tile's cover geometry) will result in `dataMask` 0. Note also that for floating point rasters, NaN is always treated as no data. See [here](../../../APIs/SentinelHub/UserGuides/Datamask.llms.md) for more information.

### Units

The only units available are digital numbers (`DN`) so any unit conversions, if necessary, are the responsibility of your evalscript.

### OGC API

To access your data via OGC you need to create a layer in the [Configuration utility](https://shapps.dataspace.copernicus.eu/dashboard/#/configurations) in either an existing or new configuration. When adding a layer you should set `Source` to `Bring Your Own COG` and `Collection id` to the id of your collection. You should also enter a custom script in `Data processing` field. This should return the appropriate values based on bands that are defined in the collection.

Once this is done the layer can be used via [OGC API](../../../APIs/SentinelHub/OGC.llms.md) in the usual way.

For example: `https://sh.dataspace.copernicus.eu/ogc/wms/<MyInstanceID>?REQUEST=GetMap&BBOX=15959450,8695500,16059450,8795500&CRS=EPSG:3857&WIDTH=500&HEIGHT=500&LAYERS=<MyLayerName>`

#### WFS

To query your tiles using WFS you need to set the WFS feature type (`TYPENAMES` parameter) to `byoc-<MyCollectionID>` e.g. `byoc-a550f5e9-84d0-441a-8338-bbb04d42a72e`.

Here is an example of a WFS `GetFeature` request:

`https://sh.dataspace.copernicus.eu/ogc/wfs/<MyInstanceID>?SERVICE=wfs&REQUEST=GetFeature&BBOX=-90,180,90,-180&SRSNAME=EPSG:4326&OUTPUTFORMAT=application/json&TYPENAMES=byoc-<MyCollectionID>`

## Catalog API Capabilities

To access BYOC product metadata you need to send search request to our [Catalog API](../../../APIs/SentinelHub/Catalog.llms.md). The requested metadata will be returned as JSON formatted response to your request.

### Collection identifier: \<collection id\>

### Distinct extension

- `date`
