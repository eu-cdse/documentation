# Terra

Terra (also called EOS AM 1) is the first NASA’s flagship Earth observing platform within the Earth Observing System (EOS), launched on 18 December 1999 into a sun synchronous, near polar orbit at ~705 km altitude with a 10:30 a.m. descending node. It is designed to observe and quantify interactions among the atmosphere, land, cryosphere, and oceans, providing long term global measurements for climate research, environmental monitoring, and hazard assessment. Terra carries five complementary sensors, contributed internationally by the United States, Japan, and Canada. Although designed for a 6 year mission, Terra has operated successfully for more than 26 years. It remains operational in an extended mission phase as of 2026. In CDSE we have gathered the data from MODIS (Moderate Resolution Imaging Spectroradiometer), a 36 band multispectral scanner that measures visible to thermal infrared radiances for atmosphere, land, and ocean monitoring. MODIS provides 250 m, 500 m and 1 km spatial resolutions and a 2,300 km swath for near daily coverage. Access to Terra MODIS datasets is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'TERRA'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'TERRA')

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on:

• [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-3

Level-4

## Terra MODIS Surface Reflectance 8-Day Global 500m - MOD09A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD09A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The Terra MODIS MOD09A1.061 dataset provides an eight‑day composite of surface spectral reflectance for MODIS Bands 1–7 at a spatial resolution of 500 metres. The reflectance values are corrected for atmospheric effects, including gases, aerosols, and Rayleigh scattering, to better represent the true surface signal. For each pixel, the algorithm selects the best available observation from all Terra overpasses within the eight‑day period. The selection process prioritizes measurements acquired under clear‑sky conditions and favourable viewing geometry. If multiple observations meet these criteria, the pixel with the lowest blue‑band (Band 3) reflectance is chosen to minimize residual atmospheric contamination.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD09A1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod09a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod09a1-061)

## Terra MODIS Surface Reflectance 8-Day Global 250m - MOD09Q1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD09Q1.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD09Q1.061 product provides an eight‑day composite of surface spectral reflectance for MODIS Bands 1 and 2 at a spatial resolution of 250 metres. Like MOD09A1.061, the reflectance values are corrected for atmospheric effects such as gases, aerosols, and Rayleigh scattering, ensuring that the dataset represents surface properties rather than atmospheric influence.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD09Q1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod09q1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod09q1-061)

## Terra MODIS Snow Cover Daily Global 500m - MOD10A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://nsidc.org/sites/default/files/mod10a1-v061-userguide_1.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD10A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20day-0A4393)

#### Overview

The Terra MODIS MOD10A1.061 dataset provides a daily composite of snow‑cover extent and albedo generated from the level-2 (MOD10_L2.061) product. Each output file corresponds to a 10° × 10° tile, mapped to a sinusoidal grid at 500‑meter resolution.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD10A1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-mod10a1-61](https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-mod10a1-61)

## Terra MODIS Snow Cover 8-Day Global 500m - MOD10A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://nsidc.org/sites/default/files/mod10a2-v061-userguide_0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD10A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD10A2.061 Level‑3 global product provides the maximum snow‑cover extent observed over each eight‑day period at a spatial resolution of 500 metres. The data are delivered in 10° × 10° tiles using the MODIS sinusoidal grid. Each tile is created by compositing daily snow‑cover observations from the MOD10A1.061 dataset. For every pixel, a bit‑flag record preserves the full eight‑day snow/no‑snow history, allowing users to assess both the presence and persistence of snow cover.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD10A2.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-mod10a2-61](https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-mod10a2-61)

## Terra MODIS Land Surface Temperature/Emissivity Daily Global 1km - MOD11A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD11A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20day-0A4393)

#### Overview

The MOD11A1.061 product provides daily measurements of land‑surface temperature and emissivity at a spatial resolution of 1 kilometer, using data from the Terra MODIS instrument. Each file covers a 1,200 × 1,200 kilometer tile and includes both daytime and nighttime temperature layers.The surface‑temperature values are derived from the corresponding Level‑2 swath observations. In areas above 30 degrees latitude, a single location may be observed more than once per day under clear‑sky conditions; when this occurs, the dataset reports the average of all valid observations. In addition to temperature and emissivity, the product provides quality‑assessment information, observation times, viewing‑angle data, clear‑sky coverage, and emissivity values derived from land‑cover characteristics in key thermal‑infrared channels.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD11A1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod11a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod11a1-061)

## Terra MODIS Land Surface Temperature/Emissivity 8-Day Global 1km - MOD11A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD11A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD11A2.061 dataset provides an eight‑day composite of land‑surface temperature and emissivity at a spatial resolution of 1 kilometer using observations from the Terra MODIS instrument. Like the daily MOD11A1.061 product, it delivers both daytime and nighttime temperature fields along with supporting metadata, but with reduced noise and improved temporal consistency. While both products include similar temperature, emissivity, and quality‑related layers, MOD11A2.061 provides fewer individual observations but greater temporal stability. Each eight‑day tile is generated by calculating the simple average of all clear‑sky MOD11A1.061 observations within the period. The dataset includes quality‑assessment information, observation times, view‑geometry data, clear‑sky coverage, and emissivity values derived from thermal‑infrared channels associated with land‑cover characteristics.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD11A2.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod11a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod11a2-061)

## Terra MODIS Vegetation Indices 16-Day Global 500m - MOD13A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD13A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

The MOD13A1.061 dataset provides 16‑day composites of vegetation‑index information at a spatial resolution of 500 metres. It includes two key indicators of vegetation condition: the normalized difference vegetation index (NDVI), which continues the long‑term global vegetation record established by earlier satellite missions, and the enhanced vegetation index (EVI), which is designed to improve sensitivity in densely vegetated areas. For each 16‑day period, the algorithm selects the highest‑quality observation available for every pixel. The selection prioritises clear‑sky conditions, favourable viewing geometry, and the strongest vegetation‑index signal. This approach reduces atmospheric noise and improves temporal consistency in the vegetation record.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD13A1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13a1-061)

## Terra MODIS Vegetation Indices 16-Day Global 1km - MOD13A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD13A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

The MOD13A2.061 product provides 16‑day vegetation‑index composites at a spatial resolution of 1 kilometre, offering broader‑scale coverage compared to the finer 500‑metre MOD13A1.061 product. It includes the same two core vegetation indicators: the normalized difference vegetation index (NDVI), which extends the long‑term global vegetation record from earlier satellite missions, and the enhanced vegetation index (EVI), which improves sensitivity in regions with dense canopy cover.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD13A2.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13a2-061)

## Terra MODIS Vegetation Indices 16-Day Global 250m - MOD13Q1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD13Q1.061'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

The MOD13Q1.061 dataset provides 16‑day composites of vegetation‑index information at a 250‑metre spatial resolution. Like the MOD13A1.061 and MOD13A2.061, it includes two core vegetation indicators: NDVI and EVI. Its mapping at 250 m is ideal for landscape‑level and heterogeneous environments analysis.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD13Q1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13q1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod13q1-061)

## Terra MODIS Thermal Anomalies/Fire Daily Global 1km - MOD14A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD14A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD14A1.061 dataset provides eight consecutive days of fire‑detection information from the Terra MODIS instrument, delivered as a single Level‑3 file at 1‑kilometre spatial resolution. Although classified as a daily product, each file contains per‑pixel fire information for all eight days of the acquisition period. Each file includes daily layers for:fire mask (fire/no‑fire classification), detection‑quality indicators, maximum fire‑radiative power recorded for each pixel, pixel‑scan position for contextual interpretation. These layers allow users to assess fire occurrence, confidence, and intensity across the full eight‑day interval.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD14A1.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a1-061)

## Terra MODIS Thermal Anomalies/Fire 8-Day Global 1km - MOD14A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD14A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD14A2.061 product provides an eight‑day composite of fire‑detection information from the Terra MODIS instrument at a spatial resolution of 1 kilometer. Each Level‑3 file represents the maximum fire‑detection class recorded for every pixel during the eight‑day period, offering a simplified summary of fire activity.While MOD14A1.061 delivers daily fire layers packaged into an eight‑day file, MOD14A2.061 condenses those observations by selecting the maximum fire class detected for each pixel across the entire compositing window. This aggregation reduces noise and highlights the highest‑confidence or most intense fire detection observed.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD14A2.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod14a2-061)

## Terra MODIS Leaf Area Index/FPAR 8-Day Global 500m - MOD15A2H.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD15A2H.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD15A2H Version 6.1 product provides an eight‑day composite of vegetation structural and functional properties at a spatial resolution of 500 metres. The dataset combines observations from the Terra MODIS sensor and selects the highest‑quality measurement available within each eight‑day period.The product includes two key vegetation variables: leaf area index (LAI), describing the amount of green leaf surface area relative to the ground area it covers and fraction of photosynthetically active radiation (FPAR), representing the proportion of sunlight in the photosynthetically active range absorbed by the plant canopy layer.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|--------------|----------------|----------------|--------------------|--------|
| MOD15A2H.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod15a2h-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod15a2h-061)

## Terra MODIS Net Evapotranspiration Gap-Filled 8-Day Global 500m - MOD16A2GF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/931/MOD16_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD16A2GF.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD16A2GF.061 dataset provides an eight‑day composite of evapotranspiration and latent‑heat flux at a spatial resolution of 500 metres. It is produced as a year‑end, gap‑filled dataset, offering improved spatial completeness and data quality compared to the standard MOD16 series. Low‑quality or missing leaf‑area and absorbed‑radiation values are replaced through interpolation, resulting in a more stable and spatially complete dataset. Because of this annual processing step, the product is not available in near‑real time.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| MOD16A2GF.061 | Unpacked       | World          | Jan 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod16a2gf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod16a2gf-061)

## Terra MODIS Net Evapotranspiration Gap-Filled Yearly Global 500m - MOD16A3GF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/931/MOD16_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD16A3GF.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20year-0A4393)

#### Overview

The MOD16A3GF.061 product provides a yearly, gap‑filled composite of evapotranspiration and latent‑heat flux at 500 m resolution. It represents the annual summary of the MOD16 series and delivers spatially complete estimates of land–atmosphere water and energy exchange. Each MOD16A3GF.061 file includes: annual evapotranspiration (sum), annual potential evapotranspiration (sum), annual latent‑heat flux (average), annual potential latent‑heat flux (average), a quality‑control layer.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| MOD16A3GF.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod16a3gf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod16a3gf-061)

## Terra MODIS Gross Primary Productivity 8-Day Global 500m - MOD17A2H.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD17A2H.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD17A2H.061 product provides an eight‑day composite of vegetation productivity at a spatial resolution of 500 metres. It includes estimates of gross primary productivity (GPP)—the total amount of carbon fixed by vegetation through photosynthesis—and net photosynthesis (PSN), which represents the remaining carbon after subtracting the plants’ basic respiratory requirements.The dataset is based on the radiation‑use‑efficiency framework, which models how effectively vegetation converts absorbed sunlight into chemical energy. For each eight‑day period, the product accumulates all valid daily productivity estimates. Net photosynthesis is calculated by subtracting maintenance respiration from the gross productivity estimate.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|--------------|----------------|----------------|--------------------|--------|
| MOD17A2H.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod17a2h-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod17a2h-061)

## Terra MODIS Gross Primary Productivity Gap-Filled 8-Day Global 500m - MOD17A2HGF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD17A2HGF.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD17A2HGF.061 dataset provides an eight‑day composite of vegetation productivity at a spatial resolution of 500 metres. It includes gross primary productivity—the total amount of carbon fixed by vegetation through photosynthesis—and net photosynthesis, which subtracts the plants’ maintenance respiration from gross productivity. The gap‑filled version improves spatial completeness and quality compared to the standard MOD17A2H.061 product.

##### Offered Data

| Product        | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------------|----------------|----------------|--------------------|--------|
| MOD17A2HGF.061 | Unpacked       | World          | Jan 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod17a2hgf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod17a2hgf-061)

## Terra MODIS Net Primary Production Gap-Filled Yearly Global 500m - MOD17A3HGF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD17A3HGF.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20year-0A4393)

#### Overview

The Terra MODIS MOD17A3HGF.061 product provides annual estimates of vegetation productivity at a spatial resolution of 500 metres. It reports both gross primary production (GPP) and net primary production (NPP), which subtracts the carbon respired by the plants throughout the year.Annual values are generated by summing all eight‑day productivity estimates (MOD17A2H.061) for the entire year. Net primary production is calculated as the difference between gross productivity and maintenance respiration.The gap‑filled version is produced once all eight‑day vegetation inputs (MOD15A2H.061) for the year become available. Low‑quality or missing vegetation parameters are replaced through interpolation based on quality information from the input data. This results in a cleaner, more spatially complete productivity dataset. Because this process requires full‑year inputs, MOD17A3HGF.061 is available only at year‑end, not in near‑real time.

##### Offered Data

| Product        | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------------|----------------|----------------|--------------------|--------|
| MOD17A3HGF.061 | Unpacked       | World          | Jan 2001 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod17a3hgf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod17a3hgf-061)

## Terra MODIS Land Surface Temperature/3-Band Emissivity 8-Day Global 1km - MOD21A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1398/MOD21_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'TERRA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MOD21A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MOD21A2.061 product is an eight‑day Level‑3 composite generated by averaging all cloud‑free daily daytime (MOD21A1D) and nighttime (MOD21A1N) observations within the compositing period. Each file includes separate day and night layers for: land‑surface temperature, quality information, view‑angle and observation‑time metadata. Emissivity in bands 29, 31, and 32 is reported as the average of day and night retrievals. All information is stored in a single file using the HDF format.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MOD21A2.061 | Unpacked       | World          | Feb 2000 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod21a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod21a2-061)
