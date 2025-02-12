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

# An overview of Git & GitHub

Version control is essential in open source software development and increasingly important in sharing and working on open science workflows. GitHub is the most commonly used cloud-based version control platform. GitHub integrates the power of Git with online collaboration and project management tools.

Many think about GitHub as a social coding platform.

GitHub enables:
- **Version control with Git**: Track changes, save work at various stages and revert to earlier versions if needed.
- **Cloud-based backup**: Keep your local work securely backed up online.
- **Collaboration tools**: Share code, streamline contributions, and improve projects collectively.
- **Project management**: Organize updates, assign tasks, and manage milestones.
- **Review processes**: Facilitate clear and collaborative reviews of changes.

## GitHub in open science  

Related to open science, GitHub:
- **Promote transparency**: Share results and methods through accessible code and history.
- **Enables collaboration**: Supports people worldwide working together on the same code and documentation in a structured way.  
- **Ensures reproducibility**: Help others contribute to and build upon your work. 

By combining Git’s version control with GitHub’s collaborative features, you can manage code efficiently while supporting openness,  transparency, and truly open collaboration. 

(what-is-git)=
## What is git?

Git is a powerful **version control system** that enables teams to track, manage, and collaborate on code and documentation changes over time. While it is best known for its use in software development, Git is equally valuable in **open science** and **open source workflows**. 

## Features that make Git version control powerful 

- **Track Changes**  
  Git keeps a detailed history of all changes made to your files. This is critical for open science and open source, as it provides a transparent record of how data, code, or documents have evolved over time.

::::{todo}
:::{figure}  /images/github/image-coming-soon.png
:alt: Alt here

The graphic here shows the commit history: commit 1, commit 2, commit 3, and review merge into main. 
:::
::::

- **Branching and Merging**  
  Branches allow users to work independently on new features, experiments, or ideas without affecting the main project. This is particularly useful in research for testing hypotheses or in software development for building new features. Once work is complete, branches can be merged back into the main project.

::::{todo}
:::{figure}  /images/github/image-coming-soon.png
:alt: Alt here

Graphic here showing commit branching   
:::
::::

- **Distributed Version Control**  
  Git enables every collaborator to own a full copy of the project and its history. This decentralization supports the open workflows of both open science and open source by allowing everyone to work offline and maintain redundancy.

::::{todo}
:::{figure}  /images/github/image-coming-soon.png
:alt: Alt here

Graphic here showing a main repo and then numerous forks    
:::
::::
- **Collaboration Across Teams**  
  Git makes it easy for multiple contributors to work on the same project. It provides tools to integrate changes, resolve conflicts, and ensure everyone's contributions are recognized—a key aspect of inclusive open workflows.

## Why Use Git in Open Science and Open Source?
- **Reproducibility**: Git ensures a detailed history of every change, allowing others to reproduce your results or track how your code evolved.
- **Transparency**: Git commit history also provides a clear, open record of changes to a project over time. This supports sharing not only the final product but also the path taken to get to that final product (i.e., the process).  
- **Collaboration at Scale**: Git supports collaboration between people worldwide.
- **Sustainability**: Git prevents accidental loss of work. If someone inadvertently adds new changes to a code base, they can always be undone using git's history.


## What is GitHub?

GitHub is a cloud-based platform built on Git, specifically designed to make Git workflows easier, more accessible, and more collaborative. It is widely used in both **open source software development** and **open science projects** to facilitate teamwork, transparency, and dissemination.

### GitHub features
- **Online Git Repositories**  
  GitHub allows you to save your git repositories online. This makes the latest versions and the history of changes to your code and documentation easily accessible to collaborators worldwide.

- **Collaboration Tools**  
  Features like pull requests, issues, and discussions make it easy for contributors to share ideas, propose changes, and review each other’s work. This fosters collaboration and builds community, which are essential elements of open software and workflows.

- **Project Visibility**  
  GitHub supports **public repositories** for sharing projects with the world, which is critical in open science and open source for disseminating knowledge and enabling broad contributions. **Private repositories** offer controlled access to private research or sensitive data.

- **Integration and Automation**  
  GitHub integrates with testing, deployment, and reproducibility tools, such as continuous integration pipelines, containerized environments, and documentation platforms. This is crucial in open science to automate reproducibility checks and in open source to ensure code quality.

### Why Use GitHub?

GitHub is a powerful platform for sharing projects with a global audience, making collaboration and reuse simple and accessible. It provides tools to manage contributions, engage with users, and build a thriving community around your work. For open science, GitHub ensures reproducibility by preserving transparent records of code, data, and analysis steps. Its pull request workflow streamlines the process of proposing and reviewing changes, enabling teams from diverse backgrounds to collaborate efficiently and effectively.
