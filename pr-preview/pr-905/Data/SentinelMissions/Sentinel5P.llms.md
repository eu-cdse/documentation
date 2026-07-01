# Sentinel-5P

The [Copernicus Sentinel-5 Precursor](https://sentiwiki.copernicus.eu/web/sentinel-5p) mission is the first Copernicus mission dedicated to monitoring our atmosphere.

The main objective of the Copernicus Sentinel-5P mission is to perform atmospheric measurements with high spatio-temporal resolution, to be used for air quality, ozone & UV radiation, and climate monitoring & forecasting.

There are [different data products](https://sentiwiki.copernicus.eu/web/s5p-products) associated with the three levels of TROPOMI processing: Level-0, Level-1B and Level-2.

Level-1

Level-2

## Sentinel-5P Level 2 Aerosol Index

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-AerosolIndex)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__AER_AI%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_AER_AI_sample.png)

[View in browser](https://sentinelshare.page.link/DmLr%20)

#### Overview

The [Sentinel-5P Level 2 Aerosol Index (AER_AI)](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) dataset provides high-resolution imagery of the UV Aerosol Index (UVAI), also called the Absorbing Aerosol Index (AAI). The AAI is based on wavelength-dependent changes in Rayleigh scattering in the UV spectral range for a pair of wavelengths. The difference between observed and modelled reflectance results in the AAI. When the AAI is positive, it indicates the presence of UV-absorbing aerosols like dust and smoke. It is useful for tracking the evolution of episodic aerosol plumes from dust outbreaks, volcanic ash, and biomass burning.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Carbon Monoxide

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-COandCH4Pre-ProcessingS5P-Processing-L2-Algorithms-SWIR-CO-and-CH4)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__CO____%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://collections.eurodatacube.com/co_3daily_data/co.png)

[View in browser](https://sentinelshare.page.link/kp7r)

#### Overview

The [Sentinel-5P Level 2 CO](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) data refers to processed and derived datasets obtained from the Sentinel-5P satellite mission, specifically focusing on measuring and analyzing the concentration of carbon monoxide in the Earth’s atmosphere. It includes data on the total column carbon monoxide content, as well as vertical profiles that describe how the concentration changes with altitude.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Cloud

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-CloudParameters)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__CLOUD_%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_CLOUD_sample.png)

[View in browser](https://sentinelshare.page.link/mtKW%20%20)

#### Overview

The [Sentinel-5P Level 2 Cloud](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) dataset provides high-resolution imagery of cloud parameters. The TROPOMI/S5P cloud properties retrieval is based on the OCRA and ROCINN algorithms currently being used in the operational GOME and GOME-2 products. OCRA retrieves the cloud fraction using measurements in the UV/VIS spectral regions and ROCINN retrieves the cloud height (pressure) and optical thickness (albedo) using measurements in and around the oxygen A-band at 760 nm. Additionally, the cloud parameters are also provided for a cloud model which assumes the cloud to be a Lambertian reflecting boundary.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Formaldehyde

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-Formaldehyde(HCHO)VerticalColumn)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__HCHO__%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_HCHO_sample.png)

[View in browser](https://sentinelshare.page.link/UY1F%20)

#### Overview

The [Sentinel-5P Level 2 HCHO](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) data refers to processed and derived datasets obtained from the Sentinel-5P satellite mission that focus on measuring and analyzing the concentration of formaldehyde in the Earth’s atmosphere. The Level 2 Formaldehyde data also incorporates auxiliary information, such as geolocation, cloud properties, and surface reflectance, which are crucial for contextualizing and interpreting the measurements.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Methane

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-COandCH4Pre-ProcessingS5P-Processing-L2-Algorithms-SWIR-CO-and-CH4)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__CH4___%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://collections.eurodatacube.com/s5p-ch4-weekly/ch4.PNG)

[View in browser](https://sentinelshare.page.link/zRc2)

#### Overview

The [Sentinel-5P Level 2 CH4](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) data from the Copernicus Sentinel-5P satellite shows the methane concentrations globally. This product provides processed and derived measurements of methane concentrations in the Earth’s atmosphere. It is a valuable resource for studying climate change, understanding methane emissions, and informing environmental policies and mitigation efforts.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Nitrogen Dioxide

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-NO2Tropospheric,StratosphericandTotalVerticalColumns)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__NO2___%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://collections.eurodatacube.com/s5p-no2-tropno-daily-check/s5p-no2-tropno-daily-check.png)

[View in browser](https://sentinelshare.page.link/ZYjb)

#### Overview

The [Sentinel-5P Level 2 NO2](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) data comes from the Copernicus Sentinel-5P satellite and shows the nitrogen dioxide concentrations across the globe. Concentrations of short-lived pollutants, such as nitrogen dioxide, are indicators of changes in economic slowdowns and are comparable to changes in emissions.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Ozone

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-Ozone(O3)FullVerticalprofile)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__O3____%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_O3_sample.png)

[View in browser](https://sentinelshare.page.link/mC1R)

#### Overview

The [Sentinel-5P Level 2 O3](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) data refers to processed and derived datasets obtained from the Sentinel-5P satellite mission that focuses on measuring and analyzing the concentration and distribution of ozone in the Earth’s atmosphere. Researchers and scientists utilize this data for various purposes, that includes monitoring and assessing ozone depletion, particularly in regions like the polar areas, where the ozone layer is crucial. Additionally, the data aids in air quality monitoring, enabling the evaluation of ozone pollution control measures and understanding of pollution sources.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 2 Sulfur Dioxide

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-SO2VerticalColumn)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L2__SO2___%27)%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

![](https://developers.google.com/earth-engine/datasets/images/COPERNICUS/COPERNICUS_S5P_NRTI_L3_SO2_sample.png)

[View in browser](https://sentinelshare.page.link/BFJV)

#### Overview

The [Sentinel-5P Level 2 SO2](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L2S5P-Products-L2) data refers to processed and derived datasets obtained from the Sentinel-5P satellite mission that focuses on measuring and analyzing the concentration and distribution of sulfur dioxide in the Earth’s atmosphere. It provides comprehensive information on atmospheric sulfur dioxide’s vertical distribution and spatial variations. It includes data on the total column sulfur dioxide content and vertical profiles that describe how the concentration changes with altitude. This data also incorporates auxiliary information, such as geolocation, cloud properties, and surface reflectance, which are crucial for contextualising and interpreting the measurements. It is a valuable resource for studying air quality, volcanic activity, atmospheric chemistry, and assessing the impacts of sulfur dioxide on human health and the environment.

##### Offered Data

| Timeliness | Archive Status | Spatial Extent | Temporal Extent |
|----|----|----|----|
| Non Time Critical (NTC) | Packed or Unpacked | World | Apr 2018 - Present |
| Near Real Time (NRT) | Packed or Unpacked | World | Last one month |

## Sentinel-5P Level 1B

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://sentiwiki.copernicus.eu/web/s5p-processing#S5PProcessing-L1BAlgorithmsS5P-Processing-L1B-Algorithms)[![Catalog API:STAC](https://img.shields.io/badge/-Catalog_API:STAC-77cc09?style=flat.png)](https://browser.stac.dataspace.copernicus.eu/?.language=en)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-5P%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27instrumentShortName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27TROPOMI%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD1%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD2%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD3%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD4%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD5%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD6%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD7%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_RA_BD8%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_IR_SIR%27)%20or%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27L1B_IR_UVN%27))%20and%20Online%20eq%20true&$top=10)

![](https://img.shields.io/badge/revisit-%3C1--day-0A4393)

#### Overview

The [Sentinel-5P Level 1B](https://sentiwiki.copernicus.eu/web/s5p-products#S5PProducts-L1BS5P-Products-L1B) data refers to a processed and calibrated dataset derived from the raw measurements acquired by the Sentinel-5P satellite. This level of data undergoes initial processing steps to correct for instrument effects, atmospheric disturbances, and other artifacts.

##### Offered Data

| Archive Status     | Spatial Extent | Temporal Extent    |
|--------------------|----------------|--------------------|
| Packed or Unpacked | World          | Apr 2018 - Present |

> **CAUTION:**
>
> In the present implementation of openEO and Sentinel Hub API, users are limited to processing or downloading only one band at a time when dealing with Sentinel 5P collection.
>
> Hence, if you try to load or process two different bands simultaneously using any of these APIs, like methane and NO2, you’ll get an error message indicating that the script can only use one product type at once.
