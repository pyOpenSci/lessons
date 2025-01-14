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

(get-to-know-repo)=
# Get to Know a (new to you) GitHub Repository

The first step in contributing to open source is finding and getting to know the GitHub repository where the code is stored. 

In this case, you will practice contributing to a sample pyOpenSci repository where you are set up to be successful and can practice without worrying about making mistakes. Making mistakes is often the best way to learn. 

You will [use this repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) as a place where you can practice for all of these lessons. 

:::{todo}

There are two options here. 

1. create a sample pyospackage repo with docs with many typos everywhere for people to fix. The downside is that it doesn't scale unless we have a reset repo action (which we could do) that essentially replaces the typos every few months. But this is likely the best option for actual practice on a (semi-real) code base

This approach could be fun as the pyos community here could submit lots of pt's that break things for people to fix :) 

2. Create a repo that people add a file to (like hometowns) with info about a town they like. This approach scales forever and ever and has worked well in the past. It's more focused on the fork, create something, pull request workflow without the open source flavor. It might be less interesting than a package where we could have bugs, typos, and other things for people to fix.
:::

## Get started

To begin, you should get to know the repository that you want to contribute to. To do this:

1. **Read the contributing guide**: In the repository, you should see a [**CONTRIBUTING.md** file](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/CONTRIBUTING.md) that tells you more about the types of contributions the project accepts and the workflows it embraces.


:::{figure} /images/github/use-github-yourself.png
:alt: Alt here

Add screenshot of the GitHub repo with the contributing file highlighted
:::

1. **Read through the documentation**: Most people's first contribution is to documentation. This is a great place to start because typos and other issues often make for great first pull requests. You can often make the changes fully in the GitHub interface online versus needing to clone the repository and work locally.

Also, let's face it--code can be scary for some as a first contribution. Don't sweat it if you aren't ready to contribute to the code; you will get here! 

1. Read through the open issues in the repository. Reading through open issues can be a great way to gauge what the project needs help with. 

**If you already have a fix in mind that you want to make:**

If you want to fix something you found, such as a typo in the documentation, you first want to see if there is an open issue you could work on directly. If an open issue about the topic doesn't exist, you should create a new GitHub issue that details the problem you found and wish to fix.

**If you are looking to contribute but you aren't sure where to start,** 

Sometimes, when reading through the project's existing issues, you will find something you might be interested in tackling. If that is the case, you can add a message to the open issue you are interested in, stating that you'd like to work on it. 

When scanning the issues, look for ones tagged "good first issue". Or "beginner friendly". Not all maintainers will tag issues but if you see such tags, you know you are in a repository that welcomes new contributions.
