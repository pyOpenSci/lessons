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


## Activity 1 - install a package from GitHub

:::{note}

If you are comfortable using Git and GitHub and have a Python package in mind, check the package's repo on GitHub or GitLab to ensure that the package structure and source code are correct. 

If you are working on this during a pyOpenSci workshop, you can use the package you created in our workshop!

If not, you can start with the [pyospackage repository](https://github.com/pyOpenSci/pyosPackage). 
:::


1. Fork the [pyospackage repository](https://github.com/pyOpenSci/pyosPackage) on GitHub.
2. This repository has a GitHub Codespace setup with VS Code. Optional: after you fork the repository, you can use a GitHub codespace to modify the source code and package name (if you wish).
3. Install the package in that repository from your fork.

+++

## Activity 2: Connect your Python package repo to Zenodo

In this activity, you will connect the GitHub repository containing a Python package to [Zenodo to create a DOI (Digital Object Identifier)](zenodo) for your code. This will allow others to cite your work and give credit to contributors. 

If you completed **Activity 1** above, you should already have a GitHub repository set up. Now, we’ll take it a step further by setting up a citation for your project using Zenodo.

### Steps to Connect Your Repository to Zenodo

1. **Connect Your Repository to Zenodo**  
   - Go to [Zenodo](https://zenodo.org/) and log in using your GitHub account.
   - Once logged in, navigate to the **GitHub** tab under **Linked Accounts** in your Zenodo settings.
   - In the list of repositories, find the repository you created in Activity 1 and flip the toggle switch to enable it for Zenodo.

2. **Create a Release**  
   - In your GitHub repository, navigate to the **Releases** section. Click on **Draft a new release**.
   - Assign an available version number to the release (e.g., `v1.0.0`) and provide a title and description.
   - Click on **Publish release**. This action will trigger Zenodo to generate a DOI for your code.

3. **Get the DOI Badge and Add It to Your README File**  
   - Go back to Zenodo and find your newly generated DOI under your repository's name in the **Upload** section.

IMPORTANT: When completing this step, be sure to grab the Zenodo badge for "all versions" rather than the most recent version.


   - Zenodo will provide a badge code that you can copy. Go back to your GitHub repository, open your `README.md` file, and paste the DOI badge code at the top or in a dedicated section like **Citing this Code**.

By completing this activity, you’ve taken an important step in making your code citable and accessible to others. Properly citing code encourages transparency and reproducibility, helping others build upon your work with confidence.
