---
layout: single
title: "Make Your First Open Source Contribution"
excerpt: ""
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

# Make Your First Open Source Contribution 

🚧 These lessons are under heavy construction and will continue to change through March 2024 🚧 

:::{todo}

what's missing
* Create a new branch to work on in your fork -- don't make a pr from your main or master branch
* Closes or addresses #issue number
:::


:::{admonition} What you will learn

After completing this tutorial, you will be able to:

* List the steps involved in contributing to an open source project
* List the ways you can get to know a repository better before contributing
* Create a fork of a repository that you want to contribute to
* Make a small contribution to a sample repository through a GitHub pull request.

:::

Whether this is your first time contributing to open source, or your 10th, making contributions can be anxiety-inducing.

* You might not know the people maintaining the project
* You might feel uncertain about your technical git and GitHub skills (imposter syndrome is real!)
* You might not be sure where to start.

This lesson will teach you how to start contributing to open source. The upcoming lessons will walk you through the technical elements associated with contributing to open source and the social elements that will make your contribution workflow more positive, easier and in some cases it will even ensure your issue or pull request is completed more efficiently.  

## 1. Get to know the GitHub repository. 

The first step in contributing to open source is finding and getting to know the GitHub repository where the code is stored. 

In this case, you will practice contributing to a sample pyOpenSci repository where you are set up to be successful and can practice without worrying about making mistakes. Making mistakes is often the best way to learn. 

:::{todo}

There are two options here. 

1. create a sample pyospackage repo with docs with many typos everywhere for people to fix. The downside is that it doesn't scale unless we have a reset repo action (which we could do) that essentially replaces the typos every few months. But this is likely the best option for actual practice on a (semi-real) code base

This approach could be fun as the pyos community here could submit lots of pt's that break things for people to fix :) 

2. Create a repo that people add a file to (like hometowns) with info about a town they like. This approach scales forever and ever and has worked well in the past. It's more focused on the fork, create something, pull request workflow without the open source flavor. It might be less interesting than a package where we could have bugs, typos and other things for people to fix. 
:::

To begin, you should get to know the repository that you wish to contribute to. To do this:

1. **Read the contributing guide**: In the repository, you should see a **CONTRIBUTING.md** file that tells you more about the types of contributions the project accepts and the workflows it embraces.

1. **Read through the documentation**: Most people's first contribution is to documentation. This is a great place to start because typos and other issues often make for great first pull requests. You can often make the changes fully in the GitHub interface online versus needing to clone the repository and work locally.

Also, let's face it--code can be scary for some as a first contribution. Don't sweat it if you aren't ready to contribute to the code; you will get here! 

1. Read through the open issues in the repository. Reading through open issues can be a great way to gauge what the project needs help with. 

**If you already have a fix in mind that you want to make:**

If you want to fix something you found, such as a typo in the documentation, you first want to see if there is an open issue you could work on directly. If an open issue about the topic doesn't exist, you should create a new GitHub issue that details the problem you found and wish to fix.

**If you are looking to contribute but you aren't sure where to start,** 

Sometimes, when reading through the project's existing issues, you will find something you might be interested in tackling. If that is the case, you can add a message to the open issue you are interested in, stating that you'd like to work on it. 

When scanning the issues, look for ones tagged "good first issue". Or "beginner friendly". Not all maintainers will tag issues but if you see such tags, you know you are in a repository that welcomes new contributions. 


## 2. Open or comment on a GitHub issue

Once you've decided what you'd like to work on, you can do one of two things

1. If an issue is already open for the item you want to work on, you can leave a comment indicating your interest in working on it. That comment might look something like this:

> Hey maintainer team 👋. I'm interested in working on this issue. Is there anything specific that I should consider before getting started?

Leaving a comment in a new-to-you repository might feel scary, but don't worry. If you communicate in a respectful way, then it's likely that you will also get a nice response in return. Also, if you don't get a supportive response, there are other projects you could work on that may be a better fit. Not all projects are open to new contributions. And that is OK, too. 

### How to create a new issue

If the issue isn't already open, you can create a new issue describing what you'd like to work on. What is most important when creating a new issue is:

1. Ensure the issue has a **carefully crafted title** that describes what you want to fix. Some packages have issue templates that you can fill out. Other projects may not have templates set up.
2. Be **specific about what you'd like to fix** in the issue. If it's a bug that you are fixing in the code, provide a **fully reproducible code example** of how to trigger the bug so the maintainers can easily understand the problem. If it is a documentation fix, link to the documentation page with the error and be specific about what you'd like to fix, add, or enhance. 

:::{todo}
Link to the stravalib issue I recently worked on where the reproducible example was missing.
:::

The content of your issue is more important than you might think. Maintainers are often volunteers, working on projects in their free time. The more information you can provide them, the easier it is for them to understand your goal and how to support you. Be as specific as you can be in your issue! This might mean that it takes you some time to create the issue. The time invested upfront will pay off the issue moving forward.

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


## Activity 2: Fork a repository and modify a file

### 1. Fork the pyOpenSci practice GitHub repository

Fork the <a href="http://www.github.com/pyopensci/repo-here" target="_blank">pyOpenSci demo repository on GitHub</a>. Remember that a fork is a copy of a repository that is owned by someone else or an organization that lives in your GitHub account.

:::{todo}
Create an animated gif showing how to fork a repo
:::


:::{tip}
A repository fork is a copy of the GitHub repository that you own in your GitHub account. The repository, however, is still connected to the main repository on GitHub that you forked. This connection means that you can submit pull requests and changes to the repository using your fork. 
:::

Once you have submitted your issue with the proposed changes, one of the package developers will review the issue and either:

* Suggest changes to your proposed edits or
* Encourage you to submit a pull request with the two identified changes.

When you have the go-ahead from someone who owns the repository, you are ready to create and submit a pull request with your changes.

### 2. Make the changes that you said you would make in the issue opened above 

After you have forked the repo and received the OK to move forward with your pull request:

* Open the file that you want to make changes to in your fork.
* Make the edits that you want to make to the file
* Commit the changes that you made to the file. Important: try to use a short descriptive commit message that describes what you have changed:
*
> fix: fixed numerous typos in the filename.py file
> fix: updated the code to align with PEP 8 syntax
> fix: fixed typo in docstring text 


:::{todo}
It might be cool to show first contributions like my first on to nbconvert could be interesting? Other people might have examples too
::: 

### 3. Create a GitHub pull request (PR)

More here.... 

## GitHub Workflow Summary

The full contribution workflow using only GitHub (without cloning or copying the repository to your local computer) looks something like this:

* `Fork` the repository you'd like to contribute to. 
* OPTIONAL: If you have already forked the repository, but some time has passed. You should consider updating or syncing your fork. GitHub has a sync button that you can use to do this (`pyopensci/repo-name`). This will ensure that all of the files in your repository are current and will prevent merge conflicts.
* Create a new branch to work on
* Make the changes to the file you proposed to change in your issue to the file in the new branch you created. If the changes are to documentation, be sure to spell check!
* Commit the changes to your fork.   
* Open a <kbd>Pull Request</kbd> to the parent repository, which for this lesson is:  `pyopensci/repo-name`. In the text of the pull request, you should include a link to the URL of the issue you opened (essentially linking the changes you are submitting to the problem you are solving). This closes the documentation loop! 
* Finally, wait for the developers to review/comment on your PR. Be patient; this step can take time as people are busy and often donate their time to this effort!
