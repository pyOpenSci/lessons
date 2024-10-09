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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Best Practices for Importing Python Packages In Scientific Code

There are a set of best practices that you should follow when importing **Python** packages in your code. These best practices are outlined in the <a href="https://www.python.org/dev/peps/pep-0008/#imports" target="_blank">PEP 8 guidelines</a> and apply to both **Python** scripts and to working in **Jupyter Notebook** files.

## Import Python Libraries at the Top of Your Script or Notebook

It is good practice to import all of the packages that you will need at the top of your **Python** script (.py file) or in the first code cell of a **Jupyter Notebook** file. 

This allows anyone looking at your code to immediately know what packages they need to have installed in order to successfully run the code. This rule also follows the PEP 8 conventions for **Python** code.

```python
import os 

import pandas as pd
import numpy as np
```

Once you have imported all of the packages that you need to run your code in a script, you have access to all of the functions and classes defined in each package. 

If these imports are at the top of the script or **Jupyter Notebook** file, then you will be able to use those packages in any code lines that follow. 

This means that if you import a package *after* running some code that requires that package, your code will not run successfully.


## 2. List Package Imports Following PEP 8 Standards: Most Common First, Followed By Third Party

<a href="https://www.python.org/dev/peps/pep-0008/#imports" target="_blank">PEP 8</a> also specifies the order in which you should list your imports as follows (starting with the most commonly used):

> Imports should be grouped in the following order:
>    Standard library imports.
>    Related third party imports.
>    Local application/library specific imports.
> You should put a blank line between each group of imports.

You may be wondering, what is a standard library import? The standard library imports are commonly used tools that are general in purpose and are part of the standard library of **Python**. These including things like:

* **os**: handle files and directories.
* **glob**: create lists of files and directories for batch processing.

In the PEP 8 order, other commonly used packages that are general in purpose will follow such as: 

* **numpy**: work with data in array formats.
* **matplotlib**: plot data.
* * **Pandas**: to work with tabular data.

A PEP 8 order of imports for commonly used **Python** packages for science would look something like this:

```python
import os
import glob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
``` 

Note that there is a space between the standard imports (`glob` and `os`)
and the rest of the third-party imports.

## What are Local application/library specific imports 

Local application / library specific imports refer to tool that you have created locally or just for your own work.  

TODO: more here...
