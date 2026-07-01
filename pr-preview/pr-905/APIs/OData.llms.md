# OData

OData is an SO/IEC approved, OASIS standard , which is based on https RESTful Application Programming Interfaces. It enables resources, which are identified by URLs and defined in a data model, to be created and edited using simple HTTPS messages. OData makes it possible to build REST-based data services that let Web clients publish and edit resources that are recognized by Uniform Resource Locators (URLs) and described in a data model using straightforward HTTPS messages.

## OData Products endpoint

> **TIP:**
>
> Crucial for the search performance is specifying the collection name. Example: Collection/Name eq ‘SENTINEL-3’
>
> The additional efficient way to accelerate the query performance is limiting the query by acquisition dates, e.g.: ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-21T00:00:00.000Z
>
> When searching for products and adding a wide range of dates to the query, e.g. from 2017 to 2023, we recommend splitting the query into individual years, e.g. from January 1, 2023 to December 31, 2023.

> **TIP:**
>
> To ensure efficient and permanent querying of the Copernicus Data Space Ecosystem Catalogue, it is highly recommended to utilize [OData Subscriptions](https://documentation.dataspace.copernicus.eu/APIs/Subscriptions.html). These subscriptions provide the most effective way to stay informed about newly added products in the catalogue.
>
> The primary objective of Subscription Services is to enable users to receive real-time notifications about relevant events occurring within the Copernicus Data Space Ecosystem Catalogue. Users can tailor their notifications by specifying filtering parameters in the subscription request.
>
> A dedicated section provides comprehensive information to guide users through the implementation process: [OData Subscriptions](https://documentation.dataspace.copernicus.eu/APIs/Subscriptions.html).

### Query structure

As a general note, the OData query consists of elements which in this documentation are called “options”. The interface supports the following search options:

- filter
- orderby
- top
- skip
- count
- expand

Search options should always be preceded with *\$* and consecutive options should be separated with *&*.

Consecutive filters within *filter* option should be separated with *and* or *or*. *Not* operator can also be used e.g.:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=not (Collection/Name eq 'SENTINEL-2') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T00:10:00.000Z&$orderby=ContentDate/Start&$top=100`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=not%20(Collection/Name%20eq%20%27SENTINEL-2%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T00:10:00.000Z&$orderby=ContentDate/Start&$top=100)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=not (Collection/Name eq 'SENTINEL-2') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T00:10:00.000Z&$orderby=ContentDate/Start&$top=100").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 1d42f2d3-2456-485f-a93e-92f08bdd5c51 | S1A_OPER_AUX_GNSSRD_POD\_\_20220510T020122_V2022... | /eodata/Sentinel-1/AUX/AUX_GNSSRD/2022/05/03/S... | None |
| 1 | 5c744d5c-c082-4a34-a181-81cde73cd25d | S1B_OPER_AUX_GNSSRD_POD\_\_20220510T023113_V2022... | /eodata/Sentinel-1/AUX/AUX_GNSSRD/2022/05/03/S... | None |
| 2 | 4a4ef482-84a2-551d-8086-e3de6d39c488 | S3B_SL_1_RBT\_\_\_\_20220503T000015_20220503T00031... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2022/05/03/S... | {'type': 'Polygon', 'coordinates': \[\[\[-29.448,... |

## Filter option

### Query by name

To search for a specific product by its exact name:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Name eq 'S1A_IW_GRDH_1SDV_20141031T161924_20141031T161949_003076_003856_634E.SAFE'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Name%20eq%20%27S1A_IW_GRDH_1SDV_20141031T161924_20141031T161949_003076_003856_634E.SAFE')

To search for Copernicus Contributing Mission (CCM) data:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Name eq 'SP07_NAO_MS4_2A_20210729T064948_20210729T064958_TOU_1234_90f0.DIMA'&$expand=Attributes`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Name%20eq%20%27SP07_NAO_MS4_2A_20210729T064948_20210729T064958_TOU_1234_90f0.DIMA%27&$expand=Attributes)

Alternatively *contains*, *endswith* and *startswith* can be used to search for products ending or starting with provided string. You should use *Collection/Name* filter even if it overlaps with *startswith* or *contains* clause.

### Query by list

In case a user desires to search for multiple products by name in one query, the POST method can be used:

**POST**

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products/OData.CSC.FilterList`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products/OData.CSC.FilterList)

**Request body**:

``` {json}
{
  "FilterProducts":
    [
     {"Name": "S1A_IW_GRDH_1SDV_20141031T161924_20141031T161949_003076_003856_634E.SAFE"},
     {"Name": "S3B_SL_1_RBT____20190116T050535_20190116T050835_20190117T125958_0179_021_048_0000_LN2_O_NT_003.SEN3"},
     {"Name": "xxxxxxxx.06.tar"}
    ]
 }
```

Two results are returned, as there is no product named xxxxxxxx.06.tar.

### Query Collection of Products

To search for products within a specific collection:

For Sentinel-2:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-2'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-2%27)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-2'").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 617cc4fb-bb72-4589-9ac7-c19a0d89ef2d | S2A_OPER_AUX_GNSSRD_POD\_\_20171211T090149_V2015... | /eodata/Sentinel-2/AUX/AUX_GNSSRD/2015/07/03/S... | None |
| 1 | 2d8eb355-3930-4a6f-b02c-f793773cb656 | S2A_OPER_AUX_GNSSRD_POD\_\_20171211T085826_V2015... | /eodata/Sentinel-2/AUX/AUX_GNSSRD/2015/06/27/S... | None |
| 2 | 5303fa53-2dd4-4ee2-b012-d123a2ccd0b4 | S2A_OPER_AUX_GNSSRD_POD\_\_20171211T085921_V2015... | /eodata/Sentinel-2/AUX/AUX_GNSSRD/2015/06/28/S... | None |

For Copernicus Contributing Missions (CCM):

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM'`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27CCM%27)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM'").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 70c20650-4621-40ee-9f29-41973e8ef96b | DEM1_SAR_DTE_90_20110204T132020_20141115T13303... | /eodata/CCM/COP-DEM_GLO-90-DTED/SAR_DTE_90_61F... | {'type': 'Polygon', 'coordinates': \[\[\[59.0, 68... |
| 1 | aabba86a-53ef-4c17-a673-ecda83e13203 | DEM1_SAR_DTE_90_20110204T091108_20131220T09231... | /eodata/CCM/COP-DEM_GLO-90-DTED/SAR_DTE_90_61F... | {'type': 'Polygon', 'coordinates': \[\[\[-58.0, -... |
| 2 | 00646e04-06e0-4462-9ef4-cf3128abda61 | PH1B_PHR_MS\_\_2A_20180920T141019_20180920T14102... | /eodata/CCM/VHR_IMAGE_2018/PHR_MS\_\_2A_E1F0/201... | {'type': 'Polygon', 'coordinates': \[\[\[-52.7024... |

The following collections are currently available:

- Copernicus Sentinel Mission
  - **SENTINEL-1**
  - **SENTINEL-2**
  - **SENTINEL-3**
  - **SENTINEL-5P**
  - **SENTINEL-6**
  - **SENTINEL-1-RTC** (Sentinel-1 Radiometric Terrain Corrected)
- Complementary data
  - **GLOBAL-MOSAICS** (Sentinel-1 and Sentinel-2 Global Mosaics)
  - **SMOS** (Soil Moisture and Ocean Salinity)
  - **ENVISAT** (ENVISAT- Medium Resolution Imaging Spectrometer - MERIS)
  - **LANDSAT-5**
  - **LANDSAT-7**
  - **LANDSAT-8**
  - **LANDSAT-9**
  - **COP-DEM** (Copernicus DEM)
  - **TERRA** (Terra MODIS)
  - **AQUA** (Aqua MODIS)
  - **TERRAAQUA** (Terra MODIS and Aqua MODIS)
  - **S2GLC** (S2GLC 2017)
- Copernicus Services
  - **CLMS** (Copernicus Land Monitoring Service)
- Copernicus Contributing Missions (CCM)

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and ContentDate/Start gt 2005-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T00:11:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27CCM%27%20and%20ContentDate/Start%20gt%202005-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T00:11:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and ContentDate/Start gt 2005-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T00:11:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 70c20650-4621-40ee-9f29-41973e8ef96b | DEM1_SAR_DTE_90_20110204T132020_20141115T13303... | /eodata/CCM/COP-DEM_GLO-90-DTED/SAR_DTE_90_61F... | {'type': 'Polygon', 'coordinates': \[\[\[59.0, 68... |
| 1 | aabba86a-53ef-4c17-a673-ecda83e13203 | DEM1_SAR_DTE_90_20110204T091108_20131220T09231... | /eodata/CCM/COP-DEM_GLO-90-DTED/SAR_DTE_90_61F... | {'type': 'Polygon', 'coordinates': \[\[\[-58.0, -... |
| 2 | 00646e04-06e0-4462-9ef4-cf3128abda61 | PH1B_PHR_MS\_\_2A_20180920T141019_20180920T14102... | /eodata/CCM/VHR_IMAGE_2018/PHR_MS\_\_2A_E1F0/201... | {'type': 'Polygon', 'coordinates': \[\[\[-52.7024... |

### Query by Publication Date

To search for products published between two dates:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate gt 2019-05-15T00:00:00.000Z and PublicationDate lt 2019-05-16T00:00:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate%20gt%202019-05-15T00:00:00.000Z%20and%20PublicationDate%20lt%202019-05-16T00:00:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate gt 2019-05-15T00:00:00.000Z and PublicationDate lt 2019-05-16T00:00:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 2997cd87-a273-5bbc-998a-1c72fe152b06 | S3A_SL_1_RBT\_\_\_\_20160904T192151_20160904T19245... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2016/09/04/S... | {'type': 'Polygon', 'coordinates': \[\[\[42.9227,... |
| 1 | 05d3b080-14b1-5e93-b72b-3743f8d8a37c | S3A_SL_1_RBT\_\_\_\_20160904T191051_20160904T19125... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2016/09/04/S... | {'type': 'Polygon', 'coordinates': \[\[\[50.5057,... |
| 2 | d204583c-2328-57c0-9534-f52121048cf1 | S3A_SL_1_RBT\_\_\_\_20160904T192451_20160904T19275... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2016/09/04/S... | {'type': 'Polygon', 'coordinates': \[\[\[41.386, ... |

To define inclusive interval *ge* and *le* parameters can be used:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate ge 2019-05-15T00:00:00.000Z and PublicationDate le 2019-05-16T00:00:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate%20ge%202019-05-15T00:00:00.000Z%20and%20PublicationDate%20le%202019-05-16T00:00:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=PublicationDate ge 2019-05-15T00:00:00.000Z and PublicationDate le 2019-05-16T00:00:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 2997cd87-a273-5bbc-998a-1c72fe152b06 | S3A_SL_1_RBT\_\_\_\_20160904T192151_20160904T19245... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2016/09/04/S... | {'type': 'Polygon', 'coordinates': \[\[\[42.9227,... |
| 1 | 05d3b080-14b1-5e93-b72b-3743f8d8a37c | S3A_SL_1_RBT\_\_\_\_20160904T191051_20160904T19125... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2016/09/04/S... | {'type': 'Polygon', 'coordinates': \[\[\[50.5057,... |
| 2 | d204583c-2328-57c0-9534-f52121048cf1 | S3A_SL_1_RBT\_\_\_\_20160904T192451_20160904T19275... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2016/09/04/S... | {'type': 'Polygon', 'coordinates': \[\[\[41.386, ... |

### Query by Sensing Date

To search for products acquired between two dates:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=ContentDate/Start gt 2019-05-15T00:00:00.000Z and ContentDate/Start lt 2019-05-16T00:00:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=ContentDate/Start%20gt%202019-05-15T00:00:00.000Z%20and%20ContentDate/Start%20lt%202019-05-16T00:00:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=ContentDate/Start gt 2019-05-15T00:00:00.000Z and ContentDate/Start lt 2019-05-16T00:00:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 4725d436-3e90-5480-bee1-0f13a7fc14fd | S3B_SL_1_RBT\_\_\_\_20190515T000040_20190515T00034... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2019/05/15/S... | {'type': 'Polygon', 'coordinates': \[\[\[-8.40421... |
| 1 | 169fda08-9928-576e-a556-97a6d3b9bacf | S3B_SL_1_RBT\_\_\_\_20190515T000040_20190515T00034... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2019/05/15/S... | {'type': 'Polygon', 'coordinates': \[\[\[-8.40421... |
| 2 | 07c0c999-5f9d-553f-9b3d-f2b8ab013856 | S3B_SL_2_LST\_\_\_\_20190515T000040_20190515T00034... | /eodata/Sentinel-3/SLSTR/SL_2_LST/2019/05/15/S... | {'type': 'Polygon', 'coordinates': \[\[\[-8.40421... |

As an example, for the Copernicus Contributions Mission Data (CCM):

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))') and ContentDate/Start gt 2021-05-20T00:00:00.000Z and ContentDate/Start lt 2021-07-21T00:00:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27CCM%27%20and%20OData.CSC.Intersects(area=geography%27SRID=4326;POLYGON((12.655118166047592%2047.44667197521409,21.39065656328509%2048.347694733853245,28.334291357162826%2041.877123516783655,17.47086198383573%2040.35854475076158,12.655118166047592%2047.44667197521409))%27)%20and%20ContentDate/Start%20gt%202021-05-20T00:00:00.000Z%20and%20ContentDate/Start%20lt%202021-07-21T00:00:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))') and ContentDate/Start gt 2021-05-20T00:00:00.000Z and ContentDate/Start lt 2021-07-21T00:00:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 19db5dbf-d394-4e7b-a7aa-b0d2629cbe68 | PH1B_PHR_MS\_\_2A_20210603T095945_20210603T09594... | /eodata/CCM/VHR_IMAGE_2021/PHR_MS\_\_2A_07B6/202... | {'type': 'Polygon', 'coordinates': \[\[\[16.87990... |
| 1 | 6c742dca-e0d6-4182-ae66-6ba5ecdfd9ce | SW00_OPT_MS4_1B_20210603T094047_20210603T09405... | /eodata/CCM/VHR_IMAGE_2021/OPT_MS4_1B_07B6/202... | {'type': 'Polygon', 'coordinates': \[\[\[19.99165... |
| 2 | 2692ef4a-3b3e-4ebc-829c-ab6a288b7820 | SW00_OPT_MS4_1B_20210603T094631_20210603T09463... | /eodata/CCM/VHR_IMAGE_2021/OPT_MS4_1B_07B6/202... | {'type': 'Polygon', 'coordinates': \[\[\[22.99911... |

Usually, there are two parameters describing the ContentDate (Acquisition Dates) for a product - Start and End. Depending on what the user is looking for, these parameters can be mixed, e.g.:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=ContentDate/Start gt 2019-05-15T00:00:00.000Z and ContentDate/End lt 2019-05-15T00:05:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=ContentDate/Start%20gt%202019-05-15T00:00:00.000Z%20and%20ContentDate/End%20lt%202019-05-15T00:05:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=ContentDate/Start gt 2019-05-15T00:00:00.000Z and ContentDate/End lt 2019-05-15T00:05:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 4725d436-3e90-5480-bee1-0f13a7fc14fd | S3B_SL_1_RBT\_\_\_\_20190515T000040_20190515T00034... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2019/05/15/S... | {'type': 'Polygon', 'coordinates': \[\[\[-8.40421... |
| 1 | 169fda08-9928-576e-a556-97a6d3b9bacf | S3B_SL_1_RBT\_\_\_\_20190515T000040_20190515T00034... | /eodata/Sentinel-3/SLSTR/SL_1_RBT/2019/05/15/S... | {'type': 'Polygon', 'coordinates': \[\[\[-8.40421... |
| 2 | 07c0c999-5f9d-553f-9b3d-f2b8ab013856 | S3B_SL_2_LST\_\_\_\_20190515T000040_20190515T00034... | /eodata/Sentinel-3/SLSTR/SL_2_LST/2019/05/15/S... | {'type': 'Polygon', 'coordinates': \[\[\[-8.40421... |

> **TIP:**
>
> Filtering by ContentDate/Start is much faster than by ContentDate/End for big collections. Narrowing ContentDate/Start gives the best performance boost for *SENTINEL-2* collection.

### Query by Geographic Criteria

To search for products intersecting the specified polygon:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))') and ContentDate/Start gt 2022-05-20T00:00:00.000Z and ContentDate/Start lt 2022-05-21T00:00:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography%27SRID=4326;POLYGON((12.655118166047592%2047.44667197521409,21.39065656328509%2048.347694733853245,28.334291357162826%2041.877123516783655,17.47086198383573%2040.35854475076158,12.655118166047592%2047.44667197521409))%27)%20and%20ContentDate/Start%20gt%202022-05-20T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-21T00:00:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))') and ContentDate/Start gt 2022-05-20T00:00:00.000Z and ContentDate/Start lt 2022-05-21T00:00:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 48c6e950-d2cf-4c58-afb4-3cc346c39c20 | c_gls_SCE_202205200000_NHEMI_SLSTR_V1.0.1_nc | /eodata/CLMS/bio-geophysical/snow_cover_extent... | {'type': 'Polygon', 'coordinates': \[\[\[-180.0, ... |
| 1 | 49bc8924-3f16-4997-b220-e95e824da8be | c_gls_SCE_202205200000_NHEMI_SLSTR_V1.0.1_cog | /eodata/CLMS/bio-geophysical/snow_cover_extent... | {'type': 'Polygon', 'coordinates': \[\[\[-180.0, ... |
| 2 | a0a96119-c333-43fb-99e3-d391779b3c49 | c_gls_SCE_202205200000_NHEMI_VIIRS_V1.0.1_cog | /eodata/CLMS/bio-geophysical/snow_cover_extent... | {'type': 'Polygon', 'coordinates': \[\[\[-180.0, ... |

Similarly, for the Copernicus Contributing Missions (CCM) data:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))')&$top=20`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27CCM%27%20and%20OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592%2047.44667197521409,21.39065656328509%2048.347694733853245,28.334291357162826%2041.877123516783655,17.47086198383573%2040.35854475076158,12.655118166047592%2047.44667197521409))')&$top=20)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))')&$top=20").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 0001013d-2221-4c09-ac51-a2e46eec07d8 | PL00_DOV_MS_L3A_20180810T082822_20180810T08282... | /eodata/CCM/VHR_IMAGE_2018/DOV_MS_L3A_E1F0-COG... | {'type': 'Polygon', 'coordinates': \[\[\[23.52656... |
| 1 | 00016ee7-3a5b-4834-b688-f90733aa0029 | PN03_PNE_MS2\_\_3_20240820T094735_20240820T09473... | /eodata/CCM/VHR_IMAGE_2024/PNE_MS2\_\_3_0476/202... | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[19... |
| 2 | 0002c916-2843-421a-8b99-81494ccbbf64 | SW00_OPT_MS4_1C_20210925T103755_20210925T10375... | /eodata/CCM/VHR_IMAGE_2021/OPT_MS4_1C_07B6-COG... | {'type': 'Polygon', 'coordinates': \[\[\[17.28215... |

To search for products intersecting the specified point:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POINT(-0.5319577002158441 28.65487836189358)') and Collection/Name eq 'SENTINEL-1'&$top=20`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography%27SRID=4326;POINT(-0.5319577002158441%2028.65487836189358)%27)%20and%20Collection/Name%20eq%20%27SENTINEL-1%27&$top=20)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POINT(-0.5319577002158441 28.65487836189358)') and Collection/Name eq 'SENTINEL-1'&$top=20").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 02469c48-150c-59c5-a740-e83a1f7698fc | S1B_IW_GRDH_1SDV_20211030T060424_20211030T0604... | /eodata/Sentinel-1/SAR/GRD/2021/10/30/S1B_IW_G... | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-0... |
| 1 | 0262f699-8d30-5952-b1c3-df07fdf9b887 | S1B_IW_GRDH_1SDV_20210227T055611_20210227T0556... | /eodata/Sentinel-1/SAR/GRD/2021/02/27/S1B_IW_G... | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[1.... |
| 2 | 02cb3891-f58a-5ce4-8259-60ec295043c0 | S1B_IW_GRDH_1SDV_20210328T060414_20210328T0604... | /eodata/Sentinel-1/SAR/GRD/2021/03/28/S1B_IW_G... | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-0... |

*Disclaimers*:

1.  Polygon must start and end with the same point.
2.  Coordinates must be given in **EPSG 4326**

> **NOTE:**
>
> Please note that the geometry is validated using the Shapely library, and invalid geometries results in an error.

### Query by attributes

To search for products by attributes, it is necessary to build a filter with the following structure:

Attributes/OData.CSC.**ValueTypeAttribute**/any(att:att/Name eq ‘\[**Attribute.Name**\]’ and att/OData.CSC.**ValueTypeAttribute**/Value eq \[**Attribute.Value**\])

where

- ***ValueTypeAttribute*** can take the following values:
  - *DoubleAttribute*
  - *IntegerAttribute*
  - *DateTimeOffsetAttribute*
  - *StringAttribute*

> **TIP:**
>
> To search for products by ***StringAttribute***, the filter query should be built with the following structure: *Attributes/OData.CSC.StringAttribute/any(att:att/Name eq ‘\[Attribute.Name\]’ and att/OData.CSC.StringAttribute/Value eq ‘\[Attribute.Value\]’)*

- ***\[Attribute.Name\]*** is the attribute name which can take multiple values depending on collection; acceptable values for the attribute name can be checked at the specified endpoints for each collection, as provided in [List of OData query attributes](https://documentation.dataspace.copernicus.eu/APIs/OData.html#list-of-odata-query-attributes-by-collection).
- ***eq*** before *\[Attribute.Value\]* can be substituted with le, lt, ge, gt in case of *Integer, Double* or *DateTimeOffset* Attributes
- ***\[Attribute.Value\]*** is the specific value that the user is searching for

To get Sentinel-2 products with CloudCover\<40% between two dates:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-2' and Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value le 40.00) and ContentDate/Start gt 2022-01-01T00:00:00.000Z and ContentDate/Start lt 2022-01-03T00:00:00.000Z&$top=10`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20Attributes/OData.CSC.DoubleAttribute/any(att:att/Name%20eq%20%27cloudCover%27%20and%20att/OData.CSC.DoubleAttribute/Value%20le%2040.00)%20and%20ContentDate/Start%20gt%202022-01-01T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-01-03T00:00:00.000Z&$top=10)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value le 40.00) and ContentDate/Start gt 2022-01-01T00:00:00.000Z and ContentDate/Start lt 2022-01-03T00:00:00.000Z&$top=10").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 3f1a7d72-2203-44b3-ae07-a9f332efd14d | S2B_MSIL1C_20220101T000459_N0510_R130_T50CNT_2... | /eodata/Sentinel-2/MSI/L1C_N0500/2022/01/01/S2... | {'type': 'Polygon', 'coordinates': \[\[\[117.6753... |
| 1 | b858743e-baa0-4f5f-bfaa-df19a740a53f | S2B_MSIL2A_20220101T000459_N0510_R130_T52CFE_2... | /eodata/Sentinel-2/MSI/L2A_N0500/2022/01/01/S2... | {'type': 'Polygon', 'coordinates': \[\[\[133.0895... |
| 2 | 31b62d3f-e45d-4277-aebd-0a709d3e0fd0 | S2B_MSIL1C_20220101T000459_N0510_R130_T49CEN_2... | /eodata/Sentinel-2/MSI/L1C_N0500/2022/01/01/S2... | {'type': 'Polygon', 'coordinates': \[\[\[113.5925... |

To get products with cloudCover\< 10% and productType=S2MSI2A

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20Attributes/OData.CSC.DoubleAttribute/any(att:att/Name%20eq%20%27cloudCover%27%20and%20att/OData.CSC.DoubleAttribute/Value%20lt%2010.00)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27S2MSI2A%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T04:00:00.000Z&$top=10`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20Attributes/OData.CSC.DoubleAttribute/any(att:att/Name%20eq%20%27cloudCover%27%20and%20att/OData.CSC.DoubleAttribute/Value%20lt%2010.00)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27S2MSI2A%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T04:00:00.000Z&$top=10)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20Attributes/OData.CSC.DoubleAttribute/any(att:att/Name%20eq%20%27cloudCover%27%20and%20att/OData.CSC.DoubleAttribute/Value%20lt%2010.00)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27S2MSI2A%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T04:00:00.000Z&$top=10").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | a49a8bc0-6266-411d-97cd-c86a974d3fe1 | S2B_MSIL2A_20220503T000139_N0510_R016_T09XWK_2... | /eodata/Sentinel-2/MSI/L2A_N0500/2022/05/03/S2... | {'type': 'Polygon', 'coordinates': \[\[\[-129.001... |
| 1 | 590dfcf9-3184-4c9a-a4a7-2e11ee1ad62a | S2B_MSIL2A_20220503T000139_N0510_R016_T08XNP_2... | /eodata/Sentinel-2/MSI/L2A_N0500/2022/05/03/S2... | {'type': 'Polygon', 'coordinates': \[\[\[-129.461... |
| 2 | e3a53df7-9c44-4ae5-a003-c6d14bda9c8d | S2B_MSIL2A_20220503T000139_N0510_R016_T10XEP_2... | /eodata/Sentinel-2/MSI/L2A_N0500/2022/05/03/S2... | {'type': 'Polygon', 'coordinates': \[\[\[-117.285... |

To query a subset of CCM data for a specific area of interest and time period, selecting a specific mission, e.g. only Worldview-3:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON ((6.535492 50.600673, 6.535492 50.937662, 7.271576 50.937662, 7.271576 50.600673, 6.535492 50.600673))') and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformName' and att/OData.CSC.StringAttribute/Value eq 'WorldView-3') and ContentDate/Start gt 2022-05-20T00:00:00.000Z and ContentDate/Start lt 2022-07-21T00:00:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27CCM%27%20and%20OData.CSC.Intersects(area=geography%27SRID=4326;POLYGON%20((6.535492%2050.600673,%206.535492%2050.937662,%207.271576%2050.937662,%207.271576%2050.600673,%206.535492%2050.600673))%27)%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27platformName%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27WorldView-3%27)%20and%20ContentDate/Start%20gt%202022-05-20T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-07-21T00:00:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'CCM' and OData.CSC.Intersects(area=geography'SRID=4326;POLYGON ((6.535492 50.600673, 6.535492 50.937662, 7.271576 50.937662, 7.271576 50.600673, 6.535492 50.600673))') and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'platformName' and att/OData.CSC.StringAttribute/Value eq 'WorldView-3') and ContentDate/Start gt 2022-05-20T00:00:00.000Z and ContentDate/Start lt 2022-07-21T00:00:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 9f1020e6-be24-4675-8b1a-82ce6c27913f | EW03_WV3_MS4_SO_20220717T105040_20220717T10504... | /eodata/CCM/VHR_IMAGE_2021/WV3_MS4_SO_07B6/202... | {'type': 'Polygon', 'coordinates': \[\[\[6.99509,... |
| 1 | 1aad79fa-90c6-498a-b2de-a20a34d06db8 | EW03_WV3_MS4_OR_20220717T105040_20220717T10504... | /eodata/CCM/VHR_IMAGE_2021/WV3_MS4_OR_07B6/202... | {'type': 'Polygon', 'coordinates': \[\[\[6.983405... |
| 2 | 84228bdc-ed58-4f78-9dfc-f10ad748ad96 | EW03_WV3_MS4_OR_20220717T105040_20220717T10504... | /eodata/CCM/VHR_IMAGE_2021/WV3_MS4_OR_07B6/202... | {'type': 'Polygon', 'coordinates': \[\[\[6.97417,... |

To search all products of a specific dataset under CCM (for example for the products belonging to VHR_IMAGE_2018):

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'datasetFull' and att/OData.CSC.StringAttribute/Value eq 'VHR_IMAGE_2018')`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27datasetFull%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27VHR_IMAGE_2018%27))

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'datasetFull' and att/OData.CSC.StringAttribute/Value eq 'VHR_IMAGE_2018')").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 00646e04-06e0-4462-9ef4-cf3128abda61 | PH1B_PHR_MS\_\_2A_20180920T141019_20180920T14102... | /eodata/CCM/VHR_IMAGE_2018/PHR_MS\_\_2A_E1F0/201... | {'type': 'Polygon', 'coordinates': \[\[\[-52.7024... |
| 1 | efa0f5ac-33af-45c2-adc6-04b929e2910a | SP06_NAO_MS4\_\_3_20181030T133528_20181030T13353... | /eodata/CCM/VHR_IMAGE_2018/NAO_MS4\_\_3_E1F0/201... | {'type': 'Polygon', 'coordinates': \[\[\[-52.7035... |
| 2 | 61eada6e-14e5-4cb2-a578-b44b3c7af932 | SP06_NAO_MS4\_\_3_20180705T091411_20180705T09143... | /eodata/CCM/VHR_IMAGE_2018/NAO_MS4\_\_3_E1F0-COG... | {'type': 'Polygon', 'coordinates': \[\[\[25.97452... |

To search all products of a specific dataset under CLMS (for example for the products belonging to swi-timeseries_global_12.5km_daily_v3):

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'datasetIdentifier' and att/OData.CSC.StringAttribute/Value eq 'swi-timeseries_global_12.5km_daily_v3')`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27datasetIdentifier%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27swi-timeseries_global_12.5km_daily_v3%27))

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'datasetIdentifier' and att/OData.CSC.StringAttribute/Value eq 'swi-timeseries_global_12.5km_daily_v3')").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | cce72859-d6cf-48ee-98f6-5de2a15ac586 | c_gls_SWI-TS_202412310000_C0273_ASCAT_V3.2.1_nc | /eodata/CLMS/bio-geophysical/soil_water_index/... | {'type': 'Polygon', 'coordinates': \[\[\[-27.5716... |
| 1 | 81c17fc7-41fc-48c4-a253-c1a14d8086d8 | c_gls_SWI-TS_202412310000_C0369_ASCAT_V3.2.1_nc | /eodata/CLMS/bio-geophysical/soil_water_index/... | {'type': 'Polygon', 'coordinates': \[\[\[20.00002... |
| 2 | 3755ec49-a40c-4831-825a-01a3a70dd572 | c_gls_SWI-TS_202412310000_C0425_ASCAT_V3.2.1_nc | /eodata/CLMS/bio-geophysical/soil_water_index/... | {'type': 'Polygon', 'coordinates': \[\[\[50.00176... |

More examples of OData queries for CLMS can be found [CLMS - examples of OData queries](https://documentation.dataspace.copernicus.eu/Data/CopernicusServices/CLMS.html#examples-of-odata-queries)

#### List of OData query attributes by collection

To check acceptable attribute names for all Collections:

## All collections

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes)

To check acceptable attribute names for Copernicus Sentinel Missions:

## SENTINEL-1

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-1)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-1))

## SENTINEL-2

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-2)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-2))

## SENTINEL-3

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-3)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-3))

## SENTINEL-5P

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-5P)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-5P))

## SENTINEL-6

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-6)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-6))

## SENTINEL-1-RTC

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-1-RTC)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SENTINEL-1-RTC))

To check acceptable attribute names for Copernicus Contributing Missions (CCM):

## CCM

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(CCM)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(CCM))

To check acceptable attribute names for Copernicus Land Monitoring Service:

## CLMS

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(CLMS)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(CLMS))

To check acceptable attribute names for Complementary data:

## GLOBAL-MOSAICS

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(GLOBAL-MOSAICS)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(GLOBAL-MOSAICS))

## SMOS

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SMOS)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(SMOS))

## ENVISAT

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(ENVISAT)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(ENVISAT))

## LANDSAT-5

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-5)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-5))

## LANDSAT-7

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-7)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-7))

## LANDSAT-8

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-8)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-8))

## LANDSAT-9

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-9)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(LANDSAT-9))

## COP-DEM

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(COP-DEM)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(COP-DEM))

## TERRA

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(TERRA)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(TERRA))

## AQUA

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(AQUA)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(AQUA))

## TERRAAQUA

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(TERRAAQUA)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(TERRAAQUA))

## S2GLC

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(S2GLC)`](https://catalogue.dataspace.copernicus.eu/odata/v1/Attributes(S2GLC))

## Orderby option

Orderby option can be used to order the products in an ascending (asc) or descending (desc) direction. If asc or desc is not specified, then the resources will be ordered in ascending order.

> **TIP:**
>
> Using the orderby option will exclude potential duplicates from the search results.

To order products by ContentDate/Start in a descending direction:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T03:00:00.000Z&$orderby=ContentDate/Start desc`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27EW_GRDM_1S%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T03:00:00.000Z&$orderby=ContentDate/Start%20desc)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T03:00:00.000Z&$orderby=ContentDate/Start desc").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 6928b379-4f9a-5473-a12a-7e7e4b83f776 | S1A_EW_GRDM_1SSH_20220503T024410_20220503T0244... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-105.464... |
| 1 | 4824ead5-b35c-5b83-80fa-71219c069e1c | S1A_EW_GRDM_1SSH_20220503T024310_20220503T0244... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-103.097... |
| 2 | 0929f73c-902a-506b-9646-c908199bfa23 | S1A_EW_GRDM_1SSH_20220503T024206_20220503T0243... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-97.2686... |

By default, if the orderby option is not used, the results are not ordered. If orderby option is used, additional orderby by id is also used, so that the results are fully ordered, and no products are lost while paginating through the results.

The acceptable arguments for this option: *ContentDate/Start*, *ContentDate/End, PublicationDate, ModificationDate*, in directions: *asc, desc*.

## Top option

Top option specifies the maximum number of items returned from a query.

To limit the number of results:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$top=100`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27EW_GRDM_1S%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$top=100)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$top=100").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | d1402094-d440-570c-9f55-07ffdd2fae19 | S1A_EW_GRDM_1SDH_20220503T064800_20220503T0649... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[15.66478... |
| 1 | d321960c-9d45-5660-9caf-ad587a22021b | S1A_EW_GRDM_1SDH_20220503T050916_20220503T0510... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[40.29474... |
| 2 | da10e137-b218-53b9-b83e-130f2e8da8c0 | S1A_EW_GRDM_1SDH_20220503T082621_20220503T0827... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-5.43769... |

The default value is set to 20.

The acceptable arguments for this option: *Integer \<0,1000\>*

## Skip option

The skip option can be used to skip a specific number of results. Exemplary application of this option would be paginating through the results, however, for performance reasons, we recommend limiting queries with small time intervals as a substitute for skipping in a more generic query.

To skip a specific number of results:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$skip=23`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27EW_GRDM_1S%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$skip=23)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'EW_GRDM_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$skip=23").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 81738432-1e5c-5419-9be9-4aada9160f7c | S1A_EW_GRDM_1SDH_20220503T033338_20220503T0334... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[50.73332... |
| 1 | 38306f68-853c-5011-a28c-74f4062c1f29 | S1A_EW_GRDM_1SSH_20220503T010212_20220503T0103... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-64.1217... |
| 2 | 35d932b2-715f-521b-9dbe-612d6edc4d1c | S1A_EW_GRDM_1SDH_20220503T033138_20220503T0332... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_EW_G... | {'type': 'Polygon', 'coordinates': \[\[\[58.35612... |

The default value is set to 0.

Whenever a query results in more products than 20 (default top value), the API provides a nextLink at the bottom of the page:

    "@OData.nextLink":

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_GRDH_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$skip=20`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27IW_GRDH_1S%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$skip=20)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_GRDH_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$skip=20").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 665501b5-56a4-5ba1-92ca-b62a4571afa2 | S1A_IW_GRDH_1SDV_20220503T013322_20220503T0133... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_IW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-114.503... |
| 1 | 63a43876-a5a3-52a1-a401-04c2bbd93faf | S1A_IW_GRDH_1SDV_20220503T013617_20220503T0136... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_IW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-116.981... |
| 2 | dd677ca4-b6b2-509d-8820-0d14ab5f52d5 | S1A_IW_GRDH_1SDV_20220503T013646_20220503T0137... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_IW_G... | {'type': 'Polygon', 'coordinates': \[\[\[-117.353... |

The acceptable arguments for this option: *Integer \<0,10000\>*

## Count option

The count option lets users get the exact number of products matching the query. This option is disabled by default to accelerate the query performance.

> **TIP:**
>
> Don’t use *count* option if not necessary, it slows down the execution of the request.

To get the exact number of products for a given query:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_GRDH_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$count=True`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27IW_GRDH_1S%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$count=True)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_GRDH_1S') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$count=True").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 2af72689-8608-5d24-a7bb-a143f667dbd1 | S1A_IW_GRDH_1SDV_20220503T002004_20220503T0020... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_IW_G... | {'type': 'Polygon', 'coordinates': \[\[\[91.09471... |
| 1 | cc319b60-b419-59b6-b063-ace3facc8e72 | S1A_IW_GRDH_1SDV_20220503T002033_20220503T0021... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_IW_G... | {'type': 'Polygon', 'coordinates': \[\[\[90.36774... |
| 2 | a2176410-7175-5b89-90f9-66be98f65d92 | S1A_IW_GRDH_1SDV_20220503T002641_20220503T0027... | /eodata/Sentinel-1/SAR/GRD/2022/05/03/S1A_IW_G... | {'type': 'Polygon', 'coordinates': \[\[\[84.51186... |

The acceptable arguments for this option: *True, true, 1, False, false, 0*.

## Expand option

Expand option allows users to speficy the type of information they would like to see in detail.

The acceptable arguments for this option: *Attributes*, *Assets* and *Locations*.

### Expand Attributes

The expand attributes enables users to see the full metadata of each returned result.

To see the metadata of the results:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$expand=Attributes`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$expand=Attributes)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T12:00:00.000Z&$expand=Attributes").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 1d42f2d3-2456-485f-a93e-92f08bdd5c51 | S1A_OPER_AUX_GNSSRD_POD\_\_20220510T020122_V2022... | /eodata/Sentinel-1/AUX/AUX_GNSSRD/2022/05/03/S... | None |
| 1 | 5c744d5c-c082-4a34-a181-81cde73cd25d | S1B_OPER_AUX_GNSSRD_POD\_\_20220510T023113_V2022... | /eodata/Sentinel-1/AUX/AUX_GNSSRD/2022/05/03/S... | None |
| 2 | 30252d61-e607-5525-be8d-aad13defd2c8 | S1A_IW_SLC\_\_1SDV_20220503T002004_20220503T0020... | /eodata/Sentinel-1/SAR/SLC/2022/05/03/S1A_IW_S... | {'type': 'Polygon', 'coordinates': \[\[\[91.08319... |

### Expand Assets

Expand assets allows to list additional assets of products, including quicklooks:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-3' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'SL_2_FRP___')&$expand=Assets`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-3%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27SL_2_FRP___%27)&$expand=Assets)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-3' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'SL_2_FRP___')&$expand=Assets").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | 0a9798ab-9366-4fa3-80e7-eaae981d7dcf | S3A_SL_2_FRP\_\_\_\_20201117T154352_20201117T15465... | /eodata/Sentinel-3/SLSTR/SL_2_FRP\_\_\_/2020/11/1... | {'type': 'Polygon', 'coordinates': \[\[\[107.669,... |
| 1 | 6dcaf73c-a2c1-42b8-8fb3-58a2822e7bf5 | S3B_SL_2_FRP\_\_\_\_20201231T235916_20210101T00021... | /eodata/Sentinel-3/SLSTR/SL_2_FRP\_\_\_/2020/12/3... | {'type': 'Polygon', 'coordinates': \[\[\[129.395,... |
| 2 | 24a5876e-c7d6-4629-ae08-c7bfa4028e6d | S3A_SL_2_FRP\_\_\_\_20201231T214040_20201231T21434... | /eodata/Sentinel-3/SLSTR/SL_2_FRP\_\_\_/2020/12/3... | {'type': 'Polygon', 'coordinates': \[\[\[7.45242,... |

### Expand Locations

Expand Locations allows users to see full list of available products’ forms (compressed/uncompressed) and locations from which they can be downloaded:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_RAW__0S')&$orderby=ContentDate/Start desc&$top=10&$expand=Locations`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20Attributes/OData.CSC.StringAttribute/any(att:att/Name%20eq%20%27productType%27%20and%20att/OData.CSC.StringAttribute/Value%20eq%20%27IW_RAW__0S%27)&$orderby=ContentDate/Start%20desc&$top=10&$expand=Locations)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-1' and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'IW_RAW__0S')&$orderby=ContentDate/Start desc&$top=10&$expand=Locations").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name','S3Path','GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | S3Path | GeoFootprint |
|----|----|----|----|----|
| 0 | a7b24970-d636-4d61-a3cf-a09504d1ba56 | S1C_IW_RAW\_\_0SDV_20260701T111844_20260701T1119... | /eodata/Sentinel-1/SAR/IW_RAW\_\_0S/2026/07/01/S... | {'type': 'Polygon', 'coordinates': \[\[\[100.7582... |
| 1 | e0f3c1e7-3825-49a2-a922-9a4d5bbb7d7b | S1C_IW_RAW\_\_0SDV_20260701T111819_20260701T1118... | /eodata/Sentinel-1/SAR/IW_RAW\_\_0S/2026/07/01/S... | {'type': 'Polygon', 'coordinates': \[\[\[101.0651... |
| 2 | 08434dfd-8900-4bc5-9d9a-2f9a17dafc70 | S1C_IW_RAW\_\_0SDV_20260701T111754_20260701T1118... | /eodata/Sentinel-1/SAR/IW_RAW\_\_0S/2026/07/01/S... | {'type': 'Polygon', 'coordinates': \[\[\[101.3688... |

The information about data storage locations and storage forms (compressed/uncompressed) are specified under expand=Locations.

To access more information, please review [Compressed products section](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-1) within Sentinel-1 mission description.

### Quicklook

For example, a quicklook for product `S3A_SL_2_FRP____20200821T042815_20200821T043115_20200822T092750_0179_062_033_2340_LN2_O_NT_004.SEN3` with ID of a quicklook `f4a87522-dd81-4c40-856e-41d40510e3b6`, can be downloaded with the request:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Assets(f4a87522-dd81-4c40-856e-41d40510e3b6)/$value`](https://catalogue.dataspace.copernicus.eu/odata/v1/Assets(f4a87522-dd81-4c40-856e-41d40510e3b6)/$value)

Download link is also available under *DownloadLink* parameter in Assets.

## Select option

The select option allows users to limit the requested properties to a specific subset for each product, e.g. to select products’ Name and Id:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$select=Name,Id`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$select=Name,Id)

The list of property names must be separated by a comma - it can also include an extra space. The order of attributes in the response is assigned by default and does not depend on the order of attributes specified in the user’s query.

The Id parameter is provided in the response by default, even if it is not defined in the select option.

Currently, those attributes are available:

- Id
- Name
- ContentType
- ContentLength
- OriginDate
- PublicationDate
- ModificationDate
- Online
- EvictionDate
- S3Path
- Checksum
- ContentDate
- Footprint
- Geofootprint

To select all available attributes, the `*` symbol can be used instead of listing each property name individually:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$select=*`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$select=*)

## Listing product nodes

Product content can be listed by accessing the following URL patterns using Nodes:

    https://download.dataspace.copernicus.eu/odata/v1/Products(<PRODUCT_UUID>)/Nodes
    https://download.dataspace.copernicus.eu/odata/v1/Products(<PRODUCT_UUID>)/Nodes(<NODE_NAME>)/Nodes
    https://download.dataspace.copernicus.eu/odata/v1/Products(<PRODUCT_UUID>)/Nodes(<NODE_NAME>)/Nodes(<NODE_NAME>)/Nodes

where:

\- is ID of the product obtained by search query,

\- is name of element inside product returned from previous listing response.

Only nodes that are folders can have their contents listed. Attempting to list Nodes for file results returning an empty list. The listing Nodes feature is available for both authorized and unauthorized users.

### Example nodes listing

Example URL:

    https://download.dataspace.copernicus.eu/odata/v1/Products(db0c8ef3-8ec0-5185-a537-812dad3c58f8)/Nodes

Response:

    {
       "result":[
          {
             "Id":"S2A_MSIL1C_20180927T051221_N0206_R033_T42FXL_20180927T073143.SAFE",
             "Name":"S2A_MSIL1C_20180927T051221_N0206_R033_T42FXL_20180927T073143.SAFE",
             "ContentLength":0,
             "ChildrenNumber":9,
             "Nodes":{
                "uri":"https://download.dataspace.copernicus.eu/odata/v1/Products(db0c8ef3-8ec0-5185-a537-812dad3c58f8)/Nodes(S2A_MSIL1C_20180927T051221_N0206_R033_T42FXL_20180927T073143.SAFE)/Nodes"
             }
          }
       ]
    }

Every Listed Node has “uri” field, which lists its children.

## Engineering level product search

In order to search for engineering level products, you must perform authorization by providing access token to the query.

## cURL

    curl --location "https://catalogue.dataspace.copernicus.eu/odata/v1/Products?$filter=Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'L1B_CA_SIR')" --header "Authorization: Bearer $ACCESS_TOKEN"

## Product Download

For downloading products you need an authorization token as only authorized users are allowed to download data products.

To get the token you can use the following scripts:

## cURL

    curl --location --request POST 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'grant_type=password' \
      --data-urlencode 'username=<LOGIN>' \
      --data-urlencode 'password=<PASSWORD>' \
      --data-urlencode 'client_id=cdse-public'

or

## cURL

    curl -d 'client_id=cdse-public' -d 'username=<LOGIN>' -d 'password=<PASSWORD>' -d 'grant_type=password' 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token' | python3 -m json.tool | grep "access_token" | awk -F\" '{print $4}'

Along with the Access Token, you will be returned a Refresh Token, the latter is used to generate a new Access Token without the need to specify a Username or Password; this helps to make requests less vulnerable to your credentials being exposed.

To re-generate the Access Token from the Refresh Token, it can be done with the following request:

## cURL

    curl --location --request POST 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'grant_type=refresh_token' \
      --data-urlencode 'refresh_token=<REFRESH_TOKEN>' \
      --data-urlencode 'client_id=cdse-public'

  

Once you have your token, you require a product Id which can be found in the response of the products search: [`https://catalogue.dataspace.copernicus.eu/odata/v1/Products`](https://catalogue.dataspace.copernicus.eu/odata/v1/Products)

Finally, you can download the product using this script:

> **TIP:**
>
> The examples below assume that the product is saved to a file with the “.zip” extension. The exceptions are Sentinel-5P products, which are served directly with the “.nc” extension.

## cURL

    curl -H "Authorization: Bearer $ACCESS_TOKEN" 'https://download.dataspace.copernicus.eu/odata/v1/Products(060882f4-0a34-5f14-8e25-6876e4470b0d)/$value' --location-trusted --output /tmp/product.zip

or

## Wget

    wget  --header "Authorization: Bearer $ACCESS_TOKEN" 'https://download.dataspace.copernicus.eu/odata/v1/Products(db0c8ef3-8ec0-5185-a537-812dad3c58f8)/$value' -O example_odata.zip

## Python

    import requests

    # Make sure access_token is defined
    access_token = "your_access_token"  # Replace with your actual access token

    url = f"https://download.dataspace.copernicus.eu/odata/v1/Products(a5ab498a-7b2f-4043-ae2a-f95f457e7b3b)/$value"

    headers = {"Authorization": f"Bearer {access_token}"}

    # Create a session and update headers
    session = requests.Session()
    session.headers.update(headers)

    # Perform the GET request
    response = session.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        with open("product.zip", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        print(response.text)

### Compressed Product Download

For downloading products in their native format (as zipped files) you need to proceed with the standard authorization as for [Product Download](https://documentation.dataspace.copernicus.eu/APIs/OData.html#product-download).

**Currently, users can access Sentinel-1 (RAW, GRD, SLC) data stored in native format and compressed for one month following their publication date within Data Space Catalogue.**

To access more information about compressed products, please review [Compressed products section](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-1) within Sentinel-1 mission description.

The access to compressed products (stored in native format):

## cURL

    curl -H "Authorization: Bearer $ACCESS_TOKEN" 'https://download.dataspace.copernicus.eu/odata/v1/Products(002f0c9e-8a4c-465b-9e03-479475947630)/$zip' --location-trusted --output /tmp/product.zip

or

## Wget

    wget  --header "Authorization: Bearer $ACCESS_TOKEN" 'https://download.dataspace.copernicus.eu/odata/v1/Products(002f0c9e-8a4c-465b-9e03-479475947630)/$zip' -O example_odata.zip

## Python

    import requests

    # Make sure access_token is defined
    access_token = "your_access_token"  # Replace with your actual access token

    url = f"https://download.dataspace.copernicus.eu/odata/v1/Products(002f0c9e-8a4c-465b-9e03-479475947630)/$zip"

    headers = {"Authorization": f"Bearer {access_token}"}

    # Create a session and update headers
    session = requests.Session()
    session.headers.update(headers)

    # Perform the GET request
    response = session.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        with open("product.zip", "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    file.write(chunk)
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        print(response.text)

## OData DeletedProducts endpoint

The **DeletedProducts OData** endpoint allows users to access information about the deleted products in the Copernicus Data Space Ecosystem Catalog. This endpoint provides a convenient way to retrieve details about the products that have been deleted from the CDSE Catalog. By utilizing the supported operations and filtering options, users can efficiently access the required deleted products’ details. For the DeletedProducts OData endpoint, requests should be built the same way as for the OData Products endpoint [OData Query structure](https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-structure) with the change in the endpoint URL ‘Products’ to ‘DeletedProducts’.

### Endpoint URL

The **DeletedProducts OData** endpoint can be accessed using the following URL:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts)

### Query structure

The DeletedProducts OData endpoint supports the same searching options as a standard OData Products endpoint. For more information, please go to [OData Query structure](https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-structure)

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$orderby=DeletionDate&$top=20`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20DeletionDate%20gt%202023-04-01T00:00:00.000Z%20and%20DeletionDate%20lt%202023-05-30T23:59:59.999Z&$orderby=DeletionDate&$top=20)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$orderby=DeletionDate&$top=20").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 81e390c0-4f9c-4a3c-8813-5bc6d7b48aa1 | S1A_EW_GRDM_1SSH_20220225T025010_20220225T0251... | Duplicated product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-7... |
| 1 | 1b797847-592f-4883-8cb0-e5fc9d875041 | S1A_EW_GRDM_1SSH_20220225T025010_20220225T0251... | Duplicated product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-7... |
| 2 | 90b6daea-016e-4277-9c2b-ed6e70158207 | S1B_IW_GRDH_1SDV_20180330T172340_20180330T1724... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[4.086337... |

> **TIP:**
>
> To accelerate the query performance, it is recommended to limit the query by specified dates, e.g.:
>
> DeletionDate gt 2022-05-03T00:00:00.000Z and DeletionDate lt 2023-05-03T00:00:00.000Z

### Filter option

To search for products by properties, a filter should be built as explained [Filter option](https://documentation.dataspace.copernicus.eu/APIs/OData.html#filter-option)

The acceptable products’ properties for OData DeletedProducts endpoint are:

- *Name* - search for a specific product by its exact name
- *Id* - search for a specific product by its id
- *DeletionDate* - search by deletion date
- *DeletionCause* - search by deletion cause
- *Collection/Name* - search within a specific collection
- *OriginDate* - search by origin date
- *ContentDate/Start* and *ContentDate/End* - search by sensing date
- *Footprint* - search by geographic criteria
- *Attributes* - search by product’s attributes

#### Query by name

To search for a deleted product by its exact name:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Name eq 'S2A_MSIL1C_20210404T112111_N0500_R037_T31VEG_20230209T101305.SAFE'`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Name%20eq%20%27S2A_MSIL1C_20210404T112111_N0500_R037_T31VEG_20230209T101305.SAFE%27)

#### Query by Id

To search for a deleted product by its Id:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts(29008eb1-1a51-48a8-9aec-288b00f7debe)`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts(29008eb1-1a51-48a8-9aec-288b00f7debe))

#### Query by Deletion Date

To search for products deleted between two inclusive interval dates:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=DeletionDate ge 2023-04-26T00:00:00.000Z and DeletionDate le 2023-04-27T23:59:59.999Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=DeletionDate%20ge%202023-04-26T00:00:00.000Z%20and%20DeletionDate%20le%202023-04-27T23:59:59.999Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=DeletionDate ge 2023-04-26T00:00:00.000Z and DeletionDate le 2023-04-27T23:59:59.999Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | f1a5d39a-7600-4701-9e61-03347f63d526 | S1A_IW_GRDH_1SDV_20230224T230426_20230224T2304... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[10... |
| 1 | 766c1738-3eba-4865-81e0-c5c51f5e29b6 | S1A_IW_GRDH_1SDV_20230224T231156_20230224T2312... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[99... |
| 2 | 474adc52-3a3c-4cf4-b498-47c5e5e64d27 | S1A_IW_GRDH_1SDV_20230225T000647_20230225T0007... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-9... |

#### Query by Deletion Cause

To search for products deleted from specific reason:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=DeletionCause eq 'Duplicated product' or DeletionCause eq 'Corrupted product'`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=DeletionCause%20eq%20%27Duplicated%20product%27%20or%20DeletionCause%20eq%20%27Corrupted%20product%27)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=DeletionCause eq 'Duplicated product' or DeletionCause eq 'Corrupted product'").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 96a829f7-69dc-4080-86dc-c3470b8e09b2 | S2A_MSIL2A_20210112T004001_N0500_R002_T57UUT_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[156.0657... |
| 1 | 559b6cee-d920-43d9-86a5-eb7b453506f0 | S2A_MSIL2A_20210317T051651_N0500_R062_T43PCK_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[74.17971... |
| 2 | 90b6daea-016e-4277-9c2b-ed6e70158207 | S1B_IW_GRDH_1SDV_20180330T172340_20180330T1724... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[4.086337... |

Allowed values of the `DelationCause` parameter are:

- Duplicated product
- Missing checksum
- Corrupted product
- Obsolete product or Other

#### Query by Collection of Products

To search for deleted products within a specific collection:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-2' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-09-30T23:59:59.999Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20DeletionDate%20gt%202023-04-01T00:00:00.000Z%20and%20DeletionDate%20lt%202023-09-30T23:59:59.999Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-2' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-09-30T23:59:59.999Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 9d832d07-9fe9-40ec-b843-8af32eca7c6f | S2A_MSIL2A_20200603T002611_N9999_R102_T01XDA_2... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[71... |
| 1 | df0b407e-768e-4567-9f54-cb50690907e3 | S2A_MSIL1C_20210401T010651_N0500_R131_T55TDN_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[146.2119... |
| 2 | 524ca315-7444-41b2-8e23-f3de06bc09bf | S2A_MSIL1C_20210401T010651_N0500_R131_T55TCH_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[145.9033... |

For available collections, please refer to [Query Collection of Products](https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-collection-of-products). Also, please note that it is possible that none of the products have been deleted from the available collections.

#### Query by Sensing Date

To search for deleted products acquired between two dates:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=ContentDate/Start gt 2021-09-01T00:00:00.000Z and ContentDate/End lt 2021-09-01T00:05:00.000Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=ContentDate/Start%20gt%202021-09-01T00:00:00.000Z%20and%20ContentDate/End%20lt%202021-09-01T00:05:00.000Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=ContentDate/Start gt 2021-09-01T00:00:00.000Z and ContentDate/End lt 2021-09-01T00:05:00.000Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 2b01765d-7d3c-5f8b-b69f-88d121c42c8b | S1B_IW_GRDH_1SDV_20210901T000023_20210901T0000... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[99... |
| 1 | 053f10da-3028-5ca6-9ccc-66c8c56fa439 | S1B_IW_GRDH_1SDV_20210901T000048_20210901T0001... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[98... |
| 2 | 73699a9d-cc42-5469-88a9-ecd0a595e0d9 | S1B_IW_GRDH_1SDV_20210901T000113_20210901T0001... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[97... |

#### Query by Geographic Criteria

To search for deleted products intersecting the specified polygon:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POLYGON ((-75.000244 -42.4521508418609, -75.000244 -43.4409190460844, -73.643585 -43.432873907284, -73.66513 -42.4443775132447, -75.000244 -42.4521508418609))') and ContentDate/Start gt 2021-01-01T00:00:00.000Z and ContentDate/End lt 2021-04-01T23:59:59.999Z`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=OData.CSC.Intersects(area=geography%27SRID=4326;POLYGON%20((-75.000244%20-42.4521508418609,%20-75.000244%20-43.4409190460844,%20-73.643585%20-43.432873907284,%20-73.66513%20-42.4443775132447,%20-75.000244%20-42.4521508418609))%27)%20and%20ContentDate/Start%20gt%202021-01-01T00:00:00.000Z%20and%20ContentDate/End%20lt%202021-04-01T23:59:59.999Z)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POLYGON ((-75.000244 -42.4521508418609, -75.000244 -43.4409190460844, -73.643585 -43.432873907284, -73.66513 -42.4443775132447, -75.000244 -42.4521508418609))') and ContentDate/Start gt 2021-01-01T00:00:00.000Z and ContentDate/End lt 2021-04-01T23:59:59.999Z").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 3a3e9685-ab43-41ad-9f4c-593302f4ba75 | S2A_MSIL2A_20210309T143731_N9999_R096_T18GWU_2... | Reprocessed product | {'type': 'Polygon', 'coordinates': \[\[\[-75.0002... |
| 1 | c677c050-c18a-4f87-97a0-989624ea0712 | S2A_MSIL1C_20210316T142731_N0500_R053_T18GWS_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-74.1524... |
| 2 | a56d9773-eb3d-4be0-81d4-4a526ff4bbbc | S2A_MSIL1C_20210309T143731_N0500_R096_T18GVU_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-75.9656... |

#### Query by attributes

To search for products by attributes, it is necessary to build a filter with the specified structure as defined [Query Collection of Products](https://documentation.dataspace.copernicus.eu/APIs/OData.html#query-collection-of-products).

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Attributes/OData.CSC.IntegerAttribute/any(att:att/Name%20eq%20%27orbitNumber%27%20and%20att/OData.CSC.IntegerAttribute/Value%20eq%2010844)`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Attributes/OData.CSC.IntegerAttribute/any(att:att/Name%20eq%20%27orbitNumber%27%20and%20att/OData.CSC.IntegerAttribute/Value%20eq%2010844))

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Attributes/OData.CSC.IntegerAttribute/any(att:att/Name%20eq%20%27orbitNumber%27%20and%20att/OData.CSC.IntegerAttribute/Value%20eq%2010844)").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 9a595c3d-02ba-5ae4-811c-70f8ce642580 | S1B_EW_GRDH_1SDH_20180509T120906_20180509T1210... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-71.8987... |
| 1 | f67ce5c3-65ab-5cfe-9796-c62087dfef29 | S1B_EW_GRDM_1SDH_20180509T121206_20180509T1213... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-81.6544... |
| 2 | b847c833-ceb8-5e23-a54e-c80c5d4a5be2 | S1B_EW_GRDM_1SDH_20180509T130033_20180509T1301... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[96.64321... |

### Orderby option

Orderby option works the same way as explained [Orderby option](https://documentation.dataspace.copernicus.eu/APIs/OData.html#orderby-option).

> **TIP:**
>
> Using the orderby option will exclude potential duplicates from the search results.

For OData DeletedProducts endpoint, acceptable arguments for this option are:

- *ContentDate/Start*
- *ContentDate/End*
- *DeletionDate*

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$orderby=DeletionDate desc`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20DeletionDate%20gt%202023-04-01T00:00:00.000Z%20and%20DeletionDate%20lt%202023-05-30T23:59:59.999Z&$orderby=DeletionDate%20desc)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$orderby=DeletionDate desc").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 17e63a3d-b68b-5286-9ed7-43f4260acb0a | S1A_IW_GRDH_1SDV_20210830T060853_20210830T0609... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[1.... |
| 1 | c59d69f3-59b3-5386-a4fc-ad8985d9ba37 | S1A_IW_GRDH_1SDV_20210829T233752_20210829T2338... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[96... |
| 2 | c1993b21-f1a0-5d57-a192-b35250fae50c | S1A_IW_GRDH_1SDV_20210830T060418_20210830T0604... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[6.... |

### Expand option

The expand option enables users to see the full metadata of each returned result.

The acceptable argument for this option is:

- *Attributes*

To see the metadata of the results:

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$expand=Attributes`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20DeletionDate%20gt%202023-04-01T00:00:00.000Z%20and%20DeletionDate%20lt%202023-05-30T23:59:59.999Z&$expand=Attributes)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$expand=Attributes").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 81e390c0-4f9c-4a3c-8813-5bc6d7b48aa1 | S1A_EW_GRDM_1SSH_20220225T025010_20220225T0251... | Duplicated product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-7... |
| 1 | 1b797847-592f-4883-8cb0-e5fc9d875041 | S1A_EW_GRDM_1SSH_20220225T025010_20220225T0251... | Duplicated product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[-7... |
| 2 | 90b6daea-016e-4277-9c2b-ed6e70158207 | S1B_IW_GRDH_1SDV_20180330T172340_20180330T1724... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[4.086337... |

### Skip option

Skip option can be used as defined [Skip option](https://documentation.dataspace.copernicus.eu/APIs/OData.html#skip-option).

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-2' and ContentDate/Start ge 2021-04-01T00:00:00.000Z and ContentDate/Start le 2021-04-30T23:59:59.999Z&$skip=30`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-2%27%20and%20ContentDate/Start%20ge%202021-04-01T00:00:00.000Z%20and%20ContentDate/Start%20le%202021-04-30T23:59:59.999Z&$skip=30)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-2' and ContentDate/Start ge 2021-04-01T00:00:00.000Z and ContentDate/Start le 2021-04-30T23:59:59.999Z&$skip=30").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 40fb185e-7dc9-4bfc-8e18-8796033514a6 | S2B_MSIL2A_20210401T001149_N0500_R059_T08XNQ_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-135.001... |
| 1 | a425a14e-7534-4e46-a384-7ffd5dab8f97 | S2B_MSIL1C_20210401T001149_N0500_R059_T10XDR_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-129.378... |
| 2 | 46a3452b-bd33-4fc8-8d70-0eed66d2d486 | S2B_MSIL1C_20210401T001149_N0500_R059_T07XEM_2... | Corrupted product | {'type': 'Polygon', 'coordinates': \[\[\[-141.001... |

### Top option

Top option can be used as defined [Top option](https://documentation.dataspace.copernicus.eu/APIs/OData.html#top-option).

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and ContentDate/Start ge 2021-09-01T00:00:00.000Z and ContentDate/Start le 2021-09-30T23:59:59.999Z&$top=40`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20ContentDate/Start%20ge%202021-09-01T00:00:00.000Z%20and%20ContentDate/Start%20le%202021-09-30T23:59:59.999Z&$top=40)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and ContentDate/Start ge 2021-09-01T00:00:00.000Z and ContentDate/Start le 2021-09-30T23:59:59.999Z&$top=40").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 2b01765d-7d3c-5f8b-b69f-88d121c42c8b | S1B_IW_GRDH_1SDV_20210901T000023_20210901T0000... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[99... |
| 1 | 053f10da-3028-5ca6-9ccc-66c8c56fa439 | S1B_IW_GRDH_1SDV_20210901T000048_20210901T0001... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[98... |
| 2 | 73699a9d-cc42-5469-88a9-ecd0a595e0d9 | S1B_IW_GRDH_1SDV_20210901T000113_20210901T0001... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[97... |

### Count option

Count option can be used as defined [Count option](https://documentation.dataspace.copernicus.eu/APIs/OData.html#count-option)

## HTTPS Request

[`https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$orderby=DeletionDate desc&$count=True`](https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name%20eq%20%27SENTINEL-1%27%20and%20DeletionDate%20gt%202023-04-01T00:00:00.000Z%20and%20DeletionDate%20lt%202023-05-30T23:59:59.999Z&$orderby=DeletionDate%20desc&$count=True)

## Python

Code

``` python
json = requests.get("https://catalogue.dataspace.copernicus.eu/odata/v1/DeletedProducts?$filter=Collection/Name eq 'SENTINEL-1' and DeletionDate gt 2023-04-01T00:00:00.000Z and DeletionDate lt 2023-05-30T23:59:59.999Z&$orderby=DeletionDate desc&$count=True").json()
df = pd.DataFrame.from_dict(json['value'])

# Print only specific columns
columns_to_print = ['Id', 'Name', 'DeletionCause', 'GeoFootprint']  
df[columns_to_print].head(3)
```

|  | Id | Name | DeletionCause | GeoFootprint |
|----|----|----|----|----|
| 0 | 17e63a3d-b68b-5286-9ed7-43f4260acb0a | S1A_IW_GRDH_1SDV_20210830T060853_20210830T0609... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[1.... |
| 1 | c59d69f3-59b3-5386-a4fc-ad8985d9ba37 | S1A_IW_GRDH_1SDV_20210829T233752_20210829T2338... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[96... |
| 2 | c1993b21-f1a0-5d57-a192-b35250fae50c | S1A_IW_GRDH_1SDV_20210830T060418_20210830T0604... | Corrupted product | {'type': 'MultiPolygon', 'coordinates': \[\[\[\[6.... |
