# Copernicus Data Space Ecosystem openEO Federation

The openEO standard offers a unique capability to provide access to datasets and processing capacity beyond the offering of CDSE.
This is accomplished through a single endpoint and interface for your workflows. 
This eliminates the need to register across multiple platforms and study their APIs and offerings. 
This function, referred to as the openEO federation, is available through the following endpoint:

[https://openeofed.dataspace.copernicus.eu](https://openeofed.dataspace.copernicus.eu)

Currently, we are actively encouraging early adopters and projects with specific needs to try this new capability.
While it has already been extensively tested by users of other projects, the configuration in the CDSE is still new.
As a result, we are offering this feature as a 'beta' service at first.
This approach allows us to still adjust the configuration based on your feedback.

When using the federated endpoint, you will be asked to give your consent to share basic user information with the other providers of the federation.
Additionally, you will be requested to accept the new terms and conditions. You can withdraw your consent at any time through your CDSE account dashboard.

All external providers comply with the regulations of the federation, but are not necessarily part of the CDSE service. This means that while they are part of the 
broader Copernicus ecosystem, they are either fully independent providers, or are governed and/or funded by other parties. This mainly impacts their currently foreseen lifetime, but also 
how they handle aspects that are not part of federation governance.

You can find a description of the technical design [here](./backends/design.md), as well as a more extensive [overview of federation governance](./backends/index.md).

## Federation credit usage

The usage of processing capacity in the federation is likely to lead to credit consumption.
This usage will be reported in the [openEO algorithm plaza](../../../Applications/PlazaDetails/Reporting.qmd). 
To support basic processing within the federation, external providers can allow a limited amount of credits, similar to the [free openEO credits](../../../Quotas.qmd) offered by CDSE.
It is important to note that there is clear separation of your credits amongst the external providers.
This means that using an external provider will not lead to a reduction in the free credits supplied by CDSE. 

## Latest news & important announcements {#sec-openeoannounce}

All providers in the federation will post important information about changes to their service in the openEO category of the forum: [forum](https://forum.dataspace.copernicus.eu/c/openeo), 
We encourage users to subscribe to this topic to receive important updates via email. 
Important breaking changes are announced here with a lead time of 3 months, allowing users to adjust their workflows if needed.

## Getting help

We encourage users to use the [forum](https://forum.dataspace.copernicus.eu/), a place where service providers and users can meet, to ask questions about the federation.
Our support team is not required to help with issues related to external, non-CDSE openEO services.
Additionally, the free credits offered by the service provider do not include support. 
However, the dedicated CDSE openEO endpoint does include support under normal situations.

## Long term continuity

It is important to note that external providers within the federation may not have the same long term guarantees as the CDSE service. 
Providers may discontinue their service, or may be removed from the federation if they become non-compliant with our agreements or SLA's.
If this continuity is important to your project or your organization, we recommend to contact the provider(s) directly to discuss their long term commitment. 

## Federation members

We list the members of the federation here. 
Collections in the federated endpoint are offered by one or more of these members.

### Terrascope

The [Terrascope](https://terrascope.be) platform is a Belgian initiative that offers access to Copernicus products, the full archive of the PROBA-V mission, and a range of other interesting datasets. 
The platform also offers its own processing capacity close to the datasets, and is an early implementor of the openEO open standard. 

Terrascope is operated by [VITO Remote Sensing](https://remotesensing.vito.be/), an independent research and technology leader.
The platform is guaranteed to operate until 2028.

Credit usage on Terrascope is similar to the CDSE openEO service, as it is based on the consumed cpu and memory hours.
However, actual costs for similar jobs may differ due to varying performance characteristics of underlying data centers.
