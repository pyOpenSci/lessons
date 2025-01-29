# pyOpenSci Lessons

```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/python-package-guide?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/python-package-guide?style=social)](https://github.com/pyopensci/contributing-guide)
[![DOI](https://zenodo.org/badge/556814582.svg)](https://zenodo.org/badge/latestdoi/556814582)
[![View Contributors](images/contributing/contributors-badge.svg)](https://github.com/pyOpenSci/lessons#contributors-)
[![Binder](https://binder.opensci.2i2c.cloud/badge_logo.svg)](https://binder.opensci.2i2c.cloud/v2/gh/pyopensci/lessons/HEAD)
```

:::::{grid} 2

::::{grid-item}
:::{card} ✿ Clean Code ✿
:class-card: left-aligned

* [Intro to clean code](intro-clean-code)
* [Write "Pythonic", Expressive Code](python-expressive-code)
* [Lint, Format, & Style your Code](clean-modular-code/python-pep-8)
* [Don't Repeat Yourself (DRY) Principles](clean-modular-code/python-dry-modular-code)
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
:::{card} [✿ Running Code ✿](running-code/intro)
:class-card: left-aligned

* [Execute a Python Package](running-code/execute-package)
* [Execute a Python Script](running-code/execute-script)

:::
::::

::::{grid-item}
:::{card} [✿ Share Code ✿](publish-share-code/intro)
:class-card: left-aligned

* [Share code on GitHub](share-your-code)
* [Get DOI with Zenodo](cite-your-code)

:::
::::

::::{grid-item}
:::{card} [✿ Collaborative GitHub ✿](github-git/your-first-contribution)
:class-card: left-aligned

Learn how to make your first contribution to an open source code hosted on GitHub.
Here you'll learn how to 

* [Understand contributing guidelines](first-contribution)
* How to identify and request to tackle a specific issue
* How to [fork a repo](fork-repository) and edit a file in the GitHub interface.

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
:caption: Clean Code
:maxdepth: 2

Clean Code <clean-modular-code/intro-clean-code>
:::

:::{toctree}
:hidden:
:caption: Optimize Code
:maxdepth: 2

Optimize Code <code-workflow-logic/intro>
:::

:::{toctree}
:hidden:
:caption: Running Code
:maxdepth: 2

Package Code <running-code/intro>
:::


:::{toctree}
:hidden:
:caption: Share Code
:maxdepth: 2

Share Code <publish-share-code/intro>
:::

:::{toctree}
:hidden:
:caption: GitHub
:maxdepth: 2

Collaborative GitHub <github-git/intro>
:::

:::{todolist}

:::
