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

# Clean, Modular Code

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Part 1: 3 strategies

* Use [consistent code format](pep8-code-format)
* Use [expressive object names](python-expressive-code)
* [Make your code DRY](dry-code)

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

### PEP 8 & consistent code format

* Generally accepted rules for code format: PEP 8
* Code Formatters: Tools to apply PEP 8 as you work!

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# this code is not PEP8 compliant -- why?
def doStuff(a, b):
    print("Result:", a + b)
    return a + b


x = True
if x:
    print("Messy code.")
    print("Oops!")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This code is PEP8 compliant -- why?
def do_stuff(number1, number2):
    print("Result:", number1 + number2)
    return number1 + number2


x = True
if x:
    print("This is nicer code.")
    print("Yay!")
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

#### Code format tools

* Jupyter code formatter (installed in this binder).
* Black
* Ruff

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

#### [Other tools to consider](tools-code-style)

* pre-commit hooks: if you use version control, they run when you commit changes
* setup VSCode (and other IDE's) to format on save

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Expressive code

* Code can become documentation when written well.
* Use variable, function & class names that tell a user what each thing does

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

<center><img src="../images/clean-code/clean-code-expressive-variable-names-basmati-rice.png" alt="Image showing a large see-through Tupperware container with cookies in it but a label that says Basmati Rice."></center>

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# This code is PEP8 compliant -- why?
def do_stuff(number1, number2):
    print("Result:", number1 + number2)
    return number1 + number2


x = True
if x:
    print("This is nicer code.")
    print("Yay!")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def calculate_sum(number1, number2):
    print("Result:", number1 + number2)
    return number1 + number2


is_valid = True
if is_valid:
    print("This is nicer code.")
    print("Yay!")
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## DRY code

* Don't Repeat Yourself
* Use functions, loops and conditionals instead

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
a = 5
b = 10
print(a + 2)
print(b + 2)
print(a * 2)
print(b * 2)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def process_number(x):
    print(x + 2)
    print(x * 2)


numbers = [5, 10]
for num in numbers:
    process_number(num)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

:::{admonition} Begin Activity One!
:class: tip
You are now familiar with 3 strategies for writing better, cleaner code. In the [first activity](clean-code-activity-1), you will apply these principles to example code.

Remember that this is not a test! Rather, it's a chance to think about how you write code and how others may receive it! 
:::

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Part 2: Refactor your code
The 3 things to focus on: 
* **Document:** 
* **Modularize**
* **Ensure reproducibility: (dynamic paths)**

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Document as you go

* Make it a habit
* It's easier to do it as you work!

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Document your code

Add a docstring to the top of any script or module that explains the intent of the code.

:::{tip}
This docstring will appear in API documentation if you create it for a package!
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
"""What this module does"""

import pandas as pd

# Code starts here...
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# A sad, lonely, undocumented function
def add_numbers(x, y):
    return x + y


help(add_numbers)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# Better: Add a docstring!
def add_numbers(x, y):
    """
    Add two numbers.

    Parameters
    ----------
    x : int or float
        The first number.
    y : int or float
        The second number.

    Returns
    -------
    int or float
        The sum of `x` and `y`.
    """
    return x + y
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
help(add_numbers)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# Best add docstring with examples of running the function
def add_num(x, y):
    """
    Add two numbers.

    Parameters
    ----------
    x : int or float
        The first number.
    y : int or float
        The second number.

    Returns
    -------
    int or float
        The sum of `x` and `y`.

    Examples
    --------
    >>> add_num(2, 3)
    5
    >>> add_num(4.5, 5.5)
    10.0
    """
    return x + y
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Modularize your code

Functions:
* make code more robust and testable
* make code easier to test and maintain

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# Calculate and print the areas of three circles
radius1 = 3
area1 = 3.14159 * (radius1**2)
print(f"Area of circle with radius {radius1}: {area1}")

radius2 = 5
area2 = 3.14159 * (radius2**2)
print(f"Area of circle with radius {radius2}: {area2}")

radius3 = 7
area3 = 3.14159 * (radius3**2)
print(f"Area of circle with radius {radius3}: {area3}")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters
    ----------
    radius : float
        The radius of the circle.

    Returns
    -------
    float
        The calculated area of the circle.
    """
    return 3.14159 * (radius**2)


# Calculate and print the areas of three circles using the function
for radius in [3, 5, 7]:
    area = calculate_circle_area(radius)
    print(f"Area of circle with radius {radius}: {area}")
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Create dynamic paths

* Paths on Windows are different than MAC/Linux
* Using `Path` (or `os`)

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
import pathlib

# Dynamically generate a path so it will be correct across machine
path = pathlib.Path("") / "data" / "data.json"
print(path)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Tests & checks

* Usability sometimes means failing (gracefully and with intention). 

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

* Fail fast (with useful error messages)
* try/except blocks: handle errors (exceptions)
* Conditionals to optimize and redirect workflows

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Fail fast 


```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
tags: [raises-exception]
---
# This code fails with a useful message
import json
from pathlib import Path

import pandas as pd

# Define the file path
file_path = Path("your_file.json")

# Open the JSON file and read the data
with file_path.open("r") as json_file:
    json_data = json.load(json_file)

# Normalize the JSON data into a Pandas DataFrame
df = pd.json_normalize(json_data)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# The same problem occurs in this code but it fails with a less useful message
import json
from pathlib import Path

import pandas as pd

# Create a list of json files
file_paths = list(Path(".").glob("*.json"))
# Open the first file
with file_path[0].open("r") as json_file:
    json_data = json.load(json_file)

# Normalize the JSON data into a Pandas DataFrame
df = pd.json_normalize(json_data)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Handle errors

You can often anticipate the errors a user may encounter when using your code. This is especially true when processing data. You can often identify common errors and outlier values.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# What happens when the data are in a list rather than provided as a string?
# Here, the code runs and doesn't fail at all producing a potential bug
title = "package name I'm a title"
title.split(":")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# In this case the code is provided with an int - resulting in an attribute error
title = 1
package_name = title.split(":")[0]
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This works as expected
title = "package name: i'm a title"
package_name = title.split(":")[0]
package_name
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# In some cases, you may want to capture the error and return a default value
# (or do something else)
title = 9999

try:
    package_name = title.split(":")[0]
except AttributeError:
    # Ask yourself, how do you want to handle this exception?
    package_name = None
    # Should the code keep running? Should it exit? Should it assign a default value?
    #raise AttributeError(f"Oops - I expected a string and you provided a {type(title)}")

package_name
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# In others you may want to intentionally raise an error with a custom message.
title = 999

try:
    package_name = title.split(":")[0]
except AttributeError:
    # Ask yourself, how do you want to handle this exception? 
    # Should the code keep running? Should it exit? Should it assign a default value?
    raise AttributeError(f"Oops - I expected a string and you provided a {type(title)}")

package_name
```
