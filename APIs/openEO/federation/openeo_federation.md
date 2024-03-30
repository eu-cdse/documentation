# Copernicus dataspace Ecosystem openEO federation

The openEO standard offers a unique capability to provide access to datasets and processing capacity beyond the offering of CDSE.
This gives you a single endpoint and interface for your workflows, avoiding the need to register with multiple platforms and
study their APIs and offerings. This is referred to as the openEO federation, and is offered through a this endpoint:

https://openeofed.dataspace.copernicus.eu

This capability is currently in a phase where we encourage early adopters and projects with specific needs to try it out.
It has already been extensively tested by users of other projects, but the configuration in the CDSE is new and thus we 
offer it as a 'beta' service at first, allowing us to still make changes to the configuration based on user feedback.

When using the federated endpoint, you will be asked to give consent for basic user information to be shared with the other providers
that make up the federation, as well as to accept the terms and conditions. These external providers all comply with the 
regulations of the federation, but are not necessarily part of the CDSE service. You can withdraw your consent at any time, via
your CDSE account dashboard.

The technical design is described [here](./backends/design.md). There's also a more detailed [overview of federation governance](./backends/index.md).

## Federation credit usage

The use of processing capacity in the federation is likely to lead to credit consumption, that will be reported in the 
openEO algorithm plaza dashboards. External providers will allow a limited amount of credits, just like the public service.
Usage of those external providers will not lead to a reduction in credits of the public service. 

## Getting help

We encourage users to use the CDSE forum to ask questions about the federation. The CDSE support team is not required to
help with issues related to non-CDSE openEO services, so the forum is a place where service providers and users can meet.
When using free credits offered by the service provider, the support is not considered to be included. The CDSE openEO endpoint 
does include support under the normal conditions.

## Long term continuity

Members in the federation may not have the same long term guarantees as the CDSE service. Members may discontinue their 
service, or may be removed from the federation if they become non-compliant with agreements or SLA's.
If this is of importance for your project or organization, we recommend to contact the service provider(s) directly to discuss
their long term commitment. 

## Federation members

We list the members of the federation here. Collections in the federated endpoint are offered by one or more of these members.

### Terrascope

The [Terrascope](https://terrascope.be) platform is a Belgian initiative that offers access to Copernicus products, the
full archive of the PROBA-V mission, and a range of other interesting datasets. It also provides its own processing 
capacity close to the datasets, and is an early implementor of the openEO open standard. 

Terrascope is operated by [VITO Remote Sensing](https://remotesensing.vito.be/), an independent research and technology leader.
It's lifetime is currently guaranteed until 2028.

Credit usage on Terrascope is similar to the CDSE openEO service, as it is based on consumed cpu and memory hours. This does
mean that their may be differences in actual costs for similar jobs, as the performance characteristics of the underlying
datacenters differ. 