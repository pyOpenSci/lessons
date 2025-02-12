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

# Publish Your Code

Sharing your code with others is key to open science and software development.
However, consider what platforms you want to use when sharing your code. 

Platforms like GitHub are great for getting your code online and collaborating with colleagues. However, other platforms like PyPI, conda-forge, and publications through journals like JOSS will provide additional visibility, citation benefits, and more. 

Below, you will learn about a few different ways to publish your code online and the benefits associated with each approach.

(joss)=
## JOSS

### What is JOSS?

The **Journal of Open Source Software (JOSS)** is a peer-reviewed journal that publishes research papers about open source software. JOSS focuses on ensuring that scientific software is well-documented and publicly accessible, providing credibility to the code by offering a peer-reviewed publication.

### How does the pyOpenSci partnership with JOSS work?

pyOpenSci partners with JOSS to help authors who want to publish their Python packages. Through this partnership, packages reviewed by pyOpenSci can easily be submitted to JOSS for an additional review, leading to a formal publication and a CrossRef DOI for your software. This process helps boost the visibility and credibility of your work.

For more details, visit the [JOSS website](https://joss.theoj.org/).

(pypi)=
## PyPI

### What is PyPI?

The **Python Package Index (PyPI)** is the official repository for Python packages. It allows developers to distribute their code to the broader Python community, making it easy for others to find, install, and use the packages using the `pip` command.

### How to Publish to PyPI

Publishing to PyPI involves creating a package with all the necessary metadata, ensuring your code is structured properly, and uploading it to PyPI. For a step-by-step guide on how to publish to PyPI, check out our [tutorial](https://www.pyopensci.org/python-package-guide/tutorials/publish-pypi.html).

(conda-forge)=
## conda-forge

### What is conda-forge?

**conda-forge** is a community-led collection of conda packages. It allows you to distribute Python packages and their dependencies using the `conda` package manager, which is popular in scientific computing for managing complex dependencies and non-Python packages.

### How to Publish to conda-forge

Publishing to conda-forge involves creating a package recipe and submitting it to the conda-forge community for review. For detailed instructions on publishing to conda-forge, check out our [tutorial](https://www.pyopensci.org/python-package-guide/tutorials/publish-conda-forge.html).


