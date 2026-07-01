# Landsat-5

The Landsat programme is a joint USGS and NASA-led enterprise for Earth observation that represents the world’s longest running system of satellites for moderate-resolution optical remote sensing for land, coastal areas and shallow waters.

Landsat-5 Collection 1 products in the Copernicus Data Space Ecosystem originate from the ESA processing. For more information please visit [here](https://earth.esa.int/eogateway/missions/landsat).

Landsat-5 was launched on 1 March 1984 and ended its mission on 5 June 2013. It carried the Thematic Mapper (TM), a multispectral scanning radiometer operating in the visible and infrared regions of the electromagnetic spectrum. It was characterized by 185 km swath width and 30 m resolution for visible (VIS), near infrared (NIR) and shortwave infrared (SWIR), and 120 m for thermal infrared (TIR). The acquired Landsat TM scene covers an area of approximately 183 km x 172.8 km. A standard full scene is nominally centred on the intersection of a path and a row (the actual image centre can vary by up to 100 m). A full image consists of 6920 pixels x 5760 lines and each uncompressed band in the VIS, NIR, SWIR and TIR spectral regions requires 40 MB of storage space.

The objective of Landsat-5 and every Landsat mission has been to repeatedly image Earth’s land and coastal areas in order to monitor changes to these areas over time.

Access to Landsat-5 data is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27LANDSAT-5%27`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27LANDSAT-5%27)

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on:

• [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-1

## Landsat-5 TM-L1G

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/landsat-tm-esa-archive)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27LANDSAT-5%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27L1G%27))))

![](https://img.shields.io/badge/Update_Frequency-Archived%20dataset-0A4393)

#### Overview

Landsat-5 TM-L1G stands for Landsat-5 Thematic Mapper Level-1 Ground data. The data is calibrated and corrected to remove distortions, and then orthorectified to provide systematic geometric accuracy. It is widely used for environmental monitoring, land-use mapping, and natural resource management.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent     | Origin |
|--------------|----------------|----------------|---------------------|--------|
| TM\_\_GEO_1P | Unpacked       | Europe         | Apr 1984 - Nov 2011 | ESA    |

Further details about the data collection

  

##### Useful Links

- Source: [https://landsat-diss.eo.esa.int/socat/LandsatTM](https://landsat-diss.eo.esa.int/socat/LandsatTM)
- More Information: [https://earth.esa.int/eogateway/catalog/landsat-tm-esa-archive](https://earth.esa.int/eogateway/catalog/landsat-tm-esa-archive)

## Landsat-5 TM-L1T

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/landsat-tm-esa-archive)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27LANDSAT-5%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27L1T%27))))

![](https://img.shields.io/badge/Update_Frequency-Archived%20dataset-0A4393)

#### Overview

Landsat-5 TM-L1T stands for Landsat-5 Thematic Mapper Level-1 Terrain corrected data. The Level-1 terrain-corrected data refer to the correction of the topographic displacement effects in the images, also known as relief displacement or parallax. The L1T processing level provides more precise geolocation information, which is particularly important for applications such as land-cover mapping and change detection. This product allows for more accurate and consistent image interpretation and analysis, making it a valuable tool for scientific research and environmental management.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent     | Origin |
|--------------|----------------|----------------|---------------------|--------|
| TM\_\_GTC_1P | Unpacked       | Europe         | Apr 1984 - Nov 2011 | ESA    |

Further details about the data collection

  

##### Useful Links

- Source: [https://landsat-diss.eo.esa.int/socat/LandsatTM](https://landsat-diss.eo.esa.int/socat/LandsatTM)
- More Information: [https://earth.esa.int/eogateway/catalog/landsat-tm-esa-archive](https://earth.esa.int/eogateway/catalog/landsat-tm-esa-archive)
