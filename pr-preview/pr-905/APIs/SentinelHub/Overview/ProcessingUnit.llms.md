# Processing Unit definition

*⚠ Costs marked with \*\* are not yet applied, they will come into effect in the future.*

## General data processing - applicable to Process API, OGC API, Statistical API

Each request costs a proportional amount of processing unit(s), depending on what data and processing is requested. One processing unit (PU) is defined as a request for:

- an output (image) size of 512 x 512 pixels,
- 3 collection input bands,
- one data `sample` per pixel (see [sample](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#parameters)),
- an output (image) format not exceeding 16 bits per pixel,
- without additional processing (e.g. orthorectification) applied,

In addition to this:

- Minimal cost of a request is
  - 0.005 PU for Process API and OGC API,
  - 0.01 PU for Statistical API.
- The number of remaining processing units is reduced only when a request successfully executes, i.e. when the response code is `2XX`.

"Multiplication factors" are used to calculate how many processing units are required for each request. The definition of 1 processing unit and the calculation rules are summarized in the following tables:

[TABLE]

**Surcharges**

'Surcharges' are used for non-standard requests, which impact on the execution costs.

| Surcharge | Rules for calculation |
|:---|:---|
| \*\* Evalscript execution time | Execution of evalscript with duration shorter than 200ms, is covered within the base request. Execution of complex evalscripts (i.e. neural networks, large decision trees, etc.) with duration longer than 200ms there is a surcharge of 0.5 PU per each additional started 100ms interval. |

## Sentinel-1 data processing - applicable to Process API, OGC API, Statistical API

In addition to General data processing rules defined above, the following optional multiplicators apply as well:

| Parameter/API | Rules for multiplication factors |
|:---|:---|
| Orthorectification | Requesting orthorectification will result in a multiplication factor of 2 due to additional processing requirements . |
| Radiometric Terrain Correction | Requesting radiometric terrain correction will result in a multiplication factor of 2.5 due to additional processing requirements. The orthorectification factor is not additionally applied as it is a prerequisite. |
| Speckle Filtering | Requesting speckle filtering will result in a multiplication factor of 2 due to additional processing requirements. |

## Data querying - applicable to Catalog API, OGC WFS

Each request costs a proportional amount of processing unit(s) depending on what data and processing is requested. One processing unit (PU) is defined as a request for:

- area of 1000 x 1000 km
- time period up to one month

In addition to this:

- Minimal cost of a request is 0.01 PU.
- Maximal cost of a request is 1 PU.
- The number of remaining processing units is reduced only when a request successfully executes, i.e. when the response code is 2XX.

[TABLE]

## BatchV2 Processing API

"General data processing" and "Sentinel-1 data processing" rules apply with the following exceptions:

- Minimal cost of a request is 100 PU.
- Processing with batch processing API will result in a multiplication factor of 1/3 (only applies if processed tiles is bigger than 10.000 px). Thus, three times more data can be processed comparing to process API for the same amount of PUs.
- \*\* When data is delivered to a bucket in other region within the same system (i.e. Copernicus Data Space Ecosystem, AWS) there is additional cost of 0.03 PU per MB of transferred data.

## Asynchronous Processing API

"General data processing" and "Sentinel-1 data processing" rules apply with the following exceptions:

- Minimal cost of a request is 10 PU.
- When using Asynchronous Processing API, a multiplication factor of 2/3 will be applied to all requests with an area of at least 10,000 px. Thus, up to 1.5 times more data can be processed compared to the Processing API for the same amount of PUs. If the request defines an area smaller than 10,000 px, this request will be charged at the regular rate (no multiplication factor).
- When data is delivered to a bucket in other region within the same system (i.e. Copernicus Data Space Ecosystem, AWS) there is an additional cost of 0.03 PU per MB of data.

## Batch Statistical API

"General data processing" and "Sentinel-1 data processing" rules apply with the following exceptions:

- Minimal cost of a request is 100 PU.
- \*\* When data is delivered to a bucket in other region within the same system (i.e. Copernicus Data Space Ecosystem, AWS) there is an additional cost of 0.03 PU per MB of data.

## Data ordering and delivery - applicable to Orders API, Subscriptions API and Third Party Data Import API

- \*\* Each image requested costs 20 PUs. If an image covers multiple of your areas of interest, then it is activated only once within a 24-hour time window. For example, if you have numerous small agriculture fields which are close to each other and therefore covered by one satellite image.
- \*\* Using the clip tool costs 1 PU per data asset.
- \*\* Each tool used, per data asset, costs 2 PUs. Applies to the following tools: Band Math, Composite, Coregister, Harmonization, Reproject, Tile, TOAR. To learn more, see documentation for [Planet Orders API](https://developers.planet.com/apis/orders/tools/) and [Planet Subscriptions API](https://developers.planet.com/docs/subscriptions/tools/#supported-tools).
- \*\* Each GB egressed off the platform (i.e. downloaded or delivered to your cloud) costs 200 PUs.

## Data ingestion - applicable to Bring your own COG API and Zarr API

- Each non-GET request to BYOC or Zarr API costs 1 PU.
- Usage of your BYOC and Zarr collections is billed the same as usage of public collections.

## Request cost calculation examples

### Sentinel-1 change detection

An example of calculation of processing units for a Sentinel-1 change detection request (e.g. comparison of two time slices) is presented in the table below.

[TABLE]

> **NOTE:**
>
> Statistical API is also a multi-temporal request. The same rules for calculating multiplication factors apply.

### NDVI calculation for a parcel

An example of calculation of processing units of NDVI value over a 4 hectare large parcel at 10 m spatial resolution is presented in the table below.

[TABLE]
