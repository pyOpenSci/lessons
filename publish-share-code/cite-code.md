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

(cite-your-code)=
# Cite your code

[Sharing your code](share-your-code) is a great way to contribute to make your science more open. Making your code citable allows others to acknowledge your effort and build upon your work. Citations aren’t just for papers—they’re crucial for software and datasets too! Citing your code means others can easily give you credit and trace the source of key research outputs.

:::{tip}
[Placing your code on an online platform like GitHub or GitLab](share-your-code) using an [open license](open-license) is an effective way to share your code. Once it's online, it's important to think about making it citable. 
:::


In this lesson you will learn about how to make your code citable once you've placed it online on a platform like GitHub. You will also learn the basics of 

1. What a citable element (a DOI) is
2. How you can use zenodo to create a DOI and connect that DOI to your GitHub repository.

To understand citations, it's important to understand what a DOI is.

## What is a DOI?

A **DOI**, or **Digital Object Identifier**, is a unique, permanent identifier assigned to digital content such as academic papers, datasets, software, and other research outputs. It acts like a stable web link that always directs users to the reference content, even if the location of the content changes. DOIs are commonly used in academic publishing to ensure that citations remain valid and materials are easily accessible. But you can also assign DOIs to software, data, and other research outputs and supporting elements.

By using a DOI, you can make your work more discoverable and citable, enabling others to locate and reference the material reliably now or in future research.

## Ways to make your code citable

There are multiple ways to get a DOI for your work and to make your code citable. Each way has its own benefits:


1. **Write and publish a paper about your code in a journal like JOSS (Journal of Open Source Software) via pyOpenSci** if you have written a Python package or another methods-focused scientific Journal. If you go the publication route, you will receive a cross-ref DOI that can be easily connected to your ORCID.  
3. **Use a platform like [Zenodo](zenodo)**. If you use Zenodo to create a DOI for your work, you will receive a DOI that is not CrossRef compatible. However, you can still add entries for that DOI in your ORCID profile page. 

### CrossRef vs. Zenodo DOIs - What's the difference?

In research, making your work citable and easy to find is essential. That’s where DOIs (Digital Object Identifiers) come in. But not all DOIs are the same! Let’s look at two common types: CrossRef DOIs and Zenodo DOIs.

* **CrossRef DOI**: A CrossRef DOI is typically used for formal, peer-reviewed publications like journal articles, books, or conference papers. CrossRef DOIs help ensure that these published works are easy to cite and locate in academic literature. CrossRef DOI's can also be easily connected to your ORCID.

The Journal of Open Source Software (JOSS), [a pyOpenSci partner](https://www.pyopensci.org/partners.html), offers CrossRef DOIs for scientific software with research applications.

* **Zenodo DOI**: Zenodo allows you to create DOIs for a wider range of digital content, including datasets, software (like your GitHub repositories), preprints, and event presentations. Zenodo is perfect for making your code or data citable, even if it’s not part of a formal publication.

Both types of DOIs ensure your work is easily found and cited. CrossRef is more focused on formal publications. While Zenodo offers more flexibility by covering a broader range of research outputs.

By using the right DOI for your work, you help others find and cite it easily, no matter where or how it’s shared!

## About citation.cff files

Once you have a DOI, you can add a [citation.cff file](https://citation-file-format.github.io/) to your GitHub or GitLab repository. A `CITATION.cff` file standardizes citation information, making it easy for others to correctly cite your work.

(zenodo)=
## What is Zenodo?

[Zenodo](https://zenodo.org/) is a free and open platform that allows researchers and scientists to share and archive their work. Zenodo enables you to publish datasets, software, and other research outputs while assigning a unique **DOI** to each, ensuring that your work is citable and easily discoverable.

Zenodo also integrates seamlessly with GitHub, allowing you to create DOIs for your code repositories with just a few clicks. And you can also create new versions of the DOI as you create code releases in your GitHub repo. These features make Zenodo a popular choice for researchers looking to share code and other digital content in a way that encourages proper citation and credit.

:::{admonition} pyOpensci onZenodo
:class: tip

pyOpenSci has a [Zenodo community](https://zenodo.org/communities/pyopensci/records?q=&l=list&p=1&s=10&sort=newest) where we "publish" talks that the community gives about the organization!
:::

### How does Zenodo work?

Creating a DOI for your GitHub repository using Zenodo is a straightforward way to ensure your code is citable and easily discoverable. Zenodo integrates seamlessly with GitHub, allowing you to generate a persistent DOI for any project release. 

To start, link your GitHub account to Zenodo by authorizing access through the Zenodo website. Once connected, navigate to the Zenodo settings and enable the repository you want to archive. After pushing a new release on GitHub, Zenodo will automatically archive it and generate a unique DOI. This DOI can be included in your publications or shared with others, ensuring proper credit for your work. Zenodo also supports versioning, so each release will have its own DOI while maintaining a link to the overall repository.

The video below walks you through how to set this all up. 

:::{admonition}21 October 2024
:class: important
This video is a draft. It will be updated over the next two months, and a more polished version will be available soon. 
:::


<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1021839955?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="zenodo-rough-cut"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

