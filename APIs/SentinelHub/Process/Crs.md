---
title: CRS support
---

The list of coordinate reference systems supported by Sentinel Hub API
is provided below. The coordinate reference system must be set with an
URL starting with <http://www.opengis.net/def/crs/> and it must be set
under the field `input.bounds.properties.crs`, e.g. request in WGS 84
reference system, defined with the URL
<http://www.opengis.net/def/crs/EPSG/0/4326>:

``` json
{
  "input": {
    "bounds": {
      "bbox": [
        12.8114318847656,
        41.9663828501025,
        12.8732299804687,
        42.0046623333086
      ],
      "properties": {
        "crs": "http://www.opengis.net/def/crs/EPSG/0/4326"
      }
    },
    "data": [
      {
        "type": "sentinel-2-l1c"
      }
    ]
  },
  ...
}
```

## WGS 84:

-   <http://www.opengis.net/def/crs/OGC/1.3/CRS84>
-   <http://www.opengis.net/def/crs/EPSG/0/4326>

## WGS 84 / Pseudo-Mercator: {#wgs-84--pseudo-mercator}

-   <http://www.opengis.net/def/crs/EPSG/0/3857>

## UTM northern hemisphere:

-   <http://www.opengis.net/def/crs/EPSG/0/32601>
-   <http://www.opengis.net/def/crs/EPSG/0/32602>
-   \...
-   <http://www.opengis.net/def/crs/EPSG/0/32660>

The last two digits of EPSG codes above represent the number of
corresponding UTM zone in northern hemisphere, e.g. use
<http://www.opengis.net/def/crs/EPSG/0/32612> for UTM zone 12N.

## UTM southern hemisphere:

-   <http://www.opengis.net/def/crs/EPSG/0/32701>
-   <http://www.opengis.net/def/crs/EPSG/0/32702>
-   \...
-   <http://www.opengis.net/def/crs/EPSG/0/32760>

The last two digits of EPSG codes above represent the number of
corresponding UTM zone in southern hemisphere, e.g. use
<http://www.opengis.net/def/crs/EPSG/0/32712> for UTM zone 12S.

## Others:

-   <http://www.opengis.net/def/crs/EPSG/0/2154>
-   <http://www.opengis.net/def/crs/EPSG/0/2180>
-   <http://www.opengis.net/def/crs/EPSG/0/2193>
-   <http://www.opengis.net/def/crs/EPSG/0/3003>
-   <http://www.opengis.net/def/crs/EPSG/0/3004>
-   <http://www.opengis.net/def/crs/EPSG/0/3031>
-   <http://www.opengis.net/def/crs/EPSG/0/3035>
-   <http://www.opengis.net/def/crs/EPSG/0/3346>
-   <http://www.opengis.net/def/crs/EPSG/0/3413>
-   <http://www.opengis.net/def/crs/EPSG/0/3416>
-   <http://www.opengis.net/def/crs/EPSG/0/3765>
-   <http://www.opengis.net/def/crs/EPSG/0/3794>
-   <http://www.opengis.net/def/crs/EPSG/0/3844>
-   <http://www.opengis.net/def/crs/EPSG/0/3912>
-   <http://www.opengis.net/def/crs/EPSG/0/3995>
-   <http://www.opengis.net/def/crs/EPSG/0/4026>
-   <http://www.opengis.net/def/crs/EPSG/0/5514>
-   <http://www.opengis.net/def/crs/EPSG/0/28992>
