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
  "title": "Get to know a (new to you) GitHub repository: Contribute to Open Source code and documentation."
  "description lang=en": "It's useful to get to know a GitHub repo by reading the README and CONTRIBUTING files before getting started. Learn what to look for when getting to know a new repository. A beginner-friendly guide."
  "keywords": "GitHub, OpenSource, beginner-friendly"
  "property=og:locale": "en_US"
---

# Get to Know a (new to you) GitHub Repository

:::{admonition} What you will learn:
:class: tip

In this tutorial, you will get to know a GitHub repo that you want to contribute to. You will learn how to find the CONTRIBUTING.md file in our [example GitHub repo](https://github.com/pyOpenSci/pyos-demo-package-contribute) and identify the process for submitting a contribution to the repo.
:::

## How to get to know a GitHub repo  

Before contributing, it's important to **familiarize yourself with the repository** to ensure your contribution aligns with the project's needs. Doing this **saves time** for both you and the maintainers, making the process smoother.  

### 1. Check the README and CONTRIBUTING guide  

The **README** provides an overview of the project, its purpose, and how it is used. Often, it also links to the project's contributing and development guides.  
- **Review the README file**: The [**README.md** file](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/README.md) will help you understand the project's goals.  
- **Read the CONTRIBUTING guide**: The [**CONTRIBUTING.md** file](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/CONTRIBUTING.md) explains what types of contributions are accepted and the expected workflow.  

**<i class="fa-solid fa-handshake-angle" style="color: #81c0aa;"></i> Social cue:** If these files clearly **welcome contributions** and outline next steps, it’s a good sign that the maintainers are open to contributions.

:::{figure} /images/github/github-contributing-file.png
:alt: "Screenshot of the GitHub repository ‘pyos-demo-package-contribute’ showing files and folders, including README.md, CONTRIBUTING.md, and LICENSE. The sidebar highlights metadata, such as the repository description, links, and license details. The README.md and CONTRIBUTING.md files are highlighted."

Above is a screenshot of the pyOpenSci practice repo that you will use. Notice the CONTRIBUTING.md file. You should read this file after checking out the README file.
:::

(labels-responsive)=
### 2. Look at project activity and maintainer responsiveness  

- Scan the **issues and pull requests** sections on GitHub to see how long it generally takes for maintainers to respond.  
- Check the **date of the latest commit** to determine whether the project is actively maintained.  
- Look for **"good first issue"** or **"help wanted"** labels in the issues. These labels suggest that the maintainer team welcomes contributions and might be more beginner-friendly.  

> **<i class="fa-regular fa-clock" style="color: #81c0aa;"></i> Social cue:** If maintainers **regularly respond** and merge contributions, your work is more likely to be reviewed and accepted in a timely manner as well.

### 3. Understand the project’s infrastructure  

Some repositories have specific **code and text format and workflow requirements**. Make sure to check if the project uses:  
- **Code formatters and linters**: Does the project use [code formatters or linters](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html#python-package-code-style-format-and-linters)?  
- **Continuous Integration (CI)**: Are there automated tests and checks that run when a new PR is submitted?  
- **Licensing**: The [project’s license](https://www.pyopensci.org/python-package-guide/documentation/repository-files/license-files.html) dictates how you can use, modify, and distribute the code.  
  - The **MIT and BSD-3 licenses** permit broad use with attribution; these licenses are common in the scientific open source ecosystem.  
  - A **GPL license** requires derivative works to follow the same open source terms.  This is what's known as a [copy-left license](https://www.pyopensci.org/python-package-guide/documentation/repository-files/license-files.html#use-open-permissive-licenses-when-possible). 

> **<i class="fa-solid fa-circle-check" style="color: #81c0aa;"></i> Social cue:** If the project follows **consistent coding standards and has CI in place**, it likely has an **organized review process**, that is setup to accept contributions. Further, if the project uses tools such as the [pre-commit ci bot](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html#pre-commit-ci), code formatting and linting might be possible on GitHub within the pull request it self using CI. This means you won't need to setup a development environment to "clean up" any changes that you make in a PR.  

### 4. Check for a Code of Conduct  

A **Code of Conduct** helps ensure a **welcoming and respectful** community.  
- If one exists, read it to understand community expectations.  
- If missing, check discussions in issues and pull requests to gauge how maintainers interact with contributors.  

> **<i class="fa-solid fa-scale-balanced" style="color: #81c0aa;"></i> Social cue:** A clear code of conduct signals an **inclusive and structured** community. If discussions show **helpful, constructive feedback**, it's a good sign of a positive project culture.

### 5. See if contributors are acknowledged  

- Do maintainers **thank contributors** in merged PRs or reference them in the README?  
- Is there a **CONTRIBUTORS file** or an **all-contributors bot** recognizing contributions?  

> **<i class="fa-solid fa-users" style="color: #81c0aa;"></i> Social cue:** If past contributors are **acknowledged and appreciated**, it suggests a community that values participation.

---

The above steps will help you determine whether a project is **welcoming, responsive, and well-maintained**, making it a great place to contribute! 🚀


## Next steps
Once you have explored and gotten to know the repository and decided that it's a good project to contribute to, it's time to [find an issue to work](identify-issue). You will learn more about that next.  
