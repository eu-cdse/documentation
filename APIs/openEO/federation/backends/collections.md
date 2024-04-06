# Collections
This page describes the requirements on the STAC collection metadata for backend providers in the openEO federation.
These requirements are considered an addition to what is already required by the [openEO API](https://api.openeo.org/#tag/EO-Data-Discovery/operation/describe-collection) and the [API profiles](./api.md#profiles).

## Criteria for eligible collections

The Copernicus Dataspace ecosystem federation is looking for collections that match certain criteria.
In the initial phase of the federation, the focus is on having a stable service, avoiding complex situations that may potentially cause issues.
These criteria will likely relax over time, allowing to gradually integrate and enable more complex scenarios.

The current criteria are:

1. Collections must be complementary to the existing offer, avoiding collections with the same name or similar content.
2. Only non-experimental collections will be considered.
3. Full-archive collections, or collections that fully cover a specific region are encouraged. The intention is to avoid 'demo' collections that only offer a marginal part of the actual dataset.


## Collection availability

Collections are key assets of the federation.
It is important for users to know what they can expect from any given collection.
The federation relies on openEO collection metadata following the STAC specification to communicate this to the user. 
Backend providers need to comply with these requirements for each of their collections:

The 'experimental' flag from https://stac-extensions.github.io/version/v1.1.0/schema.json is required for experimental collections. 
A collection can be experimental either due to issues with the actual data or catalog or backend specific issues that make the use of the collection unstable. 
Experimental collections do not need to comply with further requirements. 

### Requirements for non-experimental collections

Non-experimental features should aim to maximize user satisfaction by ensuring stability and usability _and_ complying with federation agreements fostering a unified service.
The list below outlines this more explicitly, but does not cover all aspects. 
Therefor providers are expected to properly assess whether a specific collection can be considered non-experimental.

1. Collections need to indicate the key 'providers' responsible for ensuring data access and continuity for active missions. 
The user may depend on the guarantees offered by these providers with respect to the properties (timeliness, completeness,...) of a specific collection. 
The providers with role 'host' and 'producer' are mandatory.

2. The collection description and extents needs to specify known limitations with respect to the original collection. 
For instance, if only a subset of the full archive is available, this should be indicated. 
Extents can be rough approximations to avoid requiring very detailed geometry in the metadata.

3. Collections without an end time are assumed to be active missions. 
By default, 99% of the items in these collections should be available within 48 hours after publication by the producer. 
This gives users a basic guarantee with respect to timeliness of products. 

4. Collection metadata should be valid STAC metadata and must include all extensions in `stac_extensions`. 
Tools like [STAC-validator](https://github.com/stac-utils/stac-validator) can indentify obvious issues.

5. FAIR principle R1: [(Meta)data are richly described with a plurality of accurate and relevant attributes](https://www.go-fair.org/fair-principles/r1-metadata-richly-described-plurality-accurate-relevant-attributes/)
6. Collections must follow harmonization guidelines specified below, if applicable.
7. Collections naming (id, dimensions, bands) should remain constant. 
8. Backwards incompatible changes or removal need to be announced with a lead time of 6 months, together with a migration path.
9. Minimum availability for non-experimental collections must be 98% on a monthly basis. 
Users must be notified of backwards incompatible changes or removals six months in advance, alongside a migration path.
In the case it is not possible to measure the availability per collection, the overall backend availability is used.

10. Collections may require special conditions to work, for instance in the case of commercial data.


## Harmonization

When back-ends offer/mirror the same datasets, alignment of the names and metadata is required. 
For the following collections and metadata this alignment has already been achieved. 
All part of the Copernicus Missions, the standard names refer to the archives prepared and distributed by ESA. 
If it is not possible/desirable to use this name as the collection ID, a `common_name` can be added alongside the `id` property to identify the collection as a standard archive.


- SENTINEL1_GRD
- SENTINEL2_L1C
- [SENTINEL2_L2A](#sentinel2-l2a)
- SENTINEL3_OLCI_L1B

### Common naming convention

A uniform structure for all collections on the federation makes it easier for users to navigate between collections.
It is therefor recommended to adhere to the following common naming convention*:

- Names should be written in capital letters ("all caps")
- Names should consist of a combination of different optional attributes (see table)
- The different attributes should be separated by an underscore

Broadly speaking, collections can be divided into two categories, but, in reality, form a spectrum with intermediate gradations:

1. Collections containing raw data or processing levels of that data. 
This data, measured directly by a satellite or other measurement platform, is often distributed by the platform operator (e.g., ESA).

2. Derived collections, which are based on (pre-processed) raw data that has been processed for a specific purpose (e.g., a land cover map).
These are often distributed by the institution, or a service of an institution, that created the collection.

| Attribute | Type |Description | Examples |
|-----------|------|------------|----------|
| Provider | string | Often used for derived collections produced or ordered by the listed provider. | `ESA`, `CNSE`, `EMODNET`, `TERRASCOPE`. `CAMS`, `CGLS` |
| Satellite/Platform | string | Name of the satellite/platform that acquired the data in the collection. | `SENTINEL2`, `LANDSAT8`, `PALSAR2` |
| Processing level | string | Name of the level to which the data was processed (often processed raw data). | `L2A`, `L3`, `L2_1` |
| Version | string | Often used for derived collections that are produced in several versions. | `V1`, `V2`|
| Resolution | string (`number + unit` or `string`) | Usually added if the resolution is of particular importance for the collection (e.g., novel product with this resolution). | `10M`, `120M`, `EUROPE`, `GLOBAL` |
| Product Description | string | Human readable label of the data within the collection. Can also be an abbreviation or acronym. | `LAND_COVER_MAP`, `WORLDCOVER`, `NDVI`, `LAI` |
| Year | number | Often used for derived products that were updated in the specified year or created based on data of the specified year. | `2022` |

> Collections containing raw data or processing levels of that data often use a combination of satellite/platform and processing level (e.g., `SENTINEL2_L1C` ). 
Derived collections often use a combination of provider and product description (e.g., `CNES_LAND_COVER_MAP`).


### Sentinel2-L2A

The common name for this collection is `SENTINEL2_L2A`. 
It refers to the L2A products generated by the Sen2Cor software, which can be made compatible with the ESA generated products. 
It's worth noting that the products in the ESA archive were also processed using different versions of Sen2Cor.
Hence, it is not possible to specify a specific version or configuration of the processing chain. 


#### Bands

For spectral bands, band names follow the Bxx naming convention used by ESA. 
For example: `B01`, `B02`, `B03`, `B08`, `B8A`, `B12`.

The collection also provides access to other bands:

| Band                             | Description                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SCL`                              | The Sen2Cor scene classification band                                                                                                                                                                                                                                                                                                                                                    |
| `approximateViewAzimuth`           | The collective term for the mean and accurate viewing azimuth angle. Depending on which backend is processing the data, the mean angle (for Sentinel Hub) or the accurate angle (for Terrascope) is used. If the accurate angle (`viewAzimuthAngles`) or the mean angle (`viewAzimuthMean`) is explicitly specified, the data is processed on the backend that holds the specified band. |
| `viewZenithMean`                   | The collective term for the mean and accurate viewing zenith angle. Depending on which backend is processing the data, the mean angle (for Sentinel Hub) or the accurate angle (for Terrascope) is used. If the accurate angle (`viewZenithMean`) or the mean angle (`viewZenithAngles`) is explicitly specified, the data is processed on the backend that holds those bands.           |
| `sunAzimuthAngles/sunZenithAngles` | The collective term for the exact sun azimuth and sun zenith angle.                                                                                                                                                                                                                                                                                                                      |
: {tbl-colwidths="[35, 65]"}

### Common Properties

Following is a set of common properties, that can be relevant for multiple collections. 
Collections are strongly encouraged to use these properties instead of using a different name for the same property.

#### Common

- [sat:orbit_state](https://github.com/stac-extensions/sat#satorbit_state)
- [sat:relative_orbit](https://github.com/stac-extensions/sat#satrelative_orbit)

#### Optical instruments

- [eo:cloud_cover](https://github.com/stac-extensions/eo#eocloud_cover)

#### SAR instruments

- [sar:instrument_mode](https://github.com/stac-extensions/sar#item-properties-or-asset-fields)
