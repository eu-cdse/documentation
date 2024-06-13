# Copernicus Data Space Ecosystem documentation portal
This repo contains the source code for the [quarto](https://quarto.org/) technical documentation portal for the Copernicus Data Space Ecosystem.'


## Branches
| Name    | Description | URL |
|---------| --- |-----|
| staging | Branch that contains the next release of the documentation portal | https://documentation-staging.dataspace.copernicus.eu/    |
| publish | Branch that contains the current release of the documentation potal | https://documentation.dataspace.copernicus.eu/ |


## Hotfix
Hotfixes to the production documentation portal are done by creating a new PR based on the `publish` branch.
Once the PR is reviewed and merged, the hotfix changes are automatically merged to both the `publish` and `staging` branch.

## Other changes
All other changes are made via a PR on the `staging` branch.
After reviewing and merging the PR, the changes are automatically pushed to the `staging`.
For more details [click here](EU-CDSE_Documentation_Guidelines_v0.pdf)

## Guidelines for editors

To get started, with exploring the documentation locally:

### 1. Clone the Repository

Clone this repository to the local machine:

    git clone https://github.com/eu-cdse/documentation.git

### 2. Install Quarto

To render/preview the documentation locally, one should install Quarto. Detailed instructions for installing Quarto in a preferred editor can be found [here](https://quarto.org/docs/get-started/).

### 3. Submodules

Here, we import two notebook repositories using git submodules to prevent the need for maintaining identical notebooks in multiple repositories. These submodules serve as additional resources for our documentation.
They are:

* https://github.com/eu-cdse/notebook-samples
* https://github.com/Open-EO/openeo-community-examples

Quarto allows integrating these notebook contents within the documentation. Moreover, editors must clone these submodules locally to render the documentation.

#### Cloning submodules

When cloning this repository, ensure that submodules are also initialized and updated:

    git clone --recurse-submodules https://github.com/eu-cdse/notebook-samples.git

For the second submodule, navigate to /APIs/openEO and then clone it:

    git clone --recurse-submodules https://github.com/Open-EO/openeo-community-examples.git

#### Update submodules

Ensure that the submodules are up-to-date and that the latest commit is synced with the documentation repository. To update the submodules to the latest commit in their respective repositories, run:

    git submodule update --remote

#### Avoiding Merge Conflicts

To avoid merge conflicts when working with submodules:


* **Communicate Changes**: Inform other contributors if you're making changes to a submodule to prevent conflicting updates.

* **Sync Submodules**: Regularly update submodules to their latest versions to minimize merge conflicts. 

* **Cross-check commits**: After pushing the latest submodule version to the Publish branch, ensure that the changes are also migrated to the Staging branch. 

* **Avoid Direct Edits**: Avoid making direct edits within submodule directories from the main repository to prevent unintentional changes.
    
### 4. Render and preview documentation

Once Quarto is installed and the repository with submodules is cloned, navigate to the qmd file host the documentation locally:

    quarto render cdse_doc.qmd 

or 

    quarto preview cdse_doc.qmd


## Points to remember


### PR commits
Commits within PR are automatically built and rendered to a custom link on the GitHub Pages. 
After a successfull build of the commits, GitHub Actions will post a new comment with a link to custom documentation portal.


### Automated merges
GitHub Actions are set up to automatically merge pull requests into the corresponding branches.
In case of a conflict, automatic merge can fail and manual resolution may be needed.

## openEO specific guidelines

## Shared notebooks

We have incorporated the repository from https://github.com/Open-EO/openeo-community-examples using git submodules, enabling Quarto to integrate the notebook content seamlessly. To facilitate this integration, a 'filter' script (notebook_filter.py) is available that preprocesses the notebooks, ensuring tasks such as configuring the correct openEO URL.

However, it's important to note that the notebooks require thorough review to ensure compatibility across multiple platforms. Moreover, any changes made to the notebooks should be reviewed to maintain consistency.



