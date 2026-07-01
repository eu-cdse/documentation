# Quotas and Limitations

Every user account is set a limited quota to guarantee fair sharing of free tier resources within all users of Copernicus Data Space Ecosystem.  
  
The following limitations and quotas are monthly and reset on the first day of every month:  

- Requests per month
- Requests per minute
- Processing units (PU) per month
- Processed Products per month
- Credits per month

The following limitations and quotas are applied based on a rolling window of 30 days:  

- Monthly transfer limit (TB)

The total volume of downloads from the Copernicus Data Space Ecosystem for each user account is summed up for the last 30 days. Downloaded volume is checked on an hourly basis, and if it exceeds the assigned quota, then that user will be moved to a slower interface. Such a user will still be able to access and download products but at a reduced speed.  
  
Once the cumulative transfer for the last 30 days falls below the limit, the transfer speed will be restored to its nominal capacity.  
  
In addition, the following limitations apply continuously:  

- Number of concurrent connections limit
- Bandwidth limit per connection

If you need more quota, please find information on commercial cloud credits and sponsorship applications [here](https://documentation.dataspace.copernicus.eu/FAQ.html#what-to-do-if-run-out-of-quota).

## Copernicus General Users

| Limitations | S3, OData, STAC | Data Workspace API | openEO API / Algorithm plaza | Sentinel Hub APIs⁸ | Direct HTTP access to COGs |
|----|:--:|:--:|:--:|:--:|:--:|
| Requests per month | \- | \- | \- | 10 000 | 50 000⁷ ⁹ |
| Requests per minute | 2000¹⁴ | \- | 12¹¹ ¹³ | 300 | \- |
| Processing units (PU) per month | \- | \- | \- | 10 000 | \- |
| Processing units (PU) per minute | \- | \- | \- | 300 | \- |
| Bandwidth limit per connection (MB/s) (IAD¹) | 20 | \- | \- | \- | \- |
| Number of concurrent connections limit (IAD¹) | 4 | \- | \- | \- | \- |
| Monthly transfer limit (TB) (IAD¹)¹⁰ | 12 | \- | \- | \- | \- |
| Number of concurrent orders limit (DAD²) | \- | 1 | \- | \- | \- |
| Monthly transfer limit (TB) (DAD²) | \- | 0,1 | \- | \- | \- |
| Processed Products per month | \- | 25 | \- | \- | \- |
| Concurrent Processing | \- | 2¹² | 2 | \- | \- |
| Number of active sessions³ | 100 | \- | \- | \- | \- |
| A token stays active for⁴ | 10 minutes | \- | \- | \- | \- |
| A token can be refreshed in⁵ | 60 minutes | \- | \- | \- | \- |
| Number of products that be accessed with one token⁶ | No limits | \- | \- | \- | \- |
| Credits per month | \- | \- | 10 000¹⁵ | \- | \- |
| Concurrent API requests | \- | \- | 2 | \- | \- |

  
¹ IAD: Immediately Available Data.  
² DAD: Deferred Available Data (known as Offline data). It is not possible to order DAD by using OData,STAC or S3, Copernicus Browser or any of the Sentinel Hub APIs. DAD (Offline data) can only be ordered by using the Data Workspace. Only after ordering, it can be downloaded from the catalogue by using the download APIs.  
³ This includes, among others, a newly generated token and logging in to the user panel. Please refer to: [Device Activity](https://identity.dataspace.copernicus.eu/auth/realms/CDSE/account/#/security/device-activity) and see the number of signed in devices - It is not possible to increase this number to a bigger value than 100, with a paid plan. Each session starts when the user generates a new token and use it for the downloading process. One session ends when the token reaches its expiry time (a token stays active for 10 min).  
⁴ After reaching this limit, the Access Token must either be refreshed by using the [Refresh Token](https://documentation.dataspace.copernicus.eu/APIs/OData.html#product-download) or be re-generated.  
⁵ Anytime within 60 minutes after the access token is generated.  
⁶ As long as any other limit(s) are not breached.  
⁷ Extensions are available via CREODIAS offering.  
⁸ Similar principles apply for all SentinelHub APIs while the differences and details are covered in the [Processing Unit](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/ProcessingUnit.html) section of our documentation. Note that there are APIs that are not available to Copernicus General Users such as Sentinel Hub Batch Processing API.  
⁹ Technical limitation may be applied to maintain platform stability.  
¹⁰ After reaching this monthly transfer limit, the maximum bandwidth drops to 1MB/s and the number of concurrent connections drops to 1.  
¹¹ Only enabled for openEO synchronous execution requests (`POST /result`) and batch execution requests (`POST /{job_id}/result`).  
¹² The maximum number of simultaneous production orders items running in parallel, i.e. the orders in “In progress” status, orders items as products items.  
¹³ 1 request per 5 seconds.  
¹⁴ Only applies to S3.  
¹⁵ Temporary Boost of monthly openEO Credits to 10 000. [Read our news item](https://dataspace.copernicus.eu/news/2024-9-3-temporary-boost-monthly-openeo-credits-10000-granted-user) published on September 3, 2024.  
