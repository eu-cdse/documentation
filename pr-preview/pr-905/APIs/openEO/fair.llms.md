# FAIR data & open science

## FAIR

One of the goals of openEO is to support [FAIR principles](https://www.go-fair.org/fair-principles/) and open science. These principles are seamlessly integrated into the Copernicus Data Space Ecosystem, making it intuitive to adhere to them. Consequently, using openEO allows users to develop FAIR-compliant open solutions automatically.

These are a few examples:

- *[F2 Rich metadata](https://www.go-fair.org/fair-principles/f2-data-described-rich-metadata/)* openEO generates rich STAC metadata that includes processing info, complete raster metadata, band information, etc.
- *[R1.2 Detailed provenance](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/)* In result metadata [derived-from](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md#derived_from) links trace back to all input products.
- *[R1.3 use of domain-relevant (meta)data standard](https://www.go-fair.org/fair-principles/r1-3-metadata-meet-domain-relevant-community-standards/)* By default, openEO generates STAC metadata. For the data formats, it supports well-known options such as Cloud-optimized Geotiff, netCDF with CF conventions, GeoParquet, and many more.

Find a concrete example of STAC metadata generated using openEO shown below:

## STAC metadata

## Open Science

In the context of open science, a significant benefit of using openEO is that it allows workflows to be saved in a standardized format called openEO “process graphs”. This enables scientists to share algorithms easily without exchanging complex code bases. OpenEO code or process graphs are also easier to understand since the backend manages much of the boilerplate logic.

This also impacts the replication of work: the same process graph can be executed on different areas or time periods. This capability allows researchers to determine whether an algorithm is broadly applicable or only effective in a specific environment.

Below is a straightforward process graph illustrating the extraction of Sentinel-2 data. While this example is simple, the underlying steps required to generate an analysis-ready datacube from raw Sentinel-2 L2A products are considerably complex. As a result, the process graph will be much easier to understand than the equivalent openEO code.
