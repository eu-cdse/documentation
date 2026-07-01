# Sentinel-5P L2

## About Sentinel-5P Data

General information about Sentinel-5p mission can be found [here](../../../Data/SentinelMissions/Sentinel5P.llms.md). Sentinel Hub offers Sentinel-5p Level 2 products.

## Accessing Sentinel-5P Data

To access data you need to send a POST request to our `process` API. The requested data will be returned as the response to your request. Each POST request can be tailored to get you exactly the data you require. To do this requires setting various parameters which depend on the datasource you are querying. This chapter will help you understand the parameters for S5PL2 data. To see examples of such requests go [here](../../../APIs/SentinelHub/Process/Examples/S5PL2.llms.md), and for an overview of all API parameters see the [API Reference](../../../APIs/SentinelHub/ApiReference.llms.md).

### Data type identifier: sentinel-5p-l2

Use `sentinel-5p-l2` (previously `S5PL2`) as the value of the `input.data.type` parameter in your API requests. This is mandatory and will ensure you get Sentinel-5P L2 data.

### Filtering Options

This chapter will explain the `input.data.dataFilter` object of the `S5PL2` `process` API.

#### timeRange

For simple mosaicking, the time range which is requested is clipped to start at most 24 hours before the `to` date-time. The reason for this is that Sentinel-5P covers the globe in one day therefore longer time ranges are not neccessary. The limitation also improves the responsiveness of Sentinel Hub.

#### mosaickingOrder

Sets the order of sources from which the output result is mosaicked. If there are multiple sources available for the same time, unless explicitly set otherwise, Sentinel Hub will take the source with the slowest [timeliness](#timeliness) (i.e. `RPRO` prefered to `OFFL` prefered to `NRTI`).

| Value | Description |
|:---|:---|
| **mostRecent** | the pixel will be selected from the tile, which was acquired most recently |
| **leastRecent** | similar to **mostRecent** but in reverse order |

#### timeliness

You can force the timeliness of the requested data. If not set and there are multiple sources available for the same time, Sentinel Hub will take the source with the slowest timeliness (`RPRO` prefered to `OFFL` prefered to `NRTI`). To explicitly set, the options are:

- **NRTI** for near realtime,
- **OFFL** for offline,
- **RPRO** for reprocessing.

### Processing Options

This chapter will explain the `input.data.processing` object of the `S5PL2` `process` API.

[TABLE]

### Available Bands and Data

Information in this chapter is useful when defining [`input` object](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#input-object-properties) in evalscript: any string listed in the column **Name** can be an element of the `input.bands` array in your evalscript.

| Name | Description |
|:---|:---|
| CO | Carbon monoxide, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-carbon-monoxide) |
| HCHO | Formaldehyde, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-formaldehyde) |
| NO2 | Nitrogen oxide, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-nitrogen-dioxide) |
| O3 | Ozone, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-ozone) |
| SO2 | Sulphur dioxide, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-sulphur-dioxide) |
| CH4 | Methane, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/tropomi-level-2-methane) |
| AER_AI_340_380 | UV (Ultraviolet) Aerosol Index calculated based on wavelengths of 340 nm and 380 nm. [More.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-ultraviolet-aerosol-index) |
| AER_AI_354_388 | UV (Ultraviolet) Aerosol Index calculated based on wavelengths of 354 nm and 388 nm. [More.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-ultraviolet-aerosol-index) |
| CLOUD_BASE_PRESSURE | Cloud base pressure, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-cloud) |
| CLOUD_TOP_PRESSURE | Cloud top pressure, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-cloud) |
| CLOUD_BASE_HEIGHT | Cloud base height, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-cloud) |
| CLOUD_TOP_HEIGHT | Cloud top height, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-cloud) |
| CLOUD_OPTICAL_THICKNESS | Cloud optical thickness, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-cloud) |
| CLOUD_FRACTION | Effective radiometric cloud fraction, [more.](https://sentinels.copernicus.eu/web/sentinel/data-products/-/asset_publisher/fp37fc19FN8F/content/sentinel-5-precursor-level-2-cloud) |
| dataMask | The mask of data/no data pixels, [more](../../../APIs/SentinelHub/UserGuides/Datamask.llms.md). |

### Units

The data values for each band in your custom script are presented in the units as specified here. In case more than one unit is available for a given band, you may optionally set the value of `input.units` in your evalscript `setup` function to one of the values in the `Sentinel Hub Units` column. Doing so will present data in that unit. The Sentinel Hub `units` parameter combines the physical quantity and corresponding units of measurement values. As such, some names more closely resemble physical quantities, others resemble units of measurement.

The `Source Format` specifies how and with what precision the digital numbers (`DN`) from which the unit is derived are encoded. Bands requested in `DN` units contain exactly the pixel values of the source data. Note that resampling may produce interpolated values. `DN` is also used whenever a band is derived computationally (like dataMask); such bands can be identified by having `DN` units and `N/A` source format. `DN` values are typically not offered if they do not simply represent any physical quantity, in particular, when `DN` values require source-specific (i.e. non-global) conversion to physical quantities.

Values in non-`DN` units are computed from the source (`DN`) values with at least float32 precision. Note that the conversion might be nonlinear, therefore the full value range and quantization step size of such a band can be hard to predict. Band values in evalscripts always behave as floating point numbers, regardless of the actual precision.

The `Typical Range` indicates what values are common for a given band and unit, however outliers can be expected.

[TABLE]

### Mosaicking

`SIMPLE` and `ORBIT` [mosaicking](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#mosaicking) types are supported.

### Scenes Object

[`scenes` object](../../../APIs/SentinelHub/Evalscript/Functions.llms.md#scenes) stores metadata. An example of metadata available in `scenes` object for Sentinel-5p L2 when mosaicking is `ORBIT`:

| Property name | Value |
|:---|:---|
| tiles\[i\].sentinel5pProductId | `'S5P_OFFL_L2__CO_____20181230T104300_20181230T122430_06286_01_010202_20190105T100707.nc`’ |
| tiles\[i\].date | `'2018-12-30T10:43:00Z'` |
| tiles\[i\].shId | `1900340` |
| tiles\[i\].dataPath | `'http://data.cloudferro.com/EODATA/Sentinel-5P/TROPOMI/L2__CO____/2018/12/30/S5P_OFFL_L2__CO_____20181230T104300_20181230T122430_06286_01_010202_20190105T100707/S5P_OFFL_L2__CO_____20181230T104300_20181230T122430_06286_01_010202_20190105T100707.nc'` |

Properties of a `scenes` object can differ depending on the selected mosaicking and in which evalscript function the object is accessed. [Working with metadata in evalscript](../../../APIs/SentinelHub/UserGuides/Metadata.llms.md) user guide explains all details and provide examples.

### Collection Specific Constraints

The raw data is encoded as 32-bit float samples. For scientific usage it is best to set `tiff` as an output format and `sampleType: SampleType.FLOAT32`.

Sentinel-5P data can potentially contain many no data pixels which is a consequence of the way it is measured. We therefore suggest using the [`dataMask`](../../../APIs/SentinelHub/UserGuides/Datamask.llms.md) band to differentiate between actual zero values and no data.

## Catalog API Capabilities

To access Sentinel 5P L2 product metadata you need to send search request to our [Catalog API](../../../APIs/SentinelHub/Catalog.llms.md). The requested metadata will be returned as JSON formatted response to your request.

### Collection identifier: sentinel-5p-l2

### Filter extension

- `sat:absolute_orbit`
- `s5p:timeliness` ([possible values](#timeliness))
- `s5p:type` (possible values: `O3`, `O3_TCL`, `O3_PR`, `O3_TPR`, `NO2`, `SO2`, `CO`, `CH4`, `HCHO`, `CLOUD`, `AER_AI`, `AER_LH`, `FRESCO`, `BD3`, `BD6`, `BD7`)

### Distinct extension

- `date`
- `s5p:type`

### Examples

[S5PL2 Examples](../../../APIs/SentinelHub/Process/Examples/S5PL2.llms.md)
