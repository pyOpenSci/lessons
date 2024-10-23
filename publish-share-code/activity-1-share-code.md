---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Share Your Code Activities
s

:::{note}

If you are comfortable using Git and GitHub and have a Python package already on GitHub, you can use that package for this activity. Otherwise, we suggest that you fork the [pyospackage repository](https://github.com/pyOpenSci/pyosPackage) for this activity! 

:::

## Activity 1: Install a package from GitHub

1. Create & activate a Python environment that you wish to use for this activity.

`python -m venv pyosworkshop`

If you are working on a Mac, A Linux machine or in the GitHub codespace that we setup, you can activate the environment using:

`source pyosworkshop/bin/activate`

If you are using Windows, use:

`.\pyosworkshop\Scripts\activate`


2. After activating the environment, [install the pyosPackage package](install-github) in that repository using `pip`.

```bash
pip install git+https://github.com/pyopensci/pyospackage.git
```

+++

## Activity 2: Fork the repo and install a package from your fork

Above, you installed a package from a pyOpenSci-owned GitHub repo. 
Now, you will do the same thing, but instead, you will install your package from a fork that you own of the pro package. 

Because you own this fork, you can make any changes you wish to the code. 

1. Fork the [pyospackage repository](https://github.com/pyOpenSci/pyosPackage) on GitHub.


:::{figure} ../images/github/github-fork-repo.gif
---
alt: "alt here."
name: fork-github-repo
width: 700px
---

To begin, fork the pyospackage GitHub repository.
:::

Now, you can install the same package into the same environment using the command below. IMPORTANT: be sure to modify the URL of the repo to represent your FORK.

```bash
pip install git+https://github.com/YOUR-GITHUB-USERNAME-HERE/pyospackage.git
```

+++

## Activity 3: Connect your Python package repo to Zenodo

In this activity, you will connect the GitHub repository that you just forked containing a Python package to [Zenodo to create a DOI (Digital Object Identifier)](zenodo) for your code. This will allow others to cite your work and give credit to contributors. 

If you completed **Activity 2** above, you should already have a GitHub repository set up. Now, we’ll take it a step further by setting up a citation for your project using Zenodo.

### Steps to Connect Your Repository to Zenodo

1. **Connect Your Repository to Zenodo**  
   - Go to [Zenodo](https://zenodo.org/) and log in using your GitHub account.
   - Once logged in, navigate to the **GitHub** tab under **Linked Accounts** in your Zenodo settings.
   - In the list of repositories, find the repository you created in Activity 1 and flip the toggle switch to enable it for Zenodo.

2. **Create a Release**  
   - In your GitHub repository, navigate to the **Releases** section. Click on **Draft a new release**.
   - Assign the release an available version number (e.g., `v1.0.0`) and provide a title and description.
   - Click on **Publish release**. This action will trigger Zenodo to generate a DOI for your code.

3. **Get the DOI Badge and Add It to Your README File**  
   - Go back to Zenodo and find your newly generated DOI under your repository's name in the **Upload** section.

IMPORTANT: When completing this step, be sure to grab the Zenodo badge for "all versions" rather than the most recent version.

Zenodo will provide a badge code that you can copy. Go back to your GitHub repository, open your `README.md` file, and paste the DOI badge code at the top or in a dedicated section like **Citing this Code**.

+++

## Activity 4: Rename your package and create a new release 

In this activity, you will further develop the Python package you have worked on (or the package you forked above). 

1. Rename the package by updating both the `pyproject.toml` file and the package directory found within the `src/package-name`

2. If you wish, add a new function to the package using the codespace provided in the repository. Commit your changes before moving on to the next step.

3. Create a new release of the package on GitHub.

4. Check out the Zenodo landing page for your package. Do you see the new release there?

:::{note}
Note: it may take 5-10 minutes for the new release to process. 
:::

+++

## Activity 5: Publish your package on test PyPI 

For this activity, you will practice publishing your package to test-pypi. We will follow the [guidance provided in this lesson](https://www.pyopensci.org/python-package-guide/tutorials/publish-pypi.html).

To be successful in this activity, you will need to have

1. A [test-PyPI account setup](https://test.pypi.org/account/register/)
2. A unique package name. Don't try to use pyospackage. We suggest renaming your package to something unique like `pyospackage-yourGitHubUserName`
