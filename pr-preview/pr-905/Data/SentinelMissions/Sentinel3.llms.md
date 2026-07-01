# Sentinel-3

The main objective of the [Copernicus Sentinel-3 mission](https://sentiwiki.copernicus.eu/web/sentinel-3) is to measure ocean and land surface colour, sea and land surface temperature, and sea surface topography with high accuracy and reliability to support ocean forecasting systems, environmental monitoring and climate monitoring. The mission definition is driven by the need for continuity in provision of ERS, ENVISAT and SPOT vegetation data, with improvements in instrument performance and coverage.

Level-1

Level-2

## Sentinel-3 OLCI Level 1

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/olci-processing#OLCIProcessing-L1AlgorithmsS3-OLCI-Processing-L1-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OLCI%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OL_1_EFR___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OL_1_ERR___%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/resolution-300m-0A4393)![](https://img.shields.io/badge/revisit-%3C2--day-0A4393)

![](https://collections.eurodatacube.com/sentinel-3-l1b-olci/sentinel-3-l1b-olci.png)

[View in browser](https://dataspace.copernicus.eu/browser/?zoom=9&lat=43.17231&lng=-3.52163&themeId=DEFAULT-THEME&visualizationUrl=https%3A%2F%2Fsh.dataspace.copernicus.eu%2Fogc%2Fwms%2F82f84fab-9b1c-4322-beeb-207b0f05afef&datasetId=S3OLCI_CDAS&fromTime=2023-05-16T00%3A00%3A00.000Z&toTime=2023-05-16T23%3A59%3A59.999Z&layerId=1_TRUE_COLOR&demSource3D=%22MAPZEN%22&cloudCoverage=30)

#### Overview

The [Sentinel-3 OLCI Level 1](https://sentiwiki.copernicus.eu/web/olci-products) products provides calibrated, geolocated, and orthorectified data from the Ocean and Land Colour Instrument (OLCI). These products are delivered not later than 1 month (commitment) after acquisition or from long-term archives.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

Further details about the data collection

[Copernicus Sentinel data 2023](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice)  

##### Spatial Extent

\[-180, -90, 180, 90\]

##### Temporal Interval

\[‘2016-04-17T11:33:13Z’, None\]

##### Spectral Bands

| Band Name | Common Name | GSD(m) | Center Wavelength(μm) |
|:--:|:--:|:--:|:--:|
| Oa01 | Aerosol correction | 300 | 0.4000 |
| Oa02 | Yellow substance and detrital pigments (turbidity) | 300 | 0.4125 |
| Oa03 | Chlorophyll absorption maximum | 300 | 0.4425 |
| Oa04 | Chlorophyll | 300 | 0.4900 |
| Oa05 | Chlorophyll | 300 | 0.5100 |
| Oa06 | Chlorophyll reference (minimum) | 300 | 0.5600 |
| Oa07 | Sediment loading | 300 | 0.6200 |
| Oa08 | 2nd Chlorophyll absorption maximum | 300 | 0.6650 |
| Oa09 | Improved fluorescence retrieval | 300 | 0.6737 |
| Oa010 | Chlorophyll fluorescence peak | 300 | 0.6813 |
| Oa11 | Chlorophyll fluorescence baseline | 300 | 0.7087 |
| Oa12 | O2 absorption / clouds | 300 | 0.7538 |
| Oa16 | Atmospheric / aerosol correction | 300 | 0.7788 |
| Oa17 | Atmospheric / aerosol correction | 300 | 0.8650 |
| Oa18 | Water vapour absorption | 300 | 0.8850 |
| Oa19 | Water vapour absorption | 300 | 0.9000 |
| Oa21 | Water vapour absorption | 300 | 1.0200 |

## Sentinel-3 OLCI Level 2

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/olci-processing#OLCIProcessing-L2AlgorithmsS3-OLCI-Processing-L2-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OLCI%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OL_2_LFR___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OL_2_LRR___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OL_2_WFR___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27OL_2_WRR___%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/resolution-300m-0A4393)![](https://img.shields.io/badge/revisit-%3C2--day-0A4393)

#### Overview

The [Sentinel-3 OLCI Level-2](https://sentiwiki.copernicus.eu/web/olci-products) product provides geophysical data that is derived from the Level-1 product. The level-2 land product provides land and atmospheric geophysical parameters computed for full and Reduced Resolution. The Level-2 product also includes data quality flags that provide information on the reliability of the geophysical parameters, as well as information on the atmospheric correction applied to the data. These flags can be used to filter out data that is not of sufficient quality for a particular application.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

Further details about the data collection

[Copernicus Sentinel data 2023](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice)  

##### Spatial Extent

\[-180, -90, 180, 90\]

##### Temporal Interval

\[‘2016-04-17T11:33:13Z’, None\]

##### Useful Links

- STAC: [https://stac-extensions.github.io/datacube/v1.0.0/schema.json](https://stac-extensions.github.io/datacube/v1.0.0/schema.json)

## Sentinel-3 SLSTR Level 1

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/slstr-processing#SLSTRProcessing-L1AlgorithmsS3-SLSTR-Processing-L1-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SLSTR%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SL_1_RBT___%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C4--day-0A4393)

![](https://collections.eurodatacube.com/sentinel-3-l1b-slstr/sentinel-3-l1b-slstr.png)

[View in browser](https://dataspace.copernicus.eu/browser/?zoom=7&lat=45.17203&lng=-1.4131&themeId=DEFAULT-THEME&visualizationUrl=https%3A%2F%2Fsh.dataspace.copernicus.eu%2Fogc%2Fwms%2F786d8259-f04e-41cb-92fa-42f66a890ff9&datasetId=S3SLSTR_CDAS&fromTime=2023-05-16T00%3A00%3A00.000Z&toTime=2023-05-16T23%3A59%3A59.999Z&layerId=F1_VISUALIZED&demSource3D=%22MAPZEN%22&cloudCoverage=30)

#### Overview

The [Sentinel-3 SLSTR Level-1](https://sentiwiki.copernicus.eu/web/slstr-products) product provides a valuable source of processed and calibrated data that is suitable for a wide range of applications. The product includes key parameters and data quality flags that provide important information on the reliability and accuracy of the data, and the product is generated offline with a delay of a few days after the acquisition of the Level-0 data.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

Further details about the data collection

[Copernicus Sentinel data 2023](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice)  

##### Spatial Extent

\[-180, -90, 180, 90\]

##### Temporal Interval

\[‘2016-04-17T11:33:13Z’, None\]

##### Spectral Bands

| Band Name |             Common Name             | GSD(m) | Center Wavelength(μm) |
|:---------:|:-----------------------------------:|:------:|:---------------------:|
|    S1     |           Cloud screening           |  500   |        0.5543         |
|    S2     |        Vegetation monitoring        |  500   |        0.6595         |
|    S3     |        NDVI, cloud flagging         |  500   |        0.8680         |
|    S4     |     Cirrus detection over land      |  500   |        1.3748         |
|    S5     |           Cloud clearing            |  500   |        1.6134         |
|    S6     | Vegetation state and cloud clearing |  500   |        2.2557         |
|    S7     |        SST, LST, Active fire        |  500   |        3.7420         |
|    S8     |        SST, LST, Active fire        |  500   |        10.8540        |
|    S9     |              SST, LST               |  1000  |        12.0225        |
|    F1     |             Active fire             |  500   |        3.7420         |
|    F2     |             Active fire             |  1000  |        3.9400         |

##### Useful Links

- STAC: [https://stac-extensions.github.io/datacube/v1.0.0/schema.json](https://stac-extensions.github.io/datacube/v1.0.0/schema.json)

## Sentinel-3 SLSTR Level 2

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/slstr-processing#SLSTRProcessing-L2AlgorithmsS3-SLSTR-Processing-L2-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SLSTR%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SL_2_AOD___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SL_2_FRP___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SL_2_LST___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SL_2_WST___%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C4--day-0A4393)

#### Overview

The [Sentinel-3 SLSTR Level-2](https://sentiwiki.copernicus.eu/web/slstr-products) product provides higher-level geophysical parameters, but with a longer processing time and coarser spatial resolution compared to the Level-1 product. The product also includes additional data quality flags to provide more information on the reliability and accuracy of the data.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-3 SYN Level 2

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/sentinel-3#Sentinel-3-SYNERGY)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SYNERGY%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SY_2_AOD___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SY_2_SYN___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SY_2_V10___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SY_2_VG1___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SY_2_VGP___%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C2--day-0A4393)

#### Overview

The [Sentinel-3 SYN Level 2](https://sentiwiki.copernicus.eu/web/sentinel-3#Sentinel-3-SYNERGY) product is a higher-level processed product that contains information about the Earth’s atmosphere and its constituents. It is derived from the Level-1 and Level-2 products of the OLCI and SLSTR instruments on board the Sentinel-3 satellite.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Short Time Critical (STC) | Packed or Unpacked | World | Last one month |

Further details about the data collection

Copernicus Sentinel data 2023  

##### Spatial Extent

\[-180, -90, 180, 90\]

##### Temporal Interval

\[‘2016-04-17T11:33:13Z’, None\]

##### Spectral Bands

| Band Name |   Common Name   | GSD(m) | Center Wavelength(μm) |
|:---------:|:---------------:|:------:|:---------------------:|
|    S1     | Cloud screening |  500   |        0.5543         |

## Sentinel-3 SRAL Level 1

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/altimetry-processing#AltimetryProcessing-L1AlgorithmsS3-Altimetry-Processing-L1-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SRAL%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_1_SRA___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_1_SRA_A_%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-28--day-0A4393)

#### Overview

The [Sentinel-3 SRAL Level-1](https://sentiwiki.copernicus.eu/web/altimetry-products) product provides corrected and validated geophysical parameters derived from the raw SRAL Level-0 data, along with metadata and data quality flags that enable the user to assess the reliability and suitability of the data for specific applications.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |
| Short Time Critical (STC) | Packed or Unpacked | World | Last one month |

## Sentinel-3 SRAL Level 2

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/altimetry-processing#AltimetryProcessing-L2AlgorithmsS3-Altimetry-Processing-L2-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SRAL%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_2_LAN___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_2_WAT___%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_2_LAN_HY%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_2_LAN_SI%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SR_2_LAN_LI%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-28--day-0A4393)

#### Overview

The [Sentinel-3 SRAL Level-2](https://sentiwiki.copernicus.eu/web/altimetry-products) product is a higher-level processed product that contains more detailed and refined geophysical parameters suitable for scientific and research applications. It contains advanced geophysical parameters such as sea surface height, significant wave height, and wind speed, that are derived from the SRAL Level-1 products using advanced processing algorithms and quality control procedures.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Mar 2016 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |
| Short Time Critical (STC) | Packed or Unpacked | World | Last one month |

## Sentinel-3 Precise Orbit Determination (POD) products

#### Overview

The Copernicus POD Service for the Sentinel-3 mission categorizes Precise Orbital products into three types based on timeliness. Near Real-Time (NRT) products are generated immediately using real-time GPS data. Short Time Critical (STC) products use data delivered by EGP with a 1-day timeliness. Non Time Critical (NTC) products are computed after several days, incorporating precise inputs like GPS data from CODE, with current ambiguity resolution.

##### Offered Data

| Product ID | Content | EOF | TGZ | zip | sp3 | Rolling Policy | Catalog API | S3 Path |
|----|----|----|----|----|----|----|----|----|
| SR\_\_\_ROE_AX | Orbit |  |  | X |  | 1 month | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27SR___ROE_AX%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/SR\_\_\_ROE_AX/ |
| AUX_MOEORB | Orbit | X |  |  |  | 1 month | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_MOEORB%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/AUX_MOEORB/ |
| AUX_POEORB | Orbit | X |  |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_POEORB%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/AUX_POEORB/ |
| AUX_PRCPTF | Platform | X |  |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_PRCPTF%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/AUX_PRCPTF/ |
| AUX_GNSSRD | RINEX |  | X |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_GNSSRD%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/AUX_GNSSRD/ |
| AUX_PROQUA | Quaternions |  | X |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_PROQUA%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/AUX_PROQUA/ |
| SR\_\_\_MDO_AX | Orbit |  | X |  |  | 1 month | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27SR___MDO_AX%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/SR\_\_\_MDO_AX/ |
| SR\_\_\_POE_AX | Orbit | X |  |  |  |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27SR___POE_AX%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/SR\_\_\_POE_AX/ |
| AUX_COMB | Orbit |  |  |  | X |  | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Online%20eq%20true)%20and%20(((((((Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27AUX_COMB__%27))))%20and%20(Collection/Name%20eq%20%27SENTINEL-3%27))))))) | /eodata/Sentinel-3/AUX/AUX_COMB\_\_/ |

# Demo products (Non-Operational)

## Sentinel-3 SRAL Level 2 AMPLI (SR_2_TDP_LI)

Ice sheet elevation estimates along the Sentinel-3 satellite track, retrieved using the Altimeter data Modelling and Processing for Land Ice (AMPLI). These products cover both Antarctica and Greenland. The dataset spans the entire Sentinel-3A and Sentinel-3B missions, except the first orbit cycles during which the altimeters operated in LRM. The dataset is currently updated every three months by the S3MPC. The user handbook for the Sentinel-3 Altimetry over Land Ice: AMPLI level-2 Products is available here: [Sentinel-3 Altimetry over Land Ice: AMPLI level-2 Products User Handbook](docs/S3_AMPLI_User_Handbook_v1.1.pdf).

## Sentinel-3 SRAL Level 2 L2 Lake Processing Prototype (SR_2_TDP_HY)

Sentinel-3 Hydrology Thematic Demonstration Products developed to showcase a new retracking simulation approach and a higher posting rate (80 Hz) over a wide selection of lakes and reservoirs worldwide. These products cover 1219 lakes and reservoirs worldwide for the time period between 06/01/2016 – 05/09/2024. The user handbook for the Sentinel-3 Altimetry over Land - Level-2 Hydrology Thematic Demonstration Products is available here: [Sentinel-3 Altimetry over Land - Level-2 Hydrology Thematic Demonstration Products User Handbook](docs/S3_LPP_HY_v1.2.pdf).
