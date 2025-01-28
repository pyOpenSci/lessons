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

In the previous lesson, [you identified something that you wanted to fix in our example GitHub repository](3-identify-issue). Ideally, the fix that you identified is small, text-based, and can be made by modifying a single file. 

After you [forked the repository that you want to contribute to](3-fork-repo) and received approval from a maintainer to work on the issue, it's time to move forward with a pull request!

:::{admonition} What you'll learn here
:class: tip
In this lesson, you will edit a file in the demo pyOpenSci repository using the GitHub interface in your [forked repo](3-fork-repo). You will then commit your changes.

:::


Here, you will make the changes that you proposed to work on using only the native GitHub interface. 
You do not need to [clone or make a copy of your repo locally](clone-repo) to do this! 


:::{admonition} Activity: Make a change to a file and commit it to your fork 

It's time to make the changes to a file in your fork that you proposed in the open issue:

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

*An overview of all of these steps is below.*
:::


## About editing files on GitHub

Editing a file on GitHub allows you to focus on the contributing workflow without needing to learn or install git, create a local development environment, or use the command line.

Following this process, you can edit as many files as you wish. However, on GitHub, you must edit and commit changes to them individually. 

### How to edit a file on GitHub

TODO: add a screen capture of opening and editing a file. 



:::{admonition} GitHub Codespaces Provide Online GitHub Development Environments

GitHub Codespaces are cloud development environments that can be created and used on GitHub.

Projects may sometimes offer [GitHub codespaces](github-codespaces), which allows you to edit multiple files and commit them together. You can also create a CodeSpace yourself in your fork! 

GitHub Codespaces allows you to work on content in a cloud-based coding environment using an interface like VSCode fully in your browser. If set up correctly, they can contain a project's development environment.
:::

## What is a commit?

Here are 3 points to remember when you think about commits:

1. A **commit** is a feature of [git version control](what-is-git) that is similar to saving your changes with a note explaining what you did.

2. Each commit that you make represents a set of changes to one or more files in your repository at a specific time.

:::{figure}  /images/github/git-commits-files.png
:alt: A visual example demonstrating how Git tracks changes to a document through commits. The image shows an “Original File” with its initial text, followed by two commits. The first commit adds a new paragraph of text, with the changes highlighted in green and the commit message, “Fix: added a new paragraph to clarify text.” The second commit fixes typos in the text, with the edits also highlighted in green, along with the commit message, “Fix: copy edits.” At the bottom, a comparison shows the document after each commit, illustrating how the file evolves with changes.

:::


3. Because you are using git, you can always revert or undo a set of changes in your commit history. While undoing things in git takes a bit more knowledge, knowing it can be done can give you the confidence to make changes without worrying about breaking things! 

:::{figure}  /images/github/git-what-are-commits.png
:alt: A diagram explaining Git commits and their role in version control. The top section shows a timeline of circular commits, each paired with a file icon to represent file changes, with the text: “Each commit represents one or more file changes made at a specific point in time.” The middle section highlights the “Latest Commit” on the timeline, showing it as the current state of the repository. The bottom section demonstrates the concept of reverting, with an arrow pointing from a later commit back to a previous one, illustrating that Git allows reverting or going back to earlier commits. The text reads: “You can also always revert or return to a previous commit. This is what makes Git powerful.”

:::


:::{todo}
It might be cool to show first contributions like my first on to nbconvert could be interesting? Other people might have examples too from the community that we could share with some stories about it??
:::
