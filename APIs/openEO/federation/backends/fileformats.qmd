# File Formats

The openEO federation offers different file formats for importing and exporting of data.
This page details the best practices and agreements for utilizing these file formats.

## Best practices file formats
Depending on the data cube that your process graph generates and the overall use case, some file formats are more suitable to export your data (`save_result`). 
Following is a brief overview of the most common use cases.

### Raster Formats

- JPEG/PNG: data formats that are well suited for use in media/printing
  - Not georeferenced and therefore only of limited use for further analysis
  - Limited to 3 (JPEG) or 4 (PNG) output bands (image channels)
  - Usually contains data from a single timestamp
- netCDF: ideal for time series data as it stores data in multi-dimensional arrays
  - Georeferenced (x/y dimensions)
  - Can store multiple bands (band dimension)
  - Can store multiple timestamps (time dimension)
  - Self-describing, portable and scalable
- GeoTiff: ideal for storing several bands in a single, cloud optimized file
  - Georeferenced
  - Can store multiple bands
  - A single GeoTiff corresponds to one timestamp (in combination with STAC, multi-temporal collections can be supported)
  - Cloud optimized

## Federation agreement file formats 
If backends support identical file formats for both import and export, it is required to align them.

For example, when files are exported through `save_result`, the output parameters and the structure of the data, which will be written to storage, needs to be defined.
Such an agreement has been achieved for the following file formats:

- GeoTiff
- netCDF

The objective of these guidelines is to maximize the alignment with capabilities of these formats and corresponding toolchains.

### GeoTiff
Defaults:

- A single GeoTiff corresponds to one timestamp (in combination with STAC, multi-temporal collections can be supported).
- All datacube bands are stored in the same geotiff.
- The full spatial extent is written to the same geotiff.
- Cloud optimized
- For ideal support in the [openEO Web Editor](../../../../Applications/WebEditor.qmd) (and other tools), the following guide is recommended to be followed: [https://github.com/Open-EO/openeo-web-editor/blob/master/docs/geotiff.md](https://github.com/Open-EO/openeo-web-editor/blob/master/docs/geotiff.md)

### netCDF
Defaults: 

- The full datacube is written to a single netCDF.
- The openEO dimension metadata is preserved in the netCDF file. 
- CF conventions ([https://cfconventions.org/](https://cfconventions.org/)) are used where applicable.
- Data is chunked and compressed.
