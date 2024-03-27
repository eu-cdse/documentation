# Collections
This page describes requirements on STAC collection metadata for backend providers in the openEO federation.
These requirements should be considered an addition to what is already required by the [openEO API](https://api.openeo.org/#tag/EO-Data-Discovery/operation/describe-collection) and the [API profiles](./api.md#profiles).

## Collection availability

The collections are a key asset of the federation, and users need to know what they can expect from a certain collection.
The federation relies on openEO collection metadata following the STAC specification to communicate this towards the user. Backend providers
need to comply with these requirements for their collection:

The 'experimental' flag from https://stac-extensions.github.io/version/v1.1.0/schema.json needs to be set on experimental collections. 
A collection can be experimental either because there are issues with the actual data or catalog, or because of backend specific issues that make the use of the collection unstable. 
A collection marked as experimental does not need to comply with further requirements. 

### Requirements for non-experimental collections

The main goal for non-experimental features is to achieve high user satisfaction by providing stability & usability _and_ to comply with federation agreements that make it possible to offer a unified service.
The list below makes this more concrete, but is not expected to cover all aspects. It is therefore important that providers, who know their implementations and datasets best, properly judge if a specific collection can be
considered non-experimental.

1. Collections need to indicate the key 'providers' that are responsible for ensuring access to the data and continuity in the case of active missions. The user may depend on the guarantees offered by these
providers with respect to the properties (timeliness, completeness,...) of a specific collection. 
The providers with role 'host' and 'producer' are mandatory.

2. The collection description and extents needs to specify known limitations with respect to the original collection. For instance, if only a subset of the full archive is available, this should be indicated. Extents can be rough approximations to avoid requiring very detailed geometry in the metadata.

3. Collections without an end time are assumed to be active missions. By default, 99% of items in these collections should be available within 48 hours after being published by the producer. This gives users a basic guarantee with respect to timeliness of products. 
4. Collection metadata should be valid STAC metadata and must include all extensions in `stac_extensions`. Tools such as [STAC-validator](https://github.com/stac-utils/stac-validator) can indicate obvious issues.
5. FAIR principle R1: [(Meta)data are richly described with a plurality of accurate and relevant attributes](https://www.go-fair.org/fair-principles/r1-metadata-richly-described-plurality-accurate-relevant-attributes/)
6. Collections have to follow harmonization guidelines specified below, if applicable.
7. Collections naming (id, dimensions, bands) should remain constant. 
8. Backwards incompatible changes or removal need to be announced with a lead time of 6 months, together with a migration path.
9. Minimum availability of non-experimental collections is 98% on a monthly basis. The backend availability is used here if availability is not measured per collection.
10. Availability of a collection means that a simple process graph (e.g. using load_collection) returns a correct result. Collections may have special conditions to work, for instance in the case of commercial data.


## Harmonization

When back-ends offer/mirror the same datasets, it is required to align names and metadata. For the following collections and metadata an agreement has been achieved. These are all Copernicus Missions, and the standard names refer to the archives prepared and distributed by ESA. If it is not possible/desirable to use this name as collection id, a 'common_name' can be added next to the 'id' property to identify the collection as a standard archive.


- SENTINEL1_GRD
- SENTINEL2_L1C
- [SENTINEL2_L2A](#sentinel2-l2a)
- SENTINEL3_OLCI_L1B

### Common naming convention

In order to achieve a uniform structure for all collections on the federation and thus make it easier for users to navigate between collections, it is recommended to follow the common naming convention*:

- Names should be written in capital letters ("all caps")
- Names should consist of a combination of different optional attributes (see table)
- The different attributes should be separated by an underscore

Very roughly speaking, collections can be divided into two groups (in reality it is more of a spectrum with all gradations in between):
- collections containing raw data (or processing levels of that data) measured directly by a satellite (or an other measurement platform) and often distributed by the platform operator (e.g., ESA)
- derived collections, which are based on (pre-processed) raw data that has been processed to create a collection with a specific purpose (e.g., a land cover map) and are often distributed by the institution (or a service of an institution) that created the collection

| Attribute | Type |Description | Examples |
|-----------|------|------------|----------|
| Provider | string | Often used for derived collections produced or order by the listed provider. | `ESA`, `CNSE`, `EMODNET`, `TERRASCOPE`. `CAMS`, `CGLS` |
| Satellite/Platform | string | Name of the satellite/platform that acquired the data in the collection. | `SENTINEL2`, `LANDSAT8`, `PALSAR2` |
| Processing level | string | Name of the level to which the data was processed (often processed raw data). | `L2A`, `L3`, `L2_1` |
| Version | string | Often used for derived collections that are produced in several versions. | `V1`, `V2`|
| Resolution | string (`number + unit` or `string`) | Usually added, if the resolution is of particular importance for the collection (e.g., novel product with this resolution) for the collection. | `10M`, `120M`, `EUROPE`, `GLOBAL` |
| Product Description | string | Human readable description of the data within the collection. Can also be an abbreviation or acronym. | `LAND_COVER_MAP`, `WORLDCOVER`, `NDVI`, `LAI` |
| Year | number | Often used for derived products that where updated in the specified year or created based on data of the specified year. | `2022` |

Collections containing raw data or processing levels of that data often use a combination of satellite/platform and processing level (e.g., `SENTINEL2_L1C` ). Derived collections often use a combination of provider and product description (e.g., CNES_LAND_COVER_MAP).


### Sentinel2-L2A

The common name for this collection is 'SENTINEL2_L2A'. It refers to the L2A products generated by the Sen2Cor software, which can be configured to be compatible with the ESA generated products. Note that the products in the ESA archive were also processed with different versions of Sen2Cor, so it is not possible to specify a very specific version or configuration of the processing chain. 


#### Bands

Band names for spectral bands follow the Bxx naming convention used by ESA. For example: B01, B02, B03, B08, B8A, B12

- `SCL` = the Sen2Cor scene classification band
- `approximateViewAzimuth` = collective term for the mean and accurate viewing azimuth angle. Depending on which backend is processing the data, the mean angle (for Sentinel Hub) or the accurate angle (for Terrascope) is used. If the accurate angle (`viewAzimuthAngles`) or the mean angle (`viewAzimuthMean`) is explicitly specified, the data is processed on the backend that holds the specified band.
- `viewZenithMean` = collective term for the mean and accurate viewing zenith angle. Depending on which backend is processing the data, the mean angle (for Sentinel Hub) or the accurate angle (for Terrascope) is used. If the accurate angle (`viewZenithMean`) or the mean angle (`viewZenithAngles`) is explicitly specified, the data is processed on the backend that holds those bands.
- `sunAzimuthAngles`/`sunZenithAngles` = collective term for the exact sun azimuth and sun zenith angle.

### Common Properties

We list here a set of common properties, that can be relevant for multiple collections. Collections are strongly encouraged to use these properties instead of using a different name for the same property.

#### Common

- [sat:orbit_state](https://github.com/stac-extensions/sat#satorbit_state)
- [sat:relative_orbit](https://github.com/stac-extensions/sat#satrelative_orbit)

#### Optical instruments

- [eo:cloud_cover](https://github.com/stac-extensions/eo#eocloud_cover)

#### SAR instruments

- [sar:instrument_mode](https://github.com/stac-extensions/sar#item-properties-or-asset-fields)
