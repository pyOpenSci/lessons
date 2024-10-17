# <img src="https://www.pyopensci.org/images/logo.png" width=100 /> pyOpenSci Lessons

[![All Contributors](https://img.shields.io/github/all-contributors/pyOpenSci/lessons?color=ee8449)](#contributors-)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/lessons?color=purple&display_name=tag&style=plastic)

[![DOI](https://zenodo.org/badge/855935338.svg)](https://doi.org/10.5281/zenodo.13910245)

[![CircleCI](https://circleci.com/gh/pyOpenSci/lessons.svg?style=svg)](https://circleci.com/gh/pyOpenSci/lessons)

## What is pyOpenSci?

pyOpenSci is devoted to building diverse, supportive community around
the Python open source tools that drive open science. We do this through:

* open peer review
* mentorship
* training

pyOpenSci is an independent organization, fiscally sponsored by Community
Initiatives.

## About this repo

This repo contains a set of lessons being developed for pyOpenSci training
events. as of early October 2024 it is a new repo being rapidly developed.

Please expect the contents to change at any time!
With that said all contributions are always welcome!

## Contributing statement

## How to setup

This repository contains the source files for the [pyOpenSci Tutorials](https://pyopensci.org/lessons).

## Code formatting in Jupyter

If yo are working on the notebooks, you may want to apply ruff for code formatting. Instructions on how to set this up in Jupyter Lab are below:  

<https://gist.github.com/jbwhit/eecdd1cac2756df85ad165f437445b0b>

## Build the guidebook locally

Our guidebook is built with [Sphinx](https://sphinx-doc.org) which is a documentation tool and uses the pyos-sphinx-theme which customizes the pydata-sphinx-theme.

The easiest way to build our documentation is to use [the `nox` automation tool](https://nox.thea.codes/),
a tool for quickly building environments and running
commands within them.

Using `nox` ensures that your environment has all the dependencies needed to build the documentation.

To build, follow these steps:

1. Install `nox`

   ```console
   python -m pip install nox
   ```

2. Build the documentation:

   ```console
   nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
nox -s docs-live
```

## Contributing to pyOpenSci lessons

We welcome and issues and pull requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/lessons/issues/new/choose).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://www.leahwasser.com"><img src="https://avatars.githubusercontent.com/u/7649194?v=4?s=100" width="100px;" alt="Leah Wasser"/><br /><sub><b>Leah Wasser</b></sub></a><br /><a href="https://github.com/pyOpenSci/lessons/commits?author=lwasser" title="Code">💻</a> <a href="#tutorial-lwasser" title="Tutorials">✅</a> <a href="https://github.com/pyOpenSci/lessons/commits?author=lwasser" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://blog.ucodery.com"><img src="https://avatars.githubusercontent.com/u/28751151?v=4?s=100" width="100px;" alt="Jeremy Paige"/><br /><sub><b>Jeremy Paige</b></sub></a><br /><a href="https://github.com/pyOpenSci/lessons/pulls?q=is%3Apr+reviewed-by%3Aucodery" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://hachyderm.io/web/@willingc"><img src="https://avatars.githubusercontent.com/u/2680980?v=4?s=100" width="100px;" alt="Carol Willing"/><br /><sub><b>Carol Willing</b></sub></a><br /><a href="https://github.com/pyOpenSci/lessons/pulls?q=is%3Apr+reviewed-by%3Awillingc" title="Reviewed Pull Requests">👀</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://fosstodon.org/@eriknw"></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=pyOpenSci/lessons&type=Date)](https://star-history.com/#pyOpenSci/lessons&Date)
