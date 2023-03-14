---
title: Catalog API examples
---

To request data using any of the request below, you will need to replace
the string `<your access token>` with your Sentinel Hub access token.
Sentinel Hub access token will look something like this:

``` sh
ayJhbGciOiJSUzI1NiJ9.ayJzdWIiOiI0MmYwODZjCy1kMzI3LTRlOTMtYWMxNS00ODAwOGFiZjI0YjIiLCJhdWQiOiJlY2I1MGM1Zi1i
MWM1LTQ3ZTgtYWE4NC0zZTU4NzJlM2I2MTEiLCJqdGkiOiI5MzYxMWE4ODEyNTM4Y2M0MmU0NDJjYjUyMTY0YmJlNyIsImV4cCI6MTU1N
TQyMzk3MiwibmFtZSI6ImFuamEudnJlY2tvQHNpbmVyZ2lzZS5jb20iLCJlbWFpbCI6ImFuamEudnJlY2tvQHNpbmVyZ2lzZS5jb20iLC
JzaWQiOiIzZjVjZDVkNS04MjRiLTQ3ZjYtODgwNy0wNDMyNWY4ODQxZmQifQ.U7FPOy_2jlEOFxXSjyN5KEdBROna3-Dyec0feShIbUOY
1p9lEXdNaMmR5euiINi2RXDayX9Kr47CuSTsvq1zHFvZs1YgkFr1iH6kDuX-t_-wfWpqu5oPjoPVKZ4Rj0Ms_dxAUTQFTXR0rlbLuO-KS
gnaeLVb5iiv_qY3Ctq2XKdIRcFRQLFziFcP4yZJl-NZMlwzsiiwjakcpYpI5jSYAdU2hpZLHRzceseeZt5YfZOe5Px1kZXro9Nd0L2GPC
-qzOXw_V1saMGFa2ov8qV6Dvk92iv2SDDdGhOdII_JOf8XkK4E3g2z0EEFdWhG9F4Iky4ukNsqBPgE8LRb31s0hg
```

and can be obtained as described in the [Authentication
chapter](/APIs/SentinelHub/Overview/Authentication.md).

### Catalog API Entry page

Catalog API Entry page with link to other catalog API endpoints and
available collections.

``` python
response = requests.get('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/')
```

### List collections

List all available collections. The list will include deployment
specific collections and collections available to users through BYOC,
Batch or Third Party Data Import functionalities.

``` python
headers = {
}

response = requests.get('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/collections', headers=headers)
```

### Sentinel 2 L1C collection

List single collection, in this case Sentinel 2 L1C collection.

``` python
headers = {
}

response = requests.get(
    'https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/collections/sentinel-2-l1c/',
    headers=headers,
)
```

### Simple GET search

Simple version of search available via GET request is also available.
The only query parameters that can be specified in this simpler version
are: `bbox`, `datetime`, `collections`, `limit` and `next`.

``` python
headers = {
}

response = requests.get(
    'https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search?bbox=13,45,14,46&limit=5&collections=sentinel-1-grd&datetime=2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    headers=headers,
)
```

### Simple POST search

The same parameters can also be specified a POST request, query
parameters need to be specified as `json` formatted body and sent to
server like:

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-10T23:59:59Z',
    'collections': [
        'sentinel-1-grd',
    ],
    'limit': 5,
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Simple POST search with pagination

`next` token can be specified in the request to get back the next page
of results.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-10T23:59:59Z',
    'collections': [
        'sentinel-1-grd',
    ],
    'limit': 5,
    'next': 5,
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search with GeoJSON

Instead of `bbox` it is possible to add `intersects` attribute, which
can be any type of GeoJSON object (Point, LineString, Polygon,
MultiPoint, MultiPolygon).

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'datetime': '2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    'collections': [
        'sentinel-1-grd',
    ],
    'limit': 5,
    'intersects': {
        'type': 'Point',
        'coordinates': [
            13,
            45,
        ],
    },
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search with Filter

`filter` object can be used to instruct server to only return a specific
subset of data.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    'collections': [
        'sentinel-1-grd',
    ],
    'limit': 5,
    'filter': "sat:orbit_state='ascending'",
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Get Filter parameters for collection

List all available filter parameters represented as JSON Schema.

``` python
headers = {
}

response = requests.get(
    'https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/collections/sentinel-1-grd/queryables',
    headers=headers,
)
```

### Search with Fields: No fields

Default outputs from the server can be quite verbose for some
collections. By default, all available item properties are included in
the response.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    'collections': [
        'sentinel-2-l1c',
    ],
    'limit': 1,
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search with Fields: Empty fields

`fields` attribute can be specific to return less information. When
`fields` object is empty only a default set of properties is included:
`id`, `type`, `geometry`, `bbox`, `links`, `assets`.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    'collections': [
        'sentinel-2-l1c',
    ],
    'limit': 1,
    'fields': {},
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search with Fields: Include

By specifying additional attributes in the `include` list, those
attributes are added to the output along with the default ones.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    'collections': [
        'sentinel-2-l1c',
    ],
    'limit': 1,
    'fields': {
        'include': [
            'properties.gsd',
        ],
    },
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search with Fields: Exclude

`exlude` list can be used to exclude even the default ones from the
output.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    'collections': [
        'sentinel-2-l1c',
    ],
    'limit': 1,
    'fields': {
        'exclude': [
            'properties.datetime',
        ],
    },
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search with distinct

Using `distinct` it is possible to get some overview of the data
available inside the specified query. For example specifying `date` as
an option will return a list of dates where data is available.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-01T00:00:00Z/2020-01-01T00:00:00Z',
    'collections': [
        'sentinel-1-grd',
    ],
    'limit': 100,
    'distinct': 'date',
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

Or see different Sentinel 1 instrument modes used.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-01T00:00:00Z/2020-01-01T00:00:00Z',
    'collections': [
        'sentinel-1-grd',
    ],
    'limit': 100,
    'distinct': 'sar:instrument_mode',
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

### Search on BYOC/BATCH collections

You can search for features on your own BYOC or Batch collections. The
functionality described above regarding GET and POST search is the same.
The only difference is that you have to specify the collection id with
the appropriate prefix on `collections` parameter (e.g:
`byoc-<your-collection-id>` for byoc or `batch-<your-collection-id>` for
batch). Remember that you will have to use the appropriate deployment
endpoint depending on where your collection is hosted.

``` python
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'bbox': [
        13,
        45,
        14,
        46,
    ],
    'datetime': '2019-12-10T00:00:00Z/2019-12-10T23:59:59Z',
    'collections': [
        'byoc-<byoc-collection-id>',
    ],
    'limit': 5,
}

response = requests.post('https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search', headers=headers, json=json_data)
```

Or using GET simple search endpoint:

``` python
headers = {
}

response = requests.get(
    'https://sh.dataspace.copernicus.eu/api/v1/catalog/1.0.0/search?bbox=13,45,14,46&limit=5&collections=batch-<batch-collection-id>&datetime=2019-12-10T00:00:00Z/2019-12-11T00:00:00Z',
    headers=headers,
)
```
