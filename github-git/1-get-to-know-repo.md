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

:::{admonition} What you will learn:
:class: tip

In this tutorial, you will get to know a GitHub repo that you want to contribute to. You will learn how to find the CONTRIBUTING.md file in our [example GitHub repo](https://github.com/pyOpenSci/pyos-demo-package-contribute) and identify the process for submitting a contribution to the repo.
:::

The activity that you will complete is below. Read on, however, to learn more about the steps.

:::{admonition} Activity 1: Get to know the repository

In your browser, navigate to [https://github.com/pyOpenSci/pyos-demo-package-contribute/](https://github.com/pyOpenSci/pyos-demo-package-contribute/).

* Check out the README and CONTRIBUTING files.

### Answer these questions

* Does the repository accept contributions? If so, what types of contributions are accepted?
* Does the repository use specific code or text formatting standards or liters?
* Does the repository have continuous integration (CI) set up?
* What is the license associated with the code in the repository?
* Are the issues labeled and are there "good first issue" or "help wanted" labels 
:::

(contributing)=
## How to get to know a repo

Familiarize yourself with the repository you want to contribute to:

* **Check out the README file**: The [**README.md** file](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/README.md) provides an overview of the project, its purpose, and how it is used. Often, it also links to the project's contributing and development guides, if they exist.
* **Read the contributing guide**: The [**CONTRIBUTING.md** file](https://github.com/pyOpenSci/pyos-demo-package-contribute/blob/main/CONTRIBUTING.md) explains what types of contributions the project accepts and the workflows contributors should follow.
* **Evaluate the documentation**: Consider whether the documentation (README, CONTRIBUTING, or others) is comprehensive and up to date. If it's not, this could be a great starting point for your first contribution!

:::{figure} /images/github/github-contributing-file.png
:alt: "Screenshot of the GitHub repository ‘pyos-demo-package-contribute’ showing files and folders, including README.md, CONTRIBUTING.md, and LICENSE. The sidebar highlights metadata, such as the repository description, links, and license details. The README.md and CONTRIBUTING.md files are highlighted."

Above is a screenshot of the pyOpenSci practice repo that you will use. Notice the CONTRIBUTING.md file. You should read this file after checking out the README file.
:::

### Get to know the project's infrastructure

* **Code formatters and linters**: Does the project use any [code formatters or linters](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html#python-package-code-style-format-and-linters) in its workflows? This information is often found in the development or contributing guide.
* **Continuous Integration (CI)**: Does the project have [Continuous Integration](https://www.pyopensci.org/python-package-guide/continuous-integration/ci.html#what-is-continuous-integration) set up to run tests when a new pull request or change is submitted?
* **License**: Check the [project’s license](https://www.pyopensci.org/python-package-guide/documentation/repository-files/license-files.html) to understand the terms for using, modifying, and contributing to the code. For example:
  - An MIT license permits broad use, modification, and distribution with attribution.
  - A GPL license requires that derivative works are open-sourced under the same terms.
  Understanding the project's license helps you understand your rights and responsibilities as a contributor.

### Project organization 

* Look for labels like **"good first issue"** or **"help wanted"** on the repository’s issues page. These highlight tasks ideal for beginners. If you don’t see these labels, ask maintainers for guidance on where to start.
* Check if the repository includes a **Code of Conduct** or community guidelines. These outline expectations for respectful collaboration. If absent, observe discussions in issues or pull requests or ask maintainers for clarification.

### Social cues and repository activity

You might also want to evaluate the activity and health of the community. This can signal whether the project is actively maintained.

* What is the date of the most recent commit to the repository?
* Are there a lot of open issues and pull requests?
* How long does it take for maintainers to respond to open issues or pull requests?
* Does the repository have many forks and stars? While not a definitive metric, these can indicate community interest and engagement.

If the project has recent commits, a responsive maintainer team, and clear documentation, it is likely a good candidate for contributions. Conversely, many unresolved issues or stale pull requests might indicate less active maintenance.
