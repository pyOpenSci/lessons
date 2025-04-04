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
  "title": "Intro"
  "description lang=en": "More"
  "keywords": "GitHub, OpenSource"
  "property=og:locale": "en_US"
---

# Introduction to GitHub and Open Source Collaboration

[GitHub is one of many **social coding platforms**](what-is-git-github) that allows individuals and teams to manage, track, and collaborate on software projects. Social coding platforms play a key role in **open source development**, enabling contributors worldwide to work on, improve, and maintain code and documentation together.

> This guide covers:
> <i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> [The social aspects of contributing to an open source project](social-github)
>
> <i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> [How to get started contributing to open source](pyos-first-contribution)
>
> <i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> The technical aspects of contributing including:
>
> * [How to get to know a new repo](new-repo)
> * [How to find an issue to work on](identify-github-issue)
> * [How to fork a repo](fork-repository)
> * [How to edit & commit files](pyos-edit-commit-files)
> * [How to submit a pull request](pyos-pull-request)
>
> <i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> [What GitHub is](what-is-git-github) and how it supports **open source communities**

## Social coding platforms and open source

**Open source software (OSS)** is code that is publicly accessible—anyone can view, modify, and distribute it. GitHub provides the tools needed for open source projects to store code publically, manage contributions, track and address issues, and collaborate efficiently.

Specifically, in the Python language, the software is often [associated with Python packages](https://www.pyopensci.org/python-package-guide/tutorials/intro.html), where you bundle up code and make it easier for a user to install on their computer. Reusable software allows developers and scientists to share common workflows rather than needing to recreate the code needed for each workflow from scratch.

### Why open source communities use GitHub

* **<i class="fa-solid fa-globe" style="color: #81c0aa;"></i> Global collaboration**: Developers from around the world can contribute.
* **<i class="fa-solid fa-code-branch" style="color: #81c0aa;"></i> Version control**: Track every change made to the project.
* **<i class="fa-solid fa-comments" style="color: #81c0aa;"></i> Transparent discussions**: Use issues and pull requests to propose and review changes.
* **<i class="fa-solid fa-shield-halved" style="color: #81c0aa;"></i> Permission control**: Maintainers decide what contributions get merged.

> **<i class="fa-solid fa-handshake-angle" style="color: #81c0aa;"></i> Social cue:**
> Contributing to open source is [more than just writing code](social-github). GitHub allows you to collaborate, discuss ideas, and learn from others.

## Why contribute to open source?

Contributing to open source is a way to **build skills, expand your network, and give back** to projects you care about.

* **Improve your skills**: Gain hands-on experience with real-world projects.
* **Grow your network**: Connect with developers, maintainers, and potential collaborators.
* **Showcase your work**: Contributions become part of your **public portfolio**.
* **Support tools you use**: Many contributors improve projects they rely on for work or hobbies.
* **Learn from others**: See how experienced developers write and manage code.

> **<i class="fa-solid fa-handshake" style="color: #81c0aa;"></i> Social cue:**
> Open source is collaborative—every contribution, big or small, helps the community.

:::{admonition} Open source and academia
:class: note

Academia heavily values publications for career advancement, yet open source contributions are often not recognized and valued in traditional academic credit systems despite being essential to scientific progress. pyOpenSci is an organization committed to helping scientists get support and recognition for their important work in developing and supporting open source through [peer review](https://www.pyopensci.org/about-peer-review/index.html) and its vibrant and supportive [community of practice](https://www.pyopensci.org/our-community/index.html).
:::

## Using GitHub for personal projects

Many people start using GitHub as a **personal version control tool**.
This means tracking changes to your own work **without** collaborating with others.

### Solo workflow

1. **<i class="fa-solid fa-download" style="color: #81c0aa;"></i> Clone a repository**: Copy the project to your local computer.
2. **<i class="fa-solid fa-edit" style="color: #81c0aa;"></i> Work locally**: Edit files and make changes.
3. **<i class="fa-solid fa-save" style="color: #81c0aa;"></i> Commit changes**: Save changes with a description of what was modified.
4. **<i class="fa-solid fa-upload" style="color: #81c0aa;"></i> Push changes**: Upload updates to GitHub as a backup.

:::{figure} /images/github/use-github-yourself.png
:alt: "Visual representation of using GitHub for personal projects."
:::

> **<i class="fa-solid fa-user" style="color: #81c0aa;"></i> Social cue:**
> GitHub is **useful even when working alone**. It creates a backup of your work and
> allows you to track changes over time—helpful for research, coding, or writing.

## Using GitHub collaboratively

GitHub is widely used in **open source** and **team-based projects** where multiple people work on the same codebase.

### Collaborative workflow

1. **<i class="fa-solid fa-code-fork" style="color: #81c0aa;"></i> Fork a repository**: Create your own copy of the project on GitHub.
2. **<i class="fa-solid fa-download" style="color: #81c0aa;"></i> Clone locally**: Download your fork to work on it.
3. **<i class="fa-solid fa-edit" style="color: #81c0aa;"></i> Make and commit changes**: Edit files and save your changes.
4. **<i class="fa-solid fa-upload" style="color: #81c0aa;"></i> Push to your fork**: Upload updates to your GitHub copy.
5. **<i class="fa-solid fa-paper-plane" style="color: #81c0aa;"></i> Open a pull request**: Suggest changes to the main project.
6. **<i class="fa-solid fa-people-arrows" style="color: #81c0aa;"></i> Collaborate and merge**: Review and integrate updates.

> **Key difference:** Instead of pushing changes directly to the project, you first **fork it** and work within your own copy before submitting a **pull request** to propose changes.

:::{figure} /images/github/use-github-collaboratively.png
:alt: "Diagram of how GitHub enables collaborative work through forking and pull requests."
:::

> **<i class="fa-solid fa-users" style="color: #81c0aa;"></i> Social cue:**
> Working on GitHub is more than writing code—it’s about **communication, teamwork, and reviewing each other's work**.

## Summary

| | **Feature**         | **Solo Use**                     | **Collaborative Use**                 |
|-|---------------------|--------------------------------|--------------------------------------|
| | **Main goal**      | Personal version control      | Team-based development              |
| | **Repository type** | Single personal repo         | Forked repositories linked together |
| | **Workflow steps**    | Clone, edit, commit, push    | Fork, branch, pull request, merge   |
| | **Review process** | Self-review changes          | Maintainers review contributions    |

:::{admonition} What's next?
:class: seealso

Now that you understand GitHub's role in **open source** and **collaboration**,
you're ready to dive into **contributing to a project!**

*****

* <i class="fa-brands fa-github-alt"></i> [Get started with activities to guide you through your first contribution →](pyos-first-contribution)
* <i class="fa-brands fa-github-alt"></i> [Learn how to identify an issue →](identify-github-issue)
* <i class="fa-brands fa-github-alt"></i> [Learn how to fork a repository →](fork-repository)
:::

*********

*This work was supported by the Better Scientific Software Fellowship Program, a collaborative effort of the U.S. Department of Energy (DOE), Office of Advanced Scientific Research via ANL under Contract DE-AC02-06CH11357 and the National Nuclear Security Administration Advanced Simulation and Computing Program via LLNL under Contract DE-AC52-07NA27344; and by the National Science Foundation (NSF) via SHI under Grant No. 2327079.*

:::{todo}
resources
<https://www.youtube.com/watch?v=eWxxfttcMts>
:::

:::{toctree}
:maxdepth: 2
:hidden:

About These Lessons  <self>
Social Etiquette in Open Source  <social-open-source>
:::

:::{toctree}
:caption: Contribute to Another Repo
:maxdepth: 2
:hidden:

0. Your contributing path <your-first-contribution>
1. Get to know the repo <get-to-know-repo>
2. Find an issue <identify-issue>
3. Fork GitHub Repo <fork-repo>
4. Edit & commit files <edit-commit-files>
5. Submit Pull Request <pull-request>
:::

:::{toctree}
:caption: Work locally
:hidden:

Clone a GitHub Repo <clone-repo>
:::

:::{toctree}
:caption: Background
:maxdepth: 2
:hidden:

What is Git/GitHub <what-is-git-github>
Use GitHub codespaces <github-codespaces>
Ways to contribute <ways-to-contribute>
:::
