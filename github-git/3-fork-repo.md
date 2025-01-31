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
  "title": "How to fork a GitHub repository and make a copy of it in your GitHub account: Intro to Collaborative GitHub"
  "description lang=en": "A complete guide to forking or making a copy of a GitHub repository that you don't own into your own account."
  "keywords": "GitHub, OpenSource, beginner-friendly"
  "property=og:locale": "en_US"
myst_html_meta:
    "title": "Learn how to fork a GitHub repo: Contribute to Open Source on GitHub for beginners"
    "description lang=en": "A fork is a copy of a GitHub repository that you make in your GitHub account. Learn how to fork any open repository on GitHub in just a few minutes."
    "keywords": "GitHub, OpenSource, beginner-friendly"
    "property=og:locale": "en_US"
    "og:image": /images/github/fork-repo.png
    "og:image:alt": An image that shows the steps for contributing to open source on GitHub.
---

(fork-repository)=
# A Guide to Forks on GitHub Forks


:::{admonition} What You Will Learn  
:class: tip  

In this lesson, you’ll learn how to **fork** (copy) a GitHub repository to your own account. Forking lets you work on a project independently before suggesting changes.  
:::

## What is forking and why use it?  

Forking a repository **creates a copy** in your GitHub account while keeping a link to the original.  

- <i class="fa-solid fa-pencil" style="color: #81c0aa;"></i> **Edit without concern**: Work on your fork without affecting the original project.  
- <i class="fa-solid fa-arrows-rotate" style="color: #81c0aa;"></i> **Stay up to date**: Sync your fork with the latest changes from the original repo.  
- <i class="fa-solid fa-paper-plane" style="color: #81c0aa;"></i> **Propose changes**: Suggest edits by submitting a **pull request** to the original repository.   

> **<i class="fa-solid fa-lightbulb" style="color: #81c0aa;"></i> Example**: You want to fix a typo in a project’s documentation. Instead of requesting permission, you fork the repo, make the fix, and submit a pull request with your update.

:::{figure} /images/github/fork-repo.png
:alt: ""

When you fork a GitHub repository, you make a copy of the files and the commit history into your personal account. This allows you to work on the files independently before suggesting changes through a pull request to make to the parent repository you forked from.
:::

By forking, everyone collaborates on their own copies of the project, ensuring the original files stay intact. All changes are tracked in the file history and can be undone if needed. You can fork a repository directly from its main page on GitHub.com.

## How to fork a GitHub repository

To fork a GitHub repository:

1. **Go to the repository page** you want to fork: [https://github.com/pyopensci/pyos-demo-package-contribute](https://github.com/pyopensci/pyos-demo-package-contribute)).  
2. **Click the** <kbd><i class="fa-solid fa-code-fork" style="color: #81c0aa;"></i> Fork</kbd> **button** in the top-right corner.  
3. **Choose your GitHub account** as the destination.  
4. **Wait for GitHub** to create your fork. You’ll now have a copy in your account!  

The URL of your fork will be:  

`https://github.com/your-username/pyos-demo-package-contribute`


:::{tip}
The number next to the <kbd><i class="fa-solid fa-code-fork"></i> button tells you how many times other users have forked the repository. 
:::


:::{figure} /images/github/fork-repo-animated.gif
:alt: GIF showing how to fork a repository on GitHub 

To fork a repo, navigate to it on GitHub and click the **Fork** button. Your copy will appear under your account.  
:::


:::{admonition} Who owns the repo? 

Every GitHub repository has an **owner**, which can be:  

- <i class="fa-solid fa-user" style="color: #81c0aa;"></i> **An individual** (e.g., `https://github.com/username/repository-name`).  
- <i class="fa-solid fa-building" style="color: #81c0aa;"></i> **An organization** (e.g., `https://github.com/org-name/repository-name`).  

The **owner’s username appears first in the URL**, showing who controls the repository.  

**Example**:  
 - A personal repo: `https://github.com/your-gh-username/my-project`  
 - An organization-owned repo: `https://github.com/pyOpenSci/repo-name`  

If you **fork a repo**, your GitHub username becomes the owner of the fork:  

> **Forked URL:** `https://github.com/your-username/repository-name`

:::


## What happens after you fork a repo?  

Your fork **is a separate copy**, but it remains linked to the original repository.  

- **Your fork is stored at:** `https://github.com/your-username/repository-name`  
- **The original repo stays at:** `https://github.com/original-owner/repository-name`  

> **<i class="fa-solid fa-lightbulb" style="color: #81c0aa;"></i>  You can now:**  
> - Make changes without affecting the original repository.  
> - Keep your fork updated as the original repo evolves.  
> - Submit changes back using a **pull request**.  
 
::::{todo}
 /images/github/fork-structure.png  
:alt: "Diagram showing how forking creates a personal copy linked to the original."  
Graphic: A simple diagram showing "Original Repo → Fork → Your Account".  
::::


## Keep your fork in sync  

Your fork doesn't automatically get updated when the **original repository is updated**. Periodically, you will need to **sync your fork** to keep it current.  

To sync a GitHub fork:
1. **Go to your fork** on GitHub.  
2. **Click the** <i class="fa-solid fa-arrows-rotate" style="color: #81c0aa;"></i> **Sync fork** **button** (available on GitHub’s UI).  
3. Your fork's main branch will now match the latest version of the original repository. This means that it has the most recent commits that have been made to the parent repository.  

:::{todo} 
/images/github/sync-fork.png  
:alt: "GitHub interface showing how to sync a fork with the original repo."  
Graphi:  Screenshot of GitHub’s "Sync Fork" button  
:::

---

## Takeaways  

✅ **Forking creates a personal copy of a repository** that you can edit freely.  
✅ **Your fork stays linked** to the original repo, allowing you to propose changes.  
✅ **Sync your fork regularly** to keep it up to date if you plan to contribute to the repo more over time.  

:::{admonition} Next steps  
:class: important  

Now that you’ve forked a repository, the next step is to **edit a file and commit your changes**.  
[Learn how to edit and commit files →](edit-commit-files)  
:::
