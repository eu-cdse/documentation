# Frequently Asked Questions

## General

<details>
  <summary>What is the phase-out timing for the current Copernicus Data Hub distribution services?</summary>
  <p>
   The legacy Copernicus Data Hub distribution service will remain in operations until end of June 2023 to allow a smooth migration to the new Copernicus Data Access service by all user communities. The Copernicus Data Hub distribution service will continue offering access to Sentinel data  with a gradual ramp-down of the operations capacity and data offering until end of September 2023.
  </p>
</details>


<details>
  <summary>Comparing with existing legacy Copernicus Data Hub, what will be the other free services other than stac/cog?</summary>
    <p>
    Compared to existing Copernicus Data Hub, there will indeed be additional APIs - OGC interfaces (WMS, WMTS, WCS), OpenEO, Sentinel Hub API, S3, and others. Please refer to the <a href="#/Roadmap">Roadmap</a> for more info on the timing of these interfaces.
    </p>
</details>

<details>
  <summary>Is there an end user document available online that describes the specific data products available and specific services?</summary>
    <p>
    The user level document describing the details for every service and dataset can be found <a href="#/Applications/Browser">here</a>(LINK WILL LATER BE UPDATED).
     </p>
</details>
<details>
  <summary>How long is the project timescale in total ?</summary>
    <p>
   The time scale of the project is 6 years (ie. to the end of 2028) with an optional extension up to 10 years (ie. 2032).
     </p>
</details>
<details>
  <summary>Can anyone outside from Europe have free access to any data?</summary>
    <p>
   Yes, data and services will be available to users worldwide.
     </p>
</details>

## Data

<details>
  <summary>What data will be offered online and what is the timeline for the following months?</summary>
    <p>
    For the details on the data offer and timing, we would like to refer to the <a href="#/Roadmap">Roadmap</a>
     </p>
</details>
<details>
  <summary>Is there a page that indicates anomalies with the datasets?</summary>
    <p>
    A dashboard where any user can find planned and unplanned anomalies per Sentinel satellite is available in this <a href="https://operations.dashboard.copernicus.eu/index" target="_blank">link</a>
     </p>
</details>
<details>
  <summary>With regard to cloud native formats/interfaces, will the data also be available in the original data formats (e.g. for data downloading)?</summary>
    <p>
    Yes, data will also be available in original data formats (i.e. .SAFE).
     </p>
</details>
<details>
  <summary>At the moment some of the data are delivered in Jpeg2000, is there any plan to abandon that format for the COG?</summary>
    <p>
    There is currently no plan to convert Sentinel-2 in COGs. However, there is a parallel activity happening within ESA to define format evolution for all Sentinels which will be followed, once decisions are taken. But this is not something that is happening on the short term.
     </p>
</details>
<details>
  <summary>Will data, such as Sentinel-2, be processed to a consistent version?</summary>
    <p>
    The Sentinel-2 data will be available at the latest processing baseline. And with the reprocessing of Sentinel-2 happening in parallel (out of scope of this project), these will become available on this service as well.
     </p>
</details>
<details>
  <summary>Is it possible to download a subset of data corresponding to an AOI, instead of the whole image?</summary>
    <p>
    Yes, you will be able to download a subset of data, either using S3 interface, or dedicated APIs, i.e. Sentinel Hub, OpenEO when they become available. See <a href="#/Roadmap">Roadmap</a> section of the documentation.
     </p>
</details>
<details>
  <summary>Are the data offered via Cloud Optimized Geotiffs (also Level 1)?</summary>
    <p>
    Sentinel-1 GRD data will be available in COG format. Sentinel-2 will stay in JP2 for the moment, as it is a similarly performant cloud optimised format.
     </p>
</details>
<details>
  <summary>When "on-line data" is mentioned, does that mean the data are not on tape?</summary>
    <p>
    The “on-line data” or IAD we are referring to, are indeed not on the tapes.  Tapes will still be there for redundancy reasons.
     </p>
</details>
<details>
  <summary>For the S3 access in the free tier, will there be no cost for network traffic?</summary>
    <p>
    S3 access will be part of free services as well, within the same constraints as the rest of the services.
     </p>
</details>
<details>
  <summary>Can we download the data acquired by all Sentinel missions (1, 2, 3, 5P, 6) and the other satellites (e.g. Meteosat) via the new interface? Some missions are not managed by ESA, but by EUMETSAT for example.</summary>
    <p>
    Initialy Sentinel 1, Sentinel 2, Sentinel 3 and Sentinel 5P data up to L2 products will be available. Sentinel 6 data and data from Meteosat are currently not in the roadmap of the project. However access to Copernicus Contributing Missions CORE Datasets, Digital Elevation Models, data from Copernicus Services and additional data sets such as Landsat and ENVISAT and Belgian Collaborative Ground Segment hosted data are planned in the future. The <a href="#/Roadmap/DataTable.html">Data Roadmap</a> shows how the Copernicus Data Space Ecosystem will be continously upgraded and how more data will become available.
     </p>
</details>
<details>
  <summary>Will it still be the case that data is labelled as “on/offline" on the current legacy portal?</summary>
    <p>
    The vast majority of the data will be on-line : all Sentinel-2 L1C/L2A, Sentinel-1 SLC/GRD  and just about all other relevant data collections.
     </p>
</details>
<details>
  <summary>Will the new interface offer EO ready-to-use products or just L0 and L1 data?</summary>
    <p>
    Up to L2 products will be available. The <a href="#/Roadmap">Roadmap</a> shows how the Copernicus Data Space Ecosystem will be continously upgraded and how more data become available.
     </p>
</details>

## Services

<details>
  <summary>Will there be an integrated free and commercial offering to support/encourage the transfer of the users from "try basics for free towards paid subscriptions"?</summary>
    <p>
    Yes, there will be a common user identity, which will allow registered users to seamlessly transfer between systems. This will also extend to other systems that will be added to the free tier to the commerical tier ecosystem in the future, assuming they will integrate it.
     </p>
</details>
<details>
  <summary>When we develop an EO ready-to-use product, could we integrate it into the interface and ask the payment from clients?</summary>
    <p>
    Yes, commercial services can be built on top, similar to Copernicus open license.
     </p>
</details>
<details>
  <summary>Can the user come with wish-list to services data products?</summary>
    <p>
    User can come with suggestions to improve or expand the service portfolio. A user forum will be set up and released by July to accommodate this.
     </p>
</details>
<details>
  <summary>Are you going to develop new services on DAS after July 2023?</summary>
    <p>
    Yes, a marketplace will be available where new Third party services will be able to onboard from July onwards to expand the ecosystem.
     </p>
</details>
<details>
  <summary>Is there any limitation on the max number of downloads at one time?</summary>
    <p>
    Yes, there will be quotas and constraints for different services.
     </p>
</details>

## Registration and authentication

<details>
  <summary>Will there be an integrated free and commercial offering to support/encourage the transfer of the users from "try basics for free towards paid subscriptions"?</summary>
    <p>
    Yes, there will be a common user identity, which will allow registered users to seamlessly transfer between systems. This will also extend to other systems that will be added to the free tier to the commerical tier ecosystem in the future, assuming they will integrate it.
     </p>
</details>
<details>
  <summary>If I'm having troubles with registering, what can I do?</summary>
    <p>
    Please e-mail the <a href="mailto:help-login@dataspace.copernicus.eu">help-login@dataspace.copernicus.eu</a> address for direct support on this matter.
     </p>
</details>

## APIs

<details>
  <summary>SNAP/gpt processing codes can be used in these on-line and cloud processing services?</summary>
    <p>
    SNAP is integrated in cloud environment, and there will even be some dedicated on-demand services based on SNAP  (i.e. S1 processing to coherence, etc). 
     </p>
</details>
<details>
  <summary>Is a STAC catalog planned ? Will the data be accessible on cloud object storage (S3)?</summary>
    <p>
    STAC Catalog API is indeed planned.  Note that the phase-in will take from end of January to July 2023.  So services will be added during this timeline, not everything will be available at the beginning. All the data will be available over S3 as well.
     </p>
</details>
<details>
  <summary>Will LTA process be discontinued when all archived data become online?</summary>
    <p>
    There will still be services available for so called “deferred data access” :  data collections that are not commonly used. That said, all most relevant collections will be available on-line.  The <a href="#/Roadmap">Roadmap</a> shows how the Copernicus Data Space Ecosystem will be continously upgraded and how more data become available.
     </p>
</details>
<details>
  <summary>Will the platform use STAC standards?</summary>
    <p>
    Yes, there will be STAC compliant Catalog API, as well as STAC items for inpidual products.
     </p>
</details>
<details>
  <summary>Any plan to offer the Pangeo platform for a "pythonist"?</summary>
    <p>
    This is currently not in the offer or roadmap.
     </p>
</details>

## Documentation

<details>
  <summary>Is there any difference between EU users and non-EU users?</summary>
    <p>
    There is no difference between EU users and non-EU users. That said, there will be a continuity of the accounts with higher throughput, managed by ESA (i.e. Copernicus Services, International Hub, etc.).
     </p>
</details>
<details>
  <summary>Which distribution channels will be available for high-throughput data access? I assume the public side (dataspase.copernicus.eu) has a bandwidth limitation. Or does the public side have user tiers, or is high-throughput data transfer (such as https://creodias.eu/remote-transfer-for-eodata) only a paid service?</summary>
    <p>
    All distribution options (i.e. OData, S3, Sentinel Hub,..) will be constrained with user quotas, which includes both bandwidth limitation, as well as monthly limits.
     </p>
</details>
<details>
  <summary>Can you give indictions about the cost of the "extra" services?</summary>
    <p>
    Pricing will be published soon.
     </p>
</details>
<details>
  <summary><span>
  This December advertisement of <a href="https://medium.com/sentinel-hub/new-copernicus-data-access-service-to-support-the-ecosystem-for-earth-observation-412f829355a3">DAS</a> says that "For those interested in processing, there will be scalable cloud resources available, optimized for EO tasks". Does this refer to the current CreoDIAS resources, or something completely new that hasn't been addressed yet?
  </span>
  </summary>
    <p>
    Scalable cloud resources will be part of the commercial offering and can be obtained at <a href = "https://creodias.eu/">CREODIAS</a> in first instance. ICT-wise, there will be two options, including Open Telekom Cloud.
     </p>
</details>
<details>
  <summary>Are there tutorials (online & physical meetings) to use the new interface?</summary>
    <p>
    Tutorials will be added to the documentation in due time explaining the usage of the different interfaces. We will also be present on different conferences explaining the service & ecosystem.
     </p>
</details>
