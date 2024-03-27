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
