# Comparative study of before and after flash flood in Cologne using NDWI service available in EOplaza

In this notebook, we tried to perform a comparative study between the pre and post-image of Cologne during the 2021 flood. A simple technique to subtract pre- and post-images is done to determine the change in water content due to flooding in that region.

Reference: https://labo.obs-mip.fr/multitemp/the-ndwi-applied-to-the-recent-flooding-in-the-central-us/

``` python
# import necessary packages
import openeo
from openeo.api.process import Parameter
import json
from pathlib import Path
import matplotlib.pyplot as plt
import rasterio
import numpy as np

# connect with the backend
eoconn = openeo.connect("openeo.vito.be").authenticate_oidc()
```

    Authenticated using refresh token.

Users can choose among different backend available [here](https://hub.openeo.org/) to connect to the backend. Regarding the authentication process, OpenID connect (oidc) is recommended, but it is not always straightforward to use.

``` python
# function to load geojson file
def read_json(path: Path) -> dict:
    with open(path) as input:
        field = json.load(input)
        input.close()
    return field
```

Since this is an already published service available service, they need not be concerned with selecting the backend. They can directly execute the process by providing time and area of interest.

``` python
before_date = ["2021-05-12","2021-05-12"]
after_date = ["2021-06-18", "2021-06-18"]
aoi = read_json("cologne_all.geojson")

# Create a processing graph from the NDWI process using an active openEO connection
before_ndwi = eoconn.datacube_from_process("NDWI", namespace="vito", date=before_date
                                        ,polygon=aoi)
# Create a processing graph from the NDWI process using an active openEO connection
after_ndwi = eoconn.datacube_from_process("NDWI", namespace="vito", date=after_date
                                        ,polygon=aoi)
```

As you can see, a user warning for missing data pops up, which might not be an issue in typical cases. However, we wish to evaluate our results further in our process; thus, defining metadata is needed.

Not all the available services require updating metadata. If a service lacks metadata, performing further computation on the output of the service could be an issue. The user can update the metadata based on its status in such cases.

``` python
# check available information is available in metadata or not
before_ndwi.metadata
```

``` python
# updating our metadata
from openeo.metadata import CollectionMetadata

before_ndwi.metadata = CollectionMetadata({"cube:dimensions":{"t":{"type":"temporal"}}})
after_ndwi.metadata = CollectionMetadata({"cube:dimensions":{"t":{"type":"temporal"}}})
```

Once the metadata is updated, you can perform further operations like subtraction, sum, etc.

Since we now have details on temporal dimension, we can reduce dimension. As we loaded our collection for specific time intervals, it can include multiple time dimensions. Thus, [reduce_dimension](https://processes.openeo.org/#reduce_dimension) applies a reducer to a data cube dimension by collapsing all the pixel values along the time dimension into an output value computed by the reducer.

It is then followed by subtracting our before datacube from the later.

``` python
# compute the change between pre and post image
merging_cubes = after_ndwi.merge_cubes(-before_ndwi)
differenced_cube = merging_cubes.reduce_dimension(dimension="t",reducer='sum')
```

Once the process is completed, you can also save it as your process using [save_user_defined_process](https://open-eo.github.io/openeo-python-client/udp.html) that can later be used for a similar task. Otherwise, you can download the result either by direct download (in case of the small spatial extent with little processing) or by creating a [batch job](https://open-eo.github.io/openeo-python-client/batch_jobs.html).

``` python
# download your result either using synchronous method or batch
# synchronous download
differenced_cube.download("changed_ndwi.tiff")
```
