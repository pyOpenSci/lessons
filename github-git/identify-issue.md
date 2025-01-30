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
    "title": "Identify an issue in an open source project: Contribute to Open Source on GitHub for beginners"
    "description lang=en": "When contributing to open source software, one of the first steps is identifying an issue to work on. Learn about the ways you can identify both what the project needs help with and what you'd like to work on."
    "keywords": "GitHub, OpenSource, beginner-friendly"
    "property=og:locale": "en_US"
    "og:image": /images/github/steps-to-contribute.png
    "og:image:alt": An image that shows the steps for contributing to open source on GitHub.
---

(identify-github-issue)=

# Identify an Issue to Work On: Collaborative GitHub for Open Source  

Contributing to an open source project starts with identifying an issue to work on. Open issues help developers track bugs, new features, or needed improvements in a repository. Whether you have a specific fix in mind or are looking for ideas, exploring existing issues is the best place to start.  

As discussed in the [get to know a repo lesson](labels-responsive), the way issues are labeled and organized can both help you find issues that maintianers want help with and also tell you a lot about a project. If you see 
beginner-friendly labels like **"good first issue"** or **"help wanted,"** it's a clear signal that the maintainers welcome new contributors. Further those might be good issues for you to start working on!  

:::{figure} /images/github/github-issues-good-first-issue.png  
:alt: "A screenshot of an open GitHub issue for the pyOpenSci pyosMeta project, showing labels like 'good first issue'. pyOpenSci curates beginner-friendly issues for sprints and first-time contributors."  

The image shows an open GitHub issue for the pyOpenSci pyosMeta project.
pyOpenSci runs beginner-friendly sprints and spends time curating issues for  
new contributors to work on during these events.
:::  

This lesson guides you through **finding or creating an issue** in a repository you don’t own. 


## Start by scanning existing project issues 

When contributing to a new open source project, the best place to start is by **scanning open issues**. This helps you find tasks maintainers need help with and ensures you don’t duplicate existing work.  


### 1. You already have identified an issue 

Sometimes, while using a project or reading its documentation, you notice a bug, typo, or improvement. Before starting to work on it, check if the issue **already exists** in the repository.  

- **If the issue exists**, leave a comment to let others know you're interested in working on it.  


Your comment might look like this:  

> Hey maintainer team 👋. I’d like to work on this issue. Is there anything specific I should consider before getting started?  

If the issue you identified doesn't exist yet, you can create a new one. You will learn how to do that below. 

> **<i class="fa-solid fa-handshake-angle" style="color: #81c0aa;"></i> Social Cue:** Opening an issue (or commenting on an existing one) helps maintainers track who is working on what and prevents duplicate work. It also ensures the issue can be properly closed once your pull request is merged. A PR without an issue might catch maintainers off guard, so confirming before starting makes collaboration smoother.  


### 2. You're looking for an issue to work on 

If you don’t have a specific issue in mind, explore the **open issues** list to find something that interests you. A great place to start is by looking for labels like **"good first issue"** or **"help wanted"**—these are beginner-friendly and often well-scoped.  

- **Start small**—fixing typos, improving documentation, or tackling minor bugs are great first contributions.  
- **Leave a comment** on the issue to let maintainers know you'd like to help.  

:::{tip}  
Leaving comments in a new repository can feel intimidating, but most 
maintainers appreciate respectful communication and enthusiasm. If a project 
isn’t open to contributions, they will let you know—and there are plenty of 
other projects to explore!  
:::  

(create-issue)=

## How to create a new issue

If an issue doesn’t already exist for the thing you'd like to work on, here’s how to create a new one:

1. Go to the Issues tab in GitHub
2. Click on the {bdg-success}`New issue` button.

:::{tip}  
Some projects use templates for reporting **bugs, documentation fixes, or new features**. If a template is available, fill it out—it helps maintainers quickly understand your issue.  
::: 

4. Create a **clear title** summarizing what you’d like to fix.  
5. Be **specific about what you'd like to fix**:  
   - Explain the problem or fix you’re proposing.  
   - For **bugs**, include steps to reproduce the issue.  
   - For **documentation**, link to the page and describe what you’d like to update or enhance. 

:::{figure} /images/github/open-issue.gif
:alt: alt text here

:::

:::{admonition} Why Detail Matters
:class: tip

Maintainers are often volunteers, so the more information you provide, the easier it is for them to support you. A well-crafted issue saves time and helps get faster responses.

**<i class="fa-solid fa-magnifying-glass" style="color: #6ec9c3;"></i> Social Cue:** Before submitting the issue, ask yourself:
 * Could someone unfamiliar with the project understand this issue?
 * Did I provide enough detail for a maintainer to respond without extra questions?
:::

## Examples of Good vs. Less Useful Issue Titles

| ✅ Good Issue Titles                        | 🚫 Less Useful Titles  |
|-------------------------------------------------|---------------------------|
| Add: update docstring in the `function_name_here()` function.| Update documentation. |
| Fix: Typo in the documentation page for `doc-page-here`. | Fix formatting. |
| Fix: Bug in `xxx` module that causes `x, y, z` to happen. | This feature is broken. |
| Update the `module_name.py` module with a clearer docstring. | Bad UI, please fix. |


> **<i class="fa-solid fa-user-tag" style="color: #6ec9c3;"></i> Social Cue:** For smaller projects, tagging a maintainer can help get feedback faster. However, check contributor guidelines first to see if this is encouraged. Example:  
> `@maintainer-name, I'd love to help with this! Let me know if there's anything I should consider before starting.`  


### After you've opened an issue

Once you've submitted your issue, give maintainers time to respond.  

**<i class="fa-solid fa-hourglass-start"></i> Be Patient:** Maintainers balance many tasks, and response times vary based on project activity, team size, and personal schedules.  

If you don’t hear back after a few weeks, a polite nudge is fine:  

> Hi team 👋, just following up on my issue. Let me know if you’d like me to move forward with a pull request or if there’s anything I should address first.  

:::{tip}
Focus on making small, meaningful contributions. Most first contributions are small updates to documentation—these are great for building confidence as they often can be merged more quickly.
:::

## What happens next

If the maintainers invite you to submit a pull request, it's time to:

* [Fork the repository](fork-repository) if you haven't already.
* [Make your changes on a new branch in your fork.](edit-commit-files)
* [Submit a pull request](pull-request) with your updates.

