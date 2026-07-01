# Soil Moisture and Ocean Salinity (SMOS)

The Soil Moisture and Ocean Salinity (SMOS) mission was launched on 2 November 2009. It is one of the European Space Agency’s Earth Explorer missions, which form the science and research element of ESA’s Living Planet Programme.

The SMOS payload consists of the Microwave Imaging Radiometer using Aperture Synthesis (MIRAS) instrument, a passive microwave 2-D interferometric radiometer operating in the L-band (1.413 GHz, 21 cm) within a protected wavelength/frequency band. The SMOS mission operates on a sun-synchronous orbit (dusk-dawn 6am/6pm). SMOS measurements are made over a range of incidence angles (0 to 55°) across a swath of approximately 1000 km with a spatial resolution of 35 to 50 km. MIRAS can provide measurements in dual and full polarisation, the latter being its current mode of operation.

SMOS Level 1 data products are designed for scientific and operational users who need to work with calibrated MIRAS instrument measurements, while SMOS Level 2 data products are designed for scientific and operational users who need to work with geo-located estimates of soil moisture and sea surface salinity as retrieved from the Level 1 dataset.

Access to SMOS data is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SMOS%27`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SMOS%27)

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on:

• [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-1

Level-2

## Soil Moisture and Ocean Salinity - L1B

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/smos-science-products)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27processingLevel%27%20and%20i0/Value%20eq%20%271B%27))))

![](https://img.shields.io/badge/Update_Frequency-%3C1%20day-0A4393)

#### Overview

Soil Moisture and Ocean Salinity - L1B are processed data of the SMOS mission. These are geolocated brightness temperatures that have been calibrated and corrected to provide valuable input for further processing into higher-level products like soil moisture and ocean salinity maps.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent | OData |
|----|----|----|----|----|
| MIR_SC_F1B | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_SC_F1B%27)))) |
| MIR_SC_D1B | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_SC_D1B%27)))) |

Further details about the data collection

  

##### Useful Links

- Source: [https://smos-diss.eo.esa.int/oads/access/](https://smos-diss.eo.esa.int/oads/access/)
- More Information: [https://earth.esa.int/eogateway/missions/smos#instruments-section](https://earth.esa.int/eogateway/missions/smos#instruments-section)

## Soil Moisture and Ocean Salinity - L1CL

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/smos-science-products)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27processingLevel%27%20and%20i0/Value%20eq%20%27other:%201C%27))))

![](https://img.shields.io/badge/Update_Frequency-%3C1%20day-0A4393)

#### Overview

The Soil Moisture and Ocean Salinity (SMOS) The L1CL product is an intermediate SMOS soil moisture and ocean salinity product that is used as input to generate other higher-level SMOS products such as L2 soil moisture and ocean salinity products, which combine SMOS data with other satellite and ground-based observations.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent | OData |
|----|----|----|----|----|
| MIR_BWLF1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_BWLF1C%27)))) |
| MIR_BWLD1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_BWLD1C%27)))) |
| MIR_BWSF1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_BWSD1C%27)))) |
| MIR_BWSD1C - SCLD1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_BWSD1C%27)))) |

Further details about the data collection

  

##### Useful Links

- Source: [https://smos-diss.eo.esa.int/oads/access/](https://smos-diss.eo.esa.int/oads/access/)
- More Information: [https://earth.esa.int/eogateway/missions/smos#instruments-section](https://earth.esa.int/eogateway/missions/smos#instruments-section)

## Soil Moisture and Ocean Salinity - L1CS

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/smos-science-products)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27processingLevel%27%20and%20i0/Value%20eq%20%27other:%201C%27))))

![](https://img.shields.io/badge/Update_Frequency-%3C1%20day-0A4393)

#### Overview

SMOS L1CS is an intermediate product that measures soil moisture and ocean salinity derived from raw data collected by the microwave radiometer onboard the SMOS satellite. It has a spatial resolution of 40 km and provides brightness temperatures and scattering angles to calculate the essential values for understanding the global water cycle. The data is useful for weather forecasting, drought monitoring, crop management, and coastal ecosystem protection. The product is used to generate higher-level SMOS products to manage water resources and monitor ecological systems.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent | OData |
|----|----|----|----|----|
| MIR_SCLF1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_SCLF1C%27)))) |
| MIR_SCLD1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_SCLD1C%27)))) |
| MIR_SCSF1C/MIR_SCSD1C | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_SCSD1C%27)))) |

Further details about the data collection

  

##### Useful Links

- Source: [https://smos-diss.eo.esa.int/oads/access/](https://smos-diss.eo.esa.int/oads/access/)
- More Information: [https://earth.esa.int/eogateway/missions/smos#instruments-section](https://earth.esa.int/eogateway/missions/smos#instruments-section)

## Soil Moisture and Ocean Salinity - L2OS

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/smos-science-products)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27processingLevel%27%20and%20i0/Value%20eq%20%272%27))))

![](https://img.shields.io/badge/Update_Frequency-%3C1%20day-0A4393)

#### Overview

The SMOS L1OS product is an intermediate data product derived from the raw data collected by the microwave radiometer on board the SMOS satellite. It is used to derive higher-level SMOS products, such as L2 soil moisture and ocean salinity products, which are used for various applications, including weather forecasting, climate monitoring, agricultural planning, and water management. The SMOS L1OS data product is important for understanding the earth’s water cycle and the impacts of climate change on water resources. The data is used by scientists, policymakers, and resource managers to better understand and manage water resources, monitor ecological systems, and improve weather and climate forecasting.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent | OData |
|----|----|----|----|----|
| MIR_OSUDP2 | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_OSUDP2%27)))) |

Further details about the data collection

  

##### Useful Links

- Source: [https://smos-diss.eo.esa.int/oads/access/](https://smos-diss.eo.esa.int/oads/access/)
- More Information: [https://earth.esa.int/eogateway/missions/smos#instruments-section](https://earth.esa.int/eogateway/missions/smos#instruments-section)

## Soil Moisture and Ocean Salinity - L2SM

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://earth.esa.int/eogateway/catalog/smos-science-products)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27processingLevel%27%20and%20i0/Value%20eq%20%272%27))))

![](https://img.shields.io/badge/Update_Frequency-%3C1%20day-0A4393)

#### Overview

The Level 2 Soil Moisture (SM) product comprises soil moisture measurements geo-located in an equal-area grid system ISEA 4H9. The product contains not only the retrieved soil moisture, but also a series of ancillary data derived from the processing (nadir optical thickness, surface temperature, roughness parameter, dielectric constant and brightness temperature retrieved at top of atmosphere and on the surface) with the corresponding uncertainties.

##### Offered Data

| Product | Archive Status | Spatial Extent | Temporal Extent | OData |
|----|----|----|----|----|
| MIR_SMUDP2 | Unpacked | World | Jan 2010 - Present | [OData](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20%27SMOS%27)%20and%20(Attributes/OData.CSC.StringAttribute/any(i0:i0/Name%20eq%20%27productType%27%20and%20i0/Value%20eq%20%27MIR_SMUDP2%27)))) |

Further details about the data collection

  

##### Useful Links

- Source: [https://smos-diss.eo.esa.int/oads/access/](https://smos-diss.eo.esa.int/oads/access/)
- More Information: [https://earth.esa.int/eogateway/missions/smos#instruments-section](https://earth.esa.int/eogateway/missions/smos#instruments-section)
