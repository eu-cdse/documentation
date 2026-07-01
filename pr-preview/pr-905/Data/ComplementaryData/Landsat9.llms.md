# Landsat-9

Landsat 9 mission, collaborative effort between the U.S. Geological Survey (USGS) and NASA, continuing the Landsat program’s legacy of providing crucial global observations for monitoring, understanding and managing Earth’s natural resources.

> **NOTE:**
>
> Landsat-9 Collection 2 Level-1 data with full worldwide coverage, mirrored from the United States Geological Survey, for the years 2021 to the present are now available in the Copernicus Data Space Ecosystem Catalogue. These datasets are indexed in the OData and STAC Catalogue. This Landsat collection will be searchable via the Sentinel Hub API-s and the Copernicus Browser, including visualization. Downloading the full product is not available to general users.

Launched in September 2021 satellite continues the legacy of providing critical moderate-resolution satellite imagery for land, coastal, and shallow water analysis. It is equiped in two primary sensors: the Operational Land Imager 2 (OLI-2) and the Thermal Infrared Sensor 2 (TIRS-2). OLI-2 captures multispectral imagery in the visible, near-infrared, and shortwave infrared spectral ranges, with spatial resolutions of 30 meters and a panchromatic band at 15 meters, covering a swath width of 185 km. TIRS-2 provides thermal imaging in two infrared channels 10.8 µm and 12 µm with a spatial resolution of 100 meters. The instruments on Landsat-9, while similar to those on Landsat-8, have been refined to improve data accuracy and reliability. Collecting up to 750 scenes daily, this mission ensures the continuity of Earth’s observational record with a revisit period of 16 days, supporting environmental monitoring, land use planning, and climate research. Landsat 9 expands the archive’s volume by capturing images of all global landmasses and nearshore coastal areas, including islands, at solar elevation angles greater than 5 degrees - areas that were not consistently imaged prior to Landsat 8.

Access to Landsat-9 data is possible via API:

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'LANDSAT-9'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'LANDSAT-9')

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-1

## Landsat-9 OLI_L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-2082_L9-Data-Users-Handbook_v1.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-9')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1GT'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-9 OLI L1GT refers to the Collection 2 Level-1 product that is systematically corrected and includes terrain correction, acquired by the Operational Land Imager (OLI) onboard the Landsat 9 satellite. Data were collected from only one instrument because the other instrument was unable to gather data due to technical issues, such as incomplete or incorrect data. L1GT product corrects for geometric distortions caused by satellite altitude, position, and attitude, as well as variations in terrain height. The corrected images are aligned to a cartographic projection and include radiometric corrections but they do not have the full atmospheric corrections required for precise top-of-atmosphere reflectance calculations. The L1GT product offers a geolocation accuracy that is lower than L1TP, typically more than 30 meters.

##### Offered Data

| Product  | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------|----------------|----------------|--------------------|--------|
| OLI_L1GT | Unpacked       | World          | Nov 2021 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-9](https://www.usgs.gov/landsat-missions/landsat-9)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-9 OLI_L1TP

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-2082_L9-Data-Users-Handbook_v1.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-9')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1TP'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-9 OLI L1TP refers to the Collection 2 Level-1 Precision Terrain Corrected product acquired by the Operational Land Imager (OLI) onboard the Landsat 9 satellite. Data were collected from only one instrument because the other instrument was unable to gather data due to technical issues, such as incomplete or incorrect data. L1TP product includes radiometric, geometric and precision corrections, utilizing ground control points (GCPs) and a digital elevation model (DEM) to correct for parallax errors due to local topographic relief. The corrected images are orthorectified to a cartographic projection, ensuring high geometric accuracy. This processing level also provides radiometric corrections and may include some level of atmospheric correction to produce accurate top-of-atmosphere reflectance values. The L1TP product achieves a high level of geolocation accuracy, typically within 12 meters, making it suitable for detailed analysis and time-series studies.

##### Offered Data

| Product  | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------|----------------|----------------|--------------------|--------|
| OLI_L1TP | Unpacked       | World          | Nov 2021 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-9](https://www.usgs.gov/landsat-missions/landsat-9)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-9 OLI/TIRS_L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-2082_L9-Data-Users-Handbook_v1.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-9')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI_TIRS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1GT'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-9 OLI/TIRS L1GT refers to the Collection 2 Level-1 product that is systematically corrected and includes terrain correction, acquired by the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) instruments on board the Landsat 9 satellite. This product corrects for geometric distortions caused by satellite altitude, position, and attitude, as well as variations in terrain height. The corrected images are aligned to a cartographic projection and include radiometric corrections but they do not have the full atmospheric corrections required for precise top-of-atmosphere reflectance calculations. The L1GT product offers a geolocation accuracy that is lower than L1TP, typically more than 30 meters.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| OLI/TIRS_L1GT | Unpacked       | World          | Nov 2021 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-9](https://www.usgs.gov/landsat-missions/landsat-9)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-9 OLI/TIRS_L1TP

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-2082_L9-Data-Users-Handbook_v1.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-9')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI_TIRS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1TP'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-9 OLI/TIRS L1TP refers to the Collection 2 Level-1 Precision Terrain Corrected product acquired by the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) instruments on board the Landsat 9 satellite. This product includes radiometric, geometric and precision corrections, utilizing ground control points (GCPs) and a digital elevation model (DEM) to correct for parallax errors due to local topographic relief. The corrected images are orthorectified to a cartographic projection, ensuring high geometric accuracy. This processing level also provides radiometric corrections and may include some level of atmospheric correction to produce accurate top-of-atmosphere reflectance values. The L1TP product achieves a high level of geolocation accuracy, typically within 12 meters, making it suitable for detailed analysis and time-series studies.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| OLI/TIRS_L1TP | Unpacked       | World          | Nov 2021 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-9](https://www.usgs.gov/landsat-missions/landsat-9)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-9 TIRS_L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-2082_L9-Data-Users-Handbook_v1.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-9')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'TIRS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1GT'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-9 TIRS L1GT refers to the Collection 2 Level-1 product that is systematically corrected and includes terrain correction, acquired by the Thermal Infrared Sensor (TIRS) onboard the Landsat 9 satellite. Data were collected from only one instrument because the other instrument was unable to gather data due to technical issues, such as incomplete or incorrect data. L1GT product corrects for geometric distortions caused by satellite altitude, position, and attitude, as well as variations in terrain height. The corrected images are aligned to a cartographic projection and include radiometric corrections but they do not have the full atmospheric corrections required for precise top-of-atmosphere reflectance calculations. The L1GT product offers a geolocation accuracy that is lower than L1TP, typically more than 30 meters.

##### Offered Data

| Product   | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-----------|----------------|----------------|--------------------|--------|
| TIRS_L1GT | Unpacked       | World          | Nov 2021 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-9](https://www.usgs.gov/landsat-missions/landsat-9)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)
