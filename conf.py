# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime
import subprocess

current_year = datetime.now().year
organization_name = "pyOpenSci"


# -- Project information -----------------------------------------------------

project = "pyOpenSci Open Source Lessons"
copyright = f"{current_year}, {organization_name}"
author = "pyOpenSci Community"
# Version is needed to avoid "cant describe anything fatal error"
version = "0.1"
release = "0.1"

# Get the latest Git tag - there might be a prettier way to do this but...
try:
    release_value = (
        subprocess.check_output(["git", "describe", "--tags"])
        .decode("utf-8")
        .strip()
    )
    release_value = release_value[:4]
except subprocess.CalledProcessError:
    release_value = "0.1"  # Default value in case there's no tag

# Update the release value
release = release_value

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_favicon",
    "sphinx.ext.todo",
    #"sphinx_codeautolink",
    "sphinx.ext.todo",
]

# colon fence for card support in md
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
]
myst_heading_anchors = 3
myst_footnote_transition = False

# Sphinx_favicon is used now in favor of built in support
# https://pypi.org/project/sphinx-favicon/
favicons = [
    {"href": "https://www.pyopensci.org/images/favicon.ico"},
]

# Link to our repo for easy PR/ editing
html_theme_options = {
    # "navbar_center": ["nav"], this can be a way to override the default navigation structure
    "external_links": [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/software-peer-review",
            "name": "Peer Review Guide",
        },
        {
            "url": "https://pyopensci.org/handbook",
            "name": "Handbook",
        },
    ],
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@pyOpenSci",
            "icon": "fa-brands fa-mastodon",
        },
    ],
    "logo": {
        # "text": "Python Packaging",
        "image_dark": "logo-dark-mode.png",
        "image_light": "logo-light-mode.png",
        "alt_text": "pyOpenSci Open Source Lessons. The pyOpenSci logo is a purple flower with pyOpenSci under it. The o in open sci is the center of the flower",
    },
    # Increase this as lessons are added - 
    # set low to hide links to other pyos sites and allow nav between lessons
    "header_links_before_dropdown": 5,
    "use_edit_page_button": True,
    "show_nav_level": 2,
    "navigation_depth": 3,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "github_url": "https://github.com/pyopensci/lessons",
    "footer_start": ["code_of_conduct", "copyright"],
    "footer_end": [],
    "navigation_with_keys": False,
}

html_context = {
    "github_user": "pyopensci",
    "github_repo": "lessons",
    "github_version": "main",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".direnv",
    ".github",
    ".nox",
    ".venv",
    "README.md",
    "**/README.md",
    "styles/*",
    "vale-styles/*",
    "CODE_OF_CONDUCT.md",
    "**/data/**",
    "_law_tests",
    "**/*.ipynb",  # we use myst notebooks for publishing
    "venv",
]

# For sitemap generation
html_baseurl = "https://www.pyopensci.org/lessons/"
sitemap_url_scheme = "{link}"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pyos_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["css/styles.css"]
html_title = "pyOpenSci Lessons"
html_js_files = ["matomo.js"]


# Social cards
ogp_site_url = "https://www.pyopensci.org/lessons/"
ogp_social_cards = {
    "line_color": "#6D597A",
    # "image": "_static/pyopensci-logo-package-guide.png",
}


# myst nb extension used to execute notebooks
nb_execution_mode = "auto"

# ------------------
# Intersphinx & code linking

# intersphinx_mapping = {
#     "python": ("https://docs.python.org/3", None),
#     "numpy": ("https://numpy.org/doc/stable/", None),
#     "pandas": ('https://pandas.pydata.org/docs/', None),
#     "earthpy": ("https://earthpy.readthedocs.io/en/latest/", None),
#     "matplotlib": ('https://matplotlib.org/stable/', None),
# }

# codeautolink_global_preface = """
# import numpy as np
# import pandas as pd
# import os
# """
# codeautolink_concat_default=True


# # suppress all codeautolink warnings, we don't really care if it's busted
# suppress_warnings = [
#     "codeautolink.clean_block",
#     "codeautolink.parse_block",
#     "codeautolink.import_star",
#     "codeautolink.match_block",
#     "codeautolink.match_name",
#     "codeautolink.failed_resolve",
# ]