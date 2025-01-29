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
title: "Contribute to Open Source: How to Submit a Pull request"
description: "A description here"
keywords: python, open source, tutorial
---
```

# How to Submit a GitHub Pull Request

In the last lesson, you learned how to [make and commit a change to a document in a GitHub repository](4-edit-commit-files). 
In this lesson, you will learn how to submit a pull request after making changes to a file in a GitHub repository.  

A GitHub pull request (**PR**):

1. **Allows you to suggest changes rather than making them directly to a repo you don't own** in a transparent way. You can't break things by submitting a PR!
1. **Supports Review**: A pull request also triggers a review process where other repository owners and users can review and comment on your changes and suggest edits to your changes line-by-line.
1. **Maintainers to manage contributions**: PRs allow maintainers to document, approve, and merge contributions into the project in a consistent way.

Pull requests empower you to contribute to the work of others in an open and accessible way, even if you don't have direct access to the repository.

:::{admonition} Activity: Submit a PR to the pyOS parent repository

Using the branch that you created in the previous lesson, create a pull request for the pyOS parent repository. 
:::

## Step 1: Open your GitHub pull request 

To start a PR, click the <kbd>`New pull request`</kbd> button on the main page of your forked repository. Or, if you recently made a change to a branch in your fork, then GitHub will recognize is and prompt you to submit a PR (see the image below). 


:::{figure} /images/github/create-pr-fork.gif

When you edit a file in your fork, GitHub recognizes it and prompts you to create a pull request. 
:::


:::{tip}
You will notice the Pull Request button in different places in the GitHub interface. Note that even tho you see the button on different pages, it does the same thing.
:::


### Step 2: Setup your pull request targets (head and base)

When you create your pull request, take note of the head and base targets. 
The repo that you wish to update is the base repo) and the
repo that contains the content that you want to use to update the base
(the head repo).

In this example, you want to update:

* **base**: `pyopensci/pyos-demo-package-contribute` with
* **head**: commits in your fork `your-username/pyos-demo-package-contribute`.

The above pull request configuration tells **GitHub** to update the base repository with contents from your forked repository or the head repository.


:::{admonition} Pull request terminology: Head vs. Base

When submitting a pull request, you specify two repositories:

- **Base**: The repository you want to update (e.g., your colleague's repo).
- **Head**: The repository with the changes to be added (e.g., your fork).

The **head** is a**head** of the **base**, meaning the head repo has changes that the base repo doesn't yet have. The goal is to merge changes from the **head** (your fork) into the **base** (your colleague's repo).

When you create a pull request, GitHub will auto-fill these fields. For example:
- **Base fork**: `colleague-username/project-name`
- **Head fork**: `your-username/project-name`
:::

### Step 3 - Verify The Changes In Your Pull Request

When you compare two repos in a pull request page, **GitHub** provides an overview of the differences (diffs) between the files. 

Carefully review these changes to
ensure that the changes that you are submitting are in fact the ones that you
want to submit.

1. First, look at the number of files. How many files did you modify? Do you see that many files listed in the **PR**?
2. Look over the changes made to each file. Do the changes all look correct (likechanges that you committed to the repository)?

:::{figure} /images/github/pr-check-files.gif

When you first create a PR, be sure to check the PR contents. Notice that the number of files and commits are displayed in this image. Make sure these numbers make sense based upon the changes that you made.
:::

<i class="fa fa-star"></i> **Data Tip:** You can also click on the commit titles to see the specific changes in each commit. This is another way to check that the contents of a PR are what you expect them to be.
{: .notice--success}

This review of your own **PR** before submitting it is important. Remember that someone
else is going to take time to review your PR. 

Make sure that you take care of
cleaning up what you can FIRST, before submitting the PR.

### Step 4 - Click on the Create New Pull Request Button

The next step of the create PR process is to click the "Create Pull Request" button. Note that this button will NOT be available if you have not changed your repo (e.g. fork). 

Click the green “Create Pull Request” button to start your pull request. Once you do that, a title box and description box will be visible.

Add a title and write a brief description of your changes. When you have added your
title and description, click on “Create Pull Request”.

:::{tip} 
You can modify the title and description of your pull request at any time - even after you've submitted the pull request!
:::

Pull request titles should be concise and descriptive of the content in the pull request. More detailed notes can be left in the comments box.



## Pull Requests and Your Location On GitHub

When you create a new pull request, you will be automatically transferred to the
**GitHub.com** URL or landing page for the base repository (your colleague's
repository). 

At this point, you have submitted your pull request!

At the bottom of your pull request, you may see an large green button that says
**Merge Pull Request**. This button will be used by owner of the
repository (your colleague or perhaps others working on this collaborative project)
to merge in your changes, when a review has been completed. 

The repo owner will
review your PR and may ask for changes. When they are happy with all of the changes, your PR could get merged!

<i class="fa fa-star"></i> **Data Tip:** All future commits that you make to your fork (on the branch where you are working) will continue to be added to the open pull request UNTIL it is merged.
{: .notice--success}

## How To Merge GitHub Pull Requests on GitHub

After you have submitted your PR, someone who owns or manages the repo where you
are submitting the PR will review it. At this point, they will either:

1. suggest that you make some changes to the PR or
2. merge the PR if they are happy with all of the changes that you made.

:::{todo}
A screencast showing how this process works is below.

It's common for a reviewer to comment on your pull request and request changes. Once the reviewer is happy with the PR, they will merge it using the merge button on the bottom of the PR. It is important to note that you can only merge a PR in a repo in which you have permission to merge.
:::

## Pull Requests and Your Location On GitHub

When you create a new pull request, you will be automatically transferred to the
**GitHub.com** URL or landing page for the base repository (your colleague's
repository). 

At this point, you have submitted your pull request!

At the bottom of your pull request, you may see an large green button that says
**Merge Pull Request**. This button will be used by owner of the
repository (your colleague or perhaps others working on this collaborative project)
to merge in your changes, when a review has been completed. 

The repo owner will
review your PR and may ask for changes. When they are happy with all of the changes, your PR could get merged!

<i class="fa fa-star"></i> **Data Tip:** All future commits that you make to your fork (on the branch where you are working) will continue to be added to the open pull request UNTIL it is merged.
{: .notice--success}

## How To Merge GitHub Pull Requests on GitHub

After you have submitted your PR, someone who owns or manages the repo where you
are submitting the PR will review it. At this point, they will either:

1. suggest that you make some changes to the PR or
2. merge the PR if they are happy with all of the changes that you made.



### How To Close Pull Requests on GitHub

You can also close a pull request on **GitHub** if you decide you are not
ready to submit your files from your forked repository to the original repository.

For example, the pull request you just created in this lesson can be closed anytime before it is merged. 

When you are ready to submit changes,
you can simply create a new pull request on **GitHub** following these same steps.

To close a pull request, click on `Close pull request` button towards the
bottom of the pull request page.
