---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
---

# Introduction to Collaborative GitHub and Git

🚧 These lessons are under heavy construction and will continue to change through March 2024 🚧 

Version control is essential in open source software development and increasingly important in sharing and working on open science workflows. GitHub is the most commonly used cloud-based version control platform. GitHub integrates the power of Git with online collaboration and project management tools.

Many think about GitHub as a social coding platform.

GitHub enables:
- **Version control with Git**: Track changes, save work at various stages and revert to earlier versions if needed.
- **Cloud-based backup**: Keep your local work securely backed up online.
- **Collaboration tools**: Share code, streamline contributions, and improve projects collectively.
- **Project management**: Organize updates, assign tasks, and manage milestones.
- **Review processes**: Facilitate clear and collaborative reviews of changes.

## GitHub in open science  

Related to open science, GitHub:
- **Promote transparency**: Share results and methods through accessible code and history.
- **Enables collaboration**: Supports people worldwide working together on the same code and documentation in a structured way.  
- **Ensures reproducibility**: Help others contribute to and build upon your work. 

By combining Git’s version control with GitHub’s collaborative features, you can manage code efficiently while supporting openness,  transparency, and truly open collaboration. 

## Use GitHub by yourself vs. collaboratively  

Git and GitHub are used in two primary ways: **independently** or **collaboratively**. 

### Use GitHub by yourself
Most scientists start using GitHub (and git) on their own. In this scenario, Git is a personal version control system, enabling you to track changes and maintain a complete work history. Working on your own is ideal for personal projects, preliminary research, or prototyping, as it allows you to revert to earlier versions if needed. 

If you are using GitHub on your own, your workflow probably looks something like this:

1. **Clone a Repository**: Copy the project to your local computer.
2. **Work Locally**: Edit files and make changes on your machine.
3. **Commit Changes**: Save your changes to the project history.
4. **Push Changes**: Upload your updates to GitHub as a backup.

:::{figure} /images/github/use-github-yourself.png
:alt: Alt here

Caption here
:::

### Use Git and GitHub collaboratively

In the open source world, GitHub is used to work collaboratively on software. GitHub is a shared platform where contributors can propose changes, review each other's work, and integrate updates through features like pull requests and issue tracking. 

In a collaborative setting, your workflow looks something like this:

1. **Fork a Repository**: Create your own copy of the project on GitHub.
2. **Clone Locally**: Download your fork to work on it.
3. **Make and Commit Changes**: Edit files and save your changes locally.
4. **Push to Your Fork**: Upload updates to your GitHub fork.
5. **Open a Pull Request**: Suggest changes to the main project.
6. **Collaborate and Merge**: Review and merge changes into the main project.

Note that the big change in workflow is that you are forking a main repository rather than working directly on that main repository. And you have a team of people who will review and decide if changes made through pull requests should be merged (or integrated into the existing code base).

:::{figure} /images/github/use-github-collaboratively.png
:alt: Alt here

Caption here
:::


## What's next

In this lesson series, you will learn how to work collaboratively using GitHub. The lessons will combine the technical elements that you need to use git and GitHub with the social dynamics that are not often taught. 

:::{todo}
resources
https://www.youtube.com/watch?v=eWxxfttcMts
:::


:::{toctree}
:caption: Collaborative GitHub
:maxdepth: 2
:hidden:

Intro <self>
What is Git/GitHub <what-is-git-github>
Your First Contribution <first-issue-contribution>
Fork a GitHub Repo <github-fork-repo>
Social <github-social-platform>

:::

