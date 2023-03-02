# Sentinel 1


## Description
The [Sentinel-1 radar imaging mission](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1) is composed of a constellation of two polar-orbiting satellites providing continous all-weather, day and night imagery for Land and Maritime Monitoring. C-band synthentic aperture radar imaging has the advantage of operating at wavelenghts that are not obstructed by clouds or lack of illumination and therefore can acquire data during day or night under all weather conditions. With 6 days repeat cycle on the entire world and daily acquistions of sea ice zones and Europe's major shipping routes, Sentinel-1 ensures reliable data availability to support emergency services and applications requiring time series observations.

**The end of mission of the Sentinel-1B satellite has been declared in July 2022**
<br>On 23 December 2021, Copernicus Sentinel-1B experienced an anomaly related to the instrument electronics power supply provided by the satellite platform, leaving it unable to deliver radar data. Despite all investigations and recovery attempts, ESA and the European Commission had to announce that it is the end of the mission for Sentinel-1B. Copernicus Sentinel-1A remains fully operational. More information about the end of the mission for the Sentinel-1B satellite can be found on the webpage [Mission ends for Copernicus Sentinel-1B satellite](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/Mission_ends_for_Copernicus_Sentinel-1B_satellite).
<br>In response to the loss of Sentinel-1B, **the mission observation scenario of Sentinel-1A was adjusted**, affecting the nominal global coverage frequency. An up-to-date overview of the observation scenario in place can be consulted on the webpage [Sentinel-1 Observation Scenario](https://sentinel.esa.int/web/sentinel/missions/sentinel-1/observation-scenario). Some regions are currently not observed by Sentinel-1. All regions that are still observed now have a repeat cycle of 12 under a one-satellite constellation scenario, which affects possible interferometric analyses.


Sentinel data products are made available systematically and free of charge to all data users including the general public, scientific and commercial users. 

[Data products](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-1/data-products) are available in single polarisation for Wave mode and dual polarisation or single polarisation for SM, IW and EW modes.

The table below indicates for each type of user level product, the format in which the data will be available, the access type (IAD or DAD), the spatial and temporal extent of the offer and from when the data will be available in the Copernicus Data Space Ecosystem. 
The data offer will gradually extend starting from January 2023 (an “*” indicates a temporary offer that will change when the target service offer becomes available within July 2023). 

## Data Offer
### Already available (from January 2023)

|Product Type| File Description| Data Access Type | Spatial Extent | Temporal Extent | More Information | Available from |
|------------ | ---------------------- | ---------------------- | ------------ | ------------ | ------------| -----------|
|GRD | packed or unpacked | IAD (Immediately available data) | World | Oct-14 - Present| [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23(*)|
|OCN | packed or unpacked | IAD | World | Dec-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-2)| Jan-23(*)|
|SLC | packed or unpacked | IAD | Europe | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23(*)|
|SLC | packed or unpacked | IAD | RoW (World with exception of Europe) | Feb-21 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23(*)|
|L0 (RAW) | packed or unpacked | IAD | World | Jan-21 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jan-23(*)|
|L0 (RAW) | packed | DAD | World | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jan-23(*)|

(*) temporary offer available until the target service offer becomes available in July 2023.

### Available from July 2023

|Product Type| File Description| Data Access Type | Spatial Extent | Temporal Extent | More Information | Available from |
|------------ | ---------------------- | ---------------------- | ------------ | ------------ | ------------| -----------|
|GRD | packed or unpacked, SAFE with Cloud Optimized GeoTIFF | IAD (Immediately available data) | World | Oct-14 - Present| [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|GRD | packed, original SAFE | IAD | World | Last 1 year| [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23
|GRD | packed, original SAFE | DAD (Deferred available data) | World | Oct-14 - Present-1 year| [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23||
|OCN | packed or unpacked | IAD | World | Dec-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-2)| Jan-23|
|SLC | packed or unpacked | IAD | World | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|L0 (RAW) | packed or unpacked | IAD | Europe | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jul-23|
|L0 (RAW) | packed or unpacked | IAD | RoW | Last 1 year | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jul-23|
|L0 (RAW) | packed | DAD | World | Oct-14 - Present-1 year | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jan-23(*)|



<!--|Product Type| File Description| Data Access Type | Spatial Extent | Temporal Extent | More Information | Available from |
|------------ | ---------------------- | ---------------------- | ------------ | ------------ | ------------| -----------|
|GRD | packed, original SAFE | IAD (Immediately available data) | World | Last 1 month | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23|
|GRD | unpacked, original SAFE | IAD | World | Jun-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23(*)|
|GRD | unpacked, SAFE with Cloud Optimized GeoTIFF | IAD | World | Jun-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|GRD | packed, original SAFE | IAD | World | Last 1 year | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|GRD | packed, original SAFE | DAD (Deferred available data) | World | Jun-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|OCN | packed | IAD | World | Last 1 month | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-2)| Jan-23|
|OCN | unpacked | IAD | World | Dec-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-2)| Jan-23|
|SLC | packed | IAD | Europe | Last 1 month | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23|
|SLC | unpacked | IAD | Europe | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23(*)|
|SLC | unpacked | IAD | RoW (World with exception of Europe) | Feb-21 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jan-23(*)|
|SLC | unpacked | IAD | World | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|SLC | packed | DAD | World | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-1)| Jul-23|
|L0 (RAW) | packed | IAD | World | Last 1 month | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jan-23|
|L0 (RAW) | unpacked | IAD | World | Jan-21 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jan-23(*)|
|L0 (RAW) | packed or unpacked | IAD | Europe | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jul-23|
|L0 (RAW) | packed or unpacked | IAD | RoW | Last 1 year| [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jul-23|
|L0 (RAW) | packed | DAD | World | Oct-14 - Present | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jan-23(*)|
|L0 (RAW) | packed | DAD | World | Oct-14 - Present - 1 year | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Jul-23|
|L0 (RFC) | packed | IAD | World | Last 2 weeks | [Details](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-1-sar/product-types-processing-levels/level-0)| Oct-23|

(*) temporary offer available until the target service offer becomes available in July 2023.-->