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
  "title": "How to fork a GitHub repository and make a copy of it in your GitHub account: Intro to Collaborative GitHub"
  "description lang=en": "A complete guide to forking or making a copy of a GitHub repository that you don't own into your own account."
  "keywords": "GitHub, OpenSource, beginner-friendly"
  "property=og:locale": "en_US"
---

(fork-repository)=
# How to Fork a GitHub Repository 


:::{admonition} What you will learn:
:class: tip

In this lesson, you will learn how to <kbd>fork</kbd> (or create a copy of) a GitHub repo into your own **GitHub.com** account. You can practice forking the pyOpenSci example repository. 
::: 



## How to fork a GitHub repository

To fork a GitHub repository:

1. Navigate to the repo page that you wish to <kbd><i class="fa-solid fa-code-fork"></i> Fork</kbd> - for example:

`https://github.com/pyopensci/pyos-demo-package-contribute`

2. On that page, you will see a button in the upper right-hand corner that says <kbd><i class="fa-solid fa-code-fork"></i> Fork</kbd>. The number next to that button tells you how many times the repository has already been forked by other users (or how many other repository copies exist on GitHub.com. 
3. Click on the <kbd><i class="fa-solid fa-code-fork"></i> Fork</kbd> button and select your user account when it asks you where you want to fork the repo. 
4. Once you have forked the repo, you will have a copy in your account. Navigate to your repo page. The URL should look something like this:

`https://github.com/your-user-name/pyos-demo-package-contribute`


:::{figure} /images/github/fork-repo-animated.gif
:alt: alt 

To fork a repo, first, navigate to the repo you want to fork. Then click the **fork** button in the upper right-hand corner of your screen. You can then create a copy of this repo in your account.
:::



## Who owns a GitHub repository?

When a repository is stored on **GitHub.com**, it is assigned a unique URL (i.e. link on the **GitHub.com** website) that can be used to find the repository and access its files. While repositories on **GitHub.com** can be made either public or private, the default is public for free **GitHub** accounts.

In either case (public or private), the URL links to a **GitHub** repository always follows the same format: 

`https://github.com/username/repository-name`

The username is the username owner of the repo owner. The username can either be an individual such as `lwasser` (your **GitHub** username), or it can represent an organization such as `pyOpenSci`.

For example, the repository that you will work within this lesson is owned by `pyopensci.` Therefore, the URL looks like this:

`https://github.com/pyopensci/repo-name`


## What is forking a GitHub repository?

:::{figure} /images/github/fork-repo.png
:alt: ""

When you fork a GitHub repository, you make a copy of the files and the commit history into your personal account. This allows you to work on the files independently before suggesting changes through a pull request to make to the parent repository you forked from.
:::

Using **GitHub.com**, you can create a copy of another user's or organization’s repository—a process called `forking`. When you fork a repository, you get your own version to work on. You can do that without affecting the original files in the parent repository. Others can also fork your repositories, creating their own copies.

Forking is useful because the fork remains linked to the original repository. This allows you to:
- Update your fork with changes from the original repository.
- Suggest changes to the original repository, which the owner can review and accept.

By forking, everyone collaborates on their own copies of the project, ensuring the original files stay intact. All changes are tracked in the file history and can be undone if needed. You can fork a repository directly from its main page on **GitHub.com**.

## A few tips about forking a repo


1. A GitHub (or GitLab) repository fork is a copy of the GitHub repository that you own in your account. The repository, however, is still connected to the parent repository on GitHub that you forked. This connection means that you can submit pull requests and changes to the repository using your fork.

It also means you can update your fork anytime, as the parent repository is updated to ensure it stays in sync.

2. If you have already forked the repository but some time has passed. You should consider updating or syncing your fork. GitHub has a sync button that you can use to do this (`pyopensci/repo-name`). This will ensure that all of the files in your repository are current.
