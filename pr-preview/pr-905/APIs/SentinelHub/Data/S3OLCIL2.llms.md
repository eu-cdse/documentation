# Sentinel-3 OLCI L2

## About Sentinel-3 OLCI L2 Data

General information about Sentinel-3 mission can be found [here](../../../Data/SentinelMissions/Sentinel3.llms.md). Sentinel Hub offers [Sentinel-3 OLCI Level 2](../../../Data/SentinelMissions/Sentinel3.llms.md#sentinel-3-olci-level-2) products.

### Attribution and use

EU law grants free access to Copernicus Sentinel Data and Service Information for the purpose of the following use in so far as it is lawful: a) reproduction; b) distribution; c) communication to the public; d) adaptation, modification and combination with other data and information; e) any combination of points a to d.

[See more details on the use of Copernicus Sentinel data and service information](https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice)

Tracing based on Sentinel imagery is allowed for commercial purposes as well.

Acknowledgment or credit: *Contains modified Copernicus Sentinel data \[Year\] processed by Sentinel Hub.*

## Accessing Sentinel-3 OLCI L2 Data

To access data you need to send a POST request to our `process` API. The requested data will be returned as the response to your request. Each POST request can be tailored to get you exactly the data you require. To do this requires setting various parameters which depend on the datasource you are querying. This chapter will help you understand the parameters for S3OLCI L2 data. To see examples of such requests go [here](../../../APIs/SentinelHub/Process/Examples/S3OLCI.llms.md), and for an overview of all API parameters see the [API Reference](../../../APIs/SentinelHub/ApiReference.llms.md).

### Data type identifier: sentinel-3-olci-l2

Use `sentinel-3-olci-l2` as the value of the `input.data.type` parameter in your API requests. This is mandatory and will ensure you get Sentinel-3 OLCI L2 data.

### Filtering Options

This chapter will explain the `input.data.dataFilter` object of the `S3OLCI L2` `process` API.

#### mosaickingOrder

Sets the order of overlapping tiles from which the output result is mosaicked. The tiling is based on ESA's [Product Dissemination Units](https://sentinels.copernicus.eu/web/sentinel/search?p_p_id=com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_mvcPath=%2Fview_content.jsp&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_redirect=%2Fweb%2Fsentinel%2Fsearch%3Fq%3Dnight%2520crows%2520diamonds%2520site%252C%25E3%2580%2590Site%253A%2520NCD4%252ECOM%25E3%2580%2591%25E3%2580%259030%2525OFF%2520code%253A%2520NC2024%25E3%2580%2591night%2520crows%2520diamonds%2520site%252Cwhere%2520to%2520buy%2520night%2520crows%2520diamond%252Cnight%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamonds%2520site%252C....6f43%26tag%3Dyear-2017%26category%3D4208307%26delta%3D4%26start%3D180&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_assetEntryId=1741471&_com_liferay_portal_search_web_search_results_portlet_SearchResultsPortlet_INSTANCE_XIxtnlMxlnwC_type=content&p_l_back_url=%2Fweb%2Fsentinel%2Fsearch%3Fq%3Dnight%2520crows%2520diamonds%2520site%252C%25E3%2580%2590Site%253A%2520NCD4%252ECOM%25E3%2580%2591%25E3%2580%259030%2525OFF%2520code%253A%2520NC2024%25E3%2580%2591night%2520crows%2520diamonds%2520site%252Cwhere%2520to%2520buy%2520night%2520crows%2520diamond%252Cnight%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamond%2520site%252Cbest%2520night%2520crows%2520diamonds%2520site%252C....6f43%26tag%3Dyear-2017%26category%3D4208307%26delta%3D4%26start%3D180) for easier distribution.

| Value | Description | Notes |
|:---|:---|:---|
| **mostRecent** | the pixel will be selected from the most recently acquired tile | If there are multiple products with the same timestamp then NTC will be used over NRT. Default value. |
| **leastRecent** | the pixel will be selected from the oldest acquired tile | If there are multiple products with the same timestamp then NTC will be used over NRT. |
| **leastCC** | pixel is selected from tile with the least cloud coverage metadata | Note that "per tile" information is used here. |

#### maxCloudCoverage

Sets the upper limit for cloud coverage in percent based on the precomputed cloud coverage estimate for each Sentinel-3 tile as present in the tile metadata. Satellite data will therefore not be retrieved for tiles with a higher cloud coverage estimate. For example, by setting the value to `20`, only tiles with at most 20% cloud coverage will be used. Note that this parameter is set per tile and might not be directly applicable to the chosen area of interest.

### Processing Options

This chapter will explain the `input.data.processing` object of the `S3OLCI L2` `process` API.

[TABLE]

### Available Bands and Data

For more about Sentinel-3 OLCI L2 bands, visit [this Copernicus website](https://sentiwiki.copernicus.eu/web/olci-products).

### Units

The data values for each band in your custom script are presented in the units as specified here. In case more than one unit is available for a given band, you may optionally set the value of `input.units` in your evalscript `setup` function to one of the values in the `Sentinel Hub Units` column. Doing so will present data in that unit. The Sentinel Hub `units` parameter combines the physical quantity and corresponding units of measurement values. As such, some names more closely resemble physical quantities, others resemble units of measurement.

The `Source Format` specifies how and with what precision the digital numbers (`DN`) from which the unit is derived are encoded. Bands requested in `DN` units contain exactly the pixel values of the source data. Note that resampling may produce interpolated values. `DN` is also used whenever a band is derived computationally (like dataMask); such bands can be identified by having `DN` units and `REFLECTANCE` source format. `DN` values are typically not offered if they do not simply represent any physical quantity, in particular, when `DN` values require source-specific (i.e. non-global) conversion to physical quantities.

Values in non-`DN` units are computed from the source (`DN`) values with at least float32 precision. Note that the conversion might be nonlinear, therefore the full value range and quantization step size of such a band can be hard to predict. Band values in evalscripts always behave as floating point numbers, regardless of the actual precision.

The `Typical Range` indicates what values are common for a given band and unit, however outliers can be expected.

### Sentinel-3 OLCI L2 LAND

[TABLE]

### Sentinel-3 OLCI L2 WATER

[TABLE]

### Mosaicking

All [mosaicking](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#mosaicking) types are supported.

### Scenes Object

[`scenes` object](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#scenes) stores metadata. An example of metadata available in `scenes` object for Sentinel-3 OLCI L2 when mosaicking is `ORBIT`:

| Property name | Value |
|:---|:---|
| tiles\[i\].sentinel3ProductId | `'S3B_OL_2_LFR____20201129T040222_20201129T040522_20201130T074446_0179_046_161_2700_LN1_O_NT_002.SEN3`’ |
| tiles\[i\].date | `'2019-04-02T17:05:39Z'` |
| tiles\[i\].shId | `881338` |
| tiles\[i\].dataPath | `'http://data.cloudferro.com/EODATA/Sentinel-3/OLCI/OL_2_LFR/2020/11/29/S3B_OL_2_LFR____20201129T040222_20201129T040522_20201130T074446_0179_046_161_2700_LN1_O_NT_002.SEN3'` |

Properties of a `scenes` object can differ depending on the selected mosaicking and in which evalscript function the object is accessed. [Working with metadata in evalscript](../../../APIs/SentinelHub/UserGuides/Metadata.llms.md) user guide explains all details and provides examples.

## Catalog API Capabilities

To access Sentinel 3 OLCI L2 product metadata you need to send search request to our [Catalog API](../../../APIs/SentinelHub/Catalog.llms.md). The requested metadata will be returned as JSON formatted response to your request.

### Collection identifier: sentinel-3-olci-l2

### Distinct extension

- `date`

## Footnotes
