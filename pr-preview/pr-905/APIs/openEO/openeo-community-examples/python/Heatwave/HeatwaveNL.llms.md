# Heatwave in the Netherlands

As an impact of global warming, an increase in temperature has been reported, which can lead to potential health risks and environmental stress. Several research studies have been presented over the years, such as in this [paper](https://www.mdpi.com/2072-4292/14/3/561), where they explain the change in Land surface temperature over several regions.

Thus, in this notebook, we want to showcase a tool for mapping heatwaves using Sentinel-3 products. For this, we focused on the Netherlands and used specific conditions proposed by the [“National Heatwave Plan”](https://www.rivm.nl/en/heat/national-heatwave-plan) in the Netherlands. The condition implies:

> 5 days \>25 and 3 days \>30

Moreover, in De Bilt, a municipality in the province of Utrecht had a temperature of 25°C at least five days in a row, with at least three days hotter than 30 °C

https://nltimes.nl/2023/09/08/dutch-heat-record-broken-third-day-row-warm-sunny-weekend-ahead

``` python
import openeo
import json
from pathlib import Path
import folium
```

``` python
connection = openeo.connect(
    "openeo.dataspace.copernicus.eu"
).authenticate_oidc()
```

    Authenticated using refresh token.

Let us load 5 month data for the area of interest

``` python
def read_json(filename: str) -> dict:
    with open(filename) as input:
        field = json.load(input)
    return field


date = ["2023-06-01", "2023-10-30"]
aoi = read_json("Netherlands_polygon.geojson")
```

``` python
m = folium.Map([52.2, 5], zoom_start=7)
folium.GeoJson(aoi).add_to(m)
m
```

Make this Notebook Trusted to load map: File -\> Trust Notebook

``` python
lst = connection.load_collection(
    "SENTINEL3_SLSTR_L2_LST",
    temporal_extent=date,
    bands=["LST"],
).filter_spatial(aoi)
```

``` python
# apply cloud masking

mask = connection.load_collection(
    "SENTINEL3_SLSTR_L2_LST",
    temporal_extent=date,
    bands=["confidence_in"],
).filter_spatial(aoi)

mask = mask >= 16384

lst_masked = lst.mask(mask).aggregate_temporal_period(period="day",reducer="max")
```

Next, we define a User Defined Function (UDF) that takes in the datacube and checks whether both specified conditions are satisfied. Given that the unit of the Land Surface Temperature (LST) layer is Kelvin, the conditions are applied accordingly. If the values meet the designated threshold and continue for more than two days, a new resulting array is generated and returned.

Please note that, here we gave 295 and 300 Kelvin as two thresholds since we chose a relatively small region. You can change match your requirement.

``` python
udf = openeo.UDF(
    """
import xarray
from openeo.udf import inspect

def apply_datacube(cube: xarray.DataArray, context: dict) -> xarray.DataArray:
    
    condition_all_above_295 = (cube > 295).rolling(t=5).construct('window_dim').all(dim='window_dim')
    
    condition_at_least_3_above_300 = (cube > 300).rolling(t=5).construct('window_dim').sum(dim='window_dim') >= 3
    
    result = condition_all_above_295 & condition_at_least_3_above_300
    
    return result
"""
)
```

``` python
heatwave_loc = lst_masked.apply_dimension(process=udf, dimension="t")
```

Now let us use `sum` as the reducer to count the total number of times each pixels had a heat wave in the Netherlands during June-September 2023.

``` python
heatwave_loc = heatwave_loc.reduce_dimension(reducer="sum", dimension="t")
```

Since the workflow covers an entire country, we assume that the processing might take a longer time and the default amount of CPU and memory resources assigned might not be sufficient. Therefore, we can use the job configuration capabilities provided in openEO to execute the workflow when using batch job-based methods.

You can find more information on Job configuration on [this page](https://documentation.dataspace.copernicus.eu/APIs/openEO/job_config.html).

``` python
job_options = {
    "executor-memory": "3G",
    "executor-memoryOverhead": "4G",
    "executor-cores": "2",
}
```

``` python
# execute using batch job
heatwave_job = heatwave_loc.execute_batch(
    title="Heatwave Locations in the Netherlands",
    outputfile="Heatwave_NL_v5.nc"
)
```

    0:00:00 Job 'j-25061218511240e2ab3b07a5973ba4a7': send 'start'
    0:00:13 Job 'j-25061218511240e2ab3b07a5973ba4a7': created (progress 0%)
    0:00:18 Job 'j-25061218511240e2ab3b07a5973ba4a7': created (progress 0%)
    0:00:25 Job 'j-25061218511240e2ab3b07a5973ba4a7': created (progress 0%)
    0:00:33 Job 'j-25061218511240e2ab3b07a5973ba4a7': created (progress 0%)
    0:00:43 Job 'j-25061218511240e2ab3b07a5973ba4a7': created (progress 0%)
    0:00:55 Job 'j-25061218511240e2ab3b07a5973ba4a7': created (progress 0%)
    0:01:11 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:01:30 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:01:54 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:02:24 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:03:01 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:03:48 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:04:47 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:05:47 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:06:47 Job 'j-25061218511240e2ab3b07a5973ba4a7': running (progress N/A)
    0:07:47 Job 'j-25061218511240e2ab3b07a5973ba4a7': finished (progress 100%)

``` python
print(f""" The total openEO credits consumed when executing heatwave workflow is 
        {heatwave_job.describe()['costs']} 
        credits."""
     )
```

     The total openEO credits consumed when executing heatwave workflow is 
            7 
            credits.

However, please note that the cost mentioned above was incurred during the preparation of this notebook and could change over time.

## Let’s plot the results

``` python
import matplotlib.pyplot as plt
import matplotlib
import xarray as xr
import numpy as np
```

``` python
heatwave = xr.load_dataset("Heatwave_NL_v5.nc")
```

``` python
data = heatwave[["LST"]].to_array(dim="bands")[0]
data.values[data==0] = np.nan
```

## Interactive plot

Using Folium, we can easily create an interactive map with a background that allows us to easily spot areas affected by heatwaves.

``` python
lon, lat = np.meshgrid(data.x.values.astype(np.float64), data.y.values.astype(np.float64))
cm = matplotlib.colormaps.get_cmap('hot_r')
colored_data = cm(data/20)
```

``` python
m = folium.Map(location=[lat.mean(), lon.mean()], zoom_start=8)
folium.raster_layers.ImageOverlay(colored_data,
                     [[lat.min(), lon.min()], [lat.max(), lon.max()]],
                     mercator_project=True,
                     opacity=0.5).add_to(m)
m
```

Make this Notebook Trusted to load map: File -\> Trust Notebook

## Static plot

Using cartopy, we can create a static plot.

``` python
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

axes = plt.axes(projection=ccrs.PlateCarree())
axes.coastlines()
axes.add_feature(cfeature.BORDERS, linestyle=':')
data.plot.imshow(vmin=0, vmax=10, ax=axes, cmap="hot_r")
axes.set_title("# of Days with Heatwave in 2023")
```

    Text(0.5, 1.0, '# of Days with Heatwave in 2023')

![](HeatwaveNL_files/figure-html/cell-19-output-2.png)

The above plot shows the number of days with a heatwave in the area of interest in the specified time interval.
