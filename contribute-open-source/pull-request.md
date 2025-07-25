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
  "title": "How to submit a GitHub pull request: Collaborative GitHub for beginners"
  "description lang=en": "Learn how to submit a pull request after making changes to a file in a GitHub repository"
  "keywords": "GitHub, OpenSource"
  "property=og:locale": "en_US"
---

(pyos-pull-request)=

# About Pull Requests

> In this lesson, you’ll learn how to:
> <i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> Submit a pull request with changes to a file in your fork to the parent repo using the GitHub interface
>

In the last lesson, you learned how to [make and commit a change to a document in a GitHub repository](pyos-edit-commit-files).
In this lesson, you will learn how to submit a pull request after making changes to a file in a GitHub repository.

A GitHub pull request (**PR**):

1. **Allows you to suggest changes rather than making them directly to a repo you don't own** in a transparent way. You can't break things by submitting a PR!
1. **Supports Review**: A pull request also triggers a review process where other repository owners and users can review and comment on your changes and suggest edits to your changes line-by-line. This makes incorporating your changes fully transparent.
1. **Maintainers to manage contributions**: PRs allow maintainers to document, approve, and merge contributions into the project in a consistent way.

> **<i class="fa-solid fa-handshake-angle" style="color: #81c0aa;"></i> Social cue:**
> A pull request is a **collaborative tool**—it lets maintainers review changes
> before merging them. PRs **show transparency** and let others give feedback,
> making sure every update aligns with the project's goals.

Pull requests empower you to contribute to the work of others in an open and accessible way, even if you don't have direct access to the repository.

## How to Submit a GitHub Pull Request

### Step 1: Open your GitHub pull request

To start a new pull request, click the <kbd>`New pull request`</kbd> button on the main page of your forked repository. Or, if you recently made a change to a branch in your fork, then GitHub will recognize it and prompt you to submit a PR (see the image below).

:::{figure} /images/github/github-create-pull-request.png
To create a pull request, go to the Pull Request tab in your account. Then click on the New pull request button.
:::

:::{tip}
You will notice the Pull Request button in different places in the GitHub interface. Note that even tho you see the button on different pages, it does the same thing.
:::

:::{figure} /images/github/create-pr-fork.gif

Animated gif showing that GitHub will prompt you to make a new pull request when it notices new commits to a branch in your fork.
:::

### Step 2: Setup your pull request targets (head and base)

:::{figure} /images/github/github-pr-targets-head-base.png
When you setup your pull request, you need to specify the head and the base. The head refers to the branch and associated repository that is **a-HEAD** of the parent repository--for example, a branch on your fork! The base is the parent repository that you wish to submit changes to.
:::


When creating a **pull request (PR)**, you need to define where your changes should be added and where they come from.

- **<i class="fa-solid fa-database" style="color: #81c0aa;"></i> Base:** The repository where you want your changes to be merged. *(This is usually the original repo you forked.)*
- **<i class="fa-solid fa-code-branch" style="color: #81c0aa;"></i> Head:** The repository containing your changes. *(This is your fork. The copy of the repo that you own, where you made edits.)*

> **🔹 Quick way to remember:** The **head** is "ahead" of the base, meaning it has new changes that the base repository does **not** yet have.

In this example, you want to update:

- **base**: `pyopensci/pyos-demo-package-contribute` with
- **head**: commits in your fork `your-username/pyos-demo-package-contribute`.

> **<i class="fa-solid fa-code-branch" style="color: #81c0aa;"></i> Social Tip:**
> Choosing the correct **head** and **base** repositories ensures that your changes
> go to the right place. If you accidentally select the wrong base, your PR might not
> reach the maintainers you intended. Double-check this before submitting!

:::{admonition} What is a branch

A branch is a working version of a git repository that you can use to work on features, bugs, and more. Branches allow you to work on files in isolation, rather than working on the main version of the repository.
[Learn more about GitHub branches here.](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
:::

:::{todo}

/images/github/base-vs-head.png
:alt: "Diagram showing how base and head work in GitHub pull requests."
Create Graphic: Simple diagram with arrows from "Your Fork (Head)" → "Original Repo (Base)"

:::

### Step 3: Review your own pull request first

When comparing repositories in a **pull request (PR)**, GitHub provides a **diff view** of changes between files (diff as in difference). Before submitting the PR, carefully review these changes to ensure that what you intended to submit is in the PR (and nothing else).

Since others will review your PR, take time to **clean up unnecessary changes** before submitting. Your time upfront will lead to the PR being merged sooner and will make it easier for others to review.

> **<i class="fa-solid fa-magnifying-glass" style="color: #81c0aa;"></i> Social cue:**
> A PR isn't just about submitting changes—it’s about **communicating clearly** with
> maintainers. A well-reviewed PR with **only relevant changes** is easier to merge.
> **Check that your PR doesn’t include unintended file modifications.**

Before you submit your PR, check:

1. **The number of files:** Do they match what you intended to modify?
2. **Review changes in each file:** Are all modifications correct and expected?
3. **Make sure there aren't merge conflicts:** A merge conflict occurs when two or more people edit the same lines of a file, and Git doesn’t know which changes to accept. This most commonly happens when you modify a file on a branch, but someone else also updates those same lines in the parent repository before your changes are merged. You can check if your PR has merge conflicts by looking at the bottom of the PR page.

:::{figure} /images/github/pr-check-files.gif

When you first create a PR, be sure to check the PR contents. Notice that the number of files and commits are displayed in this image. Make sure these numbers make sense based upon the changes that you made.
:::

:::{admonition} <i class="fa fa-star"></i> Exploring commits
You can also click on the commit titles to see the specific changes in each commit. This is another way to check that the contents of a PR are what you expect them to be.
:::

### Step 4: Finalize and submit your PR

Once you've reviewed your PR and everything looks good, it's time to submit it.

Add a descriptive title and write a brief description of your changes. Pull request titles should be concise and descriptive of the content in the pull request. When you have added your
title and description, click on “Create Pull Request” one more time to submit the PR.

> **<i class="fa-solid fa-pen-to-square" style="color: #81c0aa;"></i> Social cue:**
> A **clear, descriptive PR title** helps maintainers quickly understand your changes.
> A good title is specific: **"Fix typo in README"** is better than **"Updated file"**.
> Your description should also **explain why** the change was made.

If you go to the parent repository, you will see the PR listed there.

:::{tip}
Note that your pull request can be modified at any time, but do so cautiously.

- You can modify the title and description of your pull request even after you've submitted it.
- New commits to your working branch will be visible in your open PR until they are merged.
-

Any changes made to it will potentially delay a review from maintainers. It's best to submit the PR, review it, and leave it unchanged until you get feedback.
:::

## Close or move a Pull Request to draft

Sometimes, after opening a pull request, you realize it's **not quite ready for review**. In that case, you have two options:

1. **<i class="fa-solid fa-file-pen" style="color: #81c0aa;"></i> Convert it to a draft** – A draft pull request signals to maintainers that your PR is **still in progress** and not yet ready for review.
2. **<i class="fa-solid fa-xmark" style="color: #81c0aa;"></i> Close the PR** – You can close a PR anytime via the **Close pull request** button and reopen it later when you're ready to submit.

## Who can merge a pull request?

When you create a **pull request (PR)**, GitHub directs you to the parent repository (e.g., the pyOpenSci repo). At the bottom of the PR, a **Merge Pull Request** button appears, which only the **repository owner** or collaborators can use after reviewing your changes.

> **<i class="fa-solid fa-user-shield" style="color: #81c0aa;"></i> Social cue:**
> Only maintainers can merge PRs, but **you can make their job easier**!
>
> - **Be responsive** if they ask for changes.
> - **Follow repository guidelines** for PR structure.
> - **Check for review comments** and update your PR accordingly.

The repo owner may request modifications before merging. Any future commits to the same branch will be added to the PR until it is merged.

:::{admonition} You did it!
:class: seealso

Once you've opened your **pull request (PR)**, you wait for a response from the maintainer team! Congratulations on submitting a contribution to open source!

If you want to dig deeper, you may want to learn how to clone a repo and work on changes locally on your computer.
[<i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> Learn how to clone a GitHub repository →](clone-repo)
:::
