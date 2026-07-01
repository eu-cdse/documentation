# Landsat-8

The Landsat programme is a joint USGS and NASA-led enterprise for Earth observation that represents the world’s longest running system of satellites for moderate-resolution optical remote sensing for land, coastal areas and shallow waters.

> **NOTE:**
>
> Landsat-8 Collection 2 Level-1 data with full worldwide coverage, mirrored from the United States Geological Survey, for the years 2015 to the present are now available in the Copernicus Data Space Ecosystem Catalogue. These datasets are indexed in the OData and STAC Catalogue. This Landsat collection will be searchable via the Sentinel Hub API-s and the Copernicus Browser, including visualization. Downloading the full product is not available to general users.

Landsat-8 carries the Operational Land Imager (OLI) and the Thermal Infrared Sensor (TIRS). OLI provides imagery in the VIS, NIR and SWIR spectral ranges. It acquires images with 15 m panchromatic and 30 m multi-spectral spatial resolutions, covering a wide 185 km swath. This allows it to capture extensive areas of the Earth’s landscape while maintaining enough resolution to identify features like urban centers, farms, forests, and other land uses. The entire Earth falls within view once every 16 days due to Landsat-8’s near-polar orbit. The TIRS instrument is a thermal imager operating in a pushbroom mode with two Infra-Red channels: 10.8 µm and 12 µm with 100 m spatial resolution.

Access to Landsat-8 data is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'LANDSAT-8'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'LANDSAT-8')

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-1

## Landsat-8 OLI_L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/LSDS-1574_L8_Data_Users_Handbook-v5.0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-8')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1GT'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-8 OLI L1GT refers to the Collection 2 Level-1 product that is systematically corrected and includes terrain correction, acquired by the Operational Land Imager (OLI) onboard the Landsat 8 satellite. Data were collected from only one instrument because the other instrument was unable to gather data due to technical issues, such as incomplete or incorrect data. L1GT product corrects for geometric distortions caused by satellite altitude, position, and attitude, as well as variations in terrain height. The corrected images are aligned to a cartographic projection and include radiometric corrections but they do not have the full atmospheric corrections required for precise top-of-atmosphere reflectance calculations. The L1GT product offers a geolocation accuracy that is lower than L1TP, typically more than 30 meters.

##### Offered Data

| Product  | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------|----------------|----------------|--------------------|--------|
| OLI_L1GT | Unpacked       | World          | Jan 2015 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-8](https://www.usgs.gov/landsat-missions/landsat-8)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-8 OLI_L1TP

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/LSDS-1574_L8_Data_Users_Handbook-v5.0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-8')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1TP'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-8 OLI L1TP refers to the Collection 2 Level-1 Precision Terrain Corrected product acquired by the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) instruments on board the Landsat 8 satellite. This product includes radiometric, geometric and precision corrections, utilizing ground control points (GCPs) and a digital elevation model (DEM) to correct for parallax errors due to local topographic relief. The corrected images are orthorectified to a cartographic projection, ensuring high geometric accuracy. This processing level also provides radiometric corrections and may include some level of atmospheric correction to produce accurate top-of-atmosphere reflectance values. The L1TP product achieves a high level of geolocation accuracy, typically within 12 meters, making it suitable for detailed analysis and time-series studies.

##### Offered Data

| Product  | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------|----------------|----------------|--------------------|--------|
| OLI_L1TP | Unpacked       | World          | Jan 2015 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-8](https://www.usgs.gov/landsat-missions/landsat-8)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-8 OLI/TIRS_L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/LSDS-1574_L8_Data_Users_Handbook-v5.0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-8')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI_TIRS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1GT'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-8 OLI/TIRS L1GT refers to the Collection 2 Level-1 product that is systematically corrected and includes terrain correction, acquired by the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) instruments on board the Landsat 8 satellite. This product corrects for geometric distortions caused by satellite altitude, position, and attitude, as well as variations in terrain height. The corrected images are aligned to a cartographic projection and include radiometric corrections but they do not have the full atmospheric corrections required for precise top-of-atmosphere reflectance calculations. The L1GT product offers a geolocation accuracy that is lower than L1TP, typically more than 30 meters.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| OLI/TIRS_L1GT | Unpacked       | World          | Jan 2015 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-8](https://www.usgs.gov/landsat-missions/landsat-8)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-8 OLI_TIRS_L1TP

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/LSDS-1574_L8_Data_Users_Handbook-v5.0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-8')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'OLI_TIRS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1TP'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-8 OLI/TIRS L1TP refers to the Collection 2 Level-1 Precision Terrain Corrected product acquired by the Operational Land Imager (OLI) and Thermal Infrared Sensor (TIRS) instruments on board the Landsat 8 satellite. This product includes radiometric, geometric and precision corrections, utilizing ground control points (GCPs) and a digital elevation model (DEM) to correct for parallax errors due to local topographic relief. The corrected images are orthorectified to a cartographic projection, ensuring high geometric accuracy. This processing level also provides radiometric corrections and may include some level of atmospheric correction to produce accurate top-of-atmosphere reflectance values. The L1TP product achieves a high level of geolocation accuracy, typically within 12 meters, making it suitable for detailed analysis and time-series studies.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| OLI/TIRS_L1TP | Unpacked       | World          | Jan 2015 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-8](https://www.usgs.gov/landsat-missions/landsat-8)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)

## Landsat-8 TIRS_L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/atoms/files/LSDS-1574_L8_Data_Users_Handbook-v5.0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'LANDSAT-8')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'TIRS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'L1GT'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

Landsat-8 TIRS L1GT refers to the Collection 2 Level-1 product that is systematically corrected and includes terrain correction, acquired by the Thermal Infrared Sensor (TIRS) onboard the Landsat 8 satellite. Data were collected from only one instrument because the other instrument was unable to gather data due to technical issues, such as incomplete or incorrect data. L1GT product corrects for geometric distortions caused by satellite altitude, position, and attitude, as well as variations in terrain height. The corrected images are aligned to a cartographic projection and include radiometric corrections but they do not have the full atmospheric corrections required for precise top-of-atmosphere reflectance calculations. The L1GT product offers a geolocation accuracy that is lower than L1TP, typically more than 30 meters.

##### Offered Data

| Product   | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-----------|----------------|----------------|--------------------|--------|
| TIRS_L1GT | Unpacked       | World          | Jan 2015 - Present | USGS   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.usgs.gov/landsat-missions/landsat-8](https://www.usgs.gov/landsat-missions/landsat-8)
- More Information: [https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)
