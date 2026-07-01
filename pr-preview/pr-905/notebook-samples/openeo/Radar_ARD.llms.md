![Sentinel-1](https://github.com/openEOPlatform/SRR1_notebooks/raw/main/data/images/Sentinel_1.jpg) \# Radar - Sentinel-1: ARD SAR Backscatter

For certain use cases, the readily available preprocessed data collections in the openEO back-ends are not sufficient or inappropriately preprocessed. openEO supports some processes to address very common preprocessing scenarios:

- Atmospheric correction of optical data
- SAR backscatter computation

These processes also offer a number of parameters to customize the processing.

However, please note that these operations can be computationally expensive, so they certainly affect the overall processing time and cost of your final algorithm. Hence, make sure to make an informed decision when using these methods.

In this notebook has been duplicated from an existing sample processing pipeline for Radar ARD on the openEO platform. In this instance, we aim to showcase it with the Copernicus Data Space Ecosystem backend.

## Setup

Import the `openeo` package and connect to the Copernicus Data Space Ecosystem openEO back-end.

``` python
import openeo
```

``` python
backend = "openeo.dataspace.copernicus.eu"
conn = openeo.connect(backend).authenticate_oidc()
```

    Authenticated using refresh token.

### On-demand SAR Backscatter

Data from synthetic aperture radar (SAR) sensors requires significant preprocessing to be calibrated and normalized. This is referred to as backscatter computation and is provided in the openEO by the [`sar_backscatter` process](https://docs.openeo.cloud/processes/#sar_backscatter).

The radiometric correction coefficient used in this example is `sigma0-ellipsoid`.

## Specify area of interest, temporal extent, polarization

``` python
spatial_extent = {
    "west": 11.293602,
    "east": 11.382866,
    "south": 46.460163,
    "north": 46.514768,
    "crs": "EPSG:4326",
}

s1 = conn.load_collection(
    "SENTINEL1_GRD",
    spatial_extent=spatial_extent,
    bands=["VV", "VH"],
    temporal_extent=["2021-01-01", "2021-01-08"],
    properties={"sat:orbit_state": lambda od: od == "ASCENDING"},
)
```

## Apply openEO processes

Here we apply both the SAR backscattering processes on the datacube and then convert it from linear to dB scale.

``` python
s1_scatter = s1.sar_backscatter(
    coefficient="sigma0-ellipsoid", elevation_model="COPERNICUS_30"
)
s1bs = s1_scatter.apply(lambda x: 10 * x.log(base=10))
```

## Execution

Since our area of interest is small, a direct request is preferred. Nevertheless, please note that this approach will not return the JSON metadata. If you want JSON metadata along with the result you can choose the Batch job-based method too.

Note that this step automatically adds the save_result process at the end based on the output format we choose.

``` python
%time s1bs.download("sar_bs.nc")
```

    CPU times: user 13.6 ms, sys: 22.7 ms, total: 36.3 ms
    Wall time: 28 s

## Output visualization

``` python
import xarray as xr

S1_ard = xr.open_dataset("sar_bs.nc")
S1_ard
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset>
Dimensions:  (t: 1, x: 704, y: 628)
Coordinates:
  * t        (t) datetime64[ns] 2021-01-03
  * x        (x) float64 6.759e+05 6.76e+05 6.76e+05 ... 6.83e+05 6.83e+05
  * y        (y) float64 5.154e+06 5.154e+06 5.154e+06 ... 5.148e+06 5.148e+06
Data variables:
    crs      |S1 ...
    VV       (t, y, x) float32 ...
    VH       (t, y, x) float32 ...
Attributes:
    Conventions:  CF-1.9
    institution:  openEO platform
```

xarray.Dataset

Dimensions:

- t: 1
- x: 704
- y: 628

Coordinates: (3)

t

\(t\)

datetime64\[ns\]

2021-01-03

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
t

long_name :  
t

axis :  
T

    array(['2021-01-03T00:00:00.000000000'], dtype='datetime64[ns]')

x

\(x\)

float64

6.759e+05 6.76e+05 ... 6.83e+05

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_x_coordinate

long_name :  
x coordinate of projection

units :  
m

    array([675945., 675955., 675965., ..., 682955., 682965., 682975.])

y

\(y\)

float64

5.154e+06 5.154e+06 ... 5.148e+06

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
projection_y_coordinate

long_name :  
y coordinate of projection

units :  
m

    array([5154005., 5153995., 5153985., ..., 5147755., 5147745., 5147735.])

Data variables: (3)

crs

()

\|S1

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

crs_wkt :  
PROJCS\["WGS 84 / UTM zone 32N", GEOGCS\["WGS 84", DATUM\["World Geodetic System 1984", SPHEROID\["WGS 84", 6378137.0, 298.257223563, AUTHORITY\["EPSG","7030"\]\], AUTHORITY\["EPSG","6326"\]\], PRIMEM\["Greenwich", 0.0, AUTHORITY\["EPSG","8901"\]\], UNIT\["degree", 0.017453292519943295\], AXIS\["Geodetic longitude", EAST\], AXIS\["Geodetic latitude", NORTH\], AUTHORITY\["EPSG","4326"\]\], PROJECTION\["Transverse_Mercator", AUTHORITY\["EPSG","9807"\]\], PARAMETER\["central_meridian", 9.0\], PARAMETER\["latitude_of_origin", 0.0\], PARAMETER\["scale_factor", 0.9996\], PARAMETER\["false_easting", 500000.0\], PARAMETER\["false_northing", 0.0\], UNIT\["m", 1.0\], AXIS\["Easting", EAST\], AXIS\["Northing", NORTH\], AUTHORITY\["EPSG","32632"\]\]

spatial_ref :  
PROJCS\["WGS 84 / UTM zone 32N", GEOGCS\["WGS 84", DATUM\["World Geodetic System 1984", SPHEROID\["WGS 84", 6378137.0, 298.257223563, AUTHORITY\["EPSG","7030"\]\], AUTHORITY\["EPSG","6326"\]\], PRIMEM\["Greenwich", 0.0, AUTHORITY\["EPSG","8901"\]\], UNIT\["degree", 0.017453292519943295\], AXIS\["Geodetic longitude", EAST\], AXIS\["Geodetic latitude", NORTH\], AUTHORITY\["EPSG","4326"\]\], PROJECTION\["Transverse_Mercator", AUTHORITY\["EPSG","9807"\]\], PARAMETER\["central_meridian", 9.0\], PARAMETER\["latitude_of_origin", 0.0\], PARAMETER\["scale_factor", 0.9996\], PARAMETER\["false_easting", 500000.0\], PARAMETER\["false_northing", 0.0\], UNIT\["m", 1.0\], AXIS\["Easting", EAST\], AXIS\["Northing", NORTH\], AUTHORITY\["EPSG","32632"\]\]

    [1 values with dtype=|S1]

VV

(t, y, x)

float32

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
VV

units :  

grid_mapping :  
crs

    [442112 values with dtype=float32]

VH

(t, y, x)

float32

...

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

long_name :  
VH

units :  

grid_mapping :  
crs

    [442112 values with dtype=float32]

Indexes: (3)

t

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2021-01-03'], dtype='datetime64[ns]', name='t', freq=None))

x

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([675945.0, 675955.0, 675965.0, 675975.0, 675985.0, 675995.0, 676005.0,
           676015.0, 676025.0, 676035.0,
           ...
           682885.0, 682895.0, 682905.0, 682915.0, 682925.0, 682935.0, 682945.0,
           682955.0, 682965.0, 682975.0],
          dtype='float64', name='x', length=704))

y

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([5154005.0, 5153995.0, 5153985.0, 5153975.0, 5153965.0, 5153955.0,
           5153945.0, 5153935.0, 5153925.0, 5153915.0,
           ...
           5147825.0, 5147815.0, 5147805.0, 5147795.0, 5147785.0, 5147775.0,
           5147765.0, 5147755.0, 5147745.0, 5147735.0],
          dtype='float64', name='y', length=628))

Attributes: (2)

Conventions :  
CF-1.9

institution :  
openEO platform

``` python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
ax1.imshow(S1_ard.VV[0].values, cmap="Greys_r", vmin=-30, vmax=30)
ax1.set_title("VV sigma0")
ax2.imshow(S1_ard.VH[0].values, cmap="Greys_r", vmin=-30, vmax=30)
ax2.set_title("VH sigma0")
plt.show()
```

![](Radar_ARD_files/figure-html/cell-8-output-1.png)
