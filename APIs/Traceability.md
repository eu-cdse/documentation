# Traceability Service

Traceability Service provides the user with means to track the lifecycle of a data product. It acts as a
historian of the product’s lifecycle, collecting the traces of all related events.
These traces then can be used to check the integrity of the product, its current whereabouts, its
impact on other products or ultimately its inadequacy for continued use in case of obsolescence.
Digital signatures on the traces provide users with the ability to verify authenticity and integrity of the
traces themselves – this also enables users to detect any alterations of the product during its
lifecycle.

Users may interact with Traceability service by either curl command (on both Windows and Linux),
directly via the Traceability Service API endpoint or via the Traceability Service API documentation.

Traceability Service API endpoint: [https://trace.dataspace.copernicus.eu/api](https://trace.dataspace.copernicus.eu/api)

Documentation related to Traceability Service API: [https://trace.dataspace.copernicus.eu/api/docs](https://trace.dataspace.copernicus.eu/api/docs)

## Example

Interaction with Traceability Service by using curl command on Linux:
```
curl -X 'GET' 'https://trace.dataspace.copernicus.eu/api/v1/traces/name/S2A_MSIL1C_20230420T100021_N0509_R122_T33UVP_20230420T120027.SAFE.zip' -H 'accept: application/json'
```
Please be aware that curl command might have a different syntax on Windows. Please refer to curl
official documentation if you have any questions ([https://curl.se/docs/manual.html](https://curl.se/docs/manual.html)).

## Direct access

Interaction with Traceability Service directly via the Traceability Service API:
[https://trace.dataspace.copernicus.eu/api/v1/traces/name/S2A_MSIL1C_20230420T100021_N0509_R122_T33UVP_20230420T120027.SAFE.zip](https://trace.dataspace.copernicus.eu/api/v1/traces/name/S2A_MSIL1C_20230420T100021_N0509_R122_T33UVP_20230420T120027.SAFE.zip)
