# Landsat-7

The Landsat programme is a joint USGS and NASA-led enterprise for Earth observation that represents the world’s longest running system of satellites for moderate-resolution optical remote sensing for land, coastal areas and shallow waters.

Landsat-7 Collection 1 products in the Copernicus Data Space Ecosystem originate from the ESA processing. For more information please visit [here](https://earth.esa.int/eogateway/missions/landsat).

Landsat-7 has continued the goal of the Landsat programme to repeatedly image Earth’s land and coastal areas in order to monitor changes to these areas over time. The satellite has continued to provide data continuity for the Thematic Mapper aboard Landsat-4 and 5, utilising an enhanced version of the instrument.

The Enhanced Thematic Mapper Plus (ETM+) is the main instrument on board Landsat-7 and has been operational since 1999. It provides 30 m resolution for visible (VIS), near-infrared (NIR) and shortwave infrared (SWIR) as well as 60 m resolution for thermal infrared. Moreover, it adds a 15 m resolution panchromatic band (PAN).

Access to Landsat-7 data is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27LANDSAT-7%27`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27LANDSAT-7%27)

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on:

• [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-1

## Landsat-7 ETM+GTC-1P

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27LANDSAT-7%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27GTC_1P%27))))

![](https://img.shields.io/badge/Update_Frequency-Archived%20dataset-0A4393)

#### Overview

Landsat-7 ETM+ GTC (Global Land Survey) 1-arc second Panchromatic (1P) product is particularly useful for applications such as detailed land-cover mapping, change detection, and mapping of urban areas, as it enables the ability to discriminate between objects with higher detail. However, the Landsat-7 satellite experienced a hardware malfunction that caused a loss of data in every image acquired after May 2003. Therefore, the Landsat-7 ETM+ GTC 1-arc second Panchromatic (1P) product is limited to images acquired before the malfunction occurred.

##### Offered Data

| Product        | Archive Status | Spatial Extent | Temporal Extent     | Origin |
|----------------|----------------|----------------|---------------------|--------|
| (\*)ETM-GTC-1P | (\*) Unpacked  | Europe         | Sep 1999 - Dec 2003 | ESA    |

(\*) Landsat ETM+ ESA archive

Further details about the data collection

  

##### Useful Links

- Source: [https://landsat-diss.eo.esa.int/socat/LandsatETM](https://landsat-diss.eo.esa.int/socat/LandsatETM)
- More Information: [https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)

## Landsat-7 ETM+L1G

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27LANDSAT-7%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27L1G%27))))

![](https://img.shields.io/badge/Update_Frequency-Archived%20dataset-0A4393)

#### Overview

Landsat-7 ETM+ Level-1 Georeferenced (L1G) product is suitable for applications such as land-use mapping, change detection, and ecological monitoring, where the spatial accuracy may not be critical. The data is provided in an unprocessed, uncalibrated format. However, it also includes georeferencing information, allowing for easy integration into geospatial analysis systems.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent     | Origin |
|---------|----------------|----------------|---------------------|--------|
| ETM-L1G | Unpacked       | Europe         | Sep 1999 - Nov 2015 | ESA    |

Further details about the data collection

  

##### Useful Links

- Source: [https://landsat-diss.eo.esa.int/socat/LandsatETM](https://landsat-diss.eo.esa.int/socat/LandsatETM)
- More Information: [https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)

## Landsat-7 ETM+L1GT

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27LANDSAT-7%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27L1GT%27))))

![](https://img.shields.io/badge/Update_Frequency-Archived%20dataset-0A4393)

#### Overview

Landsat-7 ETM+ L1GT refers to the Level-1 Geocorrected and Terrain corrected product acquired by the Enhanced Thematic Mapper Plus (ETM+) instrument on board Landsat 7 satellite. This product is corrected for geometric distortions caused by the satellite’s altitude, position, and attitude, as well as to correct for variations in terrain height. The corrected images are orthorectified to a cartographic projection, with radiometric and atmospheric corrections applied to produce accurate and calibrated reflectance values. This product is widely used for various applications including crop management, forest management, geological studies, land-use planning, and environmental monitoring.

##### Offered Data

| Product  | Archive Status | Spatial Extent | Temporal Extent     | Origin |
|----------|----------------|----------------|---------------------|--------|
| ETM-L1GT | Unpacked       | Europe         | Sep 1999 - Jan 2017 | ESA    |

Further details about the data collection

  

##### Useful Links

- Source: [https://landsat-diss.eo.esa.int/socat/LandsatETM](https://landsat-diss.eo.esa.int/socat/LandsatETM)
- More Information: [https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)

## Landsat-7 ETM+L1T

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27LANDSAT-7%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27L1T%27))))

![](https://img.shields.io/badge/Update_Frequency-Archived%20dataset-0A4393)

#### Overview

Landsat-7 ETM+ L1T refers to the Level-1 Precision Terrain corrected product acquired by the Enhanced Thematic Mapper Plus (ETM+) instrument on board Landsat 7 satellite. This product is corrected for geometric distortions caused by the satellite’s altitude, position, and attitude, as well as to correct for variations in terrain height. The corrected images are orthorectified to a cartographic projection, with radiometric and atmospheric corrections applied to produce accurate and calibrated reflectance values. In addition to the correction for terrain effects, this product also has geometric accuracy maintained to 1/3 of a Landsat pixel. The Landsat-7 ETM+ L1T product is mostly used for precision mapping and monitoring of natural resources, such as land cover classification, vegetation change detection, and urban growth analysis.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent     | Origin |
|---------|----------------|----------------|---------------------|--------|
| ETM-L1T | Unpacked       | Europe         | Sep 1999 - Jan 2017 | ESA    |

Further details about the data collection

  

##### Useful Links

- Source: [https://landsat-diss.eo.esa.int/socat/LandsatETM](https://landsat-diss.eo.esa.int/socat/LandsatETM)
- More Information: [https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive](https://earth.esa.int/eogateway/catalog/landsat-etm-esa-archive)
