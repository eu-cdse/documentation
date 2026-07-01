# WorldCereal product download

This example illustrates the use of openEO for combining and downloading data from the [ESA WorldCereal](https://esa-worldcereal.org) project.

This project provides a global map of cereals for 2021 at 10m resolution! It can be used as an important base layer for agriculture use cases. Combined with the power of openEO, you can easily generate agricultural statistics over an area of interest, or use this data as a masking layer in an advanced workflow.

In this example, we’ll illustrate a fairly simple case of combining two collections into a single image file.

``` python
import openeo

c = openeo.connect("openeofed.dataspace.copernicus.eu").authenticate_oidc()
```

    Authenticated using refresh token.

We list the available collection id’s to make sure we have the right name.

``` python
[col["id"] for col in c.list_collections() if "WORLDCEREAL" in col["id"]]
```

    ['ESA_WORLDCEREAL_ACTIVECROPLAND',
     'ESA_WORLDCEREAL_IRRIGATION',
     'ESA_WORLDCEREAL_TEMPORARYCROPS',
     'ESA_WORLDCEREAL_WINTERCEREALS',
     'ESA_WORLDCEREAL_MAIZE',
     'ESA_WORLDCEREAL_SPRINGCEREALS']

``` python
c.describe_collection("ESA_WORLDCEREAL_MAIZE")
```

In the following block, we combine two WorldCereal collections into a single output. Both the maize and the wintercereal collection will have value 100 for their respective crops. This means that once the two datacubes are merged, it’s impossible to distinguish between the two. Therefore, a linear transformation is applied to the winter datacube. Furthermore, since both collections are mapped to a different point in time, the time dimension is reduced, such that the resulting map only contains one timestep with both crops shown. The formula used here is just an example, and can be made much more complex depending on your use case.

``` python
extent = {'west': 3.0, 'south': 50.0, 'east': 4.0, 'north': 51.0, 'crs': 'EPSG:4326'}

temporal = ('2020-09-01T00:00:00Z', '2021-12-31T00:00:00Z')

maize = c.load_collection("ESA_WORLDCEREAL_MAIZE",
                         temporal_extent= temporal,
                         spatial_extent=extent,
                         bands=["CLASSIFICATION"]).reduce_dimension(dimension="t",reducer="mean")

winter = c.load_collection("ESA_WORLDCEREAL_WINTERCEREALS",
                         temporal_extent= temporal,
                         spatial_extent=extent,
                         bands=["CLASSIFICATION"]).apply(lambda x:100*(x+10)).reduce_dimension(dimension="t",reducer="mean")

combined = maize.merge_cubes(winter, overlap_resolver="sum")
```

We now have defined what openEO calls a ‘process graph’, but still need to execute it. We will use an ‘asynchronous’ [batch job](https://open-eo.github.io/openeo-python-client/batch_jobs.html#batch-jobs) that gets sent to the server, as it can take a longer time to execute.

When finished, this command will automatically download the result from openEO to your local working directory. You can also follow the progress and view results in the [openEO web editor](https://editor.openeo.cloud).

``` python
job = combined.execute_batch(
    title = "Worldcereal example Terrascope",
    out_format="GTiff",
)
```

    0:00:00 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': send 'start'
    0:00:22 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:00:28 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:00:35 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:00:43 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:01:18 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:01:31 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:01:47 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:02:06 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:02:30 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:03:00 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': queued (progress N/A)
    0:03:54 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': running (progress N/A)
    0:04:42 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': running (progress N/A)
    0:05:40 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': running (progress N/A)
    0:06:41 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': running (progress N/A)
    0:07:41 Job 'vito-j-0e6bd54acb9d4de2b6b6e03a5bb120dd': finished (progress N/A)

``` python
job.get_results().download_files()
```
