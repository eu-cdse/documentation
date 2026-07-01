# Sentinel-3 SLSTR L1B

## About Sentinel-3 SLSTR L1B Data

General information about Sentinel-3 mission can be found [here](../../../Data/SentinelMissions/Sentinel3.llms.md). Sentinel Hub offers [Sentinel-3 SLSTR Level 1B](../../../Data/SentinelMissions/Sentinel3.llms.md#sentinel-3-slstr-level-1) products.

## Accessing Sentinel-3 SLSTR Data

To access data you need to send a POST request to our `process` API. The requested data will be returned as the response to your request. Each POST request can be tailored to get you exactly the data you require. To do this requires setting various parameters which depend on the datasource you are querying. This chapter will help you understand the parameters for S3SLSTR data. To see examples of such requests go [here](../../../APIs/SentinelHub/Process/Examples/S3SLSTR.llms.md), and for an overview of all API parameters see the [API Reference](../../../APIs/SentinelHub/ApiReference.llms.md).

### Data type identifier: sentinel-3-slstr

Use `sentinel-3-slstr` (previously `S3SLSTR`) as the value of the `input.data.type` parameter in your API requests. This is mandatory and will ensure you get Sentinel-3 SLSTR L1B data.

### Filtering Options

This chapter will explain the `input.data.dataFilter` object of the `S3SLSTR` `process` API.

#### mosaickingOrder

Sets the order of overlapping tiles from which the output result is mosaicked. The tiling is based on ESA's [Product Dissemination Units](https://sentinels.copernicus.eu/web/sentinel/search?p_p_id=com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_mvcPath=%2Fview_content.jsp&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_redirect=%2Fweb%2Fsentinel%2Fsearch%3Fq%3Dnight%2520crows%2520diamonds%2520site%252C%25E3%2580%2590Site%253A%2520NCD4%252ECOM%25E3%2580%2591%25E3%2580%259030%2525OFF%2520code%253A%2520NC2024%25E3%2580%2591night%2520crows%2520diamonds%2520site%252Cwhere%2520to%2520buy%2520night%2520crows%2520diamond%252Cnight%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamonds%2520site%252C....6f43%26tag%3Dyear-2017%26category%3D4208307%26delta%3D4%26start%3D180&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_assetEntryId=1741471&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_type=content&p_l_back_url=%2Fweb%2Fsentinel%2Fsearch%3Fq%3Dnight%2520crows%2520diamonds%2520site%252C%25E3%2580%2590Site%253A%2520NCD4%252ECOM%25E3%2580%2591%25E3%2580%259030%2525OFF%2520code%253A%2520NC2024%25E3%2580%2591night%2520crows%2520diamonds%2520site%252Cwhere%2520to%2520buy%2520night%2520crows%2520diamond%252Cnight%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamonds%2520site%252C....6f43%26tag%3Dyear-2017%26category%3D4208307%26delta%3D4%26start%3D180) for easier distribution.

| Value | Description | Notes |
|:---|:---|:---|
| **mostRecent** | the pixel will be selected from the most recently acquired tile | If there are multiple products with the same timestamp then NTC will be used over NRT. Default value. |
| **leastRecent** | the pixel will be selected from the oldest acquired tile | If there are multiple products with the same timestamp then NTC will be used over NRT. |
| **leastCC** | pixel is selected from tile with the least cloud coverage metadata | Note that "per tile" information is used here. |

#### orbitDirection

Filters the acquisition [orbit](https://sentiwiki.copernicus.eu/web/s3-mission#S3Mission-OrbitS3-Mission-Orbittrue) direction. For ascending orbits optical bands will typically return a black image as there is no sunlight to illuminate the earth, though you may get some usable data in regions of midnight sun. Thermal bands will return data normally as they do not depend on sunlight.

| Value | Description | Notes |
|:---|:---|:---|
| **ASCENDING** | Data acquired when the satellite was traveling approximately towards the Earth's North pole | Night (not for optical bands) |
| **DESCENDING** | Data acquired when the satellite was traveling approximately towards the Earth's South pole | Day (for optical bands) |

#### view

Filters the acquisition by [view](https://sentiwiki.copernicus.eu/web/s3-mission#S3Mission-SLSTRCoverageS3-Mission-SLSTR-Coveragetrue).

| Value | Description | Notes |
|:---|:---|:---|
| **NADIR** | the image acquired by the nadir viewing scanner will be selected | Default value |
| **OBLIQUE** | the image acquired by the oblique (rear) viewing scanner will be selected |  |

### Processing Options

This chapter will explain the `input.data.processing` object of the `S3SLSTR` `process` API.

[TABLE]

### Available Bands and Data

This chapter will explain the bands and data which can be set in the [evalscript input object](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#input-object-properties): Any string listed in the column **Name** can be an element of the `input.bands` array in your evalscript.

| Name | Description | Wavelength centre (nm) | Resolution (m/px) |
|:---|:---|:--:|:--:|
| S1 | Cloud screening, vegetation monitoring, aerosol | 554.27 | 500 |
| S2 | NDVI, vegetation monitoring, aerosol | 659.47 | 500 |
| S3 | NDVI, cloud flagging, pixel co-registration | 868 | 500 |
| S4 | Cirrus detection over land | 1374.80 | 500 |
| S5 | Cloud clearing, ice, snow, vegetation monitoring | 1613.40 | 500 |
| S6 | Vegetation state and cloud clearing | 2255.70 | 500 |
| S7 | SST, LST, Active fire | 3742 | 1000 |
| S8 | SST, LST, Active fire | 10854 | 1000 |
| S9 | SST, LST | 12022.50 | 1000 |
| F1 | Active fire | 3742 | 1000 |
| F2 | Active fire | 10854 | 1000 |
| dataMask | The mask of data/no data pixels ([more](../../../APIs/SentinelHub/UserGuides/Datamask.llms.md)). | N/A\* | N/A\*\* |

\*dataMask has no wavelength information, as it carries only boolean information on whether a pixel has data or not. See the chapter on Units for more.  
\*\*dataMask has no source resolution as it is calculated for each output pixel.

For more about Sentinel-3 SLSTR bands, visit this [ESA website](https://sentiwiki.copernicus.eu/web/slstr-products#SLSTRProducts-Resolution).

### Units

The data values for each band in your custom script are presented in the units as specified here. In case more than one unit is available for a given band, you may optionally set the value of `input.units` in your evalscript `setup` function to one of the values in the `Sentinel Hub Units` column. Doing so will present data in that unit. The Sentinel Hub `units` parameter combines the physical quantity and corresponding units of measurement values. As such, some names more closely resemble physical quantities, others resemble units of measurement.

The `Source Format` specifies how and with what precision the digital numbers (`DN`) from which the unit is derived are encoded. Bands requested in `DN` units contain exactly the pixel values of the source data. Note that resampling may produce interpolated values. `DN` is also used whenever a band is derived computationally (like dataMask); such bands can be identified by having `DN` units and `N/A` source format. `DN` values are typically not offered if they do not simply represent any physical quantity, in particular, when `DN` values require source-specific (i.e. non-global) conversion to physical quantities.

Values in non-`DN` units are computed from the source (`DN`) values with at least float32 precision. Note that the conversion might be nonlinear, therefore the full value range and quantization step size of such a band can be hard to predict. Band values in evalscripts always behave as floating point numbers, regardless of the actual precision.

The `Typical Range` indicates what values are common for a given band and unit, however outliers can be expected.

[TABLE]

### Mosaicking

All [mosaicking](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#mosaicking) types are supported.

### Scenes Object

[`scenes` object](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#scenes) stores metadata. An example of metadata available in `scenes` object for Sentinel-3 SLSTR when mosaicking is `ORBIT`:

| Property name | Value |
|:---|:---|
| tiles\[i\].sentinel3ProductId | `'S3A_SL_1_RBT____20200404T205152_20200404T205452_20200406T015620_0179_056_371_0540_LN2_O_NT_004.SEN3`’ |
| tiles\[i\].date | `'2020-04-04T20:51:52.402Z'` |
| tiles\[i\].shId | `1873419` |
| tiles\[i\].cloudCoverage | `30.95142364501953` |
| tiles\[i\].dataPath | `'http://data.cloudferro.com/EODATA/Sentinel-3/SLSTR/SL_1_RBT/2020/04/04/S3A_SL_1_RBT____20200404T205152_20200404T205452_20200406T015620_0179_056_371_0540_LN2_O_NT_004.SEN3'` |

Properties of a `scenes` object can differ depending on the selected mosaicking and in which evalscript function the object is accessed. [Working with metadata in evalscript](../../../APIs/SentinelHub/UserGuides/Metadata.llms.md) user guide explains all details and provides examples.

## Catalog API Capabilities

To access Sentinel 3 SLSTR product metadata you need to send search request to our [Catalog API](../../../APIs/SentinelHub/Catalog.llms.md). The requested metadata will be returned as JSON formatted response to your request.

### Collection identifier: sentinel-3-slstr

### Filter extension

- `eo:cloud_cover` cloud cover percentage
- `sat:orbit_state` ([possible values](#orbitdirection))

### Distinct extension

- `date`
- `sat:orbit_state`

## Examples

[S3SLSTR examples](../../../APIs/SentinelHub/Process/Examples/S3SLSTR.llms.md)
