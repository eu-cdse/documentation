# Rank composites

Optical satellite imagery contains gaps due to clouds, and the observation scenario. Many methods rely on having gap-free data available at regular time intervals. The most common technique to achieve this is to combine pixels from different observations, which is also referred to as compositing.

Various compositing approaches exist, in this notebook, we demonstrate ‘rank composites’ or more specifically the ‘max NDVI’ composite. A rank composite uses a single ‘rank band’ to decide if pixels of other bands are included in the composite. The advantage of rank composites over compositing per band is that the spectral signal represented by the different bands has been observed in reality in a single observation, and is not a combination of spectral values that occurred at different points in time.

This method is used in various peer reviewed publications, and some of its properties have been validated based on specific sensors: https://www.tandfonline.com/doi/abs/10.1080/01431168608948945

In this case the ‘rank band’ is a simple NDVI, which we ‘score’ based on the maximum value. The rank band can also be a combination of values leading to a more complex score, such as distance to cloud and observation angles. This variant is called a ‘best available pixel’ composite. (https://doi.org/10.1080/07038992.2014.945827)

## openEO implementation

The steps to implement this method in openEO are relatively simple, but may be different from the steps in a ‘traditional’ programming language:

1.  We load and compute the rank band separately
2.  The rank band is converted into a mask, retaining only pixels that we want to select
3.  A datacube with raw bands is loaded, and the rank band mask is applied to it
4.  aggregate_temporal(\_period) is used to create a composite at regular intervals if needed

Most methods require composites for multiple time periods as input. For instance, one composite per month, or every 10 days. We can compute these in one process graph, using apply_neighborhood, so that the result is also an immediate input for further processing.

``` python
spatial_extent = {'west': 4.45, 'east': 4.50, 'south': 51.16, 'north': 51.17, 'crs': 'epsg:4326'}
```

``` python
import openeo
import xarray
import numpy as np
import io
import requests

import panel as pn

import pyproj
import matplotlib.pyplot as plt
import matplotlib

%matplotlib inline
```

``` python
c=openeo.connect("openeofed.dataspace.copernicus.eu")
c.authenticate_oidc()
```

    Authenticated using refresh token.

    <Connection to 'https://openeocloud.vito.be/openeo/1.0.0/' with OidcBearerAuth>

We first create a binary cloud mask, as we don’t want to consider clouded pixels. This is also a good way to avoid loading too much data, which is costly.

``` python
scl = c.load_collection(
    "SENTINEL2_L2A",
    temporal_extent = ["2022-06-04", "2022-08-01"],
    bands = ["SCL"],
    max_cloud_cover=95
)

cloud_mask = scl.process(
    "to_scl_dilation_mask",
    data=scl,
    kernel1_size=17, kernel2_size=77,
    mask1_values=[2, 4, 5, 6, 7],
    mask2_values=[3, 8, 9, 10, 11],
    erosion_kernel_size=3)
```

Now we load the bands required to compute NDVI, apply the cloud mask, and compute NDVI. The NDVI will be our ‘rank band’ in this example.

``` python
ndvi_bands = c.load_collection(
    "SENTINEL2_L2A",
    temporal_extent = ["2022-06-04", "2022-08-01"],
    bands = ["B04", "B08", "SCL"],
    max_cloud_cover=95
)

ndvi_bands = ndvi_bands.mask(cloud_mask)

ndvi = ndvi_bands.ndvi(nir="B08",red="B04")
```

The next step is the most difficult one, and constructs the final mask that will be used to load the full datacube, but with only the observations where the NDVI is equal to the maximum.

We first create a function that computes the maximum NDVI from a series of values, and then loops again over those values to set values to 1 if they are equal to the maximum, and zero otherwise.

The apply_neighborhood process is used here to define the groups of NDVI values on which we want to run this function. We want to create multiple monthly max-NDVI composites, so we specify that the size of groups along the time dimension should correspond to 1 month. Apply_neighborhood is one of the more complex processes, but once you understand it, you’ll notice it’s quite versatile and useful.

``` python
def max_ndvi_selection(ndvi):
    max_ndvi = ndvi.max()
    return ndvi.array_apply(lambda x:x!=max_ndvi)

rank_mask = ndvi.apply_neighborhood(
        max_ndvi_selection,
        size=[{'dimension': 'x', 'unit': 'px', 'value': 1}, {'dimension': 'y', 'unit': 'px', 'value': 1},
              {'dimension': 't', 'value': "month"}],
        overlap=[]
    ).linear_scale_range(0,200,0,200)
combined_mask = rank_mask.merge_cubes(cloud_mask, overlap_resolver="max")
```

At this point, we download our mask for inspection. This is just an intermediate result, and is not needed in a real use case.

``` python
combined_mask.filter_bbox(spatial_extent).execute_batch("the_mask.nc")
```

    0:00:00 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': send 'start'
    0:00:24 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': queued (progress 0%)
    0:00:30 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': queued (progress 0%)
    0:00:37 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': queued (progress 0%)
    0:00:46 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': queued (progress 0%)
    0:01:01 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': queued (progress 0%)
    0:01:15 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': queued (progress 0%)
    0:01:31 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': running (progress N/A)
    0:01:51 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': running (progress N/A)
    0:02:15 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': running (progress N/A)
    0:02:45 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': running (progress N/A)
    0:03:22 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': running (progress N/A)
    0:04:09 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': running (progress N/A)
    0:05:08 Job 'vito-j-240902405ff04d8797c7f9038cbdbe19': finished (progress 100%)

``` python
mask_ds = xarray.open_dataset('the_mask.nc')
mask_ds
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset> Size: 4MB
Dimensions:  (t: 23, x: 352, y: 119)
Coordinates:
  * t        (t) datetime64[ns] 184B 2022-06-04 2022-06-06 ... 2022-07-31
  * x        (x) float64 3kB 6.014e+05 6.014e+05 ... 6.049e+05 6.049e+05
  * y        (y) float64 952B 5.67e+06 5.67e+06 5.67e+06 ... 5.669e+06 5.669e+06
Data variables:
    crs      |S1 1B ...
    var      (t, y, x) float32 4MB ...
Attributes:
    Conventions:  CF-1.9
    institution:  openEO platform - Geotrellis backend: 0.39.0a1
    description:  
    title:        
```

xarray.Dataset

Dimensions:

- t: 23
- x: 352
- y: 119

Coordinates: (3)

t

\(t\)

datetime64\[ns\]

2022-06-04 ... 2022-07-31

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
t

long_name :  
t

axis :  
T

    array(['2022-06-04T00:00:00.000000000', '2022-06-06T00:00:00.000000000',
           '2022-06-09T00:00:00.000000000', '2022-06-11T00:00:00.000000000',
           '2022-06-14T00:00:00.000000000', '2022-06-16T00:00:00.000000000',
           '2022-06-19T00:00:00.000000000', '2022-06-24T00:00:00.000000000',
           '2022-06-26T00:00:00.000000000', '2022-06-29T00:00:00.000000000',
           '2022-07-01T00:00:00.000000000', '2022-07-04T00:00:00.000000000',
           '2022-07-06T00:00:00.000000000', '2022-07-09T00:00:00.000000000',
           '2022-07-11T00:00:00.000000000', '2022-07-14T00:00:00.000000000',
           '2022-07-16T00:00:00.000000000', '2022-07-19T00:00:00.000000000',
           '2022-07-21T00:00:00.000000000', '2022-07-24T00:00:00.000000000',
           '2022-07-26T00:00:00.000000000', '2022-07-29T00:00:00.000000000',
           '2022-07-31T00:00:00.000000000'], dtype='datetime64[ns]')

x

\(x\)

float64

6.014e+05 6.014e+05 ... 6.049e+05

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_x_coordinate

long_name :  
x coordinate of projection

units :  
m

    array([601375., 601385., 601395., ..., 604865., 604875., 604885.])

y

\(y\)

float64

5.67e+06 5.67e+06 ... 5.669e+06

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_y_coordinate

long_name :  
y coordinate of projection

units :  
m

    array([5669795., 5669785., 5669775., 5669765., 5669755., 5669745., 5669735.,
           5669725., 5669715., 5669705., 5669695., 5669685., 5669675., 5669665.,
           5669655., 5669645., 5669635., 5669625., 5669615., 5669605., 5669595.,
           5669585., 5669575., 5669565., 5669555., 5669545., 5669535., 5669525.,
           5669515., 5669505., 5669495., 5669485., 5669475., 5669465., 5669455.,
           5669445., 5669435., 5669425., 5669415., 5669405., 5669395., 5669385.,
           5669375., 5669365., 5669355., 5669345., 5669335., 5669325., 5669315.,
           5669305., 5669295., 5669285., 5669275., 5669265., 5669255., 5669245.,
           5669235., 5669225., 5669215., 5669205., 5669195., 5669185., 5669175.,
           5669165., 5669155., 5669145., 5669135., 5669125., 5669115., 5669105.,
           5669095., 5669085., 5669075., 5669065., 5669055., 5669045., 5669035.,
           5669025., 5669015., 5669005., 5668995., 5668985., 5668975., 5668965.,
           5668955., 5668945., 5668935., 5668925., 5668915., 5668905., 5668895.,
           5668885., 5668875., 5668865., 5668855., 5668845., 5668835., 5668825.,
           5668815., 5668805., 5668795., 5668785., 5668775., 5668765., 5668755.,
           5668745., 5668735., 5668725., 5668715., 5668705., 5668695., 5668685.,
           5668675., 5668665., 5668655., 5668645., 5668635., 5668625., 5668615.])

Data variables: (2)

crs

()

\|S1

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

crs_wkt :  
PROJCS\["WGS 84 / UTM zone 31N", GEOGCS\["WGS 84", DATUM\["World Geodetic System 1984", SPHEROID\["WGS 84", 6378137.0, 298.257223563, AUTHORITY\["EPSG","7030"\]\], AUTHORITY\["EPSG","6326"\]\], PRIMEM\["Greenwich", 0.0, AUTHORITY\["EPSG","8901"\]\], UNIT\["degree", 0.017453292519943295\], AXIS\["Geodetic longitude", EAST\], AXIS\["Geodetic latitude", NORTH\], AUTHORITY\["EPSG","4326"\]\], PROJECTION\["Transverse_Mercator", AUTHORITY\["EPSG","9807"\]\], PARAMETER\["central_meridian", 3.0\], PARAMETER\["latitude_of_origin", 0.0\], PARAMETER\["scale_factor", 0.9996\], PARAMETER\["false_easting", 500000.0\], PARAMETER\["false_northing", 0.0\], UNIT\["m", 1.0\], AXIS\["Easting", EAST\], AXIS\["Northing", NORTH\], AUTHORITY\["EPSG","32631"\]\]

spatial_ref :  
PROJCS\["WGS 84 / UTM zone 31N", GEOGCS\["WGS 84", DATUM\["World Geodetic System 1984", SPHEROID\["WGS 84", 6378137.0, 298.257223563, AUTHORITY\["EPSG","7030"\]\], AUTHORITY\["EPSG","6326"\]\], PRIMEM\["Greenwich", 0.0, AUTHORITY\["EPSG","8901"\]\], UNIT\["degree", 0.017453292519943295\], AXIS\["Geodetic longitude", EAST\], AXIS\["Geodetic latitude", NORTH\], AUTHORITY\["EPSG","4326"\]\], PROJECTION\["Transverse_Mercator", AUTHORITY\["EPSG","9807"\]\], PARAMETER\["central_meridian", 3.0\], PARAMETER\["latitude_of_origin", 0.0\], PARAMETER\["scale_factor", 0.9996\], PARAMETER\["false_easting", 500000.0\], PARAMETER\["false_northing", 0.0\], UNIT\["m", 1.0\], AXIS\["Easting", EAST\], AXIS\["Northing", NORTH\], AUTHORITY\["EPSG","32631"\]\]

    [1 values with dtype=|S1]

var

(t, y, x)

float32

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
var

units :  

grid_mapping :  
crs

    [963424 values with dtype=float32]

Indexes: (3)

t

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2022-06-04', '2022-06-06', '2022-06-09', '2022-06-11',
                   '2022-06-14', '2022-06-16', '2022-06-19', '2022-06-24',
                   '2022-06-26', '2022-06-29', '2022-07-01', '2022-07-04',
                   '2022-07-06', '2022-07-09', '2022-07-11', '2022-07-14',
                   '2022-07-16', '2022-07-19', '2022-07-21', '2022-07-24',
                   '2022-07-26', '2022-07-29', '2022-07-31'],
                  dtype='datetime64[ns]', name='t', freq=None))

x

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([601375.0, 601385.0, 601395.0, 601405.0, 601415.0, 601425.0, 601435.0,
           601445.0, 601455.0, 601465.0,
           ...
           604795.0, 604805.0, 604815.0, 604825.0, 604835.0, 604845.0, 604855.0,
           604865.0, 604875.0, 604885.0],
          dtype='float64', name='x', length=352))

y

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([5669795.0, 5669785.0, 5669775.0, 5669765.0, 5669755.0, 5669745.0,
           5669735.0, 5669725.0, 5669715.0, 5669705.0,
           ...
           5668705.0, 5668695.0, 5668685.0, 5668675.0, 5668665.0, 5668655.0,
           5668645.0, 5668635.0, 5668625.0, 5668615.0],
          dtype='float64', name='y', length=119))

Attributes: (4)

Conventions :  
CF-1.9

institution :  
openEO platform - Geotrellis backend: 0.39.0a1

description :  

title :  

We inspect the mask by filtering out nodata and plotting.

``` python
mask_ds['var'] = mask_ds['var'].where(mask_ds['var']!=129)
mask_ds['var'].plot(vmin=0,vmax=1,col="t",col_wrap=4)
```

![](rank_composites_files/figure-html/cell-10-output-1.png)

## Creating and downloading your composite

Now it’s time to create and load the actual composite, which is very simply once a compositing mask has been created. It’s very important in this step to use the exact same ‘load_collection’ paratemers as were used to create the mask(s), to have a correct output. Note that we still use aggregate_temporal_period, which has 2 effects: - after masking, observations will still have their original dates, this process will generate equitemporal intervals. - In the case where multiple observations have the same NDVI value, the first observation will be retained.

``` python
rgb_bands = c.load_collection(
    "SENTINEL2_L2A",
    temporal_extent = ["2022-06-04", "2022-08-01"],
    bands = ["B02", "B03","B04"],
    max_cloud_cover=95
)

composite = rgb_bands.mask(combined_mask).aggregate_temporal_period("month","first")

composite.filter_bbox(spatial_extent).execute_batch("composite.nc")
```

    0:00:00 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': send 'start'
    0:00:16 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': queued (progress 0%)
    0:00:23 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': queued (progress 0%)
    0:00:30 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': queued (progress 0%)
    0:00:40 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': queued (progress 0%)
    0:00:50 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': queued (progress 0%)
    0:01:02 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': queued (progress 0%)
    0:01:19 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': running (progress N/A)
    0:01:39 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': running (progress N/A)
    0:02:03 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': running (progress N/A)
    0:02:33 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': running (progress N/A)
    0:03:11 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': running (progress N/A)
    0:03:57 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': running (progress N/A)
    0:04:57 Job 'vito-j-2409021b1e84455aa3b1a38b83e768ad': finished (progress 100%)

``` python
composite = xarray.open_dataset('composite.nc')
composite
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset> Size: 1MB
Dimensions:  (t: 2, x: 352, y: 119)
Coordinates:
  * t        (t) datetime64[ns] 16B 2022-06-01 2022-07-01
  * x        (x) float64 3kB 6.014e+05 6.014e+05 ... 6.049e+05 6.049e+05
  * y        (y) float64 952B 5.67e+06 5.67e+06 5.67e+06 ... 5.669e+06 5.669e+06
Data variables:
    crs      |S1 1B ...
    B02      (t, y, x) float32 335kB ...
    B03      (t, y, x) float32 335kB ...
    B04      (t, y, x) float32 335kB ...
Attributes:
    Conventions:  CF-1.9
    institution:  openEO platform - Geotrellis backend: 0.39.0a1
    description:  
    title:        
```

xarray.Dataset

Dimensions:

- t: 2
- x: 352
- y: 119

Coordinates: (3)

t

\(t\)

datetime64\[ns\]

2022-06-01 2022-07-01

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
t

long_name :  
t

axis :  
T

    array(['2022-06-01T00:00:00.000000000', '2022-07-01T00:00:00.000000000'],
          dtype='datetime64[ns]')

x

\(x\)

float64

6.014e+05 6.014e+05 ... 6.049e+05

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_x_coordinate

long_name :  
x coordinate of projection

units :  
m

    array([601375., 601385., 601395., ..., 604865., 604875., 604885.])

y

\(y\)

float64

5.67e+06 5.67e+06 ... 5.669e+06

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_y_coordinate

long_name :  
y coordinate of projection

units :  
m

    array([5669795., 5669785., 5669775., 5669765., 5669755., 5669745., 5669735.,
           5669725., 5669715., 5669705., 5669695., 5669685., 5669675., 5669665.,
           5669655., 5669645., 5669635., 5669625., 5669615., 5669605., 5669595.,
           5669585., 5669575., 5669565., 5669555., 5669545., 5669535., 5669525.,
           5669515., 5669505., 5669495., 5669485., 5669475., 5669465., 5669455.,
           5669445., 5669435., 5669425., 5669415., 5669405., 5669395., 5669385.,
           5669375., 5669365., 5669355., 5669345., 5669335., 5669325., 5669315.,
           5669305., 5669295., 5669285., 5669275., 5669265., 5669255., 5669245.,
           5669235., 5669225., 5669215., 5669205., 5669195., 5669185., 5669175.,
           5669165., 5669155., 5669145., 5669135., 5669125., 5669115., 5669105.,
           5669095., 5669085., 5669075., 5669065., 5669055., 5669045., 5669035.,
           5669025., 5669015., 5669005., 5668995., 5668985., 5668975., 5668965.,
           5668955., 5668945., 5668935., 5668925., 5668915., 5668905., 5668895.,
           5668885., 5668875., 5668865., 5668855., 5668845., 5668835., 5668825.,
           5668815., 5668805., 5668795., 5668785., 5668775., 5668765., 5668755.,
           5668745., 5668735., 5668725., 5668715., 5668705., 5668695., 5668685.,
           5668675., 5668665., 5668655., 5668645., 5668635., 5668625., 5668615.])

Data variables: (4)

crs

()

\|S1

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

crs_wkt :  
PROJCS\["WGS 84 / UTM zone 31N", GEOGCS\["WGS 84", DATUM\["World Geodetic System 1984", SPHEROID\["WGS 84", 6378137.0, 298.257223563, AUTHORITY\["EPSG","7030"\]\], AUTHORITY\["EPSG","6326"\]\], PRIMEM\["Greenwich", 0.0, AUTHORITY\["EPSG","8901"\]\], UNIT\["degree", 0.017453292519943295\], AXIS\["Geodetic longitude", EAST\], AXIS\["Geodetic latitude", NORTH\], AUTHORITY\["EPSG","4326"\]\], PROJECTION\["Transverse_Mercator", AUTHORITY\["EPSG","9807"\]\], PARAMETER\["central_meridian", 3.0\], PARAMETER\["latitude_of_origin", 0.0\], PARAMETER\["scale_factor", 0.9996\], PARAMETER\["false_easting", 500000.0\], PARAMETER\["false_northing", 0.0\], UNIT\["m", 1.0\], AXIS\["Easting", EAST\], AXIS\["Northing", NORTH\], AUTHORITY\["EPSG","32631"\]\]

spatial_ref :  
PROJCS\["WGS 84 / UTM zone 31N", GEOGCS\["WGS 84", DATUM\["World Geodetic System 1984", SPHEROID\["WGS 84", 6378137.0, 298.257223563, AUTHORITY\["EPSG","7030"\]\], AUTHORITY\["EPSG","6326"\]\], PRIMEM\["Greenwich", 0.0, AUTHORITY\["EPSG","8901"\]\], UNIT\["degree", 0.017453292519943295\], AXIS\["Geodetic longitude", EAST\], AXIS\["Geodetic latitude", NORTH\], AUTHORITY\["EPSG","4326"\]\], PROJECTION\["Transverse_Mercator", AUTHORITY\["EPSG","9807"\]\], PARAMETER\["central_meridian", 3.0\], PARAMETER\["latitude_of_origin", 0.0\], PARAMETER\["scale_factor", 0.9996\], PARAMETER\["false_easting", 500000.0\], PARAMETER\["false_northing", 0.0\], UNIT\["m", 1.0\], AXIS\["Easting", EAST\], AXIS\["Northing", NORTH\], AUTHORITY\["EPSG","32631"\]\]

    [1 values with dtype=|S1]

B02

(t, y, x)

float32

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
B02

units :  

grid_mapping :  
crs

    [83776 values with dtype=float32]

B03

(t, y, x)

float32

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
B03

units :  

grid_mapping :  
crs

    [83776 values with dtype=float32]

B04

(t, y, x)

float32

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
B04

units :  

grid_mapping :  
crs

    [83776 values with dtype=float32]

Indexes: (3)

t

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2022-06-01', '2022-07-01'], dtype='datetime64[ns]', name='t', freq=None))

x

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([601375.0, 601385.0, 601395.0, 601405.0, 601415.0, 601425.0, 601435.0,
           601445.0, 601455.0, 601465.0,
           ...
           604795.0, 604805.0, 604815.0, 604825.0, 604835.0, 604845.0, 604855.0,
           604865.0, 604875.0, 604885.0],
          dtype='float64', name='x', length=352))

y

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([5669795.0, 5669785.0, 5669775.0, 5669765.0, 5669755.0, 5669745.0,
           5669735.0, 5669725.0, 5669715.0, 5669705.0,
           ...
           5668705.0, 5668695.0, 5668685.0, 5668675.0, 5668665.0, 5668655.0,
           5668645.0, 5668635.0, 5668625.0, 5668615.0],
          dtype='float64', name='y', length=119))

Attributes: (4)

Conventions :  
CF-1.9

institution :  
openEO platform - Geotrellis backend: 0.39.0a1

description :  

title :  

``` python

rgb_array=composite.to_array(dim="bands").sel(bands=["B04","B03","B02"]).astype(np.float32)/10000
rgb_array
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.DataArray (bands: 3, t: 2, y: 119, x: 352)> Size: 1MB
array([[[[0.1007, 0.1026, 0.0713, ..., 0.0566, 0.0427, 0.0598],
         [0.0868, 0.101 , 0.0811, ..., 0.083 , 0.0714, 0.104 ],
         [0.087 , 0.0872, 0.0858, ..., 0.13  , 0.097 , 0.1382],
         ...,
         [0.0996, 0.096 , 0.0677, ..., 0.0165, 0.0178, 0.0228],
         [0.0599, 0.059 , 0.0776, ..., 0.015 , 0.0168, 0.023 ],
         [0.0532, 0.0518, 0.0499, ..., 0.0145, 0.0156, 0.0192]],

        [[0.0948, 0.0891, 0.0833, ..., 0.0696, 0.0776, 0.1158],
         [0.0906, 0.091 , 0.0759, ..., 0.1292, 0.1406, 0.156 ],
         [0.1098, 0.0921, 0.092 , ..., 0.1044, 0.0991, 0.117 ],
         ...,
         [0.1048, 0.0786, 0.061 , ..., 0.0213, 0.0233, 0.0326],
         [0.0576, 0.0545, 0.0689, ..., 0.022 , 0.0211, 0.0276],
         [0.0522, 0.0497, 0.055 , ..., 0.0202, 0.0208, 0.0212]]],


       [[[0.0966, 0.0972, 0.0716, ..., 0.0665, 0.0536, 0.0714],
         [0.0845, 0.0871, 0.0762, ..., 0.0773, 0.072 , 0.1106],
         [0.083 , 0.083 , 0.0882, ..., 0.1206, 0.1004, 0.1616],
...
         [0.0628, 0.0648, 0.078 , ..., 0.0435, 0.0452, 0.0552],
         [0.0596, 0.06  , 0.0659, ..., 0.042 , 0.046 , 0.0477]]],


       [[[0.0732, 0.0776, 0.0601, ..., 0.0479, 0.0394, 0.0458],
         [0.0676, 0.078 , 0.0606, ..., 0.0708, 0.0594, 0.0787],
         [0.0746, 0.0784, 0.0802, ..., 0.1036, 0.0727, 0.145 ],
         ...,
         [0.0742, 0.0708, 0.0469, ..., 0.0196, 0.018 , 0.0236],
         [0.0438, 0.0426, 0.0546, ..., 0.0188, 0.0182, 0.0208],
         [0.0429, 0.0431, 0.0418, ..., 0.0179, 0.0188, 0.0206]],

        [[0.0675, 0.0698, 0.093 , ..., 0.0559, 0.0618, 0.0913],
         [0.0758, 0.0794, 0.0599, ..., 0.098 , 0.1118, 0.1184],
         [0.1146, 0.0814, 0.0788, ..., 0.0836, 0.0696, 0.1168],
         ...,
         [0.0838, 0.0661, 0.0495, ..., 0.0211, 0.0213, 0.0284],
         [0.0486, 0.0416, 0.0676, ..., 0.0197, 0.0181, 0.0226],
         [0.0475, 0.0442, 0.0456, ..., 0.0202, 0.0198, 0.0227]]]],
      dtype=float32)
Coordinates:
  * t        (t) datetime64[ns] 16B 2022-06-01 2022-07-01
  * x        (x) float64 3kB 6.014e+05 6.014e+05 ... 6.049e+05 6.049e+05
  * y        (y) float64 952B 5.67e+06 5.67e+06 5.67e+06 ... 5.669e+06 5.669e+06
  * bands    (bands) object 24B 'B04' 'B03' 'B02'
```

xarray.DataArray

- bands: 3
- t: 2
- y: 119
- x: 352

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

0.1007 0.1026 0.0713 0.0976 0.1158 ... 0.0212 0.0202 0.0198 0.0227

    array([[[[0.1007, 0.1026, 0.0713, ..., 0.0566, 0.0427, 0.0598],
             [0.0868, 0.101 , 0.0811, ..., 0.083 , 0.0714, 0.104 ],
             [0.087 , 0.0872, 0.0858, ..., 0.13  , 0.097 , 0.1382],
             ...,
             [0.0996, 0.096 , 0.0677, ..., 0.0165, 0.0178, 0.0228],
             [0.0599, 0.059 , 0.0776, ..., 0.015 , 0.0168, 0.023 ],
             [0.0532, 0.0518, 0.0499, ..., 0.0145, 0.0156, 0.0192]],

            [[0.0948, 0.0891, 0.0833, ..., 0.0696, 0.0776, 0.1158],
             [0.0906, 0.091 , 0.0759, ..., 0.1292, 0.1406, 0.156 ],
             [0.1098, 0.0921, 0.092 , ..., 0.1044, 0.0991, 0.117 ],
             ...,
             [0.1048, 0.0786, 0.061 , ..., 0.0213, 0.0233, 0.0326],
             [0.0576, 0.0545, 0.0689, ..., 0.022 , 0.0211, 0.0276],
             [0.0522, 0.0497, 0.055 , ..., 0.0202, 0.0208, 0.0212]]],


           [[[0.0966, 0.0972, 0.0716, ..., 0.0665, 0.0536, 0.0714],
             [0.0845, 0.0871, 0.0762, ..., 0.0773, 0.072 , 0.1106],
             [0.083 , 0.083 , 0.0882, ..., 0.1206, 0.1004, 0.1616],
    ...
             [0.0628, 0.0648, 0.078 , ..., 0.0435, 0.0452, 0.0552],
             [0.0596, 0.06  , 0.0659, ..., 0.042 , 0.046 , 0.0477]]],


           [[[0.0732, 0.0776, 0.0601, ..., 0.0479, 0.0394, 0.0458],
             [0.0676, 0.078 , 0.0606, ..., 0.0708, 0.0594, 0.0787],
             [0.0746, 0.0784, 0.0802, ..., 0.1036, 0.0727, 0.145 ],
             ...,
             [0.0742, 0.0708, 0.0469, ..., 0.0196, 0.018 , 0.0236],
             [0.0438, 0.0426, 0.0546, ..., 0.0188, 0.0182, 0.0208],
             [0.0429, 0.0431, 0.0418, ..., 0.0179, 0.0188, 0.0206]],

            [[0.0675, 0.0698, 0.093 , ..., 0.0559, 0.0618, 0.0913],
             [0.0758, 0.0794, 0.0599, ..., 0.098 , 0.1118, 0.1184],
             [0.1146, 0.0814, 0.0788, ..., 0.0836, 0.0696, 0.1168],
             ...,
             [0.0838, 0.0661, 0.0495, ..., 0.0211, 0.0213, 0.0284],
             [0.0486, 0.0416, 0.0676, ..., 0.0197, 0.0181, 0.0226],
             [0.0475, 0.0442, 0.0456, ..., 0.0202, 0.0198, 0.0227]]]],
          dtype=float32)

Coordinates: (4)

t

\(t\)

datetime64\[ns\]

2022-06-01 2022-07-01

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
t

long_name :  
t

axis :  
T

    array(['2022-06-01T00:00:00.000000000', '2022-07-01T00:00:00.000000000'],
          dtype='datetime64[ns]')

x

\(x\)

float64

6.014e+05 6.014e+05 ... 6.049e+05

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_x_coordinate

long_name :  
x coordinate of projection

units :  
m

    array([601375., 601385., 601395., ..., 604865., 604875., 604885.])

y

\(y\)

float64

5.67e+06 5.67e+06 ... 5.669e+06

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_y_coordinate

long_name :  
y coordinate of projection

units :  
m

    array([5669795., 5669785., 5669775., 5669765., 5669755., 5669745., 5669735.,
           5669725., 5669715., 5669705., 5669695., 5669685., 5669675., 5669665.,
           5669655., 5669645., 5669635., 5669625., 5669615., 5669605., 5669595.,
           5669585., 5669575., 5669565., 5669555., 5669545., 5669535., 5669525.,
           5669515., 5669505., 5669495., 5669485., 5669475., 5669465., 5669455.,
           5669445., 5669435., 5669425., 5669415., 5669405., 5669395., 5669385.,
           5669375., 5669365., 5669355., 5669345., 5669335., 5669325., 5669315.,
           5669305., 5669295., 5669285., 5669275., 5669265., 5669255., 5669245.,
           5669235., 5669225., 5669215., 5669205., 5669195., 5669185., 5669175.,
           5669165., 5669155., 5669145., 5669135., 5669125., 5669115., 5669105.,
           5669095., 5669085., 5669075., 5669065., 5669055., 5669045., 5669035.,
           5669025., 5669015., 5669005., 5668995., 5668985., 5668975., 5668965.,
           5668955., 5668945., 5668935., 5668925., 5668915., 5668905., 5668895.,
           5668885., 5668875., 5668865., 5668855., 5668845., 5668835., 5668825.,
           5668815., 5668805., 5668795., 5668785., 5668775., 5668765., 5668755.,
           5668745., 5668735., 5668725., 5668715., 5668705., 5668695., 5668685.,
           5668675., 5668665., 5668655., 5668645., 5668635., 5668625., 5668615.])

bands

(bands)

object

'B04' 'B03' 'B02'

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array(['B04', 'B03', 'B02'], dtype=object)

Indexes: (4)

t

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2022-06-01', '2022-07-01'], dtype='datetime64[ns]', name='t', freq=None))

x

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([601375.0, 601385.0, 601395.0, 601405.0, 601415.0, 601425.0, 601435.0,
           601445.0, 601455.0, 601465.0,
           ...
           604795.0, 604805.0, 604815.0, 604825.0, 604835.0, 604845.0, 604855.0,
           604865.0, 604875.0, 604885.0],
          dtype='float64', name='x', length=352))

y

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([5669795.0, 5669785.0, 5669775.0, 5669765.0, 5669755.0, 5669745.0,
           5669735.0, 5669725.0, 5669715.0, 5669705.0,
           ...
           5668705.0, 5668695.0, 5668685.0, 5668675.0, 5668665.0, 5668655.0,
           5668645.0, 5668635.0, 5668625.0, 5668615.0],
          dtype='float64', name='y', length=119))

bands

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index(['B04', 'B03', 'B02'], dtype='object', name='bands'))

Attributes: (0)

## Final result & conclusion

We finally plot composites generated for 2 months. While this notebook ends here, for most real world cases, this is the point where you can start your actual work, as you now have gap-free equitemporal composites. Note that in openEO, things happen on the fly, and this method is quite efficient, so there’s no need to actually store these intermediate composites somewhere before movin on, you can just take the composited data cube, and go from there!

### Note on performance

This approach was designed with efficiency in mind: we explicitly load a minimum amount of bands to construct the mask. As a result if observations are not used in the composite at all, they do not need to be loaded for the final result. The max-NDVI approach is however somewhat limited in this regard, because the plots of the mask show that often many chunks are needed for the final output.

One other remark is that it could be an option to construct the mask at lower resolution: this would further reduce data loading times, at the cost of a somewhat less accurate max-NDVI composite.

``` python
xarray.plot.imshow(rgb_array.isel(t=0),vmin=0,vmax=0.18,rgb="bands",col_wrap=2)
```

![](rank_composites_files/figure-html/cell-14-output-1.png)
