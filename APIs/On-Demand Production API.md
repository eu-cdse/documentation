## Introduction
On-demand processing capability for CARD-BS, CARD-COH6/12 is available on the Copernicus Data Space Ecosystem. This service is offered free to the use via a limited pool of resources, shared across all users, which can be used for processing the data free of charge. This is suitable for users who need to process smaller batches of products. There is no guarantee that processing will be completed in certain time.  For commercial use the price list is available from the Creodias portal [https://creodias.eu/billing-models](https://creodias.eu/billing-models).The service is available via an On Demand Processing API allows the users to interact with the service to issue and control the orders. It provides functionalities like creation, update, cancellation, pausing and monitoring of orders. This allows the users to have a better control over the workflow execution process. 
## OnDemand Processing API with OData interface
The OnDemand Processing API allows the users to interact with the service to issue and control the orders. It provides functionalities like creation, update, cancellation, pausing and monitoring of orders. This allows the users to have a better control over the workflow execution process.
## General information
This documentation provides an overview of the OnDemand Processing (ODP) API, which is based on the Open Data Protocol (OData) standard. The ODP API provides a RESTful interface for accessing data and metadata from the Copernicus data catalogue.
Access to the API is limited by the Authentication service. Quotas are assigned according to the user typology and include limits on number of concurrent orders and available processing workflows.
The API allows discovery of all available workflows which can be run in the CDSE platform, indicating which data types can be processed, what are the available parameters and output modes.
### API Endpoint
The **ODP API endpoint is [https://odp.dataspace.copernicus.eu/odata/v1](https://odp.dataspace.copernicus.eu/odata/v1)**. The endpoint supports both HTTP and HTTPS protocols.

**OpenAPI documentation is located at [https://odp.dataspace.copernicus.eu/odata/docs](https://odp.dataspace.copernicus.eu/odata/docs)**
### API Operations
The ODP API supports the following operations:
- GET: This operation is used to retrieve data and metadata from the ODP. The GET operation supports various query options to filter, order, and limit the data retrieved.
- POST: This operation is used to create new entities in the ODP. The POST operation requires a payload in JSON format that specifies the properties of the new entity.
- PATCH: This operation is used to update existing entities in the ODP. The PATCH operation requires a payload in JSON format that specifies the properties of the entity to update.
- DELETE: This operation is used to delete existing entities from the ODP. The DELETE operation requires the URL of the entity to delete.
### API Resources
The ODP API provides access to the following resources:
- Workflow: predefined processor which creates a single output product or series of products based on the input parameters provided by the user. Typical inputs are name of the source product and parameters specific to the processing chain.
- Production Order: request for production using a Workflow chosen by the user.
- Batch Order: request for production of multiple products using a chosen Workflow.
- Order Item: single processing job within and Production Order or Batch Order.
### Authentication
To access the ODP API you need an authorization token as only authorized users are allowed to interact with the processing service.
To get the token you can use the following script:
````
export KEYCLOAK_TOKEN=$(curl -d 'client_id=cdse-public' \
-d 'username=<LOGIN>' \
-d 'password=<PASSWORD>' \
-d 'grant_type=password' \
'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token' | \
python -m json.tool | grep "access_token" | awk -F\" '{print $4}')
````
Once you have your token, you can execute request to the API including the token in the request header. For example to list available Workflows you can use the following command:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 'https://odp.dataspace.copernicus.eu/odata/v1/Workflows'
````
More information on the tokens and authentication can be found here: [https://documentation.dataspace.copernicus.eu/APIs/OData.html#product-download](https://documentation.dataspace.copernicus.eu/APIs/OData.html#product-download)
## Querying the API
### Workflows
#### Listing available Workflows
To list all processing Workflows available to the user:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/Workflows
````
To search for specific Workflows you can use filters on the attributes. To find workflow named “coh”:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/Workflows?$filter=Name eq 'coh'
````
In a similar way to find all Workflows suitable for processing Sentinel-1 SLC products:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/Workflows?
$filter=contains(InputProductType,'SL````C')
````
Details of the Workflow in the response list the parameters which are needed to create new Production Order:
````
        {
            "Id": "47",
            "Name": "card_coh12_public",
            "DisplayName": "Sentinel-1: Coherence (12 days)",
            "Documentation": null,
            "Description": "The Sentinel-1 CARD COH12 (Copernicus Analysis Ready
             Data Coherence) processor generates a Sentinel-1 Level 2 product describing 
             the coherence of a pair of images - 12 days apart. 
             Concurrently, a terrain-correction (using DEM) is performed. This processor 
             provided by the Joint Research Centre is based on a GPT graph that can be run 
             with ESA SNAP.",
            "InputProductType": "SLC",
            "InputProductTypes": [
                "SLC",
                "S1_SLC__1S",
                "S2_SLC__1S",
                "S3_SLC__1S",
                "S4_SLC__1S",
                "S5_SLC__1S",
                "S6_SLC__1S",
                "IW_SLC__1S",
                "EW_SLC__1S",
                "WV_SLC__1S"
            ],
            "OutputProductType": "CARD-COH12",
            "WorkflowVersion": "3.1.0"
        }
````
### Production Orders
#### Create a new Production Order
To submit a new processing job you need to use the POST method and send the parameters as a JSON message according to the requirements of a specific Workflows:
````
curl -X POST -H 'Content-Type:application/json' \
-H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrder/OData.CSC.Order \
-d '<json_message>'
````
Production orders accept the following general parameters:
- WorkflowName: the  identifier of the workflow – “Name” attribute in the /Workflows response
- InputProductReference: information about the input data to be used by the processor
    - Reference: identifier of a single input product or multiple products (example – mosaicking processors)
    - ContentDate: time period which should be used by the Workflows (example - time-series based processors)
- WorkflowOptions: parameters specific to the Workflows (example – DEM version, cloud coverage)
- Priority: priority of the order in the users job queue. Orders with higher priority will be processed first
- NotificationEndpoint: (not used) URL of the endpoint which should receive the information once the order is completed (done or failed)
- Name: non-unique name for the order to help identify the orders
The structure of the JSON message:
````
{
  "WorkflowName": "string",
  "InputProductReference": {
    "Reference": "string",
    "ContentDate": {
      "Start": "YYYY-MM-DDTHH:mm:ss.SSSZ",
      "End": "YYYY-MM-DDTHH:mm:ss.SSSZ"
    }
  },
  "WorkflowOptions": [
    {
      "Name": "string",
      "Value": "string"
    }
  ],
  "Priority": 0,
  "NotificationEndpoint": "string",
  "Name": "string"
}
````
Example: to submit an order for the Sentinel-1 CARD Backscatter product:
````
curl -X POST -H 'Content-Type:application/json' \
-H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrder/OData.CSC.Order \
-d '{ \
  "WorkflowName": "card_bs",
  "InputProductReference": {
    "Reference": "S1A_IW_GRDH_1SDV_20230404T162838_20230404T162903_047949_05C333_B4FC.SAFE"
  },
  "Priority": 1,
  "Name": "card_bs_order_1"
}'
````
Sample response after successful submission of the order:
````
{
  "@odata.context": "$metadata#OData.CSC.Order",
  "value": {
    "Id": "9999999",
    "Status": "queued",
    "StatusMessage": "queued",
    "SubmissionDate": "2023-04-05T10:03:25.474Z",
    "Name": "S1A_IW_GRDH_1SDV_20230404T162838_20230404T162903_047949_05C333_B4FC.SAFE",
    "EstimatedDate": "2023-04-05T10:33:16.161Z",
    "InputProductReference": {
      "Reference": S1A_IW_GRDH_1SDV_20230404T162838_20230404T162903_047949_05C333_B4FC.SAFE",
      "ContentDate": null
    },
    "WorkflowOptions": [],
    "WorkflowName": "card_bs",
    "WorkflowId": null,
    "Priority": 1
  }
}
````
#### Check list of Production Orders
To list all Production Orders requested by the user:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrders
````
When looking for completed orders for a specific processor:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
"https:// odp.dataspace.copernicus.eu/odata/v1/ProductionOrders?
$filter=WorkflowName eq 'coh' and Status eq 'completed'"
````
#### Check the status of a single Production Order
To check details of the single order using the order Id:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
'https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrders(<order_id>)'
````
#### Cancel a Production Order
To cancel an existing order:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
'https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrder(<order_id>)/
OData.CSC.Cancel'
````
The orders which are in the queue and not yet processed will be removed instantly. For the orders in processing, the Order Items (single item within a Production Order) being processed will complete but the remaining part of the Order will be canceled.
#### Display details of the result
The order generates a new product which can be downloaded from the public repository or private storage. To check the details of the result:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
"https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrder(<order_id>)/Product"
````
#### Download the result
Once the order is successfully processed the status changes to completed and the result is ready for download. The user may choose to instruct the service to put the results in a specified location (mandatory if custom parameters have been passed to the Workflow), and standard results (for Workflows like CARD-BS or CARD-COH12) are stored in the CDSE public repository and can be retrieved through the API.
To download the result:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
'https://odp.dataspace.copernicus.eu/odata/v1/ProductionOrder(<order_id>)/Product/$value' \
-o result.zip
````
### Batch Orders
#### Create a new Batch Order
In a way similar to single Production Order you can request processing of multiple input products as a Batch Order. The Batch Order will run a selected Workflow with the same parameters for all inputs and output the results to the same location. Using Batch Orders makes it easier to process time series or large AOIs.
Batch Order endpoint uses the same mechanism as described for the Production Order:
````
curl -X POST -H 'Content-Type:application/json' \
-H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/BatchOrder/OData.CSC.Order \
-d '<json_message>'
````
Batch Orders accept the following general parameters:
- WorkflowName: the  identifier of the workflow – “Name” attribute in the /Workflows response
- IdentifierList: information about the input data to be used by the processor - identifiers of products
- WorkflowOptions: parameters specific to the Workflows (example – DEM version, cloud coverage)
- Priority: priority of the order in the users job queue. Orders with higher priority will be processed first
- Callback: (not used) URL of the endpoint which should receive the information once the order is completed (done or failed)
- Name: non-unique name for the order to help identify the orders
- BatchSize: maximum number of items in the batch
- BatchVolume: maximum size of output data
The structure of the JSON message:
````
{
  "Name": "string",
  "Priority": 0,
  "WorkflowName": "string",
  "Callback": "string",
  "WorkflowOptions": [
    {
      "Name": "string",
      "Value": "string"
    }
  ],
  "IdentifierList": [
    "string"
  ],
  "BatchSize": 0,
  "BatchVolume": 0
}
````
#### Check list of Batch Orders
To list all Production Orders requested by the user:
````
curl -X POST -H 'Content-Type:application/json' \
-H "Authorization: Bearer $KEYCLOAK_TOKEN" \ 
https://odp.dataspace.copernicus.eu/odata/v1/BatchOrder
````
When looking for batch orders for a specific processor:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
"https:// odp.dataspace.copernicus.eu/odata/v1/BatchOrder?$filter=WorkflowName eq 'coh'
````
#### Check the status of a single Batch Order
To check details of the single order using the order Id:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
'https://odp.dataspace.copernicus.eu/odata/v1/BatchOrder(<batch_order_id>)'
````
#### List products generated in a Batch Order
When the batch order is processed, for each input product an output is generated. To list the output of a batch:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
'https://odp.dataspace.copernicus.eu/odata/v1/BatchOrder(<batch_order_id>)/Products'
````
#### Display details of the results
Each item in the batch is an individual Production Order. To check the details of the single result:
````
curl -H "Authorization: Bearer $KEYCLOAK_TOKEN" \
"https://odp.dataspace.copernicus.eu/odata/v1/BatchOrder(<batch_order_id>)/Product(<order_id>)"
````


