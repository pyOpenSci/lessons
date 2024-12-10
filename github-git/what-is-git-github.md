---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
---


# An overview of Git & GitHub

🚧 These lessons are under heavy construction and will continue to change through March 2024 🚧 

## What is git?

Git is a powerful **version control system** that enables teams to track, manage, and collaborate on code and documentation changes over time. While it is best known for its use in software development, Git is equally valuable in **open science** and **open source workflows**. 

## Features that make Git version control powerful 

- **Track Changes**  
  Git keeps a detailed history of all changes made to your files. This is critical for open science and open source, as it provides a transparent record of how data, code, or documents have evolved over time.


:::{figure}  /images/github/image-coming-soon.png
:alt: Alt here

The graphic here shows the commit history: commit 1, commit 2, commit 3, and review merge into main. 
:::

- **Branching and Merging**  
  Branches allow users to work independently on new features, experiments, or ideas without affecting the main project. This is particularly useful in research for testing hypotheses or in software development for building new features. Once work is complete, branches can be merged back into the main project.


:::{figure}  /images/github/image-coming-soon.png
:alt: Alt here

Graphic here showing commit branching   
:::

- **Distributed Version Control**  
  Git enables every collaborator to own a full copy of the project and its history. This decentralization supports the open workflows of both open science and open source by allowing everyone to work offline and maintain redundancy.


:::{figure}  /images/github/image-coming-soon.png
:alt: Alt here

Graphic here showing a main repo and then numerous forks    
:::

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

