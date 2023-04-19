# Copernicus Data Space Ecosystem documentation portal

This repo contains the source code for the technical documentation portal for the Copernicus Data Space Ecosystem.

Branches:

publish: the main branch 

preview: branch for previewing quarto rendering of pull requests

# Guidelines for editors

All changes are via pull requests directly on the 'publish' branch. 

All pull requests are automatically merged into the preview branch, which will automatically be rendered.

All pull requests should be reviewed for both content and language.


## Content guidelines

* The folder structure resembles the sidebar of the documentation portal. All the relevant documents should be included within those folders or sub-folders as needed.
* Pages rendered with level 1 of the sidebar can be included at the same location along with the folder.
* Files should be provided in either markdown(.md) or quarto markdown(.qmd) format. Quarto files are highly encouraged, mainly if they include code snippets to be rendered.
* External links (outside the documentation portal domain) should always open in a new tab. This can be done by adding `{target="_blank"}` to your link in the markdown.
* Link your files within other file content or include them in the sidebar. Sidebar can be edited from the `_quarto.yml` config file.
* Additional packages required for rendering your code should be included in the requirement.txt file.

# Previewing
Rendering of the preview branch is available at: https://eu-cdse.github.io/documentation/Home.html .

# Automated merges
GitHub actions are set up to automatically merge pull requests into preview and commit to the main branch.

In case of a conflict, an automatic merge can fail, and manual resolution may be needed.
