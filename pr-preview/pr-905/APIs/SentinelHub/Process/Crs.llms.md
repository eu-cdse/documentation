# CRS support

The list of coordinate reference systems supported by Sentinel Hub API is provided below. The coordinate reference system must be set with an URL starting with [http://www.opengis.net/def/crs/](http://www.opengis.net/def/crs/) and it must be set under the field `input.bounds.properties.crs`, e.g. request in WGS 84 reference system, defined with the URL [http://www.opengis.net/def/crs/EPSG/0/4326](http://www.opengis.net/def/crs/EPSG/0/4326):

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

- [http://www.opengis.net/def/crs/OGC/1.3/CRS84](http://www.opengis.net/def/crs/OGC/1.3/CRS84)
- [http://www.opengis.net/def/crs/EPSG/0/4326](http://www.opengis.net/def/crs/EPSG/0/4326)

## WGS 84 / Pseudo-Mercator:

- [http://www.opengis.net/def/crs/EPSG/0/3857](http://www.opengis.net/def/crs/EPSG/0/3857)

## UTM northern hemisphere:

- [http://www.opengis.net/def/crs/EPSG/0/32601](http://www.opengis.net/def/crs/EPSG/0/32601)
- [http://www.opengis.net/def/crs/EPSG/0/32602](http://www.opengis.net/def/crs/EPSG/0/32602)
- ...
- [http://www.opengis.net/def/crs/EPSG/0/32660](http://www.opengis.net/def/crs/EPSG/0/32660)

The last two digits of EPSG codes above represent the number of corresponding UTM zone in northern hemisphere, e.g. use [http://www.opengis.net/def/crs/EPSG/0/32612](http://www.opengis.net/def/crs/EPSG/0/32612) for UTM zone 12N.

## UTM southern hemisphere:

- [http://www.opengis.net/def/crs/EPSG/0/32701](http://www.opengis.net/def/crs/EPSG/0/32701)
- [http://www.opengis.net/def/crs/EPSG/0/32702](http://www.opengis.net/def/crs/EPSG/0/32702)
- ...
- [http://www.opengis.net/def/crs/EPSG/0/32760](http://www.opengis.net/def/crs/EPSG/0/32760)

The last two digits of EPSG codes above represent the number of corresponding UTM zone in southern hemisphere, e.g. use [http://www.opengis.net/def/crs/EPSG/0/32712](http://www.opengis.net/def/crs/EPSG/0/32712) for UTM zone 12S.

## Others:

- [http://www.opengis.net/def/crs/EPSG/0/2154](http://www.opengis.net/def/crs/EPSG/0/2154) (RGF93 / Lambert-93)
- [http://www.opengis.net/def/crs/EPSG/0/2180](http://www.opengis.net/def/crs/EPSG/0/2180) (ETRS89 / Poland CS92)
- [http://www.opengis.net/def/crs/EPSG/0/2193](http://www.opengis.net/def/crs/EPSG/0/2193) (NZGD2000 / New Zealand Transverse Mercator 2000)
- [http://www.opengis.net/def/crs/EPSG/0/3003](http://www.opengis.net/def/crs/EPSG/0/3003) (Monte Mario / Italy zone 1)
- [http://www.opengis.net/def/crs/EPSG/0/3004](http://www.opengis.net/def/crs/EPSG/0/3004) (Monte Mario / Italy zone 2)
- [http://www.opengis.net/def/crs/EPSG/0/3005](http://www.opengis.net/def/crs/EPSG/0/3005) (NAD83 / BC Albers)
- [http://www.opengis.net/def/crs/EPSG/0/3006](http://www.opengis.net/def/crs/EPSG/0/3006) (SWEREF99 TM)
- [http://www.opengis.net/def/crs/EPSG/0/3031](http://www.opengis.net/def/crs/EPSG/0/3031) (WGS84 / Antarctic Polar Stereographic)
- [http://www.opengis.net/def/crs/EPSG/0/3035](http://www.opengis.net/def/crs/EPSG/0/3035) (ETRS89 / LAEA Europe)
- [http://www.opengis.net/def/crs/EPSG/0/3161](http://www.opengis.net/def/crs/EPSG/0/3161) (NAD83 / Ontario MNR Lambert)
- [http://www.opengis.net/def/crs/EPSG/0/3346](http://www.opengis.net/def/crs/EPSG/0/3346) (LKS94 / Lithuania TM)
- [http://www.opengis.net/def/crs/EPSG/0/3413](http://www.opengis.net/def/crs/EPSG/0/3413) (NSIDC Sea Ice Polar Stereographic North)
- [http://www.opengis.net/def/crs/EPSG/0/3416](http://www.opengis.net/def/crs/EPSG/0/3416) (ETRS89 / Austria Lambert)
- [http://www.opengis.net/def/crs/EPSG/0/3578](http://www.opengis.net/def/crs/EPSG/0/3578) (NAD83 / Yukon Albers)
- [http://www.opengis.net/def/crs/EPSG/0/3580](http://www.opengis.net/def/crs/EPSG/0/3580) (NAD83 / NWT Lambert)
- [http://www.opengis.net/def/crs/EPSG/0/3765](http://www.opengis.net/def/crs/EPSG/0/3765) (HTRS 96 / TM)
- [http://www.opengis.net/def/crs/EPSG/0/3794](http://www.opengis.net/def/crs/EPSG/0/3794) (D96 / TM)
- [http://www.opengis.net/def/crs/EPSG/0/3844](http://www.opengis.net/def/crs/EPSG/0/3844) (Pulkovo 1942(58) / Stereo70)
- [http://www.opengis.net/def/crs/EPSG/0/3912](http://www.opengis.net/def/crs/EPSG/0/3912) (D48 / GK)
- [http://www.opengis.net/def/crs/EPSG/0/3995](http://www.opengis.net/def/crs/EPSG/0/3995) (WGS 84 / Arctic Polar Stereographic)
- [http://www.opengis.net/def/crs/EPSG/0/4026](http://www.opengis.net/def/crs/EPSG/0/4026) (MOLDREF99 / Moldova TM)
- [http://www.opengis.net/def/crs/EPSG/0/5514](http://www.opengis.net/def/crs/EPSG/0/5514) (S-JTSK / Krovak East North)
- [http://www.opengis.net/def/crs/EPSG/0/28992](http://www.opengis.net/def/crs/EPSG/0/28992) (Amersfoort / RD New)
- [http://www.opengis.net/def/crs/EPSG/0/32184](http://www.opengis.net/def/crs/EPSG/0/32184) (NAD83 / MTM zone 4)
