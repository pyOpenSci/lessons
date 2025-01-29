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

As discussed in the [get to know a repo lesson](labels-responsive), the way issues are labeled and organized can both help you find issues that maintainers want help with and also tell you a lot about a project. If you see
beginner-friendly labels like **"good first issue"** or **"help wanted,"** it's a clear signal that the maintainers welcome new contributors. Further those might be good issues for you to start working on!  

:::{figure} /images/github/github-issues-good-first-issue.png  
:alt: "A screenshot of an open GitHub issue for the pyOpenSci pyosMeta project, showing labels like 'good first issue'. pyOpenSci curates beginner-friendly issues for sprints and first-time contributors."  

The image shows an open GitHub issue for the pyOpenSci pyosMeta project.
pyOpenSci runs beginner-friendly sprints and spends time curating issues for  
new contributors to work on during these events.
:::  

This lesson guides you through **finding or creating an issue** in a repository you don’t own.

## How to find an issue to work on

Generally, when you start contributing, there are two pathways: 1) you already have an issue in mind that you want to work on, or 2) you don't know what you want to work on yet; you'd like to see what the project needs first. Regardless of the pathway that you take, you'll want to remember two things:

1. You always want to search for existing issues before opening a new one
2. You want to link the work you do in a pull request back to the issue you worked on.

Both steps above make it easier for maintainers to keep their list of issues organized and to close issues as they are addressed.

> **<i class="fa-solid fa-magnifying-glass" style="color: #81c0aa;"></i> Social cue:**  
> Regardless of your pathway, you'll spend some time searching through issues. You want to demonstrate your willingness to put in effort before raising an issue.  
> Showing that you’ve already searched first is a great way to show goodwill to maintainers.  

Below, you'll learn how to navigate both pathways.

### 1. You already have identified an issue that you want to work on

Sometimes, while using a project or reading its documentation, you notice a bug, typo, or improvement. Before starting to work on it, check if the issue **already exists** in the repository.  

- **If the issue exists**, leave a comment to let others know you're interested in working on it.
  
Your comment might look like this:  

> Hey, maintainer team 👋. I’d like to work on this issue. Is there anything specific I should consider before getting started?

- **If it doesn’t exist**, you can [create a new one](create-issue) (*see below*).  

### Tips for effectively searching through GitHub issues

Before opening a **new** issue, check whether the problem has already been raised by searching through both **open** and **closed** issues. When searching, consider the following:

- **<i class="fa-solid fa-keyboard" style="color: #81c0aa;"></i> Use relevant keywords**: Search for terms related to the problem, including specific error messages, function names, or terms like documentation, typos, etc.  
- **<i class="fa-solid fa-file-circle-xmark" style="color: #81c0aa;"></i> Check closed issues**: Sometimes, an issue has already been discussed and resolved—or maintainers may have decided not to address it.  
  So be sure to scan both open and closed issues returned in a search.  
- **<i class="fa-solid fa-code" style="color: #81c0aa;"></i> Search using symbols or variable names**:  Searching for specific variable names or function signatures can help find related discussions if the issue is related to code.  

> **<i class="fa-solid fa-handshake-angle" style="color: #81c0aa;"></i> Social Cue:** Opening an issue (or commenting on an existing one) helps maintainers track who is working on what and prevents duplicate work. It also ensures the issue can be properly closed once your pull request is merged. A PR without an issue might catch maintainers off guard, so confirming before starting makes collaboration smoother.  

### 2. You're looking for an issue to work on

If you don’t have a specific issue in mind, explore the **open issues** list to find something that interests you. A great place to start is by looking for labels like **"good first issue"** or **"help wanted"**—these are beginner-friendly and often well-scoped.  

- **Start small**—fixing typos, improving documentation, or tackling minor bugs are great first contributions. The better scoped your issue is, the easier it will be for you to complete the work and get it merged.  
- **Leave a comment** on the issue to let maintainers know you'd like to help.  

> **<i class="fa-regular fa-clock" style="color: #81c0aa;"></i> Social cue:** Leaving comments in a new repository can feel intimidating, but most
maintainers appreciate respectful communication and enthusiasm. If a project
isn’t open to contributions, they will let you know—and there are plenty of
other projects to explore!

### How to know if an issue is available to work on

Even if you find an open issue that interests you, it’s important to check if someone is already working on it.  

- **<i class="fa-solid fa-comments" style="color: #81c0aa;"></i> Look for comments from other contributors**:  
  Check if someone has already offered to take on the issue.  
- **<i class="fa-solid fa-clock-rotate-left" style="color: #81c0aa;"></i> Check the timestamps**:  
  The issue may still be available if someone commented months ago but never submitted a fix.  
- **<i class="fa-solid fa-circle-question" style="color: #81c0aa;"></i> If in doubt, ask!**  
  Leaving a comment like *"Is this issue still open for contributions?"* can clarify things.  

> **<i class="fa-solid fa-hourglass-half" style="color: #81c0aa;"></i> Social cue:**  
> Just because someone expressed interest in an issue doesn’t always mean they are actively working on it.  
> If the last comment is old, the contributor may have moved on. Asking politely shows respect for their effort.  

(create-issue)=

## How to create a new issue

If an issue doesn’t already exist for the thing you'd like to work on, here’s how to create a new one:

1. Go to the Issues tab in GitHub
2. Click on the {bdg-success}`New issue` button.

:::{tip}  
Some projects use templates for reporting **bugs, documentation fixes, or new features**. If a template is available, fill it out—it helps maintainers quickly understand your issue.  
:::

3. Create a **clear title** summarizing what you’d like to fix.

:::{admonition} Examples of Good vs. Less Useful Issue Titles

| | ✅ Good Issue Titles                        | 🚫 Less Useful Titles  |
|-|-------------------------------------------------|---------------------------|
|| Add: update docstring in the `function_name_here()` function.| Update documentation. |
|| Fix: Typo in the documentation page for `doc-page-here`. | Fix formatting. |
|| Fix: Bug in `xxx` module that causes `x, y, z` to happen. | This feature is broken. |
|| Update the `module_name.py` module with a clearer docstring. | Bad UI, please fix. |
:::

4. Be **specific about what you'd like to fix**:

- Ideally, the issue that you want to address focuses on one thing and isn't too broad.
- Explain the problem or fix you’re proposing.  
- For **code bugs**: include steps to reproduce the issue; also describe what you expected would happen, and what actually happened when you ran the code.  
- For **documentation**: link to the page and describe what you’d like to update or enhance.
- For **new features**: describe what will happen once it is implemented

:::{figure} /images/github/open-issue.gif
:alt: alt text here

:::

:::{admonition} Why Detail Matters
:class: tip

Maintainers are often volunteers, so the more information you provide, the easier it is for them to support you. A well-crafted issue saves time and helps get faster responses.

>**<i class="fa-solid fa-magnifying-glass" style="color: #6ec9c3;"></i> Social Cue:** Before submitting the issue, ask yourself:
>
> - Could someone unfamiliar with the project understand this issue?
> - Did I provide enough detail for a maintainer to respond without extra questions?
:::

> **<i class="fa-solid fa-user-tag" style="color: #6ec9c3;"></i> Social Cue:** For smaller projects, tagging a maintainer can help get feedback faster. However, check contributor guidelines first to see if this is encouraged. Example:  
> `@maintainer-name, I'd love to help with this! Let me know if there's anything I should consider before starting.`

:::{todo}
Add section on issue templates, how they work, what they are
:::

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

- [Fork the repository](fork-repository) if you haven't already.
- [Make your changes on a new branch in your fork.](edit-commit-files)
- [Submit a pull request](pull-request) with your updates.
