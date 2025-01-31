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

(identify-issue)=
# Identify an issue to work on 

Open issues are where developers track bugs, new features, or other improvements needed in the repo. Whether you have a specific fix in mind or are looking for ideas, you should start by exploring existing open issues.

In this lesson you will create or comment on an issue that you'd like to fix in a GitHub repository that you don't own. 

:::{admonition} Activity: Create (or find) an issue for a bug that you'd like to fix 

1. Navigate to the [pyOpenSci example repo](https://github.com/pyOpenSci/pyos-demo-package-contribute). 
2. Explore the documentation and code. You will find many items that need to be fixed, including spelling errors, typos, and more.
3. Pick a file that you'd like to work on. Open a new issue specifying what you'd like to fix.
4. Wait for someone on the pyOpenSci team to respond to you with next steps. 

Once you have submitted an issue and someone has responded positively, you can begin working on the changes in your fork. [You will learn how to fork a repo, next.](fork-repo)
:::

As you scan the issues, look for beginner-friendly labels. Beginner-friendly labels are a clear message that the project welcomes new contributors. Many projects label issues as **good first issue** or **beginner-friendly** to highlight tasks that are approachable for new contributors.

## Open or comment on an issue
  
If you **have an idea already of what you'd like to work on**, check if an issue exists for it. If it does, comment on the issue to indicate your interest. If not, create a new issue and wait for feedback.

Your comment might look like this:

> Hey maintainer team 👋. I'm interested in working on this issue. Is there anything specific that I should consider before getting started?

If you’re **looking for something to work on,** browse the issues to find one that interests you and comment on it to let maintainers know that you'd like to help. 

:::{tip}
Leaving comments in a new repository can feel intimidating, but most maintainers appreciate respectful communication and enthusiasm. If a project isn’t open to contributions, that’s okay—there are plenty of welcoming projects to explore!
:::

(create-issue)=
### How to create a new issue

:::{tip}
Some projects use individual templates for bugs, documentation fixes, and new feature requests. Other projects might have no templates.
:::

If an issue doesn’t already exist for the thing you'd like to work on, here’s how to create a new one: 

1. Click on the new issues button. If there is a template that you can select for the issue, use one.

1. Write a **clear title** summarizing what you’d like to fix. Some repositories use templates—fill them out if available.
1. Be **specific about what you'd like to fix**:
   * Explain the problem or fix you’re proposing.
   * For bugs, include steps to reproduce the issue.
   * For documentation, link to the page and describe what you’d like to update or enhance.



:::{figure} /images/github/open-issue.gif
:alt: alt text here

:::

:::{admonition} Why Detail Matters
:class: tip

Maintainers are often volunteers, so the more information you provide, the easier it is for them to support you. Investing time in crafting a clear issue upfront pays off later.
:::

**Be patient**: Once you have opened your issue, be patient. Maintainers might take time to respond. Their timeline depends on factors like how active the repo is, the size of the maintainer team, and their personal schedules. Responses can take days or weeks.

If you don’t hear back after a few weeks, a polite nudge is fine:

> Hi team 👋, just following up on my issue. Let me know if you’d like me to move forward with a pull request or if there’s anything I should address first.


## Tips for submitting good issues

* Search First: Before creating a new issue, check if someone else has already reported it.
* Be Clear: Provide a detailed, reproducible example when reporting bugs or proposing fixes. Make your GitHub issue title specific enough that people can tell what the issue is about without reading all the details. This helps maintainers and contributors quickly identify overlapping issues.

Examples of Good Issue Titles

* Add: update docstring in the function_name_here() function.
* Update the module_name.py module with a clearer module docstring.
* Fix: Typo in the documentation page for doc-page-here.
* Fix: Bug in xxx module that causes x, y, z to happen.

Examples of less useful issue titles:
* Update documentation.
* Fix formatting.

Be Constructive: Avoid blaming or harsh criticism. Instead, frame concerns as suggestions.
    
Less Constructive: “This feature is broken and useless.”

Constructive: “I encountered an issue when using this feature. Here’s the error and steps to reproduce it.”

## What happens next

If the maintainers invite you to submit a pull request, it's time to:

* [Fork the repository](fork-repo) if you haven't already.
* [Make your changes on a new branch in your fork.](4-edit-commit-files)
* [Submit a pull request](5-pull-request) with your updates. 

A gentle nudge is ok if maintainers don't respond after a few weeks. That might look something like this:

> Hey, maintainer team 👋. I'm just following up to see if you have any feedback on my issue here to fix ___add brief description here__. Please let me know if you want me to move forward with a pull request or if you have any feedback or concerns about the issue!



:::{tip}
Focus on making small, meaningful contributions. Most first contributions are small updates to documentation—these are great for building confidence as they often can be merged more quickly.
:::
