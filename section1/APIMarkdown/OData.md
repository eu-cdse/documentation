# Data catalogue API with OData interface

## Query structure

As a general note, OData query consistst of elements which in this documentation are called "options". Interface supports the following search options:

* filter
* orderby
* top
* skip
* count
* expand

Search options should always be preceded with *$* and consecutive options should be separated with *&*.

Consecutive filters within *filter* option should be separated with *and* or *or*. *Not* operator can also be used e.g.:

    https://datahub.creodias.eu/odata/v1/Products?$filter=not contains(Name,'S2') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T00:10:00.000Z&$orderby=ContentDate/Start&$top=100

<u>Performance note</u>:

To accelerate the query performance it is recommended to limit the query by acquisition dates e.g.:

    ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-21T00:00:00.000Z

## Filter option

### Query by name

To search for a specific product by its exact name:

    https://datahub.creodias.eu/odata/v1/Products?$filter=Name eq 'S1A\_IW\_GRDH\_1SDV\_20141031T161924\_20141031T161949\_003076\_003856\_634E.SAFE'

To search for products containing "S1A" in their names:

    https://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,'S1A') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-21T00:00:00.000Z

Alternatively to *contains*, *endswith* and *startswith* can be used, to search for products ending or starting with provided string.

### Query by list

In case a user desires to search for multiple products by name in one query, POST method can be used:

**POST**

    https://datahub.creodias.eu/odata/v1/Products/OData.CSC.FilterList

**Request body**:

    {
    "FilterProducts":
    [
    {"Name": "S1A\_IW\_GRDH\_1SDV\_20141031T161924\_20141031T161949\_003076\_003856\_634E.SAFE"},
    {"Name": "S3B\_SL\_1\_RBT\_\_\_\_20190116T050535\_20190116T050835\_20190117T125958\_0179\_021\_048\_0000\_LN2\_O\_NT\_003.SEN3"},
    {"Name": "xxxxxxxx.06.tar"}
    ]
    }

Two results are returned, as there is no product named xxxxxxxx.06.tar.

### Query Collection of Products

To search for products within a specific collection:

    https://datahub.creodias.eu/odata/v1/Products?$filter=Collection/Name eq 'SENTINEL-2' and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T00:11:00.000Z

The following collections are currently available:

* SENTINEL-1
* SENTINEL-2
* SENTINEL-3
* SENTINEL-5P

### Query by Publication Date

To search for products published between two dates:

    https://datahub.creodias.eu/odata/v1/Products?$filter=PublicationDate gt 2019-05-15T00:00:00.000Z and PublicationDate lt 2019-05-16T00:00:00.000Z

To define inclusive interval *ge* and *le* parameters can be used:

    https://datahub.creodias.eu/odata/v1/Products?$filter=PublicationDate ge 2019-05-15T00:00:00.000Z and PublicationDate le 2019-05-16T00:00:00.000Z

### Query by Sensing Date

To search for products acquired between two dates:

    https://datahub.creodias.eu/odata/v1/Products?$filter=ContentDate/Start gt 2019-05-15T00:00:00.000Z and ContentDate/Start lt 2019-05-16T00:00:00.000Z

Usually, there are two parameters describing the ContentDate (Acquisition Dates) for a product - Start and End. Depending on what the user is looking for, these parameters can be mixed, e.g.:

    https://datahub.creodias.eu/odata/v1/Products?$filter=ContentDate/Start gt 2019-05-15T00:00:00.000Z and ContentDate/End lt 2019-05-15T00:05:00.000Z

### Query by Geographic Criteria

To search for products intersecting the specified polygon:

    https://datahub.creodias.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography'SRID=4326;POLYGON((12.655118166047592 47.44667197521409,21.39065656328509 48.347694733853245,28.334291357162826 41.877123516783655,17.47086198383573 40.35854475076158,12.655118166047592 47.44667197521409))') and ContentDate/Start gt 2022-05-20T00:00:00.000Z and ContentDate/Start lt 2022-05-21T00:00:00.000Z

To search for products intersecting the specified point:

    https://datahub.creodias.eu/odata/v1/Products?$filter=OData.CSC.Intersects(area=geography%27SRID=4326;POINT(-0.5319577002158441%2028.65487836189358)%27)

<u>Disclaimers</u>:

1. MULTIPOLYGON is currently not supported.
2. Polygon must start and end with the same point.
3. Coordinates must be given in EPSG 4326

### Query by attributes

To search for products by attributes it is necessary to build a filter with the following structure:

    Attributes/OData.CSC.ValueTypeAttribute/any(att:att/Name eq '[Attribute.Name]' and att/OData.CSC.ValueTypeAttribute/Value eq '[Attribute.Value]')

where

- *ValueTypeAttribute* can take the following values:
  - *StringAttribute*
  - *DoubleAttribute*
  - *IntegerAttribute*
  - *DateTimeOffsetAttribute*
- *[Attribute.Name]* is the attribute name which can take multiple values, depending on collection (Attachment 1 - Coming soon)
- *eq* before *[Attribute.Value]* can be substituted with le, lt, ge, gt in case of *Integer, Double* or *DateTimeOffset* Attributes
- *[Attribute.Value]* is the specific value that the user is searching for

To get products with CloudCover\<40% between two dates:

    https://datahub.creodias.eu/odata/v1/Products?$filter=Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value le 40.00) and ContentDate/Start gt 2022-01-01T00:00:00.000Z and ContentDate/Start lt 2022-01-03T00:00:00.000Z&$top=10

To get products with cloudCover\< 10% and productType=S2MSI2A and ASCENDING orbitDirection between two dates:

    https://datahub.creodias.eu/odata/v1/Products?$filter=Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' and att/OData.CSC.DoubleAttribute/Value lt 10.00) and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'productType' and att/OData.CSC.StringAttribute/Value eq 'S2MSI2A') and Attributes/OData.CSC.StringAttribute/any(att:att/Name eq 'orbitDirection' and att/OData.CSC.StringAttribute/Value eq 'ASCENDING') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T04:00:00.000Z&$top=10


### Orderby option

Orderby option can be used to order the products in an ascending (asc) or descending (desc) direction. If asc or desc not specified, then the resources will be ordered in ascending order.

To order products by ContentDate/Start in a descending direction:

    https://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,'S1A\_EW\_GRD') and ContentDate/Start gt 2022-05-03T00:00:00.000Z and ContentDate/Start lt 2022-05-03T03:00:00.000Z&$orderby=ContentDate/Start desc

By default, if orderby option is not used, the results are not ordered. If orderby option is used, additional orderby by id is also used, so that the results are fully ordered and no products are lost while paginating through the results.

The acceptable arguments for this option: *ContentDate/Start*, *ContentDate/End, PublicationDate, ModificationDate*, in directions: *asc, desc*.

### Top option

Top option specifies the maximum number of items returned from a query.

To limit the number of results:

    https://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,%27S1A\_EW\_GRD%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$top=100

 The default value is set to 20.

The acceptable arguments for this option: _Integer \<0,1000\>_

## Skip option 

Skip option can be used to skip a specific number of results. Exemplary application of this option would be paginating through the results, however for performance reasons, we recommend limiting queries with small time intervals as a substitute of using skip in a more generic query.

To skip a specific number of results:

    https://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,%27S1A\_EW\_GRD%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$skip=23

 The default value is set to 0.

Whenever a query results in more products than 20 (default top value), the API provides a nextLink at the bottom of the page:

    "@OData.nextLink": 
    "http://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,'S1A\_EW\_GRD')+and+ContentDate/Start+gt+2022-05-03T00:00:00.000Z+and+ContentDate/Start+lt+2022-05-03T12:00:00.000Z&$skip=20"

The acceptable arguments for this option: *Integer \<0,10000\>*

## Count option

Count option enables users to get the exact number of products matching the query. This option is disabled by default to accelerate the query performance.

To get the exact number of products for a given query:

    https://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,%27S1A\_EW\_GRD%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$count=True

 The acceptable arguments for this option: *True, true, 1, False, false, 0*.

## Expand option

Expand option enables users to see full metadata of each returned result.

To see the metadata of the results:

    https://datahub.creodias.eu/odata/v1/Products?$filter=contains(Name,%27S1A\_EW\_GRD%27)%20and%20ContentDate/Start%20gt%202022-05-03T00:00:00.000Z%20and%20ContentDate/Start%20lt%202022-05-03T12:00:00.000Z&$expand=Attributes

 The acceptable arguments for this option: *Attributes*

## Product Download

To download products:

Where Id is an Id of the product returned by the search query, e.g.:

    https://datahub.creodias.eu/odata/v1/Products(a6212de3-f2e4-58c2-840b-7f42c3c8c612)/$value

Only authorized users are allowed to download products

To get the token:

    KEYCLOAK\_TOKEN=$(curl -s --location --request POST 'https://identity.dataspace.copernicus.eu/auth/realms/\<BRAND\>/protocol/openid-connect/token' \
    --data-urlencode 'grant\_type=password' \
    --data-urlencode 'username=\<USER\>' \
    --data-urlencode 'password=\<PASSWORD\>' \
    --data-urlencode 'client\_id=CLOUDFERRO\_PUBLIC'|jq .access\_token|tr -d '"')

or

    ' -d 'password=' -d 'grant\_type=password' 'https://identity.dataspace.copernicus.eu/auth/realms//protocol/openid-connect/token' | python -m json.tool | grep "access\_token" | awk -F\" '{print $4}')]]\>

Where USER and PASSWORD are credentials to Your CloudFerro account in specific BRAND. Brand names are listed below with API from which You can get your token.

| **Brand names** | **API** |
| --- | --- |
| dias | [https://identity.dataspace.copernicus.eu/auth/realms/dias/protocol/openid-connect/token](https://identity.cloudferro.com/auth/realms/dias) |
| Creodias-new | [https://identity.dataspace.copernicus.eu/auth/realms/Creodias-new/protocol/openid-connect/token](https://identity.cloudferro.com/auth/realms/Creodias-new) |
| CODE-DE-EL | [https://identity.dataspace.copernicus.eu/auth/realms/CODE-DE-EL/protocol/openid-connect/token](https://identity.cloudferro.com/auth/realms/CODE-DE-EL) |
| wekeo-elasticity | [https://identity.dataspace.copernicus.eu/auth/realms/wekeo-elasticity/protocol/openid-connect/token](https://identity.cloudferro.com/auth/realms/wekeo-elasticity) |
| Eumetsat-elasticity | [https://identity.dataspace.copernicus.eu/auth/realms/Eumetsat-elasticity/protocol/openid-connect/token](https://identity.cloudferro.com/auth/realms/Eumetsat-elasticity) |

To download the product:

    curl -H "Authorization: Bearer $KEYLOAK\_TOKEN" 'https://datahub.creodias.eu/odata/v1/Products(060882f4-0a34-5f14-8e25-6876e4470b0d)/$value' --output /tmp/product.zip

or

    wget  --header "Authorization: Bearer $KEYCLOAK\_TOKEN" 'http://datahub.creodias.eu/odata/v1/Products(db0c8ef3-8ec0-5185-a537-812dad3c58f8)/$value' -O example\_odata.zip