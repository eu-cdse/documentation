# Copernicus Data Space Ecosystem documentation portal
This repo contains the source code for the [docsify](https://docsify.js.org/#/) technical documentation portal for the Copernicus Data Space Ecosystem.

Branches:
quartov2: main branch for the next release
main: current main, for immediate fixes to documentation
preview: branch for previewing quarto rendering of pull requests

# Guidelines for editors

All changes are made via pull requests, directly on the 'quartov2' branch.
All pull requests are automatically merged into the preview branch, which will automatically be rendered.
All pull requests should be reviewed for both content and language

# Previewing
Rendering of preview branch is available at: https://eu-cdse.github.io/documentation/Home.html

# Automated merges
Github actions are set up to automatically merge pull requests into preview and commits to the main branch.
In case of a conflict, automatic merge can fail and manual resolution may be needed.
