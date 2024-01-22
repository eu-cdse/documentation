# openEO process implementation details

This page details several relevant aspects of the implementation of specific
openEO processes that are relevant for reproducibility.

The openEO deployment of CDSE public service is 100% open source and has
a specific goal of supporting open science.

## SAR backscatter

The sar_backscatter process allows on-the-fly computation of Sentinel-1 sigma0 backscatter. It is based
on the open-source Orfeo Toolbox and sufficiently fast to provide a cost-effective option for large-scale
processing.

### Known issues

When thermal noise is removed, values are set to 0, but Orfeo also uses 0 for nodata.

## load_collection

The load_collection implementation is quite advanced and tries to optimise data loading from the data space archive.

When no resampling options are specified in the process graph, we try to respect the original pixel grid of the data.
This is done to allow processing that is equally exact as file-based processing.

### Known issues

Property filtering depends on the data space catalogue, which currently has limited STAC capabilities. 
This sometimes prevents the usage of standardised STAC property names, which affects the portability of 
other process graphs.
