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

```{raw-cell}

---
title: TITLE
description: A long time ago
---
```





# Ways to contribute 

There are several ways to contribute to open source if you are just getting started. This page overviews them and then links to more information about the various steps.

## Start here if you haven't yet forked the repository

If you don't already have a fork of the repo that you wish to contribute to in your GitHub account, and you have already opened an issue for the item that you want to fix, you can start by going to GitHub, clicking on the edit button of the file that you want to edit, in the repository that you want to work on (in this case pyopensci/pyos-package-contribute). Do the following: 

If you haven't already forked the repository, then GitHub will do the following:

1. Go to [https://github.com/pyOpenSci/pyos-demo-package-contribute](https://github.com/pyOpenSci/pyos-demo-package-contribute)
2. Navigate to the file that you wish to edit. Click on the <kbd><i class="fa-solid fa-pencil"></i></kbd> edit button.
3. Given that you haven't forked the repo yet, GitHub will inform you that you need to create a fork first. 
4. Once your fork has been created, you can edit the file in the GitHub interface. Note that you are working on your fork of the repo, not the copy that pyOpenSci owns
1. Once you are happy with the changes, you can commit them to version control. In this case you will click on the "propose changes button" to commit your changes.
7. Once you have committed the file (or hit the proposed changes button), GitHub will open a pull request for you in the parent repository. 

:::{figure} /images/github/contribute-no-fork.gif
The GitHub contribute workflow for someone who hasn't yet created a fork of the repo that they wish to contribute to. 
:::

::::{tip}

If you already have a fork of the repo, when you click on the edit file in the pyOpenSci repo, it will tell you that you will edit the file in your fork. Be careful with this approach, however, because GitHub defaults to editing the file on your main branch. 

:::{figure} /images/github/edit-file-github-fork.png
Don't do this!
:::

If you already have a fork, we suggest that you edit the file directly from your fork

:::{figure} /images/github/edit-file-github-fork.png
Edit from your fork directly instead so you can make a new branch.  
:::
::::
