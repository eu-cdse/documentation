# Access PROBA-V collection using openEO

PROBA-V was launched on May 6, 2013, to fill the gap in space-based vegetation measurements between SPOT-VGT (March 1998 – May 2014) and Sentinel-3. The mission objective of PROBA-V was to ensure continuity and consistency with the heritage of the SPOT-VGT mission.

Researchers can access Proba-V data globally through the openEO API. Leveraging the simplicity of openEO, users can utilize its scalability and interoperability features to conduct in-depth data analyses.

In this notebook, we will use the openEO platform to analyze the NDVI band from the Proba-V satellite product, enabling us to monitor vegetation health and changes over time.

``` python
# import the necessary packages

import openeo
import json
import pandas as pd
import plotly.express as px
```

The openEO standard enables access to datasets and processing capabilities beyond what CDSE offers, all through a single endpoint and interface. This simplifies workflows by removing the need to register on multiple platforms and learn their APIs. This feature is known as the openEO federation.

In this notebook, we’ve utilized the CDSE openEO federation backend to access Proba-V data from the [Terrascope](https://terrascope.be/) backend.

For more details on the openEO federation, please visit the [openEO website](https://documentation.dataspace.copernicus.eu/APIs/openEO/federation/openeo_federation.html).

``` python
# establish the connection and authenticate
connection = openeo.connect("openeofed.dataspace.copernicus.eu").authenticate_oidc()
```

    Authenticated using refresh token.

From a list of Proba-V collections, users can directly access the following 1-day, 5-day, and 10-day synthesis Proba-V data using openEO.

``` python
collections = connection.list_collections()

# Filter collections with "PROBA-V" in their title and print title and id
for collection in collections:
    if "title" in collection and "PROBA-V" in collection["title"]:
        print(f"ID: {collection.get('id')}, Title: {collection.get('title')}")
```

    ID: PROBAV_L3_S10_TOC_333M, Title: PROBA-V S10 TOC 300 m COG: Decadal synthesis of S1's as Maximum Value Compositing (MVC), COG format - Collection 2
    ID: PROBAV_L3_S5_TOC_100M, Title: PROBA-V S5 TOC 100 m COG: Data corrected for atmospheric effects with the SMAC (Simplified Method for Atmosheric Corrections) algorithm, COG format - Collection 2
    ID: PROBAV_L3_S1_TOC_100M, Title: PROBA-V S1 TOC 100 m COG: Data corrected for atmospheric effects with the SMAC (Simplified Method for Atmosheric Corrections) algorithm, COG format - Collection 2
    ID: PROBAV_L3_S1_TOC_333M, Title: PROBA-V S1 TOC 300 m COG: Data corrected for atmospheric effects with the SMAC (Simplified Method for Atmosheric Corrections) algorithm, COG format - Collection 2

Users can obtain detailed descriptions of each collection by executing the command `connection.describe_collection("PROBAV_L3_S10_TOC_333M")`.

For this example, we will use the `PROBAV_L3_S5_TOC_100M` collection.

``` python
# Load data cube from PROBAV_L3_S5_TOC_100M collection.
cube = connection.load_collection(
    "PROBAV_L3_S5_TOC_100M",
    temporal_extent=["2021-01-01", "2021-12-01"],
    bands=["NDVI"],
)
```

``` python
# apply offset and rescale
cube = cube.apply(lambda x: 0.004 * x - 0.08)
```

Users can either download the NDVI data retrieved in the previous cell or proceed with further analysis.

Here, we will create an NDVI time series. In the following cell, we will use the `DataCube.aggregate_spatial()` method to compute the mean NDVI for each specified field.

``` python
def read_json(filename: str) -> dict:
    with open(filename) as input:
        field = json.load(input)
    return field


fields = read_json("polygons.geojson")
```

``` python
ndvi_timeseries = cube.aggregate_spatial(geometries=fields, reducer="mean")
```

Finally, let us perform the computation synchronously and retrieve the results as a CSV file.

``` python
ndvi_timeseries.download("ProbaV.csv")
```

In the following cell we will visualize the distribution of NDVI (Normalized Difference Vegetation Index) values over time using a box plot. This plot helps in understanding how vegetation health evolves over time

``` python
# Load the CSV file into a DataFrame
file_path = "ProbaV.csv"
df = pd.read_csv(file_path)

# Create the box plot
px.box(
    df,
    x="date",
    y="NDVI",
    title="NDVI Over Time",
    labels={"date": "Date", "NDVI": "NDVI"},
)
```

![](ProbaVplot.png)

FInal Plot
