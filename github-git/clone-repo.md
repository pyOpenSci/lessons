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
  "title": "How to Clone a GitHub Repository to Work Locally: Collaborative GitHub for beginners"
  "description lang=en": "Learn how to clone or make a copy of a GitHub repository online on your computer so you can work locally."
  "keywords": "GitHub, OpenSource"
  "property=og:locale": "en_US"
---

(clone-repository)=
# Clone a GitHub Repository to Work Locally 
How to clone a repo. 

## Clone a repo: copy files From GitHub.com to your computer

To work locally with a **GitHub** repository (including forked repos), you must create a local copy of that repository on your computer (a task referred to as `cloning` a repo). You can clone **GitHub** repositories that you own or that are owned by others (e.g., repositories that you have forked to your **GitHub** account).

In either case, cloning allows you to create a local copy of a **GitHub** repository to work with the files locally on your computer. Cloning a repository to your computer is a great way to work on your files locally while still having a copy of your files on the cloud on **GitHub.com**. Following the steps below, you will use the `git clone` command in the **terminal** to clone **GitHub** repositories. 


### Use `Bash` to Change to Your Desired Working Directory

The first step to using any **git** command is changing the current working directory to your desired one.
In the case of `git clone`, the current working directory needs to be where you want to download a local copy of a **GitHub** repository. 

For this lesson, you will clone a repo locally on your computer (or wherever you work).   


### Copy a Github.com Repository URL From GitHub.com

To run the `git clone` command, you need the URL for the repository you want to clone (i.e., either a repository owned by you or a fork you created from another user's repository). 

On the main **GitHub.com** page of the repository, you can click on the green button for `Clone or download`, and copy the URL provided in the box, which will look like this: 

`https://github.com/your-username/repo-name`

::::{todo}
:::{figure} /images/github/image-coming-soon.png
:alt: alt text here

 You can make a local copy of your forked repository on your computer with the git clone command. 
:::
::::

:::{tip} 
You can copy the URL directly from your web browser, or in some cases, you might already know the URL. However, in many cases, you will come across a new **GitHub.com** repository on your own and will need to follow these instructions to copy the URL for future use. 
:::

### Run the `git clone` in the shell

Now that you have the URL for a repository that you want to copy locally, you can use the **terminal** to run the `git clone` command followed by the URL that you copied: 

```bash
git clone https://github.com/your-username/repo-name
```

You have now made a local copy of a repository. You can double-check that the directory exists using the `ls` command in the **terminal**. 

```bash
$ ls     
    repo-name
```


:::{admonition} <i class="fa fa-pencil-square-o" aria-hidden="true"></i> Challenge  - Fork and Clone a Repository

Go to GitHub.com and login. Then use the link below to open the **repo-name** repo.

`https://github.com/pyopensci/repo-name`

* On the main **GitHub.com** page of this repository, you will see a button on the top right that says `Fork`. The number next to `Fork` tells the number of times that the repository has been copied or forked.
* Click on the `Fork` button and select your **GitHub.com** account as the home of the forked repository. 
* Once you have forked a repository, you will have a copy (or a fork) of that repository in your **GitHub** account. The URL to your fork will contain your username:

`https://github.com/your-username/repo-name`

* Finally, clone the fork that you created above so you have a copy of all the files on github.com on your local computer. 

To make sure you did things right, in bash, cd to the repo-name directory on your computer. 
Type:

`$ git remote -v` 

The paths returned should look something like this:

`https://github.com/your-username/repo-name`


:::
