---
title: Catalog API
---

Sentinel Hub Catalog API (or shortly \"Catalog\") is an API implementing
the [STAC Specification](https://stacspec.org/), describing geospatial
information about different data used with Sentinel Hub.

## API Reference

API Reference for Sentinel Hub Catalog is available as an [OpenAPI
description](https://docs.sentinel-hub.com/api/latest/reference/#tag/catalog_core).

Simple search request for Sentinel-1 GRD with a bounding box (the
coordinate reference system of the values is WGS84 longitude/latitude),
available on 10th December 2019.

``` python
data = {
    "bbox": [13, 45, 14, 46],
    "datetime": "2019-12-10T00:00:00Z/2019-12-10T23:59:59Z",
    "collections": ["sentinel-1-grd"],
    "limit": 5,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search"
response = requests.post(url, json=data)
```

## Authentication

Authentication for the Catalog API works completely the same as
authentication for other Sentinel Hub services, see [Authentication
chapter](/APIs/SentinelHub/Overview/Authentication.md).

## Pagination

Executing the request specified above returns search context fields at
the end of the response, looking like this:

``` json
{
  "context": {
    "next": 5,
    "limit": 5,
    "returned": 5
  }
}
```

The presence of the `next` attribute indicates there is more data
available for this query, but the server chose to only return 5 results,
because the `limit` specified was `5` (if `limit` is not specified,
default value is `10`). To query the next page of items, our request
needs to include the `next` attribute with its value in the query, like
so:

``` python
data = {
    "bbox": [13, 45, 14, 46],
    "datetime": "2019-12-10T00:00:00Z/2019-12-10T23:59:59Z",
    "collections": ["sentinel-1-grd"],
    "limit": 5,
    "next": 5,
}

url = "https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search"
response = requests.post(url, json=data)
```

The response now includes the next page of items; in this case there is
no `next` token in `context`, meaning no more items exist for this
query.

## Extensions

### Filter

The search endpoint by default only accepts the parameters described in
[OpenAPI](https://docs.sentinel-hub.com/api/latest/reference/#tag/catalog_item_search/operation/postCatalogItemSearch).
The Filter extension enables users to specify an additional parameter to
filter on, while searching through data.

The syntax for `filter` is
[CQL2](https://docs.ogc.org/DRAFTS/21-065.html):

``` json
{
  "filter": {
    "op": "<operator>",
    "args": [
      {
        "property": "<property_name>"
      },
      "<value>"
    ]
  },
  "filter-lang": "cql2-json"
}
```

It is also possible to use simple cql2-text:

``` json
{
  "filter": "eo:cloud_cover > 90"
}
```

The available operators are `eq`, `neq`, `lt`, `lte`, `gt`, `gte`,
`between` and `not`. Only `and` is currently supported as a logical
operator. Be careful - different collections have different properties
for the query filter available. The information describing this is
available inside the documentation for each specific collection (ex.
[Sentinel-1 GRD](/Data/Sentinel1.md#filter-extension)).

### Fields

By default, the search endpoint returns all the available attributes of
each item. The `fields` extension provides a way for the client to
specify which attributes should not be part of the output, making it
easy for the client to not have to deal with unnecessary data.

Syntax for the `fields` is:

``` json
{
  "fields": {
    "include": [
      "<property_name_1>",
      "<property_name_2>"
    ],
    "exclude": [
      "<property_name_3>",
      "<property_name_4>",
      "<property_name_5>"
    ]
  }
}
```

#### Include/Exclude behaviour

-   When no `fields` attribute is specified in the request, all the
    available attributes will be included in the response.
-   If the `fields` attribute is specified with an empty object, or both
    `include` and `exclude` are set to null or an empty array is
    returned, the attributes for each item will be as if `include` was
    set to a default set of
    `["id", "type", "geometry", "bbox", "links", "assets", "properties.datetime"]`.
-   If only `include` is specified, the attributes in `include` will be
    merged with the default set above.
-   If only `exclude` is specified, the attributes in `exclude` will be
    removed from the default set above.
-   If both `include` and `exclude` are specified, the rule is that an
    attribute must be included in and not excluded from the response.

### Distinct

Sometimes we don\'t want to search for product metadata, but want some
general information about the product, such as for example, which
acquisition dates are available for Sentinel-1 inside the specified
`bbox` and time interval. `distinct` attribute inside a search request
makes this possible.

Syntax for `distinct` attribute is:

``` json
{
  "distinct": "<property_name>"
}
```

As with the `filter` attribute, `distinct` is also a collection limited
to some specific properties. Information describing these properties can
be found inside each collection\'s documentation (ex. [Sentinel-1
GRD](/Data/Sentinel1.md#distinct-extension)).
