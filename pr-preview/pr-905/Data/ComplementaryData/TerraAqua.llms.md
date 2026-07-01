# TerraAqua

TerraAqua is a collection created for MCD products which represent Terra+Aqua combined MODIS datasets, designed to maximize angular sampling, reduce cloud contamination, and improve temporal consistency. MCD products use reflectances and ancillary information from both MODIS instruments, enabling higher-quality BRDF (The Bidirectional Reflectance Distribution Function), albedo, reflectance, and land parameter retrievals compared to single platform MODIS datasets (MOD from Terra or MYD from Aqua). The combined approach leverages Terra’s 10:30 a.m. descending node and Aqua’s 1:30 p.m. ascending node to achieve wider angular coverage, more frequent observation opportunities, and more robust inversion of surface bidirectional reflectance. Access to TerraAqua datasets is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'TERRAAQUA'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'TERRAAQUA')

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, tiles etc. please, follow instructions on:

• [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-3

Level-4

## Terra+Aqua MODIS Land Cover Type Yearly Global 500m - MCD12Q1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1409/MCD12_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRAAQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MCD12Q1.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20year-0A4393)

#### Overview

The MCD12Q1.061 dataset provides a global land‑cover map updated each year at a spatial resolution of 500 metres. The dataset is produced by applying supervised classification methods to reflectance measurements from both the Terra and Aqua MODIS sensors. The product delivers land‑cover information according to several established global legends, vegetation characteristics based on leaf‑area index, biogeochemical vegetation types, and plant functional types. After classification, additional refinement steps incorporate prior knowledge and auxiliary data to improve class accuracy.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MCD12Q1.061 | Unpacked       | World          | Jan 2001 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd12q1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd12q1-061)

## Terra+Aqua MODIS Leaf Area Index/FPAR 8-Day Global 500m - MCD15A2H.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRAAQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MCD15A2H.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MCD15A2H.061 product provides an eight‑day composite of vegetation characteristics at 500‑metre resolution, combining observations from both the Terra and Aqua MODIS sensors. For each pixel, the algorithm selects the highest‑quality observation available during the eight‑day period. The dataset includes two key indicators of vegetation structure and function:Leaf area index (LAI), which describes the amount of green leaf surface area relative to the ground area beneath it and fraction of photosynthetically active radiation (FPAR), representing the proportion of sunlight in the photosynthetically active range that is absorbed by the canopy. These measurements support assessments of vegetation density, productivity, and energy absorption across a range of ecosystems.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|--------------|----------------|----------------|--------------------|--------|
| MCD15A2H.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd15a2h-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd15a2h-061)

## Terra+Aqua MODIS Leaf Area Index/FPAR 4-Day Global 500m - MCD15A3H.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRAAQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MCD15A3H.061'))))

![](https://img.shields.io/badge/Update_Frequency-4%20days-0A4393)

#### Overview

Similar to the MCD15A2H.061 product, the MCD15A3H.061 dataset provides a composite of vegetation structural and functional properties (LAI and FPAR indicators) at a spatial resolution of 500 metres. It combines observations from both the Terra and Aqua MODIS sensors and selects the highest‑quality measurement available within each four‑day period.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|--------------|----------------|----------------|--------------------|--------|
| MCD15A3H.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd15a3h-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd15a3h-061)

## Terra+Aqua MODIS BRDF/Albedo Nadir BRDF-Adjusted Daily Global 500m - MCD43A4.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://www.umb.edu/spectralmass/modis-user-guide-v006-and-v0061/mcd43a4-nbar-product/)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRAAQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MCD43A4.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20day-0A4393)

#### Overview

The MCD43A4.061 product provides daily surface reflectance corrected for viewing‑angle effects, offering a consistent nadir‑equivalent reflectance for MODIS spectral bands 1 through 7 at a spatial resolution of 500 metres. Each daily file is generated using a 16‑day rolling window of combined Terra and Aqua observations, with the retrieval weighted toward the ninth day of the period, which is reflected in the file’s Julian date. Each file includes nadir Bidirectional Reflectance Distribution Function(BRDF)‑adjusted reflectance values for MODIS land surface bands and a simplified mandatory quality layer.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MCD43A4.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd43a4-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd43a4-061)

## Terra+Aqua MODIS Direct Broadcast Burned Area Monthly Global 500m - MCD64A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1006/MCD64_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRAAQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MCD64A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20month-0A4393)

#### Overview

The combined MODIS MCD64A1.061 dataset provides a monthly global map of areas affected by fire at a spatial resolution of 500 metres. Each pixel contains information on whether burning occurred, the approximate day of burning within the month, and indicators describing the reliability of the detection. Burned areas are identified by combining 500-metre surface-reflectance data with active-fire detections from the MODIS thermal‑anomaly product. The algorithm uses a vegetation-based index that is sensitive to burn scars and applies dynamic thresholds to detect rapid spectral changes associated with fire. This index is derived from short-wave infrared reflectance and includes measures of temporal variability to improve detection accuracy. The dataset includes the estimated day of burning, the uncertainty associated with that estimate, a quality-assessment layer, and information identifying the first and last days within the year when reliable change detection was possible. Pixels that remain unburned, contain missing data, or represent water bodies are assigned specific coded values. The MCD64A1.061 enables consistent monthly assessments of fire-affected areas and supports analyses of fire behaviour, carbon emissions, land-cover change, and ecosystem recovery across regions and seasons.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MCD64A1.061 | Unpacked       | World          | Nov 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061)
