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

# How to Fork & Clone a GitHub Repository 

🚧 These lessons are under heavy construction and will continue to change through March 2024 🚧 

:::{admonition} What you will learn:

* Explain how a **GitHub** repository stores and tracks changes to files.
* Create a copy of (<kbd>fork</kbd>) other users' files on **GitHub.com**.
* Use the `git clone` command to download a copy of a **GitHub** repository to your computer. 
::: 


## Who owns a GitHub repository?

When a repository is stored on **GitHub.com**, it is assigned a unique URL (i.e. link on the **GitHub.com** website) that can be used to find the repository and access its files. While repositories on **GitHub.com** can be made either public or private, the default is public for free **GitHub** accounts.

In either case (public or private), the URL links to a **GitHub** repository always follows the same format: 

`https://github.com/username/repository-name`

The username is the username owner of the repo owner. The username can either be an individual such as `lwasser` (your **GitHub** username), or it can represent an organization such as `pyOpenSci`.

For example, the repository that you will work within this lesson is owned by `pyopensci.` Therefore, the URL looks like this:

`https://github.com/pyopensci/repo-name`

(fork-repo)=
## Fork a GitHub repository

Using **GitHub.com**, you can create a copy of another user's or organization’s repository—a process called `forking`. When you fork a repository, you get your own version to work on. And you can do that wrok without affecting the original files in the parent repository. Others can also fork your repositories, creating their own copies.

Forking is useful because the fork remains linked to the original repository. This allows you to:
- Update your fork with changes from the original repository.
- Suggest changes to the original repository, which the owner can review and accept.

By forking, everyone collaborates on their own copies of the project, ensuring the original files stay intact. All changes are tracked in the file history and can be undone if needed. You can fork a repository directly from its main page on **GitHub.com**.

To fork a repo:

1. Navigate to the repo page that you wish to fork - example:

`https://github.com/pyopensci/repo-name`

2. On that page, you will see a button in the UPPER RIGHT hand corner that says `Fork`. The number next to that button tells you how many times the repo has already been forked. 
3. Click on the `Fork` button and select your user account when it asks you where you want to fork the repo. 
4. Once you have forked the repo, you will have a copy in your account. Navigate to your repo page. The URL should look something like this:

`https://github.com/your-user-name/repo-name`

:::{figure} /images/github/image-coming-soon.png
:alt: alt text here

To fork a repo, first, navigate to the repo you want to fork. Then click the **fork** button in the upper right-hand corner of your screen. You can then create a copy of this repo in your account.
:::


(clone-repo)=
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


:::{figure} /images/github/image-coming-soon.png
:alt: alt text here

 You can make a local copy of your forked repository on your computer with the git clone command. 
:::


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
<!-- #endregion -->
<!-- #region -->


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
<!-- #endregion -->
