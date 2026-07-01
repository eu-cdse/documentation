# Aqua

Aqua is a NASA Earth‑observing satellite launched on May 4, 2002 as part of the Earth Observing System (EOS). Its primary objective is to study the Earth’s water cycle, including water in the atmosphere, on land, and in the oceans. The name Aqua comes from the Latin word for water and reflects the mission’s core scientific focus. Aqua carries six scientific instruments: AIRS – Atmospheric Infrared Sounder, AMSU A – Advanced Microwave Sounding Unit A, AMSR E – Advanced Microwave Scanning Radiometer for EOS, CERES – Cloud and the Earth’s Radiant Energy System, HSB – Humidity Sounder for Brazil (it failed early in the mission - February 5, 2003), MODIS – Moderate Resolution Imaging Spectroradiometer. MODIS is Aqua’s flagship imaging instrument, providing global, multispectral data used across atmosphere, land, cryosphere, and ocean science. It is one of the most widely used satellite sensors in the world. MODIS collects data in 36 spectral bands ranging from visible to thermal infrared, enabling the detection of a wide range of Earth surface and atmospheric features. Its spatial resolution varies by band: 250 m (bands 1–2), 500 m (bands 3–7), 1 km (bands 8–36). MODIS achieves global coverage every 1–2 days thanks to its 2,330 km swath. In CDSE catalogue we have gathered 17 product types which varies in temporal interval (daily, 8 day, 16 day, monthly, yearly, etc.), spatial extent and data provided.

Access to Aqua MODIS datasets is possible via API

## OData

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'AQUA'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20'AQUA')

In order to get access to data at specific processing level as well as specific product types, you are advised to use queries provided in each section below.

If it is required to customize query in respect to spatial and time coverage, satellite features etc. please, follow instructions on:

• [OData](https://documentation.dataspace.copernicus.eu/APIs/OData.html)

Level-3

Level-4

## Aqua MODIS Surface Reflectance 8-Day Global 500m - MYD09A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD09A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MODIS Aqua MYD09A1 Version 6.1 product delivers atmospherically corrected surface spectral reflectance for Aqua MODIS Bands 1–7, removing the effects of gases, aerosols, and Rayleigh scattering. In addition to the seven 500‑meter reflectance bands, the dataset includes a quality layer and four observation‑related bands. Each pixel in the 8‑day composite represents the best available observation selected from multiple acquisitions, prioritizing low cloud contamination and suitable solar zenith conditions; when several candidates satisfy these criteria, the pixel with the lowest Band 3 (blue) reflectance is chosen.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD09A1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd09a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd09a1-061)

## Aqua MODIS Surface Reflectance 8-Day Global 250m - MYD09Q1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/925/MOD09_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD09Q1.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD09Q1.061 data provide atmospherically corrected surface spectral reflectance for Aqua MODIS Bands 1 and 2 at 250 m resolution. In addition to the two reflectance bands, the dataset includes two quality‑assessment layers. For each pixel, the 8‑day composite selects the most suitable observation based on factors such as cloud conditions and solar zenith angle.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD09Q1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd09q1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd09q1-061)

## Aqua MODIS Snow Cover Daily Global 500m - MYD10A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://nsidc.org/sites/default/files/myd10a1-v061-userguide_0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD10A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20day-0A4393)

#### Overview

The MYD10A1.061 Level‑3 MODIS dataset provides a daily composite of snow‑cover extent and albedo generated from the level-2 (MYD10_L2.061) product. Each output file corresponds to a 10° × 10° tile, mapped to a sinusoidal grid at 500‑meter resolution.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD10A1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-myd10a1-61](https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-myd10a1-61)

## Aqua MODIS Snow Cover 8-Day Global 500m - MYD10A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://nsidc.org/sites/default/files/myd10a2-v061-userguide_0.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD10A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD10A2.061 Level‑3 MODIS product summarizes the maximum snow‑cover extent observed over an eight‑day period within each 10° × 10° MODIS sinusoidal tile. It is created by compositing 500 m observations from the MYD10A1.061 (see above) dataset. A bit‑flag index records the snow or no‑snow status for every 500 m pixel across the full eight‑day interval.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD10A2.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-myd10a2-61](https://www.earthdata.nasa.gov/data/catalog/nsidc-cprd-myd10a2-61)

## Aqua MODIS Land Surface Temperature/Emissivity Daily Global 1km - MYD11A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD11A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20day-0A4393)

#### Overview

The MODIS Aqua MYD09A1 Version 6.1 dataset provides a daily map of the temperature of the land surface and its emissivity, which describes how efficiently the surface emits thermal radiation. The information is calculated for every pixel at a spatial resolution of 1 kilometer, using a grid that covers an area of 1,200 by 1,200 kilometers. The surface temperature is derived from the corresponding Level‑2 swath data produced by the Aqua satellite sensor. In regions above 30 degrees latitude, a single pixel may be observed more than once per day under clear‑sky conditions. When this happens, the dataset reports the average temperature from all valid observations. Alongside the daytime and nighttime temperature layers, the product includes additional information such as quality assessment data, the time of each observation, the viewing angle of the sensor, clear‑sky coverage, and emissivity values calculated from land‑cover properties using the sensor’s thermal infrared bands.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD11A1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd11a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd11a1-061)

## Aqua MODIS Land Surface Temperature/Emissivity 8-Day Global 1km - MYD11A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD11A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

This MYD11A2.061 Aqua MODIS 8‑day product offers a multi‑day average, giving a more stable view of thermal conditions over time. The dataset contains temperature and emissivity values for every pixel at a spatial resolution of 1 kilometer, arranged in a grid measuring 1,200 by 1,200 kilometers, just like the daily version. Instead of using only one day of observations, each pixel in this 8‑day map represents the average of all valid land‑surface temperature measurements collected during that period from the corresponding daily dataset. This method smooths out daily fluctuations caused by clouds or limited visibility.As with the daily product, the dataset includes daytime and nighttime land‑surface temperature, along with supporting information: quality assessments, the time of the observations, the viewing angle of the sensor, clear‑sky coverage, and emissivity values based on land‑cover characteristics from the instrument’s thermal infrared bands.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD11A2.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd11a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd11a2-061)

## Aqua MODIS Vegetation Indices 16-Day Global 500m - MYD13A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD13A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

The Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) Vegetation Indices 16-Day (MYD13A1) Version 6.1 dataset provides measurements of plant condition for every 500‑meter pixel using data collected by the Aqua satellite sensor. It includes two main indicators. The first is the Normalized Difference Vegetation Index (NDVI), which continues the long‑term global vegetation record originally produced by earlier satellite instruments. The second is the Enhanced Vegetation Index (EVI), which is designed to respond more effectively in areas with dense vegetation. For each 16‑day cycle, the dataset selects the best observation available for every pixel. The selection process favors measurements taken under clear‑sky conditions, with minimal atmospheric interference and favorable viewing angles, and among the usable observations the one with the strongest vegetation‑index signal is selected.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD13A1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd13a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd13a1-061)

## Aqua MODIS Vegetation Indices 16-Day Global 1km - MYD13A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD13A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

The Aqua MODIS Vegetation Indices 16-Day (MYD13A2.061) dataset provides two primary vegetation layers: Normalized Difference Vegetation Index (NDVI) and Enhanced Vegetation Index (EVI), just like MYD13A1.061, however at 1 kilometer spatial resolution. The algorithm for this product chooses the best available pixel value from all the acquisitions from the 16 day interval. The criteria used for selection is low clouds, low view angle and the highest NDVI/EVI value.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD13A2.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd13a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd13a2-061)

## Aqua MODIS Vegetation Indices 16-Day Global 250m - MYD13Q1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/621/MOD13_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD13Q1.061'))))

![](https://img.shields.io/badge/Update_Frequency-16%20days-0A4393)

#### Overview

The Aqua MODIS MYD13Q1.061 products are generated every 16 days at 250 meter spatial resolution and also provide information regarding two commonly used vegetation indices: NDVI and EVI. The algorithm chooses the best available pixel value from all the acquisitions from the 16 day period based on low clouds, low view angle, and the highest values of NDVI or EVI indicators.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD13Q1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd13q1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd13q1-061)

## Aqua MODIS Thermal Anomalies/Fire Daily Global 1km - MYD14A1.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD14A1.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD14A1.061 dataset provides information on thermal anomalies and active fires detected by the Aqua satellite over an eight‑day period. Although it is called a “daily” product, each file actually contains data for eight consecutive days, grouped together into a single Level‑3 tile at a spatial resolution of 1 kilometer.The dataset includes several layers of information for each day within that eight‑day interval. These layers show where fires were detected, the quality of each detection, the highest measured fire‑radiative power for each pixel, and the location of the fire pixel within the instrument’s scan. Every layer provides one full set of per‑pixel observations for each of the eight days included in the composite.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD14A1.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a1-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a1-061)

## Aqua MODIS Thermal Anomalies/Fire 8-Day Global 1km - MYD14A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD14A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD14A2.061 (MODIS Thermal Anomalies and Fire 8-Day) gridded composite contains maximum value of individual fire pixel classes detected during the eight days of acquisition generated at 1 kilometer spatial resolution. The dataset includes layers showing where fires were detected and indicators describing the quality of each detection. These layers allow users to assess both the presence of fire activity and the confidence associated with each fire‑related observation.

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD14A2.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a2-061](www.earthdata.nasa.gov/data/catalog/lpcloud-myd14a2-061)

## Aqua MODIS Leaf Area Index/FPAR 8-Day Global 500m - MYD15A2H.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/926/MOD15_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD15A2H.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD15A2H.061 dataset provides an eight‑day summary of two measures that describe the structure and functioning of vegetation: leaf area index (LAI) and the fraction of photosynthetically active radiation (FPAR). Each pixel in the dataset represents an area of 500 meters by 500 meters, and for every eight‑day period the algorithm selects the highest‑quality observation collected by the Aqua satellite. Leaf area index describes how much green leaf surface exists within a given ground area. For broadleaf vegetation, it represents the total one‑sided green leaf area, while for needle‑leaf vegetation it is defined as half of the total needle surface area. The FPAR represents how much incoming light in the photosynthetically active range is absorbed by the green parts of the canopy. Together, these measurements provide insight into plant density, canopy structure, and the vegetation’s ability to capture energy from the sun.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|--------------|----------------|----------------|--------------------|--------|
| MYD15A2H.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd15a2h-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd15a2h-061)

## Aqua MODIS Net Evapotranspiration Gap-Filled Yearly Global 500m - MYD16A3GF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/931/MOD16_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD16A3GF.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20year-0A4393)

#### Overview

The MYD16A3GF.061 Aqua MODIS dataset provides a yearly summary of how much water evaporates from the land surface and how much heat is released in the process, calculated at a resolution of 500 meters. It is produced at the end of each year and includes only high‑quality input data, with missing or low‑quality values corrected through interpolation. The calculations use a physical model that combines daily weather information with satellite‑based observations of vegetation, land cover, and surface reflectance. The product contains yearly totals of evapotranspiration and potential evapotranspiration, as well as yearly average values of latent‑heat flux and potential latent‑heat flux.

##### Offered Data

| Product       | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|---------------|----------------|----------------|--------------------|--------|
| MYD16A3GF.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd16a3gf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd16a3gf-061)

## Aqua MODIS Gross Primary Productivity 8-Day Global 500m - MYD17A2H.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD17A2H.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD17A2H Version 6.1 Gross Primary Productivity (GPP) product is an eight‑day summary of how much carbon plants take in through photosynthesis. Each pixel represents an area of 500 meters and contains two key measurements: the total amount of carbon fixed by vegetation during the eight‑day period (GPP - Gross Primary Productivity), and the amount of carbon that remains after subtracting the plants’ basic respiratory needs (PSN - Net Photosynthesis). The product also includes a quality layer that allows users to judge the reliability of both measurements.

##### Offered Data

| Product      | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|--------------|----------------|----------------|--------------------|--------|
| MYD17A2H.061 | Unpacked       | World          | Jan 2021 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd17a2h-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd17a2h-061)

## Aqua MODIS Gross Primary Productivity Gap-Filled 8-Day Global 500m - MYD17A2HGF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD17A2HGF.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD17A2HGF Version 6.1 product provides an estimate of vegetation carbon uptake over eight‑day periods, expressed as gross primary productivity and net photosynthesis. The data are delivered at a spatial resolution of 500 metres and represent the amount of carbon fixed by plants through photosynthesis, along with the fraction remaining after subtracting plant respiration. The gap‑filled version ensures complete spatial coverage by correcting missing or low‑quality values in the input data.

##### Offered Data

| Product        | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------------|----------------|----------------|--------------------|--------|
| MYD17A2HGF.061 | Unpacked       | World          | Jan 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd17a2hgf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd17a2hgf-061)

## Aqua MODIS Net Primary Production Gap-Filled Yearly Global 500m - MYD17A3HGF.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD17A3HGF.061'))))

![](https://img.shields.io/badge/Update_Frequency-1%20year-0A4393)

#### Overview

The MYD17A3HGF.061 dataset provides yearly estimates of the amount of carbon fixed by vegetation through photosynthesis and the portion remaining after subtracting plant respiration. These measurements, reported at a spatial resolution of 500 metres, describe both gross primary production and net primary production for each calendar year.

##### Offered Data

| Product        | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|----------------|----------------|----------------|--------------------|--------|
| MYD17A3HGF.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd17a3hgf-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd17a3hgf-061)

## Aqua MODIS Land Surface Temperature/3-Band Emissivity 8-Day Global 1km - MYD21A2.061

[![User guide](https://img.shields.io/badge/-User_guide-77cc09.png)](https://lpdaac.usgs.gov/documents/1398/MOD21_User_Guide_V61.pdf)[![Catalog API:OData](https://img.shields.io/badge/-Catalog_API:OData-77cc09?style=flat.png)](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=((Collection/Name%20eq%20'AQUA')%20and%20(Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'instrumentShortName'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MODIS')%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20'productType'%20and%20att/OData.CSC.StringAttribute/Value%20eq%20'MYD21A2.061'))))

![](https://img.shields.io/badge/Update_Frequency-8%20days-0A4393)

#### Overview

The MYD21A2.061 is an 8‑day, Level‑3 composite of land surface temperature and emissivity at 1 km resolution from the Aqua MODIS instrument. Unlike the heritage MYD11 products, which use a split‑window approach, the MYD21 family applies the ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) Temperature/Emissivity Separation (TES) method to retrieve temperature and spectral emissivity simultaneously. The 8‑day composite averages all cloud‑free daily MYD21A1 daytime and nighttime observations within the period and stores them in one file (day and night layers separated).

##### Offered Data

| Product     | Archive Status | Spatial Extent | Temporal Extent    | Origin |
|-------------|----------------|----------------|--------------------|--------|
| MYD21A2.061 | Unpacked       | World          | Jul 2002 - Present | NASA   |

Further details about the data collection

  

##### Useful Links

- Source: [https://www.earthdata.nasa.gov/data](https://www.earthdata.nasa.gov/data)
- More Information: [https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd21a2-061](https://www.earthdata.nasa.gov/data/catalog/lpcloud-myd21a2-061)
