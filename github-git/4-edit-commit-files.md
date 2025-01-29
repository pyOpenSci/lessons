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

:::{todo}
Github has changed things a bit. If you edit the file in place, it automatically directs you to a pr workflow in the repo that you are in.

So I think we want to break this down into two things

1. The drive-by pull request
 * Click on the edit button in the repo that you want to make changes.
 * If you don't have permissions, it will automatically ask you about making a branch, which will be from your fork.

2. The pr from your fork. If the fork already exists, then you can still edit the file in place. 
   
:::

In the previous lesson, [you identified something that you wanted to fix in our example GitHub repository](2-identify-issue). Ideally, the fix that you identified is small, text-based, and can be made by modifying a single file. 

After you [forked the repository that you want to contribute to](3-fork-repo) and received approval from a maintainer to work on the issue, it's time to start making the changes you suggested. 

:::{admonition} What you'll learn here
:class: tip
In this lesson, you will edit a file in the demo pyOpenSci repository using the GitHub interface in your [forked repo](3-fork-repo). You will then commit your changes.
:::


Here, you will make the changes that you proposed to work on using only the native GitHub interface. 
To do this, you do not need to [clone or make a copy of your repo locally](clone-repo). 


:::{admonition} Activity: Make a change to a file and commit it to your fork 

1. Navigate to your fork on GitHub.com
2. In the GitHub interface, click on the file that you proposed to modify or fix [in the identify issue lesson](2-identify-issue): instructions on how to do this are below
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

:::{figure} /images/github/edit-commit-file.gif

:::


## About editing files on GitHub

Editing a file on GitHub allows you to focus on the contributing workflow without needing to learn or install git, create a local development environment, or use the command line.

Following this process, you can edit as many files as you wish. However, on GitHub, you must edit and commit changes to them individually. 

### Editing files on GitHub vs GitHub Codespaces vs Locally

In the above image, you edit the file online at GitHub.com. To do this, you navigate to the page that you want to edit and click on the <kbd><i class="fa-solid fa-pencil"></i></kbd> edit button. This approach is a great way to start contributing as you don't have to

1. use the command line to edit the file
2. know how to use .git

However, the one small downside of this approach is that you can only edit and commit one file at a time. 

An alternative way to edit multiple files on GitHub is to use GitHub Codespaces. 

[GitHub codespaces](github-codespaces) provide online GitHub development environments that allow you to edit multiple files and commit them together using an IDE (interactive development environment) such as VsCode. 

Sometimes, maintainers will set up a codespace for you to use. Or, you can also set one up yourself in your fork. GitHub codespaces also come with GitHub setup, which means that you can commit files to your fork within VsCODE vs needing to know how to use the command line. 

## What is a commit?

Here are 3 points to remember when you think about commits:

1. A **commit** is a feature of [git version control](what-is-git) that is similar to saving your changes with a note explaining what you did.

2. Each commit that you make represents a set of changes to one or more files in your repository at a specific time.

:::{figure}  /images/github/git-commits-files.png
:alt: A visual example demonstrating how Git tracks changes to a document through commits. The image shows an “Original File” with its initial text, followed by two commits. The first commit adds a new paragraph of text, with the changes highlighted in green and the commit message, “Fix: added a new paragraph to clarify text.” The second commit fixes typos in the text, with the edits highlighted in green and the commit message, “Fix: copy edits.” At the bottom, a comparison shows the document after each commit, illustrating how the file evolves with changes.

:::


3. Because you are using git, you can always revert or undo a set of changes in your commit history. While undoing things in git takes a bit more knowledge, knowing it can be done can give you the confidence to make changes without worrying about breaking things! 

:::{figure}  /images/github/git-what-are-commits.png
:alt: A diagram explaining Git commits and their role in version control. The top section shows a timeline of circular commits, each paired with a file icon to represent file changes, with the text: “Each commit represents one or more file changes made at a specific point in time.” The middle section highlights the “Latest Commit” on the timeline, showing it as the current state of the repository. The bottom section demonstrates the concept of reverting, with an arrow pointing from a later commit back to a previous one, illustrating that Git allows reverting or going back to earlier commits. The text reads: “You can also always revert or return to a previous commit. This is what makes Git powerful.”

:::

## Up next - create a pull request
Once you have made the changes to the files that you wish to change in your branch, you are ready to open a [pull request](5-pull-request). You will learn how to do that next.

:::{todo}
It might be cool to show first contributions like my first on to nbconvert could be interesting? Other people might have examples too from the community that we could share with some stories about it??
:::
