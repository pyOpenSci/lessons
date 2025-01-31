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
  "title": "How to edit and commit changes to a file on GitHub: Intro to Collaborative GitHub"
  "description lang=en": "Learn how to edit a file and then commit changes to that file to version control. All in the GitHub interface."
  "keywords": "GitHub, OpenSource, beginner-friendly"
  "property=og:locale": "en_US"
og:image: /images/github/steps-to-contribute.png
og:image:alt: An image that shows the steps for contributing to open source on GitHub.
---

# Your First Edits to a File in Your Fork: Edit & Commit

Now that you've [identified and comment on an issue](identify-issue), [forked the repository](fork-repo) and received approval to work on an issue, it's time to make your changes.  

> **💡 Reminder:** Your fix should be **small and text-based**, like updating documentation or fixing a typo.  

:::{admonition} What you'll learn  
:class: tip  
You’ll edit a file directly in your **fork** using GitHub’s interface and commit the changes using only the native GitHub interface. 

NOTE: If you want to work on the files locally on your laptop, you will need to [clone or make a copy of your repo locally](clone-repo).

:::

## How to edit a file in your fork  

GitHub lets you edit files right in your browser. Here’s how:  

1. Navigate to **your fork** of the repository.  
2. Find the file you want to edit.  
3. Click the <kbd><i class="fa-solid fa-pencil" style="color: #81c0aa;"></i> Edit</kbd> button.  
4. Make your changes and **commit** them.

:::{figure} /images/github/edit-commit-file.gif
:alt: "GIF showing how to edit and commit a file on GitHub."  

Editing a file directly in the GitHub interface is a straight forward process. 
:::

> **⚡ Quick tip:** You can edit as many files as you want, but GitHub only lets you commit them **one at a time** in the browser.  


## Ways to edit a file: GitHub vs. GitHub Codespaces  

GitHub now offers **two ways** to edit files directly in the interface or using the [cloud-based GitHub Codespaces](about-codespace). If you’re making a small change, use GitHub’s interface. If you need to edit multiple files, try Codespaces. 

| | Option  | When to Use | Pros | Limitations |  
|-|---------|------------|------|-------------|  
| | **GitHub Interface** <i class="fa-solid fa-pencil" style="color: #81c0aa;"></i> | Quick edits (typos, small fixes) | No setup needed, edit in browser | Can only commit one file at a time |  
| | **GitHub Codespaces** <i class="fa-solid fa-laptop-code" style="color: #81c0aa;"></i> | Editing multiple files | Full VS Code environment in browser | Requires configuration but once configured, you can reuse it |  

> **💡 Need to edit multiple files using a coding editor like VsCode or Jupyter?** Learn more about using [GitHub Codespaces](github-codespaces).  

## What is a commit?

A commit is like taking a snapshot of your changes so you can always "undo" the changes if needed. You can think of a **commit** as a save (or restore) point in git's history. Each commit captures changes you make to one or more files in the repository at a specific time; each commit includes a note explaining what you did. 

:::{tip}
A **commit** is a feature of [git version control](what-is-git), the version control system that GitHub runs in the background. 

:::

### How commits work

:::{figure}  /images/github/git-commits-files.png
:alt: A visual example demonstrating how Git tracks changes to a document through commits. The image shows an “Original File” with its initial text, followed by two commits. The first commit adds a new paragraph of text, with the changes highlighted in green and the commit message, “Fix: added a new paragraph to clarify text.” The second commit fixes typos in the text, with the edits highlighted in green and the commit message, “Fix: copy edits.” At the bottom, a comparison shows the document after each commit, illustrating how the file evolves with changes.

Each commit represents **a set of changes** at a specific time. 
:::

> **🛠 Do you need to undo changes that you made?** Git lets you revert to an earlier commit, so you don’t have to worry about breaking anything.


:::{figure}  /images/github/git-what-are-commits.png
:alt: A diagram explaining Git commits and their role in version control. The top section shows a timeline of circular commits, each paired with a file icon to represent file changes, with the text: “Each commit represents one or more file changes made at a specific point in time.” The middle section highlights the “Latest Commit” on the timeline, showing it as the current state of the repository. The bottom section demonstrates the concept of reverting, with an arrow pointing from a later commit back to a previous one, illustrating that Git allows reverting or going back to earlier commits. The text reads: “You can also always revert or return to a previous commit. This is what makes Git powerful.”

You can always **undo or revert** changes using Git. 
:::

:::{admonition} What's next?  
:class: seealso  

<i class="fa-brands fa-github-alt"></i> Once you've committed your changes, you can open a **pull request (PR)** to suggest your edits to the main project.  

*****

[Learn how to create a pull request →](pull-request)  
:::
 

:::{todo}

It might be cool to show first contributions like my first on to nbconvert could be interesting? Other people might have examples from the community that we could share some stories about.
:::
