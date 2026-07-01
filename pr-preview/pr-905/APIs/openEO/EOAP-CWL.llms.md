# EOAP CWL

With openEO, it is now possible to run CWL ([Common Workflow Language](https://www.commonwl.org/)) in the `run_udf` process. Workflows will be executed using Calrissian on Kubernetes. First read the general CWL documentation from `openeo-geopyspark-driver`: [udf-eoap-cwl.md](https://github.com/Open-EO/openeo-geopyspark-driver/blob/master/docs/udf-eoap-cwl.md) On the CDSE backend, there are some extra features, which are described on this page.

## S3 access

CWL workflows running on this backend will receive short-lived S3 credentials with read-only access to the `eodata` bucket on CDSE. Those credentials will be available in the following environment variables:

- `AWS_ENDPOINT_URL_S3`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

They only work inside the cluster environment, and are only temporarily valid. You can use these instead of your own credentials. This way, your Docker images can remain public.

## Docker images

CWL allows to use docker images to run code. For example:

``` yaml
requirements:
  - class: DockerRequirement
    dockerPull: ghcr.io/cloudinsar/openeo_insar:20260219T1446
```

Only whitelisted Docker images can be used in the cluster. Contact us through [support](https://helpcenter.dataspace.copernicus.eu/hc/en-gb/requests/new) if you have custom images that needs to be whitelisted. (You might need to create an account) As of February 2026, only Docker images that can be pulled without credentials are used.

## Memory limits

Increasing requested memory increases credit usage. The maximum amount of memory available is deployment specific, but would be around 20Gb.  
If your job gets stuck without being processed, consider lowering the requested memory.

## Debugging locally

To test your CWL workflow locally before running it on the cluster, you can use [cwltool](https://pypi.org/project/cwltool/) locally. You might need to provide your own S3 credentials. You can request them [here](https://documentation.dataspace.copernicus.eu/APIs/S3.html).

``` bash
cwltool \
  --tmpdir-prefix=$HOME/tmp/ \
  --force-docker-pull \
  --no-read-only \
  --parallel \
  --preserve-environment=AWS_ENDPOINT_URL_S3 \
  --preserve-environment=AWS_ACCESS_KEY_ID \
  --preserve-environment=AWS_SECRET_ACCESS_KEY \
  example_workflow.cwl example_parameters.json
```
