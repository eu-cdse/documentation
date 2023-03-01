# Frequently Asked Questions

## General

<details>
  <summary>What is the phase-out timing for the current Copernicus Data Hub distribution services?</summary>
    <div>
    The legacy Copernicus Data Hub distribution service will remain in operations until end of June 2023 to allow a smooth migration to the new Copernicus Data Access service by all user communities. The Copernicus Data Hub distribution service will continue offering access to Sentinel data  with a gradual ramp-down of the operations capacity and data offering until end of September 2023.
    </div>
</details>
<details>
  <summary>Comparing with existing legacy Copernicus Data Hub, what will be the other free services other than stac/cog?</summary>
    <div>
    Compared to existing Copernicus Data Hub, there will indeed be additional APIs - OGC interfaces (WMS, WMTS, WCS), OpenEO, Sentinel Hub API, S3, and others. Please refer to the <a href="#/Roadmap">Roadmap</a> for more info on the timing of these interfaces.
    </div>
</details>
<details>
  <summary>Is there an end user document available online that describes the specific data products available and specific services?</summary>
    <div>
    The user level document describing the details for every service and dataset can be found <a href="#/Applications/Browser">here</a>(LINK WILL LATER BE UPDATED).
    </div>
</details>
<details>
  <summary>How long is the project timescale in total ?</summary>
    <div>
   The time scale of the project is 6 years (ie. to the end of 2028) with an optional extension up to 10 years (ie. 2032).
    </div>
</details>
<details>
  <summary>Can anyone outside from Europe have free access to any data?</summary>
    <div>
   Yes, data and services will be available to users worldwide.
    </div>
</details>

## Data

<details>
  <summary>What data will be offered online and what is the timeline for the following months?</summary>
    <div>
    For the details on the data offer and timing, we would like to refer to the <a href="#/Roadmap">Roadmap</a>
    </div>
</details>
<details>
  <summary>Is there a page that indicates anomalies with the datasets?</summary>
    <div>
    A dashboard where any user can find planned and unplanned anomalies per Sentinel satellite is under construction and should be availabe in a short timeframe.
    </div>
</details>
<details>
  <summary>With regard to cloud native formats/interfaces, will the data also be available in the original data formats (e.g. for data downloading)?</summary>
    <div>
    Yes, data will also be available in original data formats (i.e. .SAFE).
    </div>
</details>
<details>
  <summary>At the moment some of the data are delivered in Jpeg2000, is there any plan to abandon that format for the COG?</summary>
    <div>
    There is currently no plan to convert Sentinel-2 in COGs. However, there is a parallel activity happening within ESA to define format evolution for all Sentinels which will be followed, once decisions are taken. But this is not something that is happening on the short term.
    </div>
</details>
<details>
  <summary>Will data, such as Sentinel-2, be processed to a consistent version?</summary>
    <div>
    The Sentinel-2 data will be available at the latest processing baseline. And with the reprocessing of Sentinel-2 happening in parallel (out of scope of this project), these will become available on this service as well.
    </div>
</details>
<details>
  <summary>Is it possible to download a subset of data corresponding to an AOI, instead of the whole image?</summary>
    <div>
    Yes, you will be able to download a subset of data, either using S3 interface, or dedicated APIs, i.e. Sentinel Hub, OpenEO when they become available. See <a href="#/Roadmap">Roadmap</a> section of the documentation.
    </div>
</details>
<details>
  <summary>Are the data offered via Cloud Optimized Geotiffs (also Level 1)?</summary>
    <div>
    Sentinel-1 GRD data will be available in COG format. Sentinel-2 will stay in JP2 for the moment, as it is a similarly performant cloud optimised format.
    </div>
</details>
<details>
  <summary>When "on-line data" is mentioned, does that mean the data are not on tape?</summary>
    <div>
    The “on-line data” or IAD we are referring to, are indeed not on the tapes.  Tapes will still be there for redundancy reasons.
    </div>
</details>
<details>
  <summary>For the S3 access in the free tier, will there be no cost for network traffic?</summary>
    <div>
    S3 access will be part of free services as well, within the same constraints as the rest of the services.
    </div>
</details>
<details>
  <summary>Can we download the data acquired by all Sentinel missions (1, 2, 3, 5P, 6) and the other satellites (e.g. Meteosat) via the new interface? Some missions are not managed by ESA, but by EUMETSAT for example.</summary>
    <div>
    Initialy Sentinel 1, Sentinel 2, Sentinel 3 and Sentinel 5P data up to L2 products will be available. Sentinel 6 data and data from Meteosat are currently not in the roadmap of the project. However access to Copernicus Contributing Missions CORE Datasets, Digital Elevation Models, data from Copernicus Services and additional data sets such as Landsat and ENVISAT and Belgian Collaborative Ground Segment hosted data are planned in the future. The <a href="#/Roadmap/DataTable.html">Data Roadmap</a> shows how the Copernicus Data Space Ecosystem will be continously upgraded and how more data will become available.
    </div>
</details>
<details>
  <summary>Will it still be the case that data is labelled as “on/offline" on the current legacy portal?</summary>
    <div>
    The vast majority of the data will be on-line : all Sentinel-2 L1C/L2A, Sentinel-1 SLC/GRD  and just about all other relevant data collections.
    </div>
</details>
<details>
  <summary>Will the new interface offer EO ready-to-use products or just L0 and L1 data?</summary>
    <div>
    Up to L2 products will be available. The <a href="#/Roadmap">Roadmap</a> shows how the Copernicus Data Space Ecosystem will be continously upgraded and how more data become available.
    </div>
</details>

## Services
<details>
  <summary>Will there be an integrated free and commercial offering to support/encourage the transfer of the users from "try basics for free towards paid subscriptions"?</summary>
    <div>
    Yes, there will be a common user identity, which will allow registered users to seamlessly transfer between systems. This will also extend to other systems that will be added to the free tier to the commerical tier ecosystem in the future, assuming they will integrate it.
    </div>
</details>
<details>
  <summary>When we develop an EO ready-to-use product, could we integrate it into the interface and ask the payment from clients?</summary>
    <div>
    Yes, commercial services can be built on top, similar to Copernicus open license.
    </div>
</details>
<details>
  <summary>Can the user come with wish-list to services data products?</summary>
    <div>
    User can come with suggestions to improve or expand the service portfolio. A user forum will be set up and released by July to accommodate this.
    </div>
</details>
<details>
  <summary>Are you going to develop new services on DAS after July 2023?</summary>
    <div>
    Yes, a marketplace will be available where new Third party services will be able to onboard from July onwards to expand the ecosystem.
    </div>
</details>
<details>
  <summary>Is there any limitation on the max number of downloads at one time?</summary>
    <div>
    Yes, there will be quotas and constraints for different services.
    </div>
</details>

## Registration and authentication
<details>
  <summary>Will there be an integrated free and commercial offering to support/encourage the transfer of the users from "try basics for free towards paid subscriptions"?</summary>
    <div>
    Yes, there will be a common user identity, which will allow registered users to seamlessly transfer between systems. This will also extend to other systems that will be added to the free tier to the commerical tier ecosystem in the future, assuming they will integrate it.
    </div>
</details>
<details>
  <summary>If I'm having troubles with registering, what can I do?</summary>
    <div>
    Please e-mail the help-cdse-login@dataspace.copernicus.eu address for direct support on this matter.
    </div>
</details>

## APIs
<details>
  <summary>SNAP/gpt processing codes can be used in these on-line and cloud processing services?</summary>
    <div>
    SNAP is integrated in cloud environment, and there will even be some dedicated on-demand services based on SNAP  (i.e. S1 processing to coherence, etc). 
    </div>
</details>
<details>
  <summary>Is a STAC catalog planned ? Will the data be accessible on cloud object storage (S3)?</summary>
    <div>
    STAC Catalog API is indeed planned.  Note that the phase-in will take from end of January to July 2023.  So services will be added during this timeline, not everything will be available at the beginning. All the data will be available over S3 as well.
    </div>
</details>
<details>
  <summary>Will LTA process be discontinued when all archived data become online?</summary>
    <div>
    There will still be services available for so called “deferred data access” :  data collections that are not commonly used. That said, all most relevant collections will be available on-line.  The <a href="#/Roadmap">Roadmap</a> shows how the Copernicus Data Space Ecosystem will be continously upgraded and how more data become available.
    </div>
</details>
<details>
  <summary>Will the platform use STAC standards?</summary>
    <div>
    Yes, there will be STAC compliant Catalog API, as well as STAC items for individual products.
    </div>
</details>
<details>
  <summary>Any plan to offer the Pangeo platform for a "pythonist"?</summary>
    <div>
    This is currently not in the offer or roadmap.
    </div>
</details>

## Documentation

<details>
  <summary>Is there any difference between EU users and non-EU users?</summary>
    <div>
    There is no difference between EU users and non-EU users. That said, there will be a continuity of the accounts with higher throughput, managed by ESA (i.e. Copernicus Services, International Hub, etc.).
    </div>
</details>
<details>
  <summary>Which distribution channels will be available for high-throughput data access? I assume the public side (dataspase.copernicus.eu) has a bandwidth limitation. Or does the public side have user tiers, or is high-throughput data transfer (such as https://creodias.eu/remote-transfer-for-eodata) only a paid service?</summary>
    <div>
    All distribution options (i.e. OData, S3, Sentinel Hub,..) will be constrained with user quotas, which includes both bandwidth limitation, as well as monthly limits.
    </div>
</details>
<details>
  <summary>Can you give indictions about the cost of the "extra" services?</summary>
    <div>
    Pricing will be published soon.
    </div>
</details>
<details>
  <summary><span>
  This December advertisement of <a href="https://medium.com/sentinel-hub/new-copernicus-data-access-service-to-support-the-ecosystem-for-earth-observation-412f829355a3">DAS</a> says that "For those interested in processing, there will be scalable cloud resources available, optimized for EO tasks". Does this refer to the current CreoDIAS resources, or something completely new that hasn't been addressed yet?
  </span>
  </summary>
    <div>
    Scalable cloud resources will be part of the commercial offering and can be obtained at <a href = "https://creodias.eu/">CREODIAS</a> in first instance. ICT-wise, there will be two options, including Open Telekom Cloud.
    </div>
</details>
<details>
  <summary>Are there tutorials (online & physical meetings) to use the new interface?</summary>
    <div>
    Tutorials will be added to the documentation in due time explaining the usage of the different interfaces. We will also be present on different conferences explaining the service & ecosystem.
    </div>
</details>


<style>@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');


.container h1{
  color: #fff;
  text-align: center;
}

details{
  background-color: #FFFFFF;
  color: #0a0a0a;
  font-size: 1.2rem;
  border-radius: 5px;

}


summary {
    background-color: #FFFFFF;
  color: #0a0a0a;
  /* height:50px; */
  font-size:1.2rem;
  border-radius: 5px;
  padding: .5em 1.3rem;
  list-style: none;
  display: flex;
  justify-content: space-between;  
  transition: height 1s ease;
  box-shadow: rgba(0, 0, 0, 0.20) 0px 5px 15px;
  margin:15px;
  
}

summary::-webkit-details-marker {
  display: none;
}

summary:after{
  content: "\002B";
}

details[open] summary {
    border-bottom: 1px solid #aaa;
    margin-bottom: .5em;

}

details[open] summary:after{
  content: "\00D7";
 
}

details[open] div{
  padding: .5em 1em;
  margin-left:25px;}
  </style>