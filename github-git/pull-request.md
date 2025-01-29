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
  "title": "Collaborative GitHub for Beginners: How to submit a GitHub pull request"
  "description lang=en": "Learn how to submit a pull request after making changes to a file in a GitHub repository"
  "keywords": "GitHub, OpenSource"
  "property=og:locale": "en_US"
---

# How to Submit a GitHub Pull Request

In the last lesson, you learned how to [make and commit a change to a document in a GitHub repository](edit-commit-files).
In this lesson, you will learn how to submit a pull request after making changes to a file in a GitHub repository.  

A GitHub pull request (**PR**):

1. **Allows you to suggest changes rather than making them directly to a repo you don't own** in a transparent way. You can't break things by submitting a PR!
1. **Supports Review**: A pull request also triggers a review process where other repository owners and users can review and comment on your changes and suggest edits to your changes line-by-line. This makes incorporateing your changes fully transparent.
1. **Maintainers to manage contributions**: PRs allow maintainers to document, approve, and merge contributions into the project in a consistent way.

Pull requests empower you to contribute to the work of others in an open and accessible way, even if you don't have direct access to the repository.

## The steps

### Step 1: Open your GitHub pull request

To start a new pull request,click the <kbd>`New pull request`</kbd> button on the main page of your forked repository. Or, if you recently made a change to a branch in your fork, then GitHub will recognize is and prompt you to submit a PR (see the image below).

:::{figure} /images/github/github-create-pull-request.png
To create a pull request, go to the Pull Request tab in your account. Then click on the New pull request button.
:::

:::{tip}
You will notice the Pull Request button in different places in the GitHub interface. Note that even tho you see the button on different pages, it does the same thing.
:::

:::{figure} /images/github/create-pr-fork.gif

Animated gif showing that GitHub will prompt you to make a new pul request when it notices new commits to a branch in your fork.  
:::

### Step 2: Setup your pull request targets (head and base)

:::{figure} /images/github/github-pr-targets-head-base.png
When you setup your pull request, you will need to specify the head and the base. The head refers to the branch that is a-HEAD of the parent repository--ie a branch on your fork! The base is the parent repository that you wish to submit changes to.
:::

When you create your pull request, take note of the head and base targets.
The repo that you wish to update is the base repo) and the
repo that contains the content that you want to use to update the base
(the head repo).

In this example, you want to update:

* **base**: `pyopensci/pyos-demo-package-contribute` with
* **head**: commits in your fork `your-username/pyos-demo-package-contribute`.

The above pull request configuration tells **GitHub** to update the base repository with contents from your forked repository or the head repository.

### Step 3: Verify changes in your pull request

When comparing repositories in a **pull request (PR)**, GitHub provides a **diff view** of changes between files (diff as in difference). Before submitting the pr, carefully review these changes to ensure that what you intended to submit is in the PR (and nothing else).

Since others will review your PR, take time to **clean up unnecessary changes** before submitting. your time upfront will lead to the PR being merged sooner and will make it easier for others to review.  

Before you submit your PR, check:

1. **The number of files:** Do they match what you intended to modify?
2. **Review changes in each file:** Are all modifications correct and expected?

:::{figure} /images/github/pr-check-files.gif

When you first create a PR, be sure to check the PR contents. Notice that the number of files and commits are displayed in this image. Make sure these numbers make sense based upon the changes that you made.
:::

:::{admonition} <i class="fa fa-star"></i> Exploring commits
You can also click on the commit titles to see the specific changes in each commit. This is another way to check that the contents of a PR are what you expect them to be.
:::

### Step 4: Finalize and submit your PR

Once you've reviewed your PR and evertyhing looks good, it's time to submit it.

Add a descriptive title and write a brief description of your changes. Pull request titles should be concise and descriptive of the content in the pull request. When you have added your
title and description, click on “Create Pull Request” one more time to submit the PR.

If you go to the parent repotiory you will see the PR listed there.

:::{tip}
You can modify the title and description of your pull request at any time - even after you've submitted the pull request.
:::

## Close a Pull Request

If you're not ready to submit, you can close a PR anytime via the **Close pull request** button. You can reopen it later if needed.

## Who Can Merge a Pull Request?

When you create a **pull request (PR)**, GitHub directs you to the parent repository (e.g., the pyOpenSci repo). At the bottom of the PR, a **Merge Pull Request** button appears, which only the **repository owner** or collaborators can use after reviewing your changes.

The repo owner may request modifications before merging. Any future commits to the same branch will be added to the PR until it is merged.

::: {note}
<i class="fa-solid fa-wand-sparkles"></i> New commits to your working branch will continue updating the open PR until it is merged.
:::
