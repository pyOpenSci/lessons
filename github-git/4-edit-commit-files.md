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

# Your first edits to a file in your fork 

:::{admonition} Activity: Fork a repository and modify a file
:class: tip
In this lesson, you will edit a file in the demo pyOpenSci repository using the GitHub interface in your [forked repo](3-fork-repo). You do not need to [clone or make a copy of your repo locally](clone-repo) to do this! 

This is a great way to make your first contribution to open source without needing to know `git` or the command line! 

:::

In the previous lesson, [you selected or identified something that you wanted to fix in our example GitHub repository](3-identify-issue). Ideally, the fix that you identified is small, text-based, and can be made by modifying a single file. Small contributions are a great way to start.

After you [forked the repository](3-fork-repo) you are contributing to and received the OK to move forward with your pull request through an open issue, you are ready to get to work.

Here you will make the changes that you proposed to work on using only the native GitHub interface.


:::{admonition} Activity: Make a change to a file and commit it to your fork 

**1. Go to your fork**
*******
**2. In the GitHub interface, click on the file that you proposed to modify or fix [in the identify issue lesson](2-identify-issue).**: instructions on how to do this are below
*******
**3. Click on the edit <kbd><i class="fa-solid fa-pencil"></i></kbd> button in the GitHub interface.**
*******
**4. Make the edits that you proposed in your issue to the file.**
*******
**5. Hit the <kbd>commit</kbd> button to save your edits** 
**6. Add a descriptive commit message that describes the change that you made** 

Some examples:
> fix: fixed numerous typos in the filename.py file
> 
> fix: updated the code to align with PEP 8 syntax
> 
> fix: fixed typo in docstring text 

*An overview of all of these steps is below.*
:::


## About editing files on GitHub

Editing a file on GitHub is a great way to start contributing because it allows you to focus on the contributing workflow without setting up a local development environment.

Following this process, you can edit as many files as you wish. However, given that you are editing files on GitHub, you must edit and commit them one at a time.  

### Codespaces: Cloud-based development environments on GitHub
In some cases, projects may use [GitHub codespaces](github-codespaces), which allow you to work on content in a coding environment using an interface like VSCode fully in your browser.

However, you will make text changes to a file to build confidence around the contributing workflow.

## What is a commit?

Here are 3 points to remember about commits:

1. A **commit** is a feature in the [git version control](what-is-git) that is similar to saving your changes with a note explaining what you did.

2. Each commit that you make represents a set of changes to one or more files in your repository at a specific time. 

3. You can always revert or undo a set of changes in the commit history. While undoing things in git takes a bit more knowledge, knowing it can be done can give you confidence to make changes without worrying about breaking things! 

:::{figure}  /images/github/git-what-are-commits.png
:alt: Alt here

:::

::::

:::{todo}
It might be cool to show first contributions like my first on to nbconvert could be interesting? Other people might have examples too from the community that we could share with some stories about it??
:::
