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
# Ways to Add a Citation to Your Code

[Sharing](share-your-code) and making your code **citable** helps others **acknowledge your work, build upon it, and give you proper credit**. 

Citations ensure that code, software, and data receive proper recognition as part of the open scientific process. Others can easily credit your work and trace research outputs by citing your code.

:::{tip}  
<i class="fa-solid fa-rocket"></i> Want to maximize your code’s impact? **Host it on [GitHub or GitLab](share-your-code) with an [open license](open-license) and make it citable.**  
:::


In this lesson, you will learn:

1. How to create a DOI using Zenodo and GitHub
2. How to create a citation file to use on GitHub
1. What a a DOI is

(zenodo)=
## What is Zenodo?
[Zenodo](https://zenodo.org/) is a free, open platform for sharing and archiving research outputs, including datasets and software. It assigns a unique **DOI** to each item, making your work **citable and easily discoverable**.  

Zenodo integrates with GitHub, allowing you to generate DOIs for your repositories in just a few clicks. It also supports versioning, so each code release gets an updated DOI. These features make Zenodo a go-to choice for researchers looking to share their work and receive proper credit. 

:::{admonition} pyOpensci on Zenodo
:class: tip

pyOpenSci has a [Zenodo community](https://zenodo.org/communities/pyopensci/records?q=&l=list&p=1&s=10&sort=newest) where we "publish" talks that the community gives about the organization.
:::

### How does Zenodo work?  

Zenodo makes it easy to create a **DOI** for your GitHub repository, ensuring your code is **citable and discoverable**. To create a DOI for your repo you need to: 

1. <i class="fas fa-link" style="color:#81c0aa;"></i> **Link your GitHub account** to Zenodo.  
2. <i class="fas fa-cogs" style="color:#81c0aa;"></i> **Enable your repository** in Zenodo’s settings.  
3. <i class="fas fa-box-open" style="color:#81c0aa;"></i> **Create a release on GitHub**—Zenodo will automatically generate a **DOI** and archive it.  

Each release gets a unique DOI, while the repository keeps a persistent record, making it easy to track versions and credit your work.  

## How to create a DOI for a Python package on GitHub

### Step 1: Setup Zenodo 

1. Go to zenodo.org and sign in using your GitHub account
2. Go to your profile drop-down and select “GitHub


:::{figure} /images/zenodo/zenodo-account.png
:alt: Text here

You should see a screen like the one below. If you‘ve never used Zenodo before it’s ok if you have no repos listed here!

:::


When you select GitHub you might see a list of repositories if you've used Zenodo before or if it finds your repos automagically. Don't worry if you don't see that list yet, you may have to sync your account with GitHub.


:::{figure} /images/zenodo/zenodo-github-repos.png
:alt: text


:::

Click the sync now button in the get started page to update your list of GitHub repos. The more repositories that you have access to, the longer this will take. It’s normal for it to take a few minutes and maybe 5 minutes or more. 

:::{figure} /images/zenodo/zenodo-sync-repos.png
:alt: text


:::

:::{tip}
If you have access to many GitHub repositories through both your own account and other organization accounts that you may have access too, the sync button may take a long time to run. It could take 5 minutes or more for someone with hundreds to thousands of repos). Be patient. 
:::

Once your repos are synced, it's time to "flip the switch" or turn on a connection between GitHub and Zenodo for your Python package. 

:::{figure} /images/zenodo/zenodo-flip-the-switch.png
:alt: text


:::


:::{figure} /images/zenodo/zenodo-switch-on.png
:alt: text


:::

:::{figure} /images/zenodo/zenodo-switch-off.png
:alt: text


:::

### Step 2: Create a release of your package on GitHub 

Head over to your repository on GitHub. The url should look something like this:

https://github.com/your-user-name/ff-2024-create-python-package
Here is my fork: https://github.com/lwasser/ff-2024-create-python-package

Go to the releases tab in github. The url will look something like this (Replace my username with your github user name!):

https://github.com/lwasser/ff-2024-create-python-package/releases

Click the green Create a new release button

:::{figure} /images/zenodo/zenodo-switch-off.png
:alt: text


:::

Create a new tagged release!

You can either generate automatic release notes or type in notes yourself. Either is acceptable but for convenience today you could opt to generate release notes for this release!

When you are ready, scroll to the bottom of the page and click "publish release" When you publish your release, Zendo will begin to do its job—generating a DOI for the repository and the release and processing the metadata for the release.

:::{figure} /images/github/github-create-release.gif
:alt: text

Once you are ready, you can create a release. Once you have created the release, zenodo will process it and create a badge for your repository. Notice that this screen cast is for a repo where a release already exists. The process is the same whether you have a release already or not!
:::

### Step 3: Get your zenodo badge and add it to your project README file

Add your zenodo badge to your readme file in your repo! 
Important: be sure to use the cite all versions badge.


AFTER YOU CREATE a release, you will see a badge on the Zenodo website. If you click on it, it will provide you with a copyable badge format for markdown and other formats. Copy the badge in markdown format. You will add this to your readme file. 

:::{figure} /images/zenodo/zenodo-badge.png
:alt: text


:::


## About citation.cff files

Now that you have a DOI, add a CITATION.cff file to make it easy for others to cite your package.
Once you have a DOI, you can add a [citation.cff file](https://citation-file-format.github.io/) to your GitHub or GitLab repository. A `CITATION.cff` file standardizes citation information, making it easy for others to cite your work correctly.



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





The video below walks you through how to set this all up. 

:::{admonition}21 October 2024
:class: important
This video is a draft. It will be updated over the next two months, and a more polished version will be available soon. 
:::


:::{todo}
<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1021839955?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="zenodo-rough-cut"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
:::
