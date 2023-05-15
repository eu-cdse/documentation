# Copernicus Data Space Ecosystem documentation portal
This repo contains the source code for the [docsify](https://docsify.js.org/#/) technical documentation portal for the Copernicus Data Space Ecosystem.

## Branches
| Name    | Description | URL |
|---------| --- |-----|
| staging | Branch that contains the next release of the documentation portal | https://documentation-staging.dataspace.copernicus.eu/    |
| publish | Branch that contains the current release of the documentation potal | https://documentation.dataspace.copernicus.eu/ |

# Guidelines for editors

## Hotfix
Hotfixes to the production documentation portal are done by creating a new PR based on the `publish` branch.
Once the PR is reviewed and merged, the hotfix changes are automatically merged to both the `publish` and `staging` branch.

## Other changes
All other changes are made via a PR on the `staging` branch.
After reviewing and merging the PR, the changes are automatically pushed to the `staging`

## PR commits
Commits within PR are automatically built and rendered to a custom link on the GitHub Pages. 
After a successfull build of the commits, GitHub Actions will post a new comment with a link to custom documentation portal.

## Automated merges
GitHub Actions are set up to automatically merge pull requests into the corresponding branches.
In case of a conflict, automatic merge can fail and manual resolution may be needed.
