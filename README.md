# Copernicus Data Space Ecosystem documentation portal
This repo contains the source code for the [docsify](https://docsify.js.org/#/) technical documentation portal for the Copernicus Data Space Ecosystem.

Branches:
publish: main branch for the next release
preview: branch for previewing quarto rendering of pull requests

# Guidelines for editors

All changes are made via pull requests, directly on the 'publish' branch.
All pull requests are automatically merged into the preview branch, which will automatically be rendered.
All pull requests should be reviewed for both content and language


## Content guidelines
* External links (outside the documentation portal domain) should always open in a new tab. This can be done by adding `{target="_blank"}` to your link in markdown.

# Previewing
Rendering of preview branch is available at: https://eu-cdse.github.io/documentation/Home.html

# Automated merges
Github actions are set up to automatically merge pull requests into preview and commits to the main branch.
In case of a conflict, automatic merge can fail and manual resolution may be needed.
