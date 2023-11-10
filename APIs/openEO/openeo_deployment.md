# openEO public service deployment

The openEO deployment of the CDSE public service has the aim to protect against lock-in in various ways:
- The software is 100% open source, preventing dependency on a vendor. 
- openEO is an open standard, with a web service API. Allowing to immediately switch to other API's that implement openEO.
- openEO workflows use standardized processes. Avoiding that your worflows are strongly coupled to a specific technology. 

## Deployment

### Data access

The service runs on Cloudferro and T-Systems infrastructure, close to the storage systems that store the Sentinel
archives. It also reads from these archives directly and processes the data on the fly. For complex products like
Sentinel-1, we have the sar_backscatter process that performs on the fly orthorectification. 

For products like Sentinel-2, with lots of overlap, we have custom code in place to resolve this as efficiently
and correctly as possible. 

We tune settings of data access libraries like GDAL to the specific needs of the clouds that we work with. This
is a tedious process and subject to change. When you observe suboptimal data access performance, it may be good
to enquire about this.

#### Sentinelhub API data access

Some datasets are accessed via the Sentinelhub API instead of the raw files. This is done to provide a 
cost-effective deployment, and be able to offer a wide choice of datasets which would otherwise be impossible.

### Processing

Processing happens on a Kubernetes cluster with auto-scaling capabilities. In that cluster, your jobs run as
Apache Spark applications. This is a very widely used and mature big data processing framework. It is comparable
to Dask, which mostly focuses on being a pure-Python implementation.

We currently do not have benchmarks that rigorously compare the performance of openEO with other processing
frameworks, but we can make some relevant observations:

- There's no technical evidence that, by design, other processing approaches are somehow better or faster.
- We have validated the backend by running large scale processing tasks, and achieved results that matched and 
sometimes even exceeded the expectations with respect to processing budgets.
- The use of a service such as openEO implies significant cost savings in terms of personnel costs compared to
an approach based on infrastructure as a service (IAAS).
- The main cost driver and performance bottleneck of many EO workflows is the data access performance, which is 
relatively independent of the software, assuming that tuning parameters are properly set.

The openEO backend will try to automatically determine performance-sensitive parameters of your processing job.
This includes settings for memory, cores and data partitioning/chunking. It is however possible that the automatic 
tuning is not working for your use case. A typical situation is that workflows require more memory, but someties
also more advanced tuning such as partitioning needs to be applied.

### Deploying your own backend

Just like any other backend you can run your own batch jobs using the open source software, and the public docker image.

At openEO.org, you can find [a list](https://openeo.org/software.html#back-ends) of open source implementations.
There's also [some guidance](https://openeo.org/documentation/1.0/developers/backends/getting-started.html) for 
getting started as a service provider.

To run your own small scale testing locally, we can recommend the Pangeo based 
['local processing'](https://open-eo.github.io/openeo-python-client/cookbook/localprocessing.html) feature.

### Alternative backends & deployments

The openEO Hub maintains a list of other openEO services: https://hub.openeo.org




