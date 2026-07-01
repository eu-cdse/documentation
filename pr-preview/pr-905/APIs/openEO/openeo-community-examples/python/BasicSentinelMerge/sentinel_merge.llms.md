# Creating multi-mission, multi-temporal datacube

``` python
import openeo
```

This notebook shows how to combine timeseries data from two popular missions, Sentinel-1 and Sentinel-2, in a single datacube for further processing. It can be considered a basic template for many use cases.

It uses precomputed backscatter if available and falls back to compute backscatter on the fly, which works globally but consumes more credits.

We also create 10-daily composites and apply linear interpolation to avoid gaps. Specific methods may require different cloud masking and preprocessing options.

``` python
c = openeo.connect("openeofed.dataspace.copernicus.eu")
c.authenticate_oidc()


scl = c.load_collection(
    "SENTINEL2_L2A",
    temporal_extent=["2022-06-04", "2022-08-04"],
    bands=["SCL"],
    max_cloud_cover=95,
)
cloud_mask = scl.process(
    "to_scl_dilation_mask",
    data=scl,
    kernel1_size=17, kernel2_size=77,
    mask1_values=[2, 4, 5, 6, 7],
    mask2_values=[3, 8, 9, 10, 11],
    erosion_kernel_size=3)


sentinel2 = c.load_collection(
    "SENTINEL2_L2A",
    temporal_extent=["2022-06-04", "2022-08-04"],
    bands=["B02", "B03", "B04"],
    max_cloud_cover=95,
)

sentinel2 = sentinel2.mask(cloud_mask)

sentinel2 = sentinel2.aggregate_temporal_period(
    "dekad", reducer="median"
).apply_dimension(dimension="t", process="array_interpolate_linear")
```

    Authenticated using refresh token.

Some openEO backends offer precomputed Sentinel-1 backscatter. We [inspect the backend metadata](https://open-eo.github.io/openeo-python-client/data_access.html#data-discovery) to check if such a collection is available otherwise we start from raw GRD and [compute it on the fly](https://open-eo.github.io/openeo-python-client/cookbook/ard.html#sar-backscatter).

``` python
S1_collection = "SENTINEL1_GRD"
if "SENTINEL1_GRD_SIGMA0" in c.list_collection_ids():
    S1_collection = "SENTINEL1_GRD_SIGMA0"

S1_collection
```

    'SENTINEL1_GRD_SIGMA0'

``` python
sentinel1 = c.load_collection(
    S1_collection, temporal_extent=["2022-06-04", "2022-08-04"], bands=["VV", "VH"]
)

if S1_collection == "SENTINEL1_GRD":
    sentinel1 = sentinel1.sar_backscatter(
        coefficient="sigma0-ellipsoid",
        local_incidence_angle=False,
        elevation_model="COPERNICUS_30",
    )

sentinel1 = sentinel1.aggregate_temporal_period(
    "dekad", reducer="median"
).apply_dimension(dimension="t", process="array_interpolate_linear")
```

Now we can simply combine both cubes. Resampling is performed implicitly if needed, but explicit resampling can also be specified.

``` python
merged = sentinel2.merge_cubes(sentinel1)
```

The next block receives the combined Sentinel-1 and Sentinel-2 input and transforms it using any method. This can be, for instance, a neural network based on PyTorch.

This example uses blocks of 128x128 pixels with an 8-pixel overlap. Sizes for the time and band dimensions are not specified so that they will be fully included.

The UDF in this example also shows how to print statements to the log, which is an easy way to understand better the XArray data passed in. More information on UDFs can be found in [the documentation](https://open-eo.github.io/openeo-python-client/udf.html).

``` python
my_udf = openeo.UDF(
    """
from openeo.udf import XarrayDataCube
from openeo.udf.debug import inspect

def apply_datacube(cube: XarrayDataCube, context: dict) -> XarrayDataCube:
    array = cube.get_array()
    inspect(array,level="ERROR",message="inspecting input cube")
    array.values = 0.0001 * array.values
    return cube
"""
)

fused = merged.apply_neighborhood(
    my_udf,
    size=[
        {"dimension": "x", "value": 112, "unit": "px"},
        {"dimension": "y", "value": 112, "unit": "px"},
    ],
    overlap=[
        {"dimension": "x", "value": 8, "unit": "px"},
        {"dimension": "y", "value": 8, "unit": "px"},
    ],
)
```

``` python
spatial_extent = {
    "west": 4.45,
    "east": 4.70,
    "south": 51.16,
    "north": 51.22,
    "crs": "epsg:4326",
}
job = fused.filter_bbox(spatial_extent).execute_batch(
    "result.nc", title="Sentinel composite", filename_prefix="merged_cube"
)
```

    0:00:00 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': send 'start'
    0:00:46 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': queued (progress 0%)
    0:00:51 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': queued (progress 0%)
    0:00:59 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': queued (progress 0%)
    0:01:09 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': queued (progress 0%)
    0:01:20 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:01:35 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:01:50 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:02:10 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:02:38 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:03:09 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:03:47 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:04:35 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:05:33 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:06:34 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:07:34 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:08:34 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:09:34 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': running (progress N/A)
    0:10:37 Job 'vito-j-24080502c7b5492191eeec5b7c2090dd': finished (progress 100%)

When the job is finished, are downloaded as netCDF and can be inspected using XArray or a desktop viewer like QGis.

``` python
import xarray as xr

xr.open_dataset("result.nc")
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset>
Dimensions:  (t: 7, x: 1762, y: 706)
Coordinates:
  * t        (t) datetime64[ns] 2022-06-01 2022-06-11 ... 2022-07-21 2022-08-01
  * x        (x) float64 6.013e+05 6.013e+05 6.013e+05 ... 6.189e+05 6.189e+05
  * y        (y) float64 5.676e+06 5.676e+06 5.676e+06 ... 5.669e+06 5.669e+06
Data variables:
    crs      |S1 ...
    B02      (t, y, x) float64 ...
    B03      (t, y, x) float64 ...
    B04      (t, y, x) float64 ...
    SCL      (t, y, x) float64 ...
    VV       (t, y, x) float64 ...
    VH       (t, y, x) float64 ...
Attributes:
    Conventions:  CF-1.9
    institution:  openEO platform - Geotrellis backend: 0.38.6a1
    description:  
    title:        
```

xarray.Dataset

Dimensions:

- t: 7
- x: 1762
- y: 706

Coordinates: (3)

t

\(t\)

datetime64\[ns\]

2022-06-01 ... 2022-08-01

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
t

long_name :  
t

axis :  
T

    array(['2022-06-01T00:00:00.000000000', '2022-06-11T00:00:00.000000000',
           '2022-06-21T00:00:00.000000000', '2022-07-01T00:00:00.000000000',
           '2022-07-11T00:00:00.000000000', '2022-07-21T00:00:00.000000000',
           '2022-08-01T00:00:00.000000000'], dtype='datetime64[ns]')

x

\(x\)

float64

6.013e+05 6.013e+05 ... 6.189e+05

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_x_coordinate

long_name :  
x coordinate of projection

units :  
m

    array([601265., 601275., 601285., ..., 618855., 618865., 618875.])

y

\(y\)

float64

5.676e+06 5.676e+06 ... 5.669e+06

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_y_coordinate

long_name :  
y coordinate of projection

units :  
m

    array([5675665., 5675655., 5675645., ..., 5668635., 5668625., 5668615.])

Data variables: (7)

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

float64

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
B02

units :  

grid_mapping :  
crs

    [8707804 values with dtype=float64]

B03

(t, y, x)

float64

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
B03

units :  

grid_mapping :  
crs

    [8707804 values with dtype=float64]

B04

(t, y, x)

float64

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
B04

units :  

grid_mapping :  
crs

    [8707804 values with dtype=float64]

SCL

(t, y, x)

float64

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
SCL

units :  

grid_mapping :  
crs

    [8707804 values with dtype=float64]

VV

(t, y, x)

float64

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
VV

units :  

grid_mapping :  
crs

    [8707804 values with dtype=float64]

VH

(t, y, x)

float64

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
VH

units :  

grid_mapping :  
crs

    [8707804 values with dtype=float64]

Indexes: (3)

t

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2022-06-01', '2022-06-11', '2022-06-21', '2022-07-01',
                   '2022-07-11', '2022-07-21', '2022-08-01'],
                  dtype='datetime64[ns]', name='t', freq=None))

x

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([601265.0, 601275.0, 601285.0, 601295.0, 601305.0, 601315.0, 601325.0,
           601335.0, 601345.0, 601355.0,
           ...
           618785.0, 618795.0, 618805.0, 618815.0, 618825.0, 618835.0, 618845.0,
           618855.0, 618865.0, 618875.0],
          dtype='float64', name='x', length=1762))

y

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([5675665.0, 5675655.0, 5675645.0, 5675635.0, 5675625.0, 5675615.0,
           5675605.0, 5675595.0, 5675585.0, 5675575.0,
           ...
           5668705.0, 5668695.0, 5668685.0, 5668675.0, 5668665.0, 5668655.0,
           5668645.0, 5668635.0, 5668625.0, 5668615.0],
          dtype='float64', name='y', length=706))

Attributes: (4)

Conventions :  
CF-1.9

institution :  
openEO platform - Geotrellis backend: 0.38.6a1

description :  

title :  

You can also inspect the result in the openEO editor: ![Result in openEO editor](result.png "Batch job result")
