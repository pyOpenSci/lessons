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

(first-contribution)=
# Make Your First Open Source Contribution 

:::{admonition} What you will learn

After completing this tutorial, you will have the skills needed to contribute to an open source GitHub 
repository. You will use the [pyOpenSci example GitHub repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) to practice making contributions. 
:::

Contributing to open source in a public space like GitHub can feel intimidating. You may not know the project maintainers, feel unsure about your GitHub skills, or wonder where to begin.

This lesson series will teach you how to collaborate on code and documentation using GitHub. It will help you confidently contribute to a GitHub repository and build skills to collaborate with colleagues (some of whom you may not have met in real life!). 

## GitHub workflow summary


:::{figure} /images/github/steps-to-contribute.png
:alt: alt text here

The steps for making your first contribution to an open source repo. In this lesson, you will do all of your work on GitHub.com, meaning you don't need to clone or make a copy of your repository locally. This is a great way to get started with contributing. It minimizes the command line skills that you will need to use git. 
:::

## Documentation counts! 

It's common for your first contribution
to be to documentation! Documentation contributions can be incredibly valuable as developers often don't have time to work on documentation and code!

Fixing typos and other small documentation issues makes for great, easy-to-create (and review) first pull requests. In fact, if you find that the contributing information isn't detailed enough, that could also be your first contribution!

When you edit documentation, you can often make the changes in the GitHub interface online versus needing to clone the repository and work locally.


:::{admonition} A real-life first contribution to PyPI

[Here is an example issue that resulted in 2 small pull requests to PyPI (warehouse)](https://github.com/pypi/warehouse/issues/17374). In this case, the images were outdated, so it was a bug in the documentation that needed to be fixed. However, while getting to know the repository, the author also found issues with the development documentation, so they submitted a pull request to address that as well. Both pull requests were small. 
:::


:::{todo}
Your GitHub contribution workflow will be something like this:

1. First, you will identify a repository you want to contribute to. Here, you can use the [pyOpenSci learning repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) to test your skills. 
    * You will [get to know that repository](get-to-know-repo) which starts with reading the [contributing guide](contributing). This guide should provide some instructions on how to make your first contribution.
1. You will [identify an issue or bug that you want to work on](identify-issue). This will involve either reading through open issues and finding good first ones to work on. If you already have a fix in mind that doesn't exist in the existing issue list, you will [create a new issue](create-issue) in the repo. 
1. Once you have created an issue or identified what you wish to work on, you will [`Fork` or create a copy of the repo](fork-repository) in your GitHub account.
1. In your fork, you will edit the file(s) addressed in your issue. In this lesson series, you will do [all of the work in the GitHub interface](4-edit-commit-files), which means that you don't have to [clone (or copy)](6-clone-repo) the repo locally to your computer. 
1. Once your edits are complete, you will commit the changes and open a <kbd>Pull Request</kbd> to the parent repository.  
     * Finally, wait for the developers to review/comment on your PR. Be patient; this step can take time as people are busy and often donate their time to this effort!
:::

## Time to get started!

Your first step in contributing to a repository you don't own is [getting to know the repo. You will do that next.](get-to-know-repo)
