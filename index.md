# pyOpenSci Lessons

```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/lessons?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/lessons?style=social)](https://github.com/pyopensci/lessons)
[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)
[![View Contributors](images/contributing/contributors-badge.svg)](https://github.com/pyOpenSci/lessons#contributors-)
[![badge](https://img.shields.io/badge/Launch-2i2c%20Binder-E66581.svg?logo=data:image/png;base64,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)](https://binder.opensci.2i2c.cloud/v2/gh/pyopensci/lessons/HEAD)
```

:::::{grid} 2

::::{grid-item}
:::{card} ✿ Contribute to Open Source ✿]
:class-card: left-aligned

Learn how to navigate the technical and [social elements](social-github) of making a contribution to open source code on GitHub.

* [Your First Contribution](pyos-first-contribution)
* [Get to know a new repo](new-repo)
* [Find an issue to work on](identify-github-issue)
* [Fork a repo](fork-repository)
* [Edit & commit files](pyos-edit-commit-files)
* [Submit a pull request](pyos-pull-request)

:::
::::

::::{grid-item}
:::{card} ✿ Clean Code ✿
:class-card: left-aligned

* [Intro to clean code](intro-clean-code)
* [Write "Pythonic", Expressive Code](python-expressive-code)
* [Lint, Format, & Style your Code](write-better-code/clean-modular-code/python-pep-8)
* [Don't Repeat Yourself (DRY) Principles](write-better-code/clean-modular-code/python-dry-modular-code)
* [Write Pseudocode](intro-write-pseudocode)

:::
::::

::::{grid-item}
:::{card} ✿ Code Checks ✿
:class-card: left-aligned

* [About Functions](about-functions)
* [Write Python Functions](write-functions)
* [Add checks to functions](functions-checks)
* [Multi parameter functions](multi-parameter-functions)
* [Write Conditionals to redirect code](conditionals)
* [Common Python exceptions](common-exceptions)

<!--
TODO: let's merge this with the conditional lesson
* [Conditionals with alternatives](conditionals-alternatives)
-->
:::
::::

::::{grid-item}
:::{card} ✿ Package & Share Your Code ✿
:class-card: left-aligned

* [Share code on GitHub](share-your-code)
* [Get DOI with Zenodo](cite-your-code)
* [Execute a Python Package](run-package)
* [Execute a Python Script](run-execute-script)

:::
::::

:::::

## Who are these lessons for

These lessons help scientists understand best practices and tools used in the Python ecosystem. We will be adding new lessons over the next year.

In these lessons, we'll be covering topics that encourage efficient, maintainable, and reproducible code. We start out
by introducing the concepts of "clean code" and "Pythonic code". Then, we move into how you can achieve clean, Pythonic
code using best practices and tools.

:::{toctree}
:hidden:
:caption: Write Better Code
:maxdepth: 2

Write Better Code <write-better-code/index>
:::

:::{toctree}
:hidden:
:caption: Package & Share Code
:maxdepth: 2

Package & Share Code <package-share-code/index>
:::

:::{toctree}
:hidden:
:caption: GitHub
:maxdepth: 2

Contribute Open Source <contribute-open-source/index>
:::
