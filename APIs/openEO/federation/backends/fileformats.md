# File Formats

The openEO federation offers different file formats for importing and exporting of data.

## Best practices file formats
Depending on the data cube that your process graph creates and on your later use case, some file formats are more suitable to export your data (`save_result`) in than others. Following a brief overview of the most common use cases.

### Raster Formats
- JPEG/PNG: data formats that are well suited for use in media/printing
  - not georeferenced (therefore only of limited use for further analysis)
  - limited to 3 (JPEG) or 4 (PNG) output bands (image channels)
  - usually contains data from 1 timestamp
- netCDF: ideal for time series data as it stores data in multi-dimensional arrays
  - georeferenced (x/y dimensions)
  - can store multiple bands (band dimension)
  - can store multiple timestamps (time dimension)
  - self-describing, portable and scalable
- GeoTiff: ideal for storing several bands in one file in cloud optimized format
  - georeferenced
  - can store multiple bands
  - a single GeoTiff corresponds to one timestamp (in combination with STAC, multi-temporal collections can be supported)
  - cloud optimized

## Federation agreement file formats 
If back-ends offer/mirror the same file formats for both import and export, it is required to align them.

For file export through `save_result` for example, the output parameters and the structure of the data that is written to storage needs to be defined.
For the following file formats an agreement has been achieved:

- GeoTiff
- netCDF

The idea of these guidelines is to align with what the formats and corresponding toolchains support as much as possible. 

### GeoTiff
Defaults:
- a single GeoTiff corresponds to one timestamp (in combination with STAC, multi-temporal collections can be supported)
- All datacube bands are stored in the same geotiff
- The full spatial extent is written to the same geotiff
- Cloud optimized
- For ideal support in the Web Editor (and other tools), the following guide is recommended to be followed: <https://github.com/Open-EO/openeo-web-editor/blob/master/docs/geotiff.md>

### netCDF
Defaults: 
- The full datacube is written to a single netCDF.
- The openEO dimension metadata is preserved in the netCDF file. 
- CF conventions (https://cfconventions.org/) are used where applicable.
- Data is chunked and compressed

More information on all supported file formats, can be found [here](../../file-formats).