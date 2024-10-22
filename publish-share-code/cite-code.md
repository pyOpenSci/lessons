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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(cite-code)=
# Cite your code

[Share your code on an online platform like GitHub or GitLab](share-code) using an [open license](open-license) is a great way to share your code. It's also important to consider making your code citable. To understand citations, it's important to understand what a DOI is.

## What is a DOI?

A **DOI**, or **Digital Object Identifier**, is a unique, permanent identifier assigned to digital content such as academic papers, datasets, software, and other research outputs. It acts like a stable web link that always directs users to the reference content, even if the location of the content changes. DOIs are commonly used in academic publishing to ensure that citations remain valid and materials are easily accessible. By using a DOI, creators can make their work more discoverable and citable, enabling others to locate and reference the material reliably now or in future research.

## TODO Add a section on citation.cff files


## CrossRef vs. Zenodo DOIs - What's the difference?

In research, making your work citable and easy to find is essential. That’s where DOIs (Digital Object Identifiers) come in. But not all DOIs are the same! Let’s look at two common types: CrossRef DOIs and Zenodo DOIs.

* **CrossRef DOI**: A CrossRef DOI is typically used for formal, peer-reviewed publications like journal articles, books, or conference papers. CrossRef DOIs help ensure that these published works are easy to cite and locate in academic literature. CrossRef DOI's can also be easily connected to your ORCID.

The Journal of Open Source Software (JOSS), [a pyOpenSci partner](https://www.pyopensci.org/partners.html), offers CrossRef DOIs for scientific software with research applications.

* **Zenodo DOI**: Zenodo allows you to create DOIs for a wider range of digital content, including datasets, software (like your GitHub repositories), preprints, and event presentations. Zenodo is perfect for making your code or data citable, even if it’s not part of a formal publication.

Both types of DOIs ensure your work is easily found and cited. CrossRef is more focused on formal publications. While Zenodo offers more flexibility by covering a broader range of research outputs.

By using the right DOI for your work, you help others find and cite it easily, no matter where or how it’s shared!

## How does Zenodo work?

Creating a DOI for your GitHub repository using Zenodo is a straightforward way to ensure your code is citable and easily discoverable. Zenodo integrates seamlessly with GitHub, allowing you to generate a persistent DOI for any release of your project. To start, link your GitHub account to Zenodo by authorizing access through the Zenodo website. Once connected, navigate to the Zenodo settings and enable the repository you want to archive. After pushing a new release on GitHub, Zenodo will automatically archive it and generate a unique DOI. This DOI can be included in your publications or shared with others, ensuring proper credit for your work. Zenodo also supports versioning, so each release will have its own DOI while maintaining a link to the overall repository.

The video below will walk you through how to set this all up. 

:::{important} 21 October 2024
This video is a DRAFT and will be updated over the next two months. A more polished version of it will be available soon. 
:::


<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1021839955?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="zenodo-rough-cut"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
