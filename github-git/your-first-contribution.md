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
myst_html_meta:
  "title": "Intro to Collaborative GitHub: Make your first contribution to open source"
  "description lang=en": "Learn about the steps involved with using GitHub to collaborate and contribute to open source."
  "keywords": "GitHub, OpenSource, beginner-friendly"
  "property=og:locale": "en_US"
og:image: /images/github/steps-to-contribute.png
og:image:alt: An image that shows the steps for contributing to open source on GitHub.
---

# Mastering GitHub Collaboration Skills 

(first-contribution)=

## Get started with your first open source contribution 

:::{admonition} What you will learn

Completing this activity will give you the technical and social skills needed to contribute to an open source GitHub
repository successfully. You will use the [pyOpenSci example GitHub repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) to practice making contributions.
:::

This lesson series will teach you how to collaborate on code and documentation using GitHub. It will help you confidently contribute to a GitHub repository and build skills to collaborate with colleagues (some of whom you may not have met in real life!).

This page introduces all of the steps and walks you through the activities. Each activity has a related lesson that will help you navigate and understand any technical elements associated with the process.

## An overview of the collaborative GitHub workflow

:::{figure} /images/github/steps-to-contribute.png
:alt: alt text here

The steps for making your first contribution to an open source repo. In this lesson, you will do all of your work on GitHub.com, meaning you don't need to clone or make a copy of your repository locally. This is a great way to get started with contributing. It minimizes the command line skills that you will need to use git.
:::

## A step-by-step guide to your first contribution

### Step 1: Identify the repository and get to know it

First, identify and get to know the repository you want to contribute to. Use the [pyOpenSci learning repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) to test out the process.

[Getting to know that repository](get-to-know-repo) will save you and the maintainers time when you make your first contribution. Ideally, the contribution process is well-documented in the repo, which will help you get started quickly and minimize the questions you must ask the maintainer team.

:::{button-link} get-to-know-repo
:color: primary
:shadow:

<i class="fa-brands fa-leanpub" style="color: #6ec9c3;"></i> Learn how to get to know a GitHub repo
:::

:::{admonition} Activity 1: Get to know the repository

In your browser, navigate to [https://github.com/pyOpenSci/pyos-demo-package-contribute/](https://github.com/pyOpenSci/pyos-demo-package-contribute/).

* Check out the [README](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/README.md) and [CONTRIBUTING](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/CONTRIBUTING.md) files.

**Answer these questions**

* Does the repository accept contributions? If so, what types of contributions are accepted?
* Is the contribution process documented in the repo?
* Does the repository use specific code or text formatting standards or liters?
* Does the repository have continuous integration (CI) set up?
* What is the license associated with the code in the repository?
* Are the issues labeled, and are there "good first issue" or "help wanted" labels
:::

******

### Step 2: Find an issue to work on

Next, [identify an issue or bug that you want to work on](identify-issue). Sometimes, there is already an open issue in a repo that you want to address. So, reading through existing open issues before opening a new one is always a good idea. If you already have a fix in mind that doesn't exist in the existing issue list, you will [create a new issue](create-issue) in the repo.

:::{button-link} identify-issue
:color: primary
:shadow:

<i class="fa-brands fa-leanpub" style="color: #6ec9c3;"></i> Learn how to identify and open an GitHub issue
:::

:::{admonition} Activity 2: Create an issue for a bug that you'd like to fix

1. Navigate to the [pyOpenSci example repo](https://github.com/pyOpenSci/pyos-demo-package-contribute).
2. Explore the documentation and code. You will find many items that need to be fixed, including spelling errors, typos, and more.
3. Pick a file that you'd like to work on. Open a new issue specifying what you'd like to fix.
4. Wait for someone on the pyOpenSci team to respond to you with next steps.

Once you have submitted an issue and someone has responded positively, you can begin working on the changes in your fork. [You will learn how to fork a repo next.](fork-repo)
:::

******

### Step 3: Fork the repository

Once you have created an issue or identified what you wish to work on, you will [`Fork` or create a copy of the repo](fork-repository) in your GitHub account.

:::{button-link} fork-repo
:color: primary
:shadow:

<i class="fa-brands fa-leanpub" style="color: #6ec9c3;"></i> Learn how to fork a GitHub repo
:::

:::{admonition} Activity: Fork a repository and modify a file

**Fork the pyOpenSci practice GitHub repository**
*******

Fork the <a href="http://www.github.com/pyopensci/repo-here" target="_blank">pyOpenSci demo repository on GitHub</a>. Remember that a fork is a copy of a repository that is owned by someone else or an organization that lives in your GitHub account.
:::

********

### Step 4: Edit and commit your changes

Once you've successfully forked the repo, it's time to edit the file you want to fix. In this lesson, you are editing documentation files in the GitHub interface. This means that you don't need to set up a local development environment.

:::{button-link} edit-commit-files
:color: primary
:shadow:

<i class="fa-brands fa-leanpub" style="color: #6ec9c3;"></i> Learn more about editing & committing files on GitHub
:::

:::{admonition} Activity: Make a change to a file and commit it to your fork

1. Navigate to your fork on GitHub.com
2. In the GitHub interface, click on the file that you proposed to modify or fix [in the identify issue lesson](identify-issue): instructions on how to do this are below
3. Click on the edit <kbd><i class="fa-solid fa-pencil"></i></kbd> button in the GitHub interface.
4. Make the edits to the file that you proposed in your issue.
5. Hit the <kbd>commit</kbd> button to save your edits
6. Add a descriptive commit message that describes the change that you made

Some examples:
> fix: fixed numerous typos in the filename.py file
>
> fix: updated the code to align with PEP 8 syntax
>
> fix: fixed typo in docstring text

:::

******

### Step 5: Submit a pull request

Once your edits are [committed to git version control](edit-commit-files), open a <kbd>Pull Request</kbd> to the parent repository.

:::{button-link} pull-request
:color: primary
:shadow:

<i class="fa-brands fa-leanpub" style="color: #6ec9c3;"></i> Learn more about creating your first GitHub pull request
:::

:::{admonition} Activity: Submit a PR to the pyOpenSci parent repository
Create a pull request to the [pyOpenSci parent repository](https://github.com/pyOpenSci/pyos-demo-package-contribute), from the branch on your fork that you worked on in the previous lesson.
:::

Once your PR is open, it's time to sit back and wait for the maintainers, collaborators, or project owners to review/comment on your PR. Be patient; this step can take time as people are busy and often donate their time to this effort!

********

## Start with contributions to documentation

Many people's first contributions are to documentation. Documentation contributions can be incredibly valuable as developers often don't have time to work on documentation and code!

Fixing typos and other small documentation issues makes for great, easy-to-create (and review) first pull requests. In fact, if you find that the contributing information isn't detailed enough, that could also be your first contribution!

When you edit documentation, you can often make the changes in the GitHub interface online versus needing to clone the repository and work locally.

:::{admonition} A real-life first contribution to PyPI

[Here is an example issue that resulted in 2 small pull requests to PyPI (warehouse)](https://github.com/pypi/warehouse/issues/17374). In this case, the images were outdated, so it was a bug in the documentation that needed to be fixed. However, while getting to know the repository, the author also found issues with the development documentation, so they submitted a pull request to address that as well. Both pull requests were small.
:::
