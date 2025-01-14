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

🚧 These lessons are under heavy construction and will continue to change through March 2025 🚧 

:::{todo}

what's missing
* Create a new branch to work on in your fork -- don't make a pr from your main or master branch
* Closes or addresses #issue number
:::


:::{admonition} What you will learn

After completing this tutorial, you will be able to:

* List the steps involved in contributing to an open source project

You can use the [pyOpenSci example GitHub repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) to practice making contributions for all of these lessons. 
:::

Contributing to open source software can feel intimidating.  

* You may not know the project maintainers.  
* You might feel unsure about your Git and GitHub skills (imposter syndrome is real!).  
* You may not know where to begin.  

This lesson series will teach you how to collaborate using GitHub, helping you confidently contribute to open source repositories and collaborate with colleagues. 

## GitHub workflow summary

The GitHub contribution workflow looks something like this:

* First, you need to identify a repository that you want to contribute to. Here, you can use the [pyOpenSci learning repository](https://github.com/pyOpenSci/pyos-demo-package-contribute) to test your skills! 
* Once you have found a repo that you want to contribute to, you need to [get to know it](get-to-know-repo). Getting to know a repo starts with reading the [contributing guide](contributing).
* Next, you will [identify an issue or bug that you want to work on](identify-issue). This will involve either reading through open issues and finding good first ones to work on. Or maybe you know the repository and already have a fix in mind that you want to implement. In this case, you will [create a new issue](create-issue) in the repo. 
* Once you have created an issue or identified what you wish to work on, you need to [`Fork` or create a copy of the repo](fork-repository) in your GitHub account.


:::{tip}
If you have already forked the repository but some time has passed. You should consider updating or syncing your fork. GitHub has a sync button that you can use to do this (`pyopensci/repo-name`). This will ensure that all of the files in your repository are current and will prevent merge conflicts.
:::

:::{todo}
The section below needs work and to be fleshed out. PR page doesn't exist yet. 
:::

* Create a new branch to work on
* Make the changes to the file you proposed to change in your issue to the file in the new branch you created. If the changes are to documentation, be sure to spell check!
* Commit the changes to your fork.   
* Open a <kbd>Pull Request</kbd> to the parent repository`. In the text of the pull request, you should include a link to the URL of the issue you opened (essentially linking the changes you are submitting to the problem you are solving). This closes the documentation loop! 
* Finally, wait for the developers to review/comment on your PR. Be patient; this step can take time as people are busy and often donate their time to this effort!

## Your first step: Get to know the repo 

Your first step in making a contribution to a repository that you don't own is [getting to know the repo. You will do that next.](get-to-know-repo)
