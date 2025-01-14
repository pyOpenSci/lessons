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
* List the ways you can get to know a repository better before contributing
* Create a fork of a repository that you want to contribute to
* Make a small contribution to a sample repository through a GitHub pull request.

:::

Whether this is your first time contributing to open source, or your 10th, making contributions can be anxiety-inducing.

* You might not know the people maintaining the project
* You might feel uncertain about your technical git and GitHub skills (imposter syndrome is real!)
* You might not be sure where to start.

This lesson will teach you how to use GitHub collaboratively so you can start contributing to open source (and working collaboratively on code) . The upcoming lessons will walk you through the technical elements associated with contributing to open source and the social elements that will make your contribution workflow more positive, and, in some cases, it will even ensure your issue or pull request is completed more efficiently.


## GitHub Workflow Summary

The full contribution workflow using only GitHub looks something like this:

* [Get to know the repo that you want to contribute to](get-to-know-repo)
* [Identify an issue or bug that you wish to work on](identify-issue)
* `Fork` the repository you'd like to contribute to. 
* OPTIONAL: If you have already forked the repository, but some time has passed. You should consider updating or syncing your fork. GitHub has a sync button that you can use to do this (`pyopensci/repo-name`). This will ensure that all of the files in your repository are current and will prevent merge conflicts.
* Create a new branch to work on
* Make the changes to the file you proposed to change in your issue to the file in the new branch you created. If the changes are to documentation, be sure to spell check!
* Commit the changes to your fork.   
* Open a <kbd>Pull Request</kbd> to the parent repository, which for this lesson is:  `pyopensci/repo-name`. In the text of the pull request, you should include a link to the URL of the issue you opened (essentially linking the changes you are submitting to the problem you are solving). This closes the documentation loop! 
* Finally, wait for the developers to review/comment on your PR. Be patient; this step can take time as people are busy and often donate their time to this effort!



## Activity: Fork a repository and modify a file

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
