# Working with xcube on CDSE

[**xcube**](https://github.com/xcube-dev/xcube) is an open-source Python package and toolkit that has been developed to provide Earth observation (EO) data in an analysis-ready form to users. This is achieved by carefully converting EO data sources into self-contained data cubes (xarray.Datasets).

This notebook shows how to: \* Access Sentinel Hub with xcube on CDSE \* Effectively mask cube data \* Develop and run a Python function to compute a new variable that is automatically utilizing multiple threads \* Compute Time-series, means, anomalies of a variable

Please, refer to the [xcube documentation](https://xcube.readthedocs.io/en/latest/index.html) for further information.  
The xcube package is developed and maintained by [Brockmann Consult GmbH](https://www.brockmann-consult.de) and contributors.

------------------------------------------------------------------------

### Prerequisites

#### Install the [xcube-sh](https://github.com/xcube-dev/xcube-sh/) data store plugin to allow accessing Setinel Hub on CDSE

Execute the following line in the Terminal to install the xcube store for Sentinel Hub into the respective environment:

    $ mamba install xcube-sh -n sentinelhub

This step could be omitted if xcube-sh is installed into the environment by default.

------------------------------------------------------------------------

``` python
# xcube imports
from xcube.core.store import new_data_store
from xcube.core.compute import compute_cube
from xcube.core.maskset import MaskSet

# Various utilities
from sentinelhub import SHConfig
```

``` python
%matplotlib inline
```

### Credentials

Load client_id and client_secret from user’s SHconfig to create a store instance. Note that the credentials they may also be inserted manually here. In a future release of xcube-sh, the endpoint urls may be integrated into a CDSE profile so that users do not have to provide them as parameters here.

The creation of a user’s SHconfig is also shown in a Jupyter Notebook under the path: `samples/sentinelhub/introduction_to_SH_APIs.ipynb`

``` python
# Only run this cell if you have not created a configuration.

import getpass

config = SHConfig()
# config.sh_client_id = getpass.getpass("Enter your SentinelHub client id")
# config.sh_client_secret = getpass.getpass("Enter your SentinelHub client secret")
config.sh_base_url = "https://sh.dataspace.copernicus.eu"
config.sh_token_url = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
# config.save("xcube")
```

------------------------------------------------------------------------

### Create store instance and get an overview over the available products

To be able to access data records with xcube, so-called store instances must be created. These create connections either to the local file system, S3 buckets or various data portals (e.g. Sentinel Hub, CMEMS, CCI etc.). An overview of all stores and their properties can be found [here](https://xcube.readthedocs.io/en/latest/dataaccess.html#available-data-stores).

``` python
# config = SHConfig("xcube")
```

``` python
store = new_data_store(
    "sentinelhub",
    client_id=config.sh_client_id,
    client_secret=config.sh_client_secret,
    instance_url=config.sh_base_url,
    oauth2_url=config.sh_token_url.rsplit("/", maxsplit=1)[0],
)
```

The following datasets are available through the sentinelhub store:

``` python
store.list_data_ids()
```

    ['S2L1C', 'S3OLCI', 'S3SLSTR', 'S1GRD', 'S2L2A', 'S5PL2']

------------------------------------------------------------------------

### Study area

For this demo, we are focussing on the small lake *Selenter See* near Kiel, Northern Germany (Baltic Sea):

``` python
x1 = 10.37  # degree
y1 = 54.28  # degree
x2 = 10.52  # degree
y2 = 54.33  # degree

bbox = x1, y1, x2, y2
```

Later in this NB we are going to compute some indexes from atmospherically corrected bands B04, B05, B06, B11 of Sentinel-2 (S2L2A). Our time range covers two and a half months of the summer 2018: 2018-05-14 to 2018-07-31

The desired resolution is 20 meters per pixel.

``` python
spatial_res = 0.00018  # = 20.038 meters in degree
```

------------------------------------------------------------------------

### Access data from sentinelhub store

Get an insight to the data product you are interested in. In the `open_params_schema` all parameters that can be used to specify the search for a product are listed. Including a list of variables, that are **required** for the search.

``` python
store.describe_data("S2L2A")
```

    <xcube.core.store.descriptor.DatasetDescriptor at 0x7fb8757c4790>

``` python
cube = store.open_data(
    "S2L2A",
    variable_names=["B04", "B05", "B06", "B11", "SCL", "CLD"],
    bbox=bbox,
    spatial_res=spatial_res,
    time_range=["2019-07-21", "2019-09-21"],
    time_period="4D",
    tile_size=[512, 512],
)
cube
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset>
Dimensions:    (time: 16, lat: 278, lon: 1024, bnds: 2)
Coordinates:
  * lat        (lat) float64 54.33 54.33 54.33 54.33 ... 54.28 54.28 54.28 54.28
  * lon        (lon) float64 10.37 10.37 10.37 10.37 ... 10.55 10.55 10.55 10.55
  * time       (time) datetime64[ns] 2019-07-23 2019-07-27 ... 2019-09-21
    time_bnds  (time, bnds) datetime64[ns] dask.array<chunksize=(16, 2), meta=np.ndarray>
Dimensions without coordinates: bnds
Data variables:
    B04        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    B05        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    B06        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    B11        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    CLD        (time, lat, lon) uint8 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    SCL        (time, lat, lon) uint8 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
Attributes: (12/13)
    Conventions:               CF-1.7
    title:                     S2L2A Data Cube Subset
    history:                   [{'program': 'xcube_sh.chunkstore.SentinelHubC...
    date_created:              2024-05-13T14:42:05.877516
    time_coverage_start:       2019-07-21T00:00:00+00:00
    time_coverage_end:         2019-09-23T00:00:00+00:00
    ...                        ...
    time_coverage_resolution:  P4DT0H0M0S
    geospatial_lon_min:        10.37
    geospatial_lat_min:        54.28
    geospatial_lon_max:        10.554319999999999
    geospatial_lat_max:        54.330040000000004
    processing_level:          L2A
```

xarray.Dataset

Dimensions:

- time: 16
- lat: 278
- lon: 1024
- bnds: 2

Coordinates: (4)

lat

(lat)

float64

54.33 54.33 54.33 ... 54.28 54.28

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

units :  
decimal_degrees

long_name :  
latitude

standard_name :  
latitude

    array([54.32995, 54.32977, 54.32959, ..., 54.28045, 54.28027, 54.28009])

lon

(lon)

float64

10.37 10.37 10.37 ... 10.55 10.55

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

units :  
decimal_degrees

long_name :  
longitude

standard_name :  
longitude

    array([10.37009, 10.37027, 10.37045, ..., 10.55387, 10.55405, 10.55423])

time

(time)

datetime64\[ns\]

2019-07-23 ... 2019-09-21

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
time

bounds :  
time_bnds

    array(['2019-07-23T00:00:00.000000000', '2019-07-27T00:00:00.000000000',
           '2019-07-31T00:00:00.000000000', '2019-08-04T00:00:00.000000000',
           '2019-08-08T00:00:00.000000000', '2019-08-12T00:00:00.000000000',
           '2019-08-16T00:00:00.000000000', '2019-08-20T00:00:00.000000000',
           '2019-08-24T00:00:00.000000000', '2019-08-28T00:00:00.000000000',
           '2019-09-01T00:00:00.000000000', '2019-09-05T00:00:00.000000000',
           '2019-09-09T00:00:00.000000000', '2019-09-13T00:00:00.000000000',
           '2019-09-17T00:00:00.000000000', '2019-09-21T00:00:00.000000000'],
          dtype='datetime64[ns]')

time_bnds

(time, bnds)

datetime64\[ns\]

dask.array\<chunksize=(16, 2), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
time

[TABLE]

Data variables: (6)

B04

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
664.75

wavelength_a :  
664.6

wavelength_b :  
664.9

bandwidth :  
31.0

bandwidth_a :  
31

bandwidth_b :  
31

resolution :  
10

[TABLE]

B05

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
703.95

wavelength_a :  
704.1

wavelength_b :  
703.8

bandwidth :  
15.5

bandwidth_a :  
15

bandwidth_b :  
16

resolution :  
20

[TABLE]

B06

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
739.8

wavelength_a :  
740.5

wavelength_b :  
739.1

bandwidth :  
15.0

bandwidth_a :  
15

bandwidth_b :  
15

resolution :  
20

[TABLE]

B11

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
1612.05

wavelength_a :  
1613.7

wavelength_b :  
1610.4

bandwidth :  
92.5

bandwidth_a :  
91

bandwidth_b :  
94

resolution :  
20

[TABLE]

CLD

(time, lat, lon)

uint8

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
UINT8

[TABLE]

SCL

(time, lat, lon)

uint8

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
UINT8

flag_values :  
0,1,2,3,4,5,6,7,8,9,10,11

flag_meanings :  
no_data saturated_or_defective dark_area_pixels cloud_shadows vegetation bare_soils water clouds_low_probability_or_unclassified clouds_medium_probability clouds_high_probability cirrus snow_or_ice

[TABLE]

Indexes: (3)

lat

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([54.329950000000004,           54.32977,           54.32959,
                     54.32941,           54.32923,           54.32905,
                     54.32887,           54.32869,           54.32851,
                     54.32833,
           ...
           54.281710000000004, 54.281530000000004,           54.28135,
                     54.28117,           54.28099,           54.28081,
                     54.28063,           54.28045,           54.28027,
                     54.28009],
          dtype='float64', name='lat', length=278))

lon

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([          10.37009,           10.37027,           10.37045,
                     10.37063, 10.370809999999999, 10.370989999999999,
                     10.37117,           10.37135,           10.37153,
                     10.37171,
           ...
           10.552609999999998, 10.552789999999998, 10.552969999999998,
           10.553149999999999, 10.553329999999999,           10.55351,
           10.553689999999998, 10.553869999999998, 10.554049999999998,
           10.554229999999999],
          dtype='float64', name='lon', length=1024))

time

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2019-07-23', '2019-07-27', '2019-07-31', '2019-08-04',
                   '2019-08-08', '2019-08-12', '2019-08-16', '2019-08-20',
                   '2019-08-24', '2019-08-28', '2019-09-01', '2019-09-05',
                   '2019-09-09', '2019-09-13', '2019-09-17', '2019-09-21'],
                  dtype='datetime64[ns]', name='time', freq=None))

Attributes: (13)

Conventions :  
CF-1.7

title :  
S2L2A Data Cube Subset

history :  
\[{'program': 'xcube_sh.chunkstore.SentinelHubChunkStore', 'cube_config': {'dataset_name': 'S2L2A', 'band_names': \['B04', 'B05', 'B06', 'B11', 'SCL', 'CLD'\], 'band_fill_values': None, 'band_sample_types': None, 'band_units': None, 'tile_size': \[512, 278\], 'bbox': \[10.37, 54.28, 10.554319999999999, 54.330040000000004\], 'spatial_res': 0.00018, 'crs': 'WGS84', 'upsampling': 'NEAREST', 'downsampling': 'NEAREST', 'mosaicking_order': 'mostRecent', 'time_range': \['2019-07-21T00:00:00+00:00', '2019-09-21T00:00:00+00:00'\], 'time_period': '4 days 00:00:00', 'time_tolerance': None, 'collection_id': None, 'four_d': False}}\]

date_created :  
2024-05-13T14:42:05.877516

time_coverage_start :  
2019-07-21T00:00:00+00:00

time_coverage_end :  
2019-09-23T00:00:00+00:00

time_coverage_duration :  
P64DT0H0M0S

time_coverage_resolution :  
P4DT0H0M0S

geospatial_lon_min :  
10.37

geospatial_lat_min :  
54.28

geospatial_lon_max :  
10.554319999999999

geospatial_lat_max :  
54.330040000000004

processing_level :  
L2A

------------------------------------------------------------------------

### Masking

The band `SCL` provides *scene classification flags*. Because this “band” has CF-compliant flag encodings in its metadata attributes, we can interpret them correctly:

``` python
scene_classif = MaskSet(cube.SCL)
scene_classif
```

|                                        |      |       |
|----------------------------------------|------|-------|
| Flag name                              | Mask | Value |
| no_data                                | None | 0     |
| saturated_or_defective                 | None | 1     |
| dark_area_pixels                       | None | 2     |
| cloud_shadows                          | None | 3     |
| vegetation                             | None | 4     |
| bare_soils                             | None | 5     |
| water                                  | None | 6     |
| clouds_low_probability_or_unclassified | None | 7     |
| clouds_medium_probability              | None | 8     |
| clouds_high_probability                | None | 9     |
| cirrus                                 | None | 10    |
| snow_or_ice                            | None | 11    |

xcube mask sets also follow data cube structure:

``` python
scene_classif.cirrus
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.DataArray 'cirrus' (time: 16, lat: 278, lon: 1024)>
dask.array<where, shape=(16, 278, 1024), dtype=uint8, chunksize=(1, 278, 512), chunktype=numpy.ndarray>
Coordinates:
  * lat      (lat) float64 54.33 54.33 54.33 54.33 ... 54.28 54.28 54.28 54.28
  * lon      (lon) float64 10.37 10.37 10.37 10.37 ... 10.55 10.55 10.55 10.55
  * time     (time) datetime64[ns] 2019-07-23 2019-07-27 ... 2019-09-21
```

xarray.DataArray

'cirrus'

- time: 16
- lat: 278
- lon: 1024

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

[TABLE]

Coordinates: (3)

lat

(lat)

float64

54.33 54.33 54.33 ... 54.28 54.28

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

units :  
decimal_degrees

long_name :  
latitude

standard_name :  
latitude

    array([54.32995, 54.32977, 54.32959, ..., 54.28045, 54.28027, 54.28009])

lon

(lon)

float64

10.37 10.37 10.37 ... 10.55 10.55

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

units :  
decimal_degrees

long_name :  
longitude

standard_name :  
longitude

    array([10.37009, 10.37027, 10.37045, ..., 10.55387, 10.55405, 10.55423])

time

(time)

datetime64\[ns\]

2019-07-23 ... 2019-09-21

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
time

bounds :  
time_bnds

    array(['2019-07-23T00:00:00.000000000', '2019-07-27T00:00:00.000000000',
           '2019-07-31T00:00:00.000000000', '2019-08-04T00:00:00.000000000',
           '2019-08-08T00:00:00.000000000', '2019-08-12T00:00:00.000000000',
           '2019-08-16T00:00:00.000000000', '2019-08-20T00:00:00.000000000',
           '2019-08-24T00:00:00.000000000', '2019-08-28T00:00:00.000000000',
           '2019-09-01T00:00:00.000000000', '2019-09-05T00:00:00.000000000',
           '2019-09-09T00:00:00.000000000', '2019-09-13T00:00:00.000000000',
           '2019-09-17T00:00:00.000000000', '2019-09-21T00:00:00.000000000'],
          dtype='datetime64[ns]')

Indexes: (3)

lat

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([54.329950000000004,           54.32977,           54.32959,
                     54.32941,           54.32923,           54.32905,
                     54.32887,           54.32869,           54.32851,
                     54.32833,
           ...
           54.281710000000004, 54.281530000000004,           54.28135,
                     54.28117,           54.28099,           54.28081,
                     54.28063,           54.28045,           54.28027,
                     54.28009],
          dtype='float64', name='lat', length=278))

lon

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([          10.37009,           10.37027,           10.37045,
                     10.37063, 10.370809999999999, 10.370989999999999,
                     10.37117,           10.37135,           10.37153,
                     10.37171,
           ...
           10.552609999999998, 10.552789999999998, 10.552969999999998,
           10.553149999999999, 10.553329999999999,           10.55351,
           10.553689999999998, 10.553869999999998, 10.554049999999998,
           10.554229999999999],
          dtype='float64', name='lon', length=1024))

time

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2019-07-23', '2019-07-27', '2019-07-31', '2019-08-04',
                   '2019-08-08', '2019-08-12', '2019-08-16', '2019-08-20',
                   '2019-08-24', '2019-08-28', '2019-09-01', '2019-09-05',
                   '2019-09-09', '2019-09-13', '2019-09-17', '2019-09-21'],
                  dtype='datetime64[ns]', name='time', freq=None))

Attributes: (0)

``` python
scene_classif.cirrus.plot.imshow(col="time", col_wrap=4, cmap="viridis")
```

![](xcube_on_CDSE_files/figure-html/cell-14-output-1.png)

We can use any of the SCL masks or combinations thereof to mask entire cubes. Here we create a “water cube”:

``` python
water_cube = cube.where(scene_classif.water)
water_cube
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset>
Dimensions:    (time: 16, lat: 278, lon: 1024, bnds: 2)
Coordinates:
  * lat        (lat) float64 54.33 54.33 54.33 54.33 ... 54.28 54.28 54.28 54.28
  * lon        (lon) float64 10.37 10.37 10.37 10.37 ... 10.55 10.55 10.55 10.55
  * time       (time) datetime64[ns] 2019-07-23 2019-07-27 ... 2019-09-21
    time_bnds  (time, bnds) datetime64[ns] dask.array<chunksize=(16, 2), meta=np.ndarray>
Dimensions without coordinates: bnds
Data variables:
    B04        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    B05        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    B06        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    B11        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    CLD        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
    SCL        (time, lat, lon) float32 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
Attributes: (12/13)
    Conventions:               CF-1.7
    title:                     S2L2A Data Cube Subset
    history:                   [{'program': 'xcube_sh.chunkstore.SentinelHubC...
    date_created:              2024-05-13T14:42:05.877516
    time_coverage_start:       2019-07-21T00:00:00+00:00
    time_coverage_end:         2019-09-23T00:00:00+00:00
    ...                        ...
    time_coverage_resolution:  P4DT0H0M0S
    geospatial_lon_min:        10.37
    geospatial_lat_min:        54.28
    geospatial_lon_max:        10.554319999999999
    geospatial_lat_max:        54.330040000000004
    processing_level:          L2A
```

xarray.Dataset

Dimensions:

- time: 16
- lat: 278
- lon: 1024
- bnds: 2

Coordinates: (4)

lat

(lat)

float64

54.33 54.33 54.33 ... 54.28 54.28

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

units :  
decimal_degrees

long_name :  
latitude

standard_name :  
latitude

    array([54.32995, 54.32977, 54.32959, ..., 54.28045, 54.28027, 54.28009])

lon

(lon)

float64

10.37 10.37 10.37 ... 10.55 10.55

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

units :  
decimal_degrees

long_name :  
longitude

standard_name :  
longitude

    array([10.37009, 10.37027, 10.37045, ..., 10.55387, 10.55405, 10.55423])

time

(time)

datetime64\[ns\]

2019-07-23 ... 2019-09-21

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
time

bounds :  
time_bnds

    array(['2019-07-23T00:00:00.000000000', '2019-07-27T00:00:00.000000000',
           '2019-07-31T00:00:00.000000000', '2019-08-04T00:00:00.000000000',
           '2019-08-08T00:00:00.000000000', '2019-08-12T00:00:00.000000000',
           '2019-08-16T00:00:00.000000000', '2019-08-20T00:00:00.000000000',
           '2019-08-24T00:00:00.000000000', '2019-08-28T00:00:00.000000000',
           '2019-09-01T00:00:00.000000000', '2019-09-05T00:00:00.000000000',
           '2019-09-09T00:00:00.000000000', '2019-09-13T00:00:00.000000000',
           '2019-09-17T00:00:00.000000000', '2019-09-21T00:00:00.000000000'],
          dtype='datetime64[ns]')

time_bnds

(time, bnds)

datetime64\[ns\]

dask.array\<chunksize=(16, 2), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

standard_name :  
time

[TABLE]

Data variables: (6)

B04

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
664.75

wavelength_a :  
664.6

wavelength_b :  
664.9

bandwidth :  
31.0

bandwidth_a :  
31

bandwidth_b :  
31

resolution :  
10

[TABLE]

B05

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
703.95

wavelength_a :  
704.1

wavelength_b :  
703.8

bandwidth :  
15.5

bandwidth_a :  
15

bandwidth_b :  
16

resolution :  
20

[TABLE]

B06

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
739.8

wavelength_a :  
740.5

wavelength_b :  
739.1

bandwidth :  
15.0

bandwidth_a :  
15

bandwidth_b :  
15

resolution :  
20

[TABLE]

B11

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
FLOAT32

units :  
reflectance

wavelength :  
1612.05

wavelength_a :  
1613.7

wavelength_b :  
1610.4

bandwidth :  
92.5

bandwidth_a :  
91

bandwidth_b :  
94

resolution :  
20

[TABLE]

CLD

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
UINT8

[TABLE]

SCL

(time, lat, lon)

float32

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

sample_type :  
UINT8

flag_values :  
0,1,2,3,4,5,6,7,8,9,10,11

flag_meanings :  
no_data saturated_or_defective dark_area_pixels cloud_shadows vegetation bare_soils water clouds_low_probability_or_unclassified clouds_medium_probability clouds_high_probability cirrus snow_or_ice

[TABLE]

Indexes: (3)

lat

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([54.329950000000004,           54.32977,           54.32959,
                     54.32941,           54.32923,           54.32905,
                     54.32887,           54.32869,           54.32851,
                     54.32833,
           ...
           54.281710000000004, 54.281530000000004,           54.28135,
                     54.28117,           54.28099,           54.28081,
                     54.28063,           54.28045,           54.28027,
                     54.28009],
          dtype='float64', name='lat', length=278))

lon

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([          10.37009,           10.37027,           10.37045,
                     10.37063, 10.370809999999999, 10.370989999999999,
                     10.37117,           10.37135,           10.37153,
                     10.37171,
           ...
           10.552609999999998, 10.552789999999998, 10.552969999999998,
           10.553149999999999, 10.553329999999999,           10.55351,
           10.553689999999998, 10.553869999999998, 10.554049999999998,
           10.554229999999999],
          dtype='float64', name='lon', length=1024))

time

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2019-07-23', '2019-07-27', '2019-07-31', '2019-08-04',
                   '2019-08-08', '2019-08-12', '2019-08-16', '2019-08-20',
                   '2019-08-24', '2019-08-28', '2019-09-01', '2019-09-05',
                   '2019-09-09', '2019-09-13', '2019-09-17', '2019-09-21'],
                  dtype='datetime64[ns]', name='time', freq=None))

Attributes: (13)

Conventions :  
CF-1.7

title :  
S2L2A Data Cube Subset

history :  
\[{'program': 'xcube_sh.chunkstore.SentinelHubChunkStore', 'cube_config': {'dataset_name': 'S2L2A', 'band_names': \['B04', 'B05', 'B06', 'B11', 'SCL', 'CLD'\], 'band_fill_values': None, 'band_sample_types': None, 'band_units': None, 'tile_size': \[512, 278\], 'bbox': \[10.37, 54.28, 10.554319999999999, 54.330040000000004\], 'spatial_res': 0.00018, 'crs': 'WGS84', 'upsampling': 'NEAREST', 'downsampling': 'NEAREST', 'mosaicking_order': 'mostRecent', 'time_range': \['2019-07-21T00:00:00+00:00', '2019-09-21T00:00:00+00:00'\], 'time_period': '4 days 00:00:00', 'time_tolerance': None, 'collection_id': None, 'four_d': False}}\]

date_created :  
2024-05-13T14:42:05.877516

time_coverage_start :  
2019-07-21T00:00:00+00:00

time_coverage_end :  
2019-09-23T00:00:00+00:00

time_coverage_duration :  
P64DT0H0M0S

time_coverage_resolution :  
P4DT0H0M0S

geospatial_lon_min :  
10.37

geospatial_lat_min :  
54.28

geospatial_lon_max :  
10.554319999999999

geospatial_lat_max :  
54.330040000000004

processing_level :  
L2A

``` python
water_cube.B04.plot.imshow(col="time", col_wrap=4, vmin=0, vmax=0.05, cmap="Greys_r")
```

![](xcube_on_CDSE_files/figure-html/cell-16-output-1.png)

------------------------------------------------------------------------

### Compute Index and generate a new cube

We now compute a Chlorophyll indicator called *Maximum Chlorophyll Index* from bands B04, B05, B06. Note, that it uses the wavelength for the bands as input parameters. The function is called for every *data chunk* in the cube and returns a chunk for the variable to be computed. Chunks are computed independently and in parallel.

``` python
def compute_mci(b_from, b_peek, b_to, input_params, dim_coords):
    # The first three arguments are chunks of the three input variables we define below.
    # You can name them as you like. They are pure 3D numpy arrays.

    # The 'input_params' argument is a standard parameter that we define in the call below.
    wlen_from = input_params["wlen_from"]
    wlen_peek = input_params["wlen_peek"]
    wlen_to = input_params["wlen_to"]

    # The 'dim_coords' argument is optional and provides the coordinate values for all dimension
    # of the current chunk. We don't use it here, but for many algorithms this is important
    # information (e.g. looking up aux data).
    lon, lat = (dim_coords[dim] for dim in ("lon", "lat"))
    # print('dim_coords from', lon[0], lat[0], 'to', lon[-1], lat[-1])

    # You can use any popular data packages such as numpy, scipy, dask here,
    # or we can use ML packages such as scikitlearn!
    # For simplity, we do some very simple array math here:

    f = (wlen_peek - wlen_from) / (wlen_to - wlen_from)
    mci = (b_peek - b_from) - f * (b_to - b_from)

    return mci
```

Prepare input parameters from band attributes:

``` python
input_params = dict(
    wlen_from=water_cube.B04.attrs["wavelength"],
    wlen_peek=water_cube.B05.attrs["wavelength"],
    wlen_to=water_cube.B06.attrs["wavelength"],
)
input_params
```

    {'wlen_from': 664.75, 'wlen_peek': 703.95, 'wlen_to': 739.8}

``` python
mci_cube = compute_cube(
    compute_mci,
    water_cube,
    input_var_names=["B04", "B05", "B06"],
    input_params=input_params,
    output_var_name="mci",
)
mci_cube
```

    /opt/conda/envs/sentinelhub/lib/python3.10/site-packages/xcube/core/compute.py:361: RuntimeWarning: Failed to open Zarr store with consolidated metadata, but successfully read with non-consolidated metadata. This is typically much slower for opening a dataset. To silence this warning, consider:
    1. Consolidating metadata in this existing store with zarr.consolidate_metadata().
    2. Explicitly setting consolidated=False, to avoid trying to read consolidate metadata, or
    3. Explicitly setting consolidated=True, to raise an error in this case instead of falling back to try reading non-consolidated metadata.
      dataset = xr.open_zarr(store)

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.Dataset>
Dimensions:  (lat: 278, lon: 1024, time: 16)
Coordinates:
  * lat      (lat) float64 54.33 54.33 54.33 54.33 ... 54.28 54.28 54.28 54.28
  * lon      (lon) float64 10.37 10.37 10.37 10.37 ... 10.55 10.55 10.55 10.55
  * time     (time) datetime64[ns] 2019-07-23 2019-07-27 ... 2019-09-21
Data variables:
    mci      (time, lat, lon) float64 dask.array<chunksize=(1, 278, 512), meta=np.ndarray>
```

xarray.Dataset

Dimensions:

- lat: 278
- lon: 1024
- time: 16

Coordinates: (3)

lat

(lat)

float64

54.33 54.33 54.33 ... 54.28 54.28

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array([54.32995, 54.32977, 54.32959, ..., 54.28045, 54.28027, 54.28009])

lon

(lon)

float64

10.37 10.37 10.37 ... 10.55 10.55

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array([10.37009, 10.37027, 10.37045, ..., 10.55387, 10.55405, 10.55423])

time

(time)

datetime64\[ns\]

2019-07-23 ... 2019-09-21

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array(['2019-07-23T00:00:00.000000000', '2019-07-27T00:00:00.000000000',
           '2019-07-31T00:00:00.000000000', '2019-08-04T00:00:00.000000000',
           '2019-08-08T00:00:00.000000000', '2019-08-12T00:00:00.000000000',
           '2019-08-16T00:00:00.000000000', '2019-08-20T00:00:00.000000000',
           '2019-08-24T00:00:00.000000000', '2019-08-28T00:00:00.000000000',
           '2019-09-01T00:00:00.000000000', '2019-09-05T00:00:00.000000000',
           '2019-09-09T00:00:00.000000000', '2019-09-13T00:00:00.000000000',
           '2019-09-17T00:00:00.000000000', '2019-09-21T00:00:00.000000000'],
          dtype='datetime64[ns]')

Data variables: (1)

mci

(time, lat, lon)

float64

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

[TABLE]

Indexes: (3)

lat

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([54.329950000000004,           54.32977,           54.32959,
                     54.32941,           54.32923,           54.32905,
                     54.32887,           54.32869,           54.32851,
                     54.32833,
           ...
           54.281710000000004, 54.281530000000004,           54.28135,
                     54.28117,           54.28099,           54.28081,
                     54.28063,           54.28045,           54.28027,
                     54.28009],
          dtype='float64', name='lat', length=278))

lon

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([          10.37009,           10.37027,           10.37045,
                     10.37063, 10.370809999999999, 10.370989999999999,
                     10.37117,           10.37135,           10.37153,
                     10.37171,
           ...
           10.552609999999998, 10.552789999999998, 10.552969999999998,
           10.553149999999999, 10.553329999999999,           10.55351,
           10.553689999999998, 10.553869999999998, 10.554049999999998,
           10.554229999999999],
          dtype='float64', name='lon', length=1024))

time

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2019-07-23', '2019-07-27', '2019-07-31', '2019-08-04',
                   '2019-08-08', '2019-08-12', '2019-08-16', '2019-08-20',
                   '2019-08-24', '2019-08-28', '2019-09-01', '2019-09-05',
                   '2019-09-09', '2019-09-13', '2019-09-17', '2019-09-21'],
                  dtype='datetime64[ns]', name='time', freq=None))

Attributes: (0)

``` python
mci_cube.mci.attrs["long_name"] = "Maximum Chlorophyll Index"
mci_cube.mci.attrs["units"] = "unitless"
mci_cube.mci
```

![](data:image/svg+xml;base64,PHN2ZyBzdHlsZT0icG9zaXRpb246IGFic29sdXRlOyB3aWR0aDogMDsgaGVpZ2h0OiAwOyBvdmVyZmxvdzogaGlkZGVuIj4KPGRlZnM+CjxzeW1ib2wgaWQ9Imljb24tZGF0YWJhc2UiIHZpZXdib3g9IjAgMCAzMiAzMiI+CjxwYXRoIGQ9Ik0xNiAwYy04LjgzNyAwLTE2IDIuMjM5LTE2IDV2NGMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di00YzAtMi43NjEtNy4xNjMtNS0xNi01eiIgLz4KPHBhdGggZD0iTTE2IDE3Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPHBhdGggZD0iTTE2IDI2Yy04LjgzNyAwLTE2LTIuMjM5LTE2LTV2NmMwIDIuNzYxIDcuMTYzIDUgMTYgNXMxNi0yLjIzOSAxNi01di02YzAgMi43NjEtNy4xNjMgNS0xNiA1eiIgLz4KPC9zeW1ib2w+CjxzeW1ib2wgaWQ9Imljb24tZmlsZS10ZXh0MiIgdmlld2JveD0iMCAwIDMyIDMyIj4KPHBhdGggZD0iTTI4LjY4MSA3LjE1OWMtMC42OTQtMC45NDctMS42NjItMi4wNTMtMi43MjQtMy4xMTZzLTIuMTY5LTIuMDMwLTMuMTE2LTIuNzI0Yy0xLjYxMi0xLjE4Mi0yLjM5My0xLjMxOS0yLjg0MS0xLjMxOWgtMTUuNWMtMS4zNzggMC0yLjUgMS4xMjEtMi41IDIuNXYyN2MwIDEuMzc4IDEuMTIyIDIuNSAyLjUgMi41aDIzYzEuMzc4IDAgMi41LTEuMTIyIDIuNS0yLjV2LTE5LjVjMC0wLjQ0OC0wLjEzNy0xLjIzLTEuMzE5LTIuODQxek0yNC41NDMgNS40NTdjMC45NTkgMC45NTkgMS43MTIgMS44MjUgMi4yNjggMi41NDNoLTQuODExdi00LjgxMWMwLjcxOCAwLjU1NiAxLjU4NCAxLjMwOSAyLjU0MyAyLjI2OHpNMjggMjkuNWMwIDAuMjcxLTAuMjI5IDAuNS0wLjUgMC41aC0yM2MtMC4yNzEgMC0wLjUtMC4yMjktMC41LTAuNXYtMjdjMC0wLjI3MSAwLjIyOS0wLjUgMC41LTAuNSAwIDAgMTUuNDk5LTAgMTUuNSAwdjdjMCAwLjU1MiAwLjQ0OCAxIDEgMWg3djE5LjV6IiAvPgo8cGF0aCBkPSJNMjMgMjZoLTE0Yy0wLjU1MiAwLTEtMC40NDgtMS0xczAuNDQ4LTEgMS0xaDE0YzAuNTUyIDAgMSAwLjQ0OCAxIDFzLTAuNDQ4IDEtMSAxeiIgLz4KPHBhdGggZD0iTTIzIDIyaC0xNGMtMC41NTIgMC0xLTAuNDQ4LTEtMXMwLjQ0OC0xIDEtMWgxNGMwLjU1MiAwIDEgMC40NDggMSAxcy0wLjQ0OCAxLTEgMXoiIC8+CjxwYXRoIGQ9Ik0yMyAxOGgtMTRjLTAuNTUyIDAtMS0wLjQ0OC0xLTFzMC40NDgtMSAxLTFoMTRjMC41NTIgMCAxIDAuNDQ4IDEgMXMtMC40NDggMS0xIDF6IiAvPgo8L3N5bWJvbD4KPC9kZWZzPgo8L3N2Zz4=)

``` xr-text-repr-fallback
<xarray.DataArray 'mci' (time: 16, lat: 278, lon: 1024)>
dask.array<transpose, shape=(16, 278, 1024), dtype=float64, chunksize=(1, 278, 512), chunktype=numpy.ndarray>
Coordinates:
  * lat      (lat) float64 54.33 54.33 54.33 54.33 ... 54.28 54.28 54.28 54.28
  * lon      (lon) float64 10.37 10.37 10.37 10.37 ... 10.55 10.55 10.55 10.55
  * time     (time) datetime64[ns] 2019-07-23 2019-07-27 ... 2019-09-21
Attributes:
    long_name:  Maximum Chlorophyll Index
    units:      unitless
```

xarray.DataArray

'mci'

- time: 16
- lat: 278
- lon: 1024

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

dask.array\<chunksize=(1, 278, 512), meta=np.ndarray\>

[TABLE]

Coordinates: (3)

lat

(lat)

float64

54.33 54.33 54.33 ... 54.28 54.28

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array([54.32995, 54.32977, 54.32959, ..., 54.28045, 54.28027, 54.28009])

lon

(lon)

float64

10.37 10.37 10.37 ... 10.55 10.55

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array([10.37009, 10.37027, 10.37045, ..., 10.55387, 10.55405, 10.55423])

time

(time)

datetime64\[ns\]

2019-07-23 ... 2019-09-21

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWZpbGUtdGV4dDIiPjx1c2UgaHJlZj0iI2ljb24tZmlsZS10ZXh0MiIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    array(['2019-07-23T00:00:00.000000000', '2019-07-27T00:00:00.000000000',
           '2019-07-31T00:00:00.000000000', '2019-08-04T00:00:00.000000000',
           '2019-08-08T00:00:00.000000000', '2019-08-12T00:00:00.000000000',
           '2019-08-16T00:00:00.000000000', '2019-08-20T00:00:00.000000000',
           '2019-08-24T00:00:00.000000000', '2019-08-28T00:00:00.000000000',
           '2019-09-01T00:00:00.000000000', '2019-09-05T00:00:00.000000000',
           '2019-09-09T00:00:00.000000000', '2019-09-13T00:00:00.000000000',
           '2019-09-17T00:00:00.000000000', '2019-09-21T00:00:00.000000000'],
          dtype='datetime64[ns]')

Indexes: (3)

lat

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([54.329950000000004,           54.32977,           54.32959,
                     54.32941,           54.32923,           54.32905,
                     54.32887,           54.32869,           54.32851,
                     54.32833,
           ...
           54.281710000000004, 54.281530000000004,           54.28135,
                     54.28117,           54.28099,           54.28081,
                     54.28063,           54.28045,           54.28027,
                     54.28009],
          dtype='float64', name='lat', length=278))

lon

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(Index([          10.37009,           10.37027,           10.37045,
                     10.37063, 10.370809999999999, 10.370989999999999,
                     10.37117,           10.37135,           10.37153,
                     10.37171,
           ...
           10.552609999999998, 10.552789999999998, 10.552969999999998,
           10.553149999999999, 10.553329999999999,           10.55351,
           10.553689999999998, 10.553869999999998, 10.554049999999998,
           10.554229999999999],
          dtype='float64', name='lon', length=1024))

time

PandasIndex

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiB4ci1pY29uLWRhdGFiYXNlIj48dXNlIGhyZWY9IiNpY29uLWRhdGFiYXNlIiAvPjwvc3ZnPg==)

    PandasIndex(DatetimeIndex(['2019-07-23', '2019-07-27', '2019-07-31', '2019-08-04',
                   '2019-08-08', '2019-08-12', '2019-08-16', '2019-08-20',
                   '2019-08-24', '2019-08-28', '2019-09-01', '2019-09-05',
                   '2019-09-09', '2019-09-13', '2019-09-17', '2019-09-21'],
                  dtype='datetime64[ns]', name='time', freq=None))

Attributes: (2)

long_name :  
Maximum Chlorophyll Index

units :  
unitless

``` python
mci_cube.mci.plot.imshow(
    col="time", col_wrap=4, vmin=-0.001, vmax=0.005, cmap="viridis"
)
```

![](xcube_on_CDSE_files/figure-html/cell-21-output-1.png)

------------------------------------------------------------------------

### Time Series

The data cube consists of 16 time steps, each representing a four-day period (see Access Data). When plotting time series, gaps may appear between some points/time intervals. This is due to missing values within those intervals, often caused by factors such as cloud cover, which has been masked above (see Masking). Alternatively, scatter plots could be used to avoid these gaps.

Time series at a given point:

``` python
mci_cube.mci.sel(lat=54.31, lon=10.45, method="nearest").plot.line(marker="x")
```

![](xcube_on_CDSE_files/figure-html/cell-22-output-1.png)

Time series of the means of each time step:

``` python
mci_cube.mci.mean(dim=("lat", "lon"), skipna=True).plot.line(marker="x")
```

![](xcube_on_CDSE_files/figure-html/cell-23-output-1.png)

Mean of all time steps:

``` python
mci_mean = mci_cube.mci.mean(dim="time")
```

``` python
mci_mean.plot.imshow(vmin=-0.005, vmax=0.005, cmap="plasma", figsize=(16, 10))
```

![](xcube_on_CDSE_files/figure-html/cell-25-output-1.png)

Anomaly w.r.t. to the mean for each time step:

``` python
mci_anomaly = mci_cube.mci - mci_mean
```

``` python
mci_anomaly.plot.imshow(col="time", col_wrap=4, vmin=-0.005, vmax=0.005, cmap="bwr")
```

![](xcube_on_CDSE_files/figure-html/cell-27-output-1.png)

------------------------------------------------------------------------

### Export result cube

Save the cube locally:

``` python
import shutil

shutil.rmtree("mci_cube.zarr", ignore_errors=True)  # Delete, if already exists
```

``` python
mci_cube.to_zarr("mci_cube.zarr")
```

    <xarray.backends.zarr.ZarrStore at 0x7fb86d8e1e00>
