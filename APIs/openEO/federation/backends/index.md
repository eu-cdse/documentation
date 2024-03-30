# Federation Contract

For a federation to work, all providers need to come up with a federation contract to agree on. 
For the Copernicus Dataspace Ecosystem, the proposed contract is derived from prior work in the ESA openEO platform, which
has done a lot of groundwork in this area.

This contract has 2 main goals:
1. Achieve user satisfaction, which can be measured in terms of user growth and number of complaints versus the usage of a specific feature.
2. Agree on interfaces and harmonization rules to align the different services in the federation.

The federation aims to be inclusive towards onboarding new features and components,
to stimulate growth and innovation. To allow this in an environment that also supports 
user-critical workflows such functionality needs to be clearly marked, for instance by setting 
an 'experimental' property on a process, collection or backend, and by indicating it in descriptions or the documentation. 

We assume that most often, an implementor knows when a feature is mature enough. However, when there is doubt about indicating a feature as experimental:
- By default or if unsure, it is probably experimental.
- If a feature is new or it hasn't been used, it's experimental.
- If still in doubt, consult with partner providers.

If a non-experimental component exceeds the [error budget](https://sre.google/workbook/implementing-slos/), for instance when downtime exceeds the objective, 
the provider is expected to stop working on new features and improve reliability, or to mark the component 
as experimental. Reverting a 'stable' feature to 'experimental' should be considered a backwards incompatible change, requiring communication towards the user and proper consideration of the impact.

::: tip Note
To join the federation, it is required to (mostly) fulfill these requirements and document differences for users in the "[Federation Aspects and Known Issues](../index.md)".
Nevertheless, these requirements are negotiable if there are good arguments for a change as the current state of the "contract" is just the compromise that the existing providers have agreed upon and if a new back-end joins the federation new compromises may need to be made.
:::

- [API](./api.md)
- [Collections](./collections.md)
- [File Formats](./fileformats.md)
- [Processes](./processes.md)

## Benefits of joining the federation

This federated concept provides a unique opportunity for smaller organizations to join strengths, allowing to build an
offer that matches or even exceeds capabilities of well-known large scale cloud providers. This is a key element for long
term sustainability of participants. There are however also short term benefits: 

1. **Increased visibility**: the federation is a single endpoint for users to access multiple services, increasing the visibility of your service.
2. **Increased user base**: users of the federation can access your service without the need to register, increasing the potential user base.
3. **Joint outreach**: outreach and promotion activities are performed together with other members of the federation, significantly reducing effort to attract new users.
4. **Shared account management**: credit usage is tracked in a central manner, commercial usage is compensated in an efficient manner.

## How to join the federation

1. Perform a basic check if you believe to be compliant with the above requirements. Determine the collections you believe to be eligible.
2. Contact the federation via CDSE support, showing your interest and detailing your offering.
3. Integrate the CDSE identity provider: you will need to accept CDSE users on your openEO service.
4. Integrate with the accounting component: report usage by CDSE users via a JSON HTTP API. API details will be provided upon request.

Finally, an agreement will need to be put in place to ensure that the service provider agrees with the federation contract and SLA.

## Providing user support

The forum of the Copernicus Dataspace ecosystem is considered the main support channel for users, and for service providers
to post news about updates or service events.
Service providers are requested to provide an email address, to which support questions arriving at the CDSE support center 
can be forwarded.

## Credit reporting

As specified, service providers will log credit usage in the central accounting service, allowing to be compensated for 
incurred usage.
The value of a credit is fixed, and service providers are free to choose the resources they log.
Typical examples include memory and cpu hours, but it can also be determined based on a more complex logic, like amount of
input data or specific processes that are used. Service providers are requested to document this.



