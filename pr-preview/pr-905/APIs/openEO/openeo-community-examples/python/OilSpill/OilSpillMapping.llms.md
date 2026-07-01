# Oil spill mapping using Sentinel-1

Several advanced techniques have been discussed and presented by researchers; however, in this notebook, we want to showcase a basic methodology for mapping oil spills using openEO.

Though openEO is fully capable of executing advanced workflows, our focus here is to show a simple yet effective method. This notebook was inspired by the algorithm shown [here](https://github.com/senbox-org/s1tbx/blob/master/s1tbx-op-feature-extraction/src/main/java/org/esa/s1tbx/fex/gpf/oceantools/OilSpillDetectionOp.java).

Additionally, the following references were equally helpful when preparing this usecase:

- https://forum.step.esa.int/t/steps-for-oil-spill-detection/7428/6
- https://ieeexplore.ieee.org/document/1370264

``` python
# Load the essentials
import openeo
import openeo.processes
import numpy as np
```

``` python
connection = openeo.connect("openeo.dataspace.copernicus.eu").authenticate_oidc()
```

    Authenticated using refresh token.

For this workflow, our area of interest is the southern coast of Kuwait near the resort community of Al Khiran, where an oil spill was reported in 2017.

https://skytruth.org/2017/08/satellite-imagery-reveals-scope-of-last-weeks-massive-oil-spill-in-kuwait/

``` python
aoi = {
    "type": "Polygon",
    "coordinates": [
        [
            [48.325487506118264, 28.742803969343313],
            [48.325487506118264, 28.414218984218607],
            [48.75387693420447, 28.414218984218607],
            [48.75387693420447, 28.742803969343313],
            [48.325487506118264, 28.742803969343313],
        ]
    ],
}
```

``` python
s1_image = connection.load_collection(
    "SENTINEL1_GRD",
    temporal_extent=["2017-08-09", "2017-08-12"],
    spatial_extent=aoi,
    bands=["VV"],
)

s1_image = s1_image.sar_backscatter(coefficient="sigma0-ellipsoid")
```

Usually the distribution of SAR backscatter values is too heavy tailed and difficult to analyse (visually and numerically). Therefore let’s normalize the backscatter values by Log with base 10. For further information See https://forum.step.esa.int/t/sigma0-vh-vs-sigma0-vhdb/2661?u=abraun

``` python
s1_image = s1_image.apply(process=lambda data: 10 * openeo.processes.log(data, base=10))
```

Now let us define the adaptive thresholding. It is a two-step process where we first identify the mean value within a window and then select anything below the mean of that threshold.

``` python
filter_window = np.ones([601, 601])
```

``` python
# calculate factor
factor = 1 / np.prod(filter_window.shape)
```

``` python
thresholds = s1_image.apply_kernel(kernel=filter_window, factor=factor)
```

``` python
threshold_shift = 3.5
thresholds = thresholds - threshold_shift
thresholds = thresholds.rename_labels(dimension="bands", target=["threshold"])
```

In the above cell, we selected the threshold based on the https://eo4society.esa.int/wp-content/uploads/2022/01/OCEA03_OilSpill_Kuwait.pdf and it can be changed to any value based on the requirements.

Now we have a separate datacube with the threshold for the entire study area. Let us compare it with our Sentinel-1 datacube. But before that, to have similar properties, we are renaming the amplitude bands and applying the `merge_cube` process.

``` python
s1_image = s1_image.rename_labels(dimension="bands", target=["amplitude"])
s1_image = s1_image.merge_cubes(thresholds)
oil_spill = s1_image.band("amplitude") < s1_image.band("threshold")
```

``` python
# execute the workflow
oil_spill.execute_batch(title="Oil Spill Data", outputfile="OilSpill.nc")
```

    0:00:00 Job 'j-2402068af9e9445cba04c4dd08152f5b': send 'start'
    0:00:22 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:00:28 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:00:36 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:00:46 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:00:58 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:01:12 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:01:32 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:01:52 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:02:17 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:02:49 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:03:29 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:04:19 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:05:20 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:06:21 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:07:24 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:08:26 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:09:33 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:10:35 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:11:36 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:12:38 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:13:40 Job 'j-2402068af9e9445cba04c4dd08152f5b': running (progress N/A)
    0:14:43 Job 'j-2402068af9e9445cba04c4dd08152f5b': finished (progress N/A)

## Let us plot the result

``` python
import matplotlib.pyplot as plt
import matplotlib
import xarray as xr
import matplotlib.patches as mpatches
from rasterio.plot import show
```

``` python
oilspill = xr.load_dataset("OilSpill.nc")
```

``` python
data = oilspill[["var"]].to_array(dim="bands")
```

``` python
cmap = matplotlib.colors.ListedColormap(["black", "#FFFFED"])
values = ["Absence", "Presence"]
colors = ["black", "#FFFFED"]

oilspill_array = data.squeeze().values[600:-600, 600:-600]
fig, axes = plt.subplots(ncols=1, figsize=(5, 5), dpi=100)
axes.imshow(oilspill_array, vmin=0, vmax=1, cmap=cmap)
axes.set_title("Oil Spill Image")

patches = [
    mpatches.Patch(color=colors[i], label="Oil {l}".format(l=values[i]))
    for i in range(len(values))
]
fig.legend(handles=patches, bbox_to_anchor=(0.9, 0.3), loc=1)
axes.axes.get_xaxis().set_visible(False)
axes.axes.get_yaxis().set_visible(False)
```

![](OilSpillMapping_files/figure-html/cell-16-output-1.png)

If we compare with the available manually mapped ground truth shown in the image below, we can conclude that our workflow effectively showed the oil spill in the selected area of interest.

![](gt.png) )
