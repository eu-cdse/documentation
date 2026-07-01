# Geospatial Job Management and Visualization with OpenEO

When executing algorithms across large spatial areas, it is often necessary to divide the area of interest into smaller regions and run the algorithm on each region independently. To streamline this process and manage multiple jobs simultaneously, the `MultiBackendJobManager` was developed.

In this example, we demonstrate how to process an algorithm across a grid of smaller tiles and visualize job statuses using interactive maps. Our use case involves calculating `Best Available Pixel Composites`, using an openEO Process hosted in the [APEX repository](https://github.com/ESA-APEx).

We will go through the following steps: 1. **Import the required packages** 2. **Generate a Spatial Grid for the Antwerp Region** 3. **Prepare Jobs for Parallel Processing** 4. **Prepare Job visualization with a Custom Color Mapping** 5. **Run the Jobs with MultiBackendJobManager**

### 1. Import the required packages

Before we start, we install the required non-native packages needed this notebook example.

``` python
!pip install shapely geopandas plotly nbformat kaleido
```

``` python
import time
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import box
import copy
from shapely import wkt

import openeo
from openeo.extra.job_management import (
        CsvJobDatabase,
        ProcessBasedJobCreator,
        MultiBackendJobManager
    )

import plotly.express as px
from plotly import offline
from IPython.display import clear_output
```

## 2. Generate a Spatial-Temporal Grid for the Antwerp Region

To manage our large-scale task efficiently, we will execute the workflow across smaller tiles that together cover the entire area of interest. This spatial grid subdivides the region into manageable sections, making data processing and analysis more scalable. In addition, we add an additional temporal extent of interest to the dataframe.

``` python
def create_tiling_grid(grid_size_m=5000, minx=590000, miny=5660000):
    """
    Creates a square tiling grid with specified dimensions and saves it as a GeoJSON file.
    
    Parameters:
        grid_size_m (int): Size of each grid cell in meters (default: 5000).
        minx (int): Minimum x-coordinate in UTM for grid bounding box.
        miny (int): Minimum y-coordinate in UTM for grid bounding box.
        output_path (str): File path to save the output GeoJSON file.

    Returns:
        None
    """
    # Fixed CRS codes
    crs_utm = "EPSG:32631"
    crs_latlon = "EPSG:4326"
    
    # Calculate max coordinates for the grid
    maxx = minx + 2 * grid_size_m
    maxy = miny + 2 * grid_size_m

    # Generate coordinates for grid
    x_coords = np.arange(minx, maxx, grid_size_m)
    y_coords = np.arange(miny, maxy, grid_size_m)
    
    # Create polygons for the grid cells
    polygons = [box(x, y, x + grid_size_m, y + grid_size_m) for x in x_coords for y in y_coords]

    # Create GeoDataFrame in UTM CRS
    grid_gdf_utm = gpd.GeoDataFrame({'geometry': polygons}, crs=crs_utm)
    
    # Convert to latitude/longitude CRS
    grid_gdf_latlon = grid_gdf_utm.to_crs(crs_latlon)
    grid_gdf_latlon['id'] = range(len(grid_gdf_latlon))

    # Save to GeoJSON file
    return grid_gdf_latlon

grid_df = create_tiling_grid()
```

### Visualize the tiling grid

We use Plotly to create an interactive visualization of the spatial grid. This allows us to examine the layout of tiles across the area of interest and ensure that the grid aligns correctly with our region.

``` python

# Convert geometries to GeoJSON serializable format
fig = px.choropleth_map(
    grid_df,
    geojson=grid_df,
    locations=grid_df.index,
    map_style="carto-positron",
    center={"lat": 51.15, "lon": 4.4},
    zoom=8,
    title="Spatial Grid for Antwerp Region"
)
fig.update_geos(fitbounds="locations")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
```

    Unable to display output for mime type(s): application/vnd.plotly.v1+json

### 3. Prepare Jobs for Parallel Processing

In this example, we will create Best Available Pixel Composites for every tile. For the implementation of this compositing workflow, we will directly make use of the standardized implementation hosed in the [APEX repository](https://github.com/ESA-APEx). To initiate this, we use the `ProcessBasedJobCreator`, which simplifies the definition of the required `start_job` functionality for algorithms defined within an openEO process graph.

In addition we initate our job tracker `jobs.csv` from the earlier created dataframe `grid_df`. This job tracker will be used to periodically obtain a status update the predefined openEO jobs.

``` python
#Make use of the Best Available Pixel openeo Process to obtain Sentinel 2 composites
process_graph_url = "https://raw.githubusercontent.com/ESA-APEx/apex_algorithms/main/openeo_udp/bap_composite.json"

start_job = ProcessBasedJobCreator(
        namespace=process_graph_url,
        parameter_defaults={},
    )

# Initiate MultiBackendJobManager 
poll_sleep  = 60
job_manager = MultiBackendJobManager(poll_sleep=poll_sleep)  
connection = openeo.connect(url="openeo.dataspace.copernicus.eu").authenticate_oidc()
job_manager.add_backend("cdse", connection=connection, parallel_jobs=2)

#Create the Job Tracker file
job_tracker = 'jobs.csv'
grid_df["temporal_extent"] = [["2024-05-01", "2024-08-01"]] * len(grid_df)
job_db = CsvJobDatabase(path=job_tracker)
if not job_db.exists():
    df = job_manager._normalize_df(grid_df)
    job_db.persist(df)
```

    Authenticated using refresh token.

### 4. Prepare Job visualization with a Custom Color Mapping

To effectively monitor the progress of geospatial processing tasks, we define a function to visualize job statuses on an interactive map. This visualization uses Plotly, with custom color mappings for each job status, providing a clear overview of the current state of all jobs.

``` python
colors = {
    "not_started": 'lightgrey', 
    "created": 'gold', 
    "queued": 'lightsteelblue', 
    "running": 'navy', 
    "finished": 'lime',
    "error": 'darkred',
    "skipped": 'darkorange',
    "start_failed": 'red',
    None: 'grey'  # Default color for any undefined status
}
```

This color scheme makes it easy to distinguish between different statuses. The `plot_job_status` function generates an interactive map.

``` python
# Define the color mapping for job statuses

def plot_job_status(status_df, color_dict):
    status_plot = copy.deepcopy(status_df)
    status_plot['geometry'] = status_plot['geometry'].apply(wkt.loads)
    status_plot = gpd.GeoDataFrame(status_plot, geometry='geometry', crs='EPSG:4326')
    status_plot['color'] = status_plot['status'].map(color_dict).fillna(color_dict[None])

    minx, miny, maxx, maxy = status_plot.total_bounds
    center_lat = (miny + maxy) / 2
    center_lon = (minx + maxx) / 2

    fig = px.choropleth_map(
        status_plot,
        geojson=status_plot.geometry.__geo_interface__,
        locations=status_plot.index,
        color='status',
        color_discrete_map=color_dict,
        map_style="carto-positron",
        center={"lat": center_lat, "lon": center_lon},
        zoom=8,
        title="Job Status Overview"
    )
    fig.update_geos(fitbounds="locations")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig
```

### 5. Running the Jobs with MultiBackendJobManager

Finally, we run the jobs using MultiBackendJobManager, which allows us to manage multiple job executions across. As a standard-user, you can run 2 parallel jobs at any time.

Threading is applied to enable the visualization of job statuses while concurrently running openEO jobs. This approach allows the jobs to execute in parallel with the status updates, ensuring that the map is refreshed regularly without blocking job execution. In total there are two threads:

- Job Execution: The jobs are initiated using the job manager that runs in its own thread. This allows the jobs to be executed asynchronously.
- Visualization: At the same time, we continually check the job statuses from a CSV file (jobs.csv) and update the visualization using the plot_job_status function.

``` python
# Start a threaded job manager
job_manager.start_job_thread(start_job=start_job, job_db=job_db)

while not job_manager._stop_thread:
    try:
        status_df = pd.read_csv('jobs.csv')
        fig = plot_job_status(status_df=status_df, color_dict=colors)
        clear_output()
        offline.iplot(fig)

        # Check if all jobs are done
        if status_df['status'].isin(["not_started", "created", "queued", "running"]).sum() == 0:
            job_manager.stop_job_thread()

        time.sleep(poll_sleep)  # Wait before the next update

    except KeyboardInterrupt:
        break
```

    Unable to display output for mime type(s): application/vnd.plotly.v1+json
