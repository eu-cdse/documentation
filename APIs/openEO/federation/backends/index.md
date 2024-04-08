# Federation Contract

For a federation to work, all providers need to agree with a common federation contract.
For the Copernicus Data Space Ecosystem, the proposed contract is based upon the groundwork established through ESA's openEO platform.

This contract has 2 main goals:

1. Boost user satisfaction, which can be measured in terms of user growth and number of complaints versus the usage of a specific feature.
2. Agree on interfaces and harmonization rules to align the different services within the federation.

The federation aims to be inclusive towards onboarding new features and components to stimulate growth and innovation.
In an environment supporting user-critical workflows, such new features need to be distinctly identified. 
For example, designating a process, collection, or backend as 'experimental' and indicating this in descriptions or official documentation.

Generally, we assume that an implementor can determine when a feature is mature enough.
However, in case of any uncertainty, we provide the following guidelines:
- By default, or if unsure, the feature is considered experimental.
- If a feature is new or unused, designate it as experimental.
- If still in doubt, consult with partner providers.

Suppose a non-experimental component exceeds the [error budget](https://sre.google/workbook/implementing-slos/), such as when downtime exceeds the objectives.
In this case, the provider is expected to stop working on new features and improve reliability or to mark the component as experimental. 
Reverting a 'stable' feature to 'experimental' should be considered as a backwards incompatible change, requiring communication towards the user and proper consideration of the impact.

> To join the federation, providers are expected to fulfill these requirements and document differences for users in the "[Federation Aspects and Known Issues](../index.md)".
However, to accommodate and encourage new backend entries into the federation, these requirements are open to negotiation if there are good arguments for changing the current contract agreements.

For more detailed information, please refer to the different parts of the federation contract:

- [API](./api.md)
- [Collections](./collections.md)
- [File Formats](./fileformats.md)
- [Processes](./processes.md)

## Benefits of joining the federation

The federation provides a unique opportunity for smaller organizations to join strengths, allowing them to build an offering that matches or even exceeds capabilities of well-known large scale cloud providers. 
This collaboration is a key element for the long term sustainability of participants. 
The short-term benefits of joining the federation include:

1. **Increased visibility**: the federation serves a single endpoint for users to access multiple services, increasing the visibility of your service.
2. **Increased user base**: thanks to the common authentication within the federation, users can access your service without any additional registration. This opens your service up to the larger openEO user community.
3. **Joint outreach**: outreach and promotion activities are performed together with other members of the federation, significantly reducing the effort to attract new users.
4. **Shared account management**: credit usage is tracked in a central manner, commercial usage is compensated in an efficient manner.

## How to join the federation

1. Assess if your system is compliant with the above requirements and identify the eligible collections. 
2. Contact the federation through [our support team](https://helpcenter.dataspace.copernicus.eu/hc/en-gb), showing your interest and detailing your offering.
3. Integrate the CDSE identity provider as your openEO service will need to accept CDSE users.
4. Integrate with the accounting component by reporting the usage of CDSE users through a JSON HTTP API. The API details will be provided upon request.

Finally, an official agreement will need to be established confirming that the service provider agrees with the federation contract and SLA.

## Providing user support

The Copernicus Data Space Ecosystem [forum](https://forum.dataspace.copernicus.eu/) is considered the main support channel for users and service providers to post updates or service events.
Service providers are also requested to provide an email address, to which support questions from users can be forwarded.

## Credit reporting

As specified, service providers need to log the resource usage in the federation's central accounting service.
This will allow them to be compensated for incurred usage.
The value of a credit is fixed, and service providers are free to choose the resources they log.
Typical examples include memory and cpu hours, but it can also be based on a more complex logic, such as amount of input data or specific processes that are used. 
To ensure full transparency, service providers are requested to document this logic.



