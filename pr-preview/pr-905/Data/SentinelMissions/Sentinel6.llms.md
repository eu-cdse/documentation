# Sentinel-6

Copernicus [Sentinel-6](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-6) Michael Freilich includes two satellites that will fly sequentially, launched in 2020 and 2025, carrying a state-of-the art optimized payload.

Copernicus Sentinel-6 Michael Freilich is an Earth Observation satellite mission developed to provide enhanced continuity to the very stable time series of mean sea level measurements and ocean sea state that started in 1992, with the TOPEX/Poseidon mission, then continued by the Jason-1, Jason-2 and Jason-3 satellite missions.

The Copernicus Sentinel-6 satellites feature three main scientific instruments: a Ku/C-band Synthetic Aperture Radar (SAR) altimeter known as Poseidon-4, a multi-frequency Advanced Microwave Radiometer for Climate (AMR-C) with an experimental High-Resolution Microwave Radiometer (HRMR), and a suite for Precise Orbit Determination (POD) incorporating Global Navigation Satellite System (GNSS) receivers, a Laser Retroreflector Array (LRA), and a Doppler Orbitography Radio-positioning Integrated by Satellite (DORIS) system. Additionally, there are secondary instruments: a Global Navigation Satellite System Radio Occultation (GNSS-RO) device for atmospheric vertical profile data, and a Radiation Environment Monitor (REM) sensor for in-situ measurement of proton and electron fluxes in the challenging space radiation environment of low-earth orbit.

## Sentinel-6 Precise Orbit Determination (POD) products

[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)

#### Overview

*The set of auxiliary (AUX/AX) products supports precise orbit and attitude determination for the Sentinel missions:*

• AUX_GNSSRD – GNSS L1b files for all Sentinels. These are disseminated via the Data Access (DA) Service,

• AUX_PROQUA – Quaternions Files for all Sentinels. These are disseminated via the Data Access Service,

• AX\_\_\_\_MOED_AX, AX\_\_\_\_POE\_\_AX, AX\_\_\_\_ROE\_\_AX, AUX_COMB – POD Orbit Files, i.e. orbit state vectors (OSV) from the orbit determination performed by the Copernicus POD Service based on the GPSR input data.

##### Offered Data

| Product ID | Content | TGZ | tar | sp3 | Rolling Policy | Catalog API | S3 Path |
|----|----|----|----|----|----|----|----|
| AX\_\_\_\_ROE\_\_AX | Orbit |  | X |  | 1 month | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AX____ROE__AX%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AUX/AX\_\_\_\_ROE\_\_AX/ |
| AUX_GNSSRD | RINEX | X |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_GNSSRD%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AUX/AUX_GNSSRD/ |
| AUX_PROQUA | Quaternions | X |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_PROQUA%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AUX/AUX_PROQUA/ |
| AX\_\_\_\_MOED_AX | Orbit |  | X |  | 1 month | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AX____MOED_AX%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AUX/AX\_\_\_\_MOED_AX/ |
| AX\_\_\_\_POE\_\_AX | Orbit |  | X |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AX____POE__AX%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AUX/AX\_\_\_\_POE\_\_AX/ |
| AUX_COMB | Orbit |  |  | X |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_COMB__%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AUX/AUX_COMB\_\_/ |

## Sentinel-6 Altimetry & Radiometry products

[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)

#### Overview

*This dataset include:*

• MW_2\_*AMR*\_\_\_ – Climate-quality Advanced Microwave Radiometer Level 2 Products which include antenna and brightness temperatures, wet tropospheric correction, water vapour content, and a rain flag,

• P4_1B_LR\_\_\_\_\_ – Poseidon-4 Altimetry Level 1B Low Resolution includes geo-located, and fully calibrated pulse-limited low-resolution Ku-band and C-band waveforms.

• P4_2\_*LR*\_\_\_\_ – Poseidon-4 Altimetry Level 2 Low Resolution the typical altimetry measurements, like the altimeter range, the sea surface height, the wind speed, significant wave height and all required geophysical corrections and related flags derived from LR.

##### Offered Data

| Product ID | Content | TGZ | tar | zip | sp3 | SEN6 | Rolling Policy | Catalog API | S3 Path |
|----|----|----|----|----|----|----|----|----|----|
| MW_2\_*AMR*\_\_\_ | Microwave Radiometer [https://navigator.eumetsat.int/product/EO:EUM:DAT:0837](https://navigator.eumetsat.int/product/EO:EUM:DAT:0837) |  |  | X |  | X | 1 month for NRT/STC products | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MW_2__AMR____%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27))))))) | /eodata/Sentinel-6/AMR-C/MW_2\_*AMR*\_\_\_/ |
| P4_1B_LR\_\_\_\_\_ | Altimetric [https://navigator.eumetsat.int/product/EO:EUM:DAT:0840](https://navigator.eumetsat.int/product/EO:EUM:DAT:0840) |  |  | X |  | X | 1 month for NRT/STC products | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=(%20(Online%20eq%20true)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27P4_1B_LR_____%27))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27)%20)) | /eodata/Sentinel-6/P4/P4_1B_LR\_\_\_\_\_/ |
| P4_2\_*LR*\_\_\_\_ | Altimetric [https://navigator.eumetsat.int/product/EO:EUM:DAT:0842](https://navigator.eumetsat.int/product/EO:EUM:DAT:0842) |  |  | X |  | X | 1 month for NRT/STC products | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=(%20(Online%20eq%20true)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27P4_2__LR_____%27))%20and%20(Collection/Name%20eq%20%27SENTINEL-6%27)%20)) | /eodata/Sentinel-6/P4/P4_2\_*LR*\_\_\_\_/ |
