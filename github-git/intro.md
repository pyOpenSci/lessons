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

# Use GitHub With Friends  

:::{todo}
This might belong in the background section.
:::

🚧 These lessons are under heavy construction and will continue to change through March 2025 🚧 

GitHub is a social coding platform.
GitHub can be used in two primary ways: **independently** or **collaboratively**. 

## Use GitHub by yourself

Most scientists start using GitHub (and git) on their own. In this scenario, Git is a personal version control system, enabling you to track changes and maintain a complete work history. Working on your own is ideal for personal projects, preliminary research, or prototyping, as it allows you to revert to earlier versions if needed. 

If you are using GitHub on your own, your workflow probably looks something like this:

1. **Clone a Repository**: Copy the project to your local computer.
2. **Work Locally**: Edit files and make changes on your machine.
3. **Commit Changes**: Save your changes to the project history.
4. **Push Changes**: Upload your updates to GitHub as a backup.

:::{figure} /images/github/use-github-yourself.png
:alt: Alt here

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

:::


## What's next

In this lesson series, you will learn how to work collaboratively using GitHub. The lessons will combine the technical elements you need to use git and GitHub with the social dynamics that are not often taught. 

:::{todo}
resources
https://www.youtube.com/watch?v=eWxxfttcMts
:::


:::{toctree}
:caption: Contribute to Another Repo
:maxdepth: 2
:hidden:

0. Your contributing path <0-first-contribution>
1. Get to know the repo <1-get-to-know-repo>
2. Find an issue <2-identify-issue>
3. Fork GitHub Repo <3-fork-repo>
4. Edit & commit files <4-edit-commit-files>
5. Submit Pull Request <5-pull-request>

::: 

:::{toctree}
:caption: Work locally
:hidden:

Clone a GitHub Repo <6-clone-repo>
:::


:::{toctree}
:caption: Background  
:maxdepth: 2
:hidden:

Use GitHub With Friends (vs. by yourself)  <self>
What is Git/GitHub <what-is-git-github>
GitHub Social platform <github-social-platform>
Use GitHub codespaces <github-codespaces>
:::
