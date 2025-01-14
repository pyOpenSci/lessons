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

Your first step is to identify an issue that you wish to work on

## 2. Open or comment on a GitHub issue

Once you've decided what you'd like to work on, you can do one of two things

1. If an issue is already open for the item you want to work on, you can leave a comment indicating your interest in working on it. That comment might look something like this:

> Hey maintainer team 👋. I'm interested in working on this issue. Is there anything specific that I should consider before getting started?

Leaving a comment in a new-to-you repository might feel scary, but don't worry. If you communicate in a respectful way, then it's likely that you will also get a nice response in return. Also, if you don't get a supportive response, there are other projects you could work on that may be a better fit. Not all projects are open to new contributions. And that is OK, too. 

(create-issue)=
### How to create a new issue

If the issue isn't already open, you can create a new issue describing what you'd like to work on. What is most important when creating a new issue is:

1. Ensure the issue has a **carefully crafted title** that describes what you want to fix. Some packages have issue templates that you can fill out. Other projects may not have templates set up.
2. Be **specific about what you'd like to fix** in the issue. If it's a bug that you are fixing in the code, provide a **fully reproducible code example** of how to trigger the bug so the maintainers can easily understand the problem. If it is a documentation fix, link to the documentation page with the error and specify what you'd like to fix, add, or enhance. 

:::{todo}
Link to the stravalib issue I recently worked on where the reproducible example was missing.
:::

The content of your issue is more important than you might think. Maintainers are often volunteers, working on projects in their free time. The more information you can provide them, the easier it is for them to understand your goal and how to support you. Be as specific as you can be in your issue! This might mean that it takes you some time to create the issue. The time invested upfront will pay off the issue moving forward.


:::{admonition} Tips for Submitting Issues

- **Search First**: Before creating a new issue, check if someone else has already reported it.
- **Be Clear**: Provide a detailed, reproducible example when reporting bugs.
- **Be Constructive**: Avoid blaming or harsh criticism. Instead, frame your concerns as suggestions.

Example:  
_Not Constructive_: "This feature is broken and useless."  
_Constructive_: "I encountered an issue when using this feature. Here's the error and steps to reproduce it."
:::

3. **Be patient**: Once you have opened your issue, be patient, as maintainers could take some time to respond. The timeline will vary based on how active the repository issue is, how many open issues there are, the size of the maintainer team, and even what's going on in the maintainer's life at that particular time.

**It could take a few weeks for someone to get back to you.**

4. If the maintainers invite you to submit a pull request addressing the issue you left or commented on, you're good to go. At that point, it's time to:

* Fork the repository if you haven't already
* Make the changes that need to be made in your fork.
* Open up a pull request to address those changes. 

:::{tip} 
Make your GitHub issue title specific enough that people can tell what the issue is about without reading all the details. This makes it easier to identify potentially overlapping issues quickly. 
A few good issue titles are below:

* Add: update docstring in the `function_name_here()` function.
* Update the module_name.py module with a more clear module docstring
* Fix: Typo in the documentation page for doc-page-here
* Fix: Bug in xxx module that causes x, y, z to happen

Bad / less descriptive issue title examples are below:
* Update documentation.
* Fix formatting
:::

If maintainers don't respond after a few weeks, a gentle nudge is ok. That might look something like this:

> Hey, maintainer team 👋. I'm just following up to see if you have any feedback on my issue here to fix ___add brief description here__. Please let me know if you would like me to move forward with a pull request or if you have any feedback or concerns about the issue!
>

:::{todo}
It may make sense to have the activities in a separate file. And to refer to the pages they should review before starting each activity.

The alternative is to put the activities at the top given people often skim
:::

## Activity 1: Create an issue for a bug that you'd like to fix 

1. go to the https://www.github.com/pyopensci/repo-name repository on GitHub
2. Explore the documentation and code. You will find many items that could be fixed, including spelling errors, typos, and more.
3. Pick something you would like to fix and open an issue specifying what you'd like to implement.
4. Wait for someone on the pyOpenSci team to respond to you with next steps! 

Once you have submitted an issue and a developer from the package you are submitting to (in this case, the pyOpenSci team) agrees to your proposed changes, you are ready to implement these changes locally on your computer and submit a pull request. 

:::{note}
For this activity, focus on the process of contributing and making a small change to a single file; you don't need to make a huge change or fix everything in a file. Most first contributions are small updates to documentation. Start there and build confidence. You can always submit more issues and pull requests later!  
:::
