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

# How to Fork a GitHub Repository 

🚧 These lessons are under heavy construction and will continue to change through March 2025 🚧 

:::{admonition} What you will learn:

* Explain how a **GitHub** repository stores and tracks changes to files.
* Create a copy of (<kbd>fork</kbd>) other users' files on **GitHub.com**.
* Use the `git clone` command to download a copy of a **GitHub** repository to your computer. 
::: 


## Who owns a GitHub repository?

When a repository is stored on **GitHub.com**, it is assigned a unique URL (i.e. link on the **GitHub.com** website) that can be used to find the repository and access its files. While repositories on **GitHub.com** can be made either public or private, the default is public for free **GitHub** accounts.

In either case (public or private), the URL links to a **GitHub** repository always follows the same format: 

`https://github.com/username/repository-name`

The username is the username owner of the repo owner. The username can either be an individual such as `lwasser` (your **GitHub** username), or it can represent an organization such as `pyOpenSci`.

For example, the repository that you will work within this lesson is owned by `pyopensci.` Therefore, the URL looks like this:

`https://github.com/pyopensci/repo-name`

(fork-repo)=
## Fork a GitHub repository

Using **GitHub.com**, you can create a copy of another user's or organization’s repository—a process called `forking`. When you fork a repository, you get your own version to work on. And you can do that wrok without affecting the original files in the parent repository. Others can also fork your repositories, creating their own copies.

Forking is useful because the fork remains linked to the original repository. This allows you to:
- Update your fork with changes from the original repository.
- Suggest changes to the original repository, which the owner can review and accept.

By forking, everyone collaborates on their own copies of the project, ensuring the original files stay intact. All changes are tracked in the file history and can be undone if needed. You can fork a repository directly from its main page on **GitHub.com**.

To fork a repo:

1. Navigate to the repo page that you wish to fork - example:

`https://github.com/pyopensci/repo-name`

2. On that page, you will see a button in the UPPER RIGHT hand corner that says `Fork`. The number next to that button tells you how many times the repo has already been forked. 
3. Click on the `Fork` button and select your user account when it asks you where you want to fork the repo. 
4. Once you have forked the repo, you will have a copy in your account. Navigate to your repo page. The URL should look something like this:

`https://github.com/your-user-name/repo-name`

:::{figure} /images/github/image-coming-soon.png
:alt: alt text here

To fork a repo, first, navigate to the repo you want to fork. Then click the **fork** button in the upper right-hand corner of your screen. You can then create a copy of this repo in your account.
:::
