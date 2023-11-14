# STAC product catalog

**STAC** (SpatioTemporal Asset Catalog) is a relatively new web service specification for catalogs that is increasingly used and supported.

The Copernicus Data Space Ecosystem STAC API was implemented as a web service interface to query over a group of STAC collections held in a database. 
All fields included in Data Space API are consistent with the [STAC Specification](https://stacspec.org/en){target="_blank"}.

The service implements the STAC API version v1.0.0. The version exposed in the Copernicus Data Space Ecosystem is still subject to change as the quality of STAC metadata is still improving. Nevertheless, it already supports basic product search.

## Endpoint URL

The Copernicus Data Space Ecosystem STAC API Catalog can be accessed using the following URL:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac`](https://catalogue.dataspace.copernicus.eu/stac){target="_blank"}

:::

## Available Collections

The data are organized in so-called collections corresponding to various satellites.

The following collections are currently available via STAC API

* Copernicus Sentinel Mission
  * **SENTINEL-1**
  * **SENTINEL-2**
  * **SENTINEL-3**
  * **SENTINEL-5P**
  * **SENTINEL-6**
  * **SENTINEL-1-RTC** (Sentinel-1 Radiometric Terrain Corrected)

* Complementary data
  * **SMOS** (Soil Moisture and Ocean Salinity)
  * **ENVISAT** (ENVISAT- Medium Resolution Imaging Spectrometer - MERIS)
  * **LANDSAT-5**
  * **LANDSAT-7**
  * **LANDSAT-8**
  * **COP-DEM** (Copernicus DEM)
  * **TERRAAQUA** (Terra MODIS and Aqua MODIS)
  * **S2GLC** (S2GLC 2017)
  
## STAC Collections Search

STAC Collections endpoint enables users to get information about collections available in Copernicus Data Space Ecosystem Catalog. 

To access the information about all STAC API Collections:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections`](https://catalogue.dataspace.copernicus.eu/stac/collections){target="_blank"}

:::


To access the information about a specified STAC API Collection (e.g. SENTINEL-2):

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-2`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-2){target="_blank"}

:::


## STAC Items Search

Search for items is possible among all collections [Link](https://documentation.dataspace.copernicus.eu/APIs/STAC.html#items-search-in-all-stac-collections) or in one specified collection only [Link](https://documentation.dataspace.copernicus.eu/APIs/STAC.html#items-search-in-a-stac-collection).

::: {.callout-note}

To accelerate the query performance, it is recommended to search for Items within one specified collection e.g.:

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-3/items`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-3/items){target="_blank"}

:::

### Items Search in a STAC Collection

#### Search for items in a collection

To list items in a given collection:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items){target="_blank"}

:::

By default, the catalogue will automatically limit the number of shown items to 20. It can be changed by filtering with the limit option, which is described below [Link](https://documentation.dataspace.copernicus.eu/APIs/STAC.html#limit-option).

#### Search for specific item

To list a specific item in a collection:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items/S1A_IW_SLC__1SDV_20221231T100709_20221231T100736_046574_0594DE_0A58.SAFE`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items/S1A_IW_SLC__1SDV_20221231T100709_20221231T100736_046574_0594DE_0A58.SAFE){target="_blank"}

:::

#### Search for items by attributes

To list items with a given attribute:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2022-12-31T09:59:31.293Z/ `](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2022-12-31T09:59:31.293Z/ ){target="_blank"}

:::

Currently those attributes are supported:

* `bbox`
* `datetime`

##### Search Items by bbox

Attribute `bbox` will list all products from a given collection within the Area of Interest (AOI). This attribute requires between 4 and 6 values (coordinates) where each coordinate is separated by a comma.

To search for items by bbox:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?bbox=-80.673805,-0.52849,-78.060341,1.689651 `](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?bbox=-80.673805,-0.52849,-78.060341,1.689651 ){target="_blank"}

:::

##### Search Items by datetime

Attribute `datetime` will list all products within specified time interval.

To search for items within specified datetime:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2021-12-31T09:59:31.293Z/2023-12-31T09:59:31.293Z`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2021-12-31T09:59:31.293Z/2023-12-31T09:59:31.293Z){target="_blank"}

:::

Attribute `datetime` can search for several different formats:

* 2022-12-31T00:00:00Z
* 2022-12-31T00:00:00
* 2022-12-31T16:00:00-08:00
* 2022-12-31T00:00:00+01:00
* 2022-12-31T00:00:00.000Z
* 2022-12-31T00:00:00.000

`datatime` intervals:

* /2021-12-31T23:59:59Z (open start interval)
* 2021-12-31T23:59:59Z/ (open end interval)
* 2022-12-30T00:00:00Z/2022-12-31T23:59:59Z (closed interval)

Please keep in mind that those are example values and might not return anything if input.

#### Search Items by two or more attributes

To list items by two or more attributes:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?bbox=-80.673805,-0.52849,-78.060341,1.689651&datetime=2014-10-13T23:28:54.650Z`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?bbox=-80.673805,-0.52849,-78.060341,1.689651&datetime=2014-10-13T23:28:54.650Z){target="_blank"}

:::

#### Limit option

Limit option allows users to increase or decrease the number of items shown. 

The default value is set to 20.

The acceptable arguments for this option: Integer <0,1000>

To list a limited number of items:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2022-12-31T09:59:31.293Z/&limit=10`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2022-12-31T09:59:31.293Z/&limit=10){target="_blank"}

:::

#### Sortby option

Sortby option allows users to define the fields by which to sort results.

The acceptable arguments for this option are:

* `end_datetime`
* `start_datetime`
* `datetime`

To set the sort order the prefix should be added to sort parameter:

* **+** for ascending (in http standard **+** sign should be encoded with **%2B**)
* **-** for descending

If no prefix is provided, ascending order is assumed.

To sort items within specified collection:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2021-12-31T09:59:31.293Z/&sortby=-start_datetime`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2021-12-31T09:59:31.293Z/&sortby=-start_datetime){target="_blank"}

:::

#### Page option

Page option determines the page of results.

The acceptable arguments for this option: Integer <1,100>

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2022-12-31T09:59:31.293Z/&page=32`](https://catalogue.dataspace.copernicus.eu/stac/collections/SENTINEL-1/items?datetime=2022-12-31T09:59:31.293Z/&page=32){target="_blank"}

:::

### Items Search in all STAC Collections

If users user would like to list items from any collection, they can use /search option, which will search all collections.

To list items in any collection:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/search?`](https://catalogue.dataspace.copernicus.eu/stac/search?){target="_blank"}

:::


This endpoint enables searching with simple filtering by:

* collectionId
* `datetime`
* `bbox`

Also, the following options are supported:

* limit
* sortby
* page

#### Search by attributes

Listing by attributes and using the limit option works the same way as before:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/search?datetime=2021-03-27T08:33:38.949Z/&limit=10`](https://catalogue.dataspace.copernicus.eu/stac/search?datetime=2021-03-27T08:33:38.949Z/&limit=10){target="_blank"}

:::


Currently those attributes are available:

* `bbox`
* `datetime`

#### Search items for many collections

Using /search option allows the user to list more than one collection.

To list more than one collection:

::: {.panel-tabset}

# HTTP Request

[`https://catalogue.dataspace.copernicus.eu/stac/search?collections=SENTINEL-1,SENTINEL-2`](https://catalogue.dataspace.copernicus.eu/stac/search?collections=SENTINEL-1,SENTINEL-2){target="_blank"}

:::



