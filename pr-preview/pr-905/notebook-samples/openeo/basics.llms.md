# openEO Basics: Discovery of Collections and Processes

## Setup

Import the `openeo` package and connect to the Copernicus Data Space Ecosystem openEO back-end.

``` python
import openeo
```

``` python
connection = openeo.connect(
    url="openeo.dataspace.copernicus.eu",
)
```

## Collections

List all available collection ids:

``` python
print(connection.list_collection_ids())
```

    ['SENTINEL3_OLCI_L1B', 'SENTINEL3_SLSTR', 'SENTINEL_5P_L2', 'SENTINEL2_L1C', 'SENTINEL2_L2A', 'SENTINEL1_GRD', 'COPERNICUS_30']

Get detailed information about a collection

``` python
connection.describe_collection("SENTINEL2_L2A")
```

## Processes

List all available processes:

``` python
connection.list_processes()
```

Inspect one process in more detail

``` python
connection.describe_process("add")
```
