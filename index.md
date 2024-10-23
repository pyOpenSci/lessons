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
* [Write Pseudocode](write-pseudocode)

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
:::{card} [✿ Share Code ✿](publish-share-code/intro)
:class-card: left-aligned

* [Share code on GitHub](share-your-code)
* [Get DOI with Zenodo](cite-your-code)

:::
::::

:::::

## Who are these lessons for

These lessons help scientists understand best practices and tools used in the Python ecosystem. We will be adding new lessons over the next year.

:::{toctree}
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
:caption: Share Code
:maxdepth: 2

Share Code <publish-share-code/intro>
:::
