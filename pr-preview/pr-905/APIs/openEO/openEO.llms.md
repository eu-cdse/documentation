# openEO

## Overview

[openEO](https://dataspace.copernicus.eu/analyse/openeo) represents an innovative community standard that revolutionizes geospatial data processing and analysis. This groundbreaking framework provides a novel approach to accessing, processing, and analyzing diverse Earth observation data. By adopting openEO, developers, researchers, and data scientists gain access to a unified and interoperable platform, empowering them to harness distributed computing environments and leverage cloud-based resources for addressing complex geospatial challenges.

[![Logo](_images/openEO_logo.png)](hhttps://dataspace.copernicus.eu/analyse/openeo)

With openEO’s collaborative nature, users can seamlessly share code, workflows, and data processing methods across platforms and tools, fostering collaboration and advancing the accessibility, scalability, and reproducibility of Earth observation data. Additionally, openEO provides intuitive programming libraries that enable easy analysis of diverse Earth observation datasets. These libraries facilitate efficient access and processing of large-scale data across multiple infrastructures, supporting various applications, including exploratory research, detailed mapping, and information extraction from Earth observation. Moreover, this streamlined approach enhances the development process, enabling the utilization of Earth observation data for a wide range of applications and services.

The endpoint for the public service is 100% open source and compatible with Pangeo technology. Read more about it [here](../../APIs/openEO/openeo_deployment.llms.md).

Endpoint: [https://openeofed.dataspace.copernicus.eu/](https://openeofed.dataspace.copernicus.eu/)

Concrete examples of what you can do with openEO can be found in the [notebooks section](../../Usecase.llms.md) of this documentation.

> **TIP:**
>
> The openEO service is unique in providing access to the core datasets as well as including partner platforms in the ecosystem.
>
> Read more about the [CDSE openEO federation](../../APIs/openEO/federation/openeo_federation.llms.md) to understand how this works, and which partners are involved.
>
> To avoid automatic use of partner resources, you can use a separate endpoint: [https://openeo.dataspace.copernicus.eu/](https://openeo.dataspace.copernicus.eu/)

## Added value of openEO API

The key benefits of using openEO API can be summarized as follows:

- Unified and straightforward access to multiple Earth observation datasets.
- Scalable and efficient processing capabilities.
- A standardized system that works across different platforms.
- Independence from underlying technologies and software libraries.
- Reproducibility through transparent workflows, [supporting principles of FAIR](../../APIs/openEO/fair.llms.md) (Findable, Accessible, Interoperable, and Reusable) and Open Science.

When using the openEO API, users can choose [JavaScript](../../APIs/openEO/JavaScript_Client/JavaScript.llms.md), [Python](../../APIs/openEO/Python_Client/Python.llms.md), or [R](../../APIs/openEO/R_Client/R.llms.md) as their client library. This allows them to work with any backend and compare them based on capacity, cost, and result quality.

Nevertheless, if you are unfamiliar with programming, you could start using the [web-based editor for openEO](https://openeofed.dataspace.copernicus.eu/). It supports visual modelling of your algorithms and simplified JavaScript-based access to the openEO workflows and providers. An overview of the openEO web-editor is available in the [Applications](https://documentation.dataspace.copernicus.eu/Applications.html) section of this documentation.

## Datacubes

In openEO, a datacube is a fundamental concept and a key component of the platform. Data is represented as datacubes in openEO, which are multi-dimensional arrays with additional information about their dimensionality. Datacubes can provide a nice and tidy interface for spatiotemporal data as well as for the operations you may want to execute on them. An in-depth introduction to datacubes and processing them with openEO can be found [here.](https://openeo.org/documentation/1.0/datacubes.html)

## Collections

In openEO, a backend offers set of collections to be processed. A user can access and process from this comprehensive [list of data collections](../../APIs/openEO/Collections.llms.md) available in the Copernicus Data Space Ecosystem backend through openEO. They can load (a subset of) a collection using the `load_collection` process, which returns a raster datacube.

## File formats

Depending on the data cube that your process graph creates and on your later use case, some [file formats](../../APIs/openEO/File_formats.llms.md) are more suitable to export your data `(save_result)` than others. A user can choose among possible output formats within openEO.

## Processes

In openEO, a user can find several [processes](../../APIs/openEO/Processes.llms.md) to perform operations on Earth Observation data. These can range from simple `add()` to complex `predict_probabilities()`. Furthermore, a user can create complex workflows by chaining multiple processes together.

## Support

Need help locating your preferred programming language? Or you need help finding functionalities that you want to use. Then you have the option to report issues via [Submit a request](https://helpcenter.dataspace.copernicus.eu/hc/en-gb/requests/new) or actively proposing API changes through Pull Request to our [GitHub repo](https://github.com/eu-cdse).

## General limitations

### Size of retrieved data

As a rule of thumb, openEO is tested up to areas of 100x100km at 10m resolution. Larger extents may work, but we recommend always starting first with smaller areas. Also, consider that large area jobs may result in outputs of multiple gigabytes that become inconveniently large to download or handle on your local machine.

Also, the temporal extent can have a significant impact, so here, we recommend starting with a small extent. Note that it is possible to [increase job resources](../../APIs/openEO/job_config.llms.md).

### Free tier limitations

The following limitations need to be taken into account:

- Synchronous requests are limited to 2 concurrent requests
- Batch jobs are limited to 2 concurrent jobs

These limits are in place to prevent individual users from overloading the service. However, if these limits cause issues with your use case, then [Submit a request](https://helpcenter.dataspace.copernicus.eu/hc/en-gb/requests/new) and our support team will do their best to help you.
