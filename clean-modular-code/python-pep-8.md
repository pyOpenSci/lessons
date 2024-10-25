---
jupytext:
  formats: ipynb,md:myst
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

# Python code style for readability and usability 

:::{admonition} What you will learn
:class: tip

* Describe the benefits of using code standards.
* Explain the `PEP 8` style guide and how it helps promote code readability.
* Describe key components of the PEP 8 style guide, including naming conventions and white space.
* List tools to help you apply the `PEP 8` style guide to your code.  

:::

## Why code style matters 

Code standards make your code more readable and easier to maintain, just like writing conventions make text easier to read. Think about how we capitalize the first word of a sentence or add spaces between words—without those conventions, text would be hard to follow. 
  
For example:

* Readable sentence: This is a sentence.
* Unformatted sentence: thisisasentence.withoutspacesitgetsconfusing.


Just like good grammar makes text easier to read, following code style rules like [PEP 8](https://peps.python.org/pep-0008/) helps make your code easier to understand and debug. It enforces rules on naming variables, capitalization, formatting code, and structuring your script. Well-formatted code also makes it easier for you to share code, given it will be easier for others to understand.  

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
#some data analysis with poor formatting
import pandas as pd
from datetime import datetime
def classify_precipitation(precip_list):
 avg_precip=pd.Series(
precip_list
 ).mean(
 )
 if avg_precip<100:
  return'Low'
 elif avg_precip>=100 and avg_precip<=150: return'Medium';



 return'High'
data={'location':['Station1','Station2','Station3','Station4'],'year':[2021,2021,2021,2021],'monthly_precipitation':[[50.0,70.0,90.0,80.0],[100.0,110.0,120.0,130.0],[150.0,160.0,170.0,180.0],[200.0,210.0,220.0,230.0]],'start_date':["2021-01-01","2021-01-01","2021-01-01","2021-01-01"]}
df=pd.DataFrame(data)
df["start_date"]=pd.to_datetime(df[str('start_date')])
df['precipitation_category']=df['monthly_precipitation'].apply(classify_precipitation)
df
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Notice that by adding docstrings, spacing to the the code, and a few comments.... 

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Import in order: standard library, third party packages, your packages
from datetime import datetime

import pandas as pd

def classify_precipitation(precip_list):
    """Classify average monthly precipitation into categories: low, medium, or high.

    Parameters
    ----------
    precip_list : list of float
        A list of monthly precipitation values (in mm).

    Returns
    -------
    str
        The precipitation category: 'Low', 'Medium', or 'High'.
    """
    avg_precip = pd.Series(precip_list).mean()

    # Define the precipitation ranges
    if avg_precip < 100:
        return 'Low'
    elif 100 <= avg_precip <= 150:
        return 'Medium'
    else:
        return 'High'


# Sample data for precipitation (in mm), locations, and date
data = {
    'location': ['Station1', 'Station2', 'Station3', 'Station4'],
    'year': [2021, 2021, 2021, 2021],
    'monthly_precipitation': [
        [50.0, 70.0, 90.0, 80.0],  # Station1
        [100.0, 110.0, 120.0, 130.0],   # Station2
        [150.0, 160.0, 170.0, 180.0],   # Station3
        [200.0, 210.0, 220.0, 230.0]    # Station4
    ],
    'start_date': ["2021-01-01", "2021-01-01", "2021-01-01", "2021-01-01"]
}

df = pd.DataFrame(data)
# format date and replace value
df['start_date'] = pd.to_datetime(df['start_date'])

# Classify precipitation levels into categories: 'Low', 'Medium', 'High'
df['precipitation_category'] = df['monthly_precipitation'].apply(classify_precipitation)

df
```



+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Tools for Consistent Code Style

It may seem overwhelming to remember hundreds of different rules from style guides like [PEP 8](https://peps.python.org/pep-0008/), [pydocstyle](https://pypi.org/project/pydocstyle/), and others --- the good news is that you don't have to! 

### Linters & Formatters

Two categories of "[static analysis](https://en.wikipedia.org/wiki/Static_analysis)" tools called **code linters and formatters** can identify and automatically apply these standards for you.

[**Linters**](https://en.wikipedia.org/wiki/Lint_(software)) are tools that analyze your code against a set of rules, show violations of those rules, and sometimes make suggestions for how to fix them. Linters will check not only for stylistic problems, but also logical problems like incorrect syntax, unreachable code, and so on. 

For example, a linter can identify the *errors* in this code, and suggest how to fix it.

```python
n_legs = {"cat": 4, "snake": 0, "centipede": 100}
for animal, legs in n_legs:
    print(f"An {animal} has {legs} legs")
```

```shell
lint.py:2:21: PLE1141 [*] Unpacking a dictionary in iteration without calling `.items()`
  |
1 | n_legs = {"cat": 4, "snake": 0, "centipede": 100}
2 | for animal, legs in n_legs:
  |                     ^^^^^^ PLE1141
3 |     print(f"An {animal} has {legs} legs")
  |
  = help: Add a call to `.items()`

Found 1 error.
[*] 1 fixable with the `--fix` option.
```

A linter can also check for *stylistic* rules you may want to keep consistent, like the PEP8 style names we'll discuss below

```python
def My_Function(x: int) -> int:
    return x * 2
```

```shell
naming.py:1:5: N802 Function name `My_Function` should be lowercase
  |
1 | def My_Function(x: int) -> int:
  |     ^^^^^^^^^^^ N802
2 |     return x * 2
  |

Found 1 error.
```

**Formatters** are tools that will reformat and *change* your code according to a style. Formatters should[^bugs_exist] only make changes to your code that don't affect its logical structure or behavior. 

For example we could apply a code formatter to the rather unfortunate function above and have it automatically cleaned up for us:

:::::{tab-set}
::::{tab-item} Unformatted

```python
def classify_precipitation(precip_list):
 avg_precip=pd.Series(
precip_list
 ).mean(
 )
 if avg_precip<100:
  return'Low'
 elif avg_precip>=100 and avg_precip<=150: return'Medium';



 return'High'
```

::::
::::{tab-item} Formatted

```python
def classify_precipitation(precip_list):
    avg_precip = pd.Series(precip_list).mean()
    if avg_precip < 100:
        return "Low"
    elif avg_precip >= 100 and avg_precip <= 150:
        return "Medium"

    return "High"
```

::::
:::::


There is not always a clear distinction between these categories of tools - formatters will correct some errors detected by linters, and linters will sometimes fix rule violations in the same way that formatters will. The distinction is more a distinction in *purpose* rather than a qualitative distinction *between tools.*


### Common Code Style Tools

#### For `.py` Files

Use popular tools like **Black** or **Ruff**:

- **[Black](https://black.readthedocs.io/en/stable/)**: Automatically reformats code according to PEP 8.
- **[Ruff](https://docs.astral.sh/ruff/configuration/#jupyter-notebook-discovery)**: A linter and formatter that also supports import sorting.

Both tools can be run manually or integrated into **pre-commit hooks** with Git to check your code before each commit. You can also configure them in your IDE (like VSCode, PyCharm, or Spyder) to format your code every time you save.


:::{note}
Ruff doesn’t fully support Jupyter/MyST markdown notebooks yet but can be integrated into a pre-commit workflow for GitHub repositories.
:::


#### For Jupyter Notebooks

For Jupyter Notebooks, try:
- **Notebook extensions**: Add extensions to your interface to format cells automatically.
- **nbQA**: A command-line tool that applies Black or Ruff to Jupyter Notebooks via the CLI.

### Using Static Analysis Tools

These tools can be used in the following ways:
- **Manually**: Run on-demand to check and format your code - e.g. running `black .` or `ruff check` in your shell.
- **Pre-commit hook**: Enforce code style checks before every commit - e.g. by adding a script to the `.git/hooks/pre-commit` file in a git repository, or using a tool like [`pre-commit`](https://pre-commit.com/).
- **IDE integration**: Automatically format code in your editor. e.g., instructions for [ruff](https://docs.astral.sh/ruff/editors/setup/) and [black](https://black.readthedocs.io/en/stable/integrations/editors.html)
- **Continuous Integration**: Enforce code style as a part of code review, e.g. with [github actions](https://black.readthedocs.io/en/stable/integrations/github_actions.html).

Using these tools ensures your code remains consistent, readable, and compliant with PEP 8, without memorizing all the rules.


+++ {"editable": true, "slideshow": {"slide_type": ""}}


## Common Python Style Rules: PEP 8 and Beyond

There is a style guide devoted to Python PEP 8 standards that you can read [here](https://www.python.org/dev/peps/pep-0008/#naming-conventions). However, below are a handful of PEP 8 Rules that you can consider following when writing code. 

### Naming

:::{admonition} Terminology Review
:class: tip

First, let's review some terminology associated with naming conventions.

* **Lowercase letter:** `b`
* **Uppercase letter:** `B`
* **lowercase:** `this is all lowercase words`
* **snake case:** when words are separated by underscores: `lower_case_with_underscores`
* **Uppercase:** All words are all uppercase letters: `UPPERCASE`
* **Snake case** upper case: `UPPER_CASE_WITH_UNDERSCORES`
* **CamelCase:** Every word is capitalized so they visually stand out: `CapitalizedWords`. This is sometimes also referred to as CapWords or StudlyCaps.
  * Note: When using acronyms in CamelCase, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.
* **mixedCase:** (differs from CapitalizedWords by initial lowercase character!)
* **Capitalized_Words_With_Underscores:** This approach is not recommended. Use one convention and stick with it.

:::

* Use **snake_case** for variables, functions, and methods
* Use **CamelCase** for class names.
* Avoid using single-character letters that could be confused with numbers  (ie the letter `l` looks similar to the number one  `1` 

```python
# Use UpperCamelCase for class definitions
class DataProcessor:
    """A class to process data and calculate statistics."""

    # lower_snake_case for methods and functions
    def calculate_average(self, data_list):
        """Calculate the average of a list of numbers."""
        total_sum = sum(data_list)
        count = len(data_list)
        return total_sum / count

# Call to create an object of a class
data_processor = DataProcessor()
numbers = [10, 20, 30, 40, 50]

# Use snake case for variable names and method call
average_value = data_processor.calculate_average(numbers)

# Example of a standard library function call
print(f"The average value is: {average_value}")
```

### Layout & Formatting

* Line Length: Limit all lines to 79 characters for better readability.

:::{tip}
Most text editors allow you to set up guides to see how long your code is. You can then use these guides to create line breaks in your code.
:::

* It’s good practice to import all required libraries at the top of your **Python** script or in the first cell of a **Jupyter Notebook**. This helps anyone understand what packages are needed to run your code. 
* PEP 8 recommends organizing imports in the following order:

1. **Standard Library Imports**: These built-in modules come with Python, such as `os` and `glob`. You can find the full list [here](https://docs.python.org/3/library/index.html).
2. **Third-Party Imports**: Libraries that you install via `pip`, like {mod}`numpy` and {mod}`pandas`.
3. **Local Imports**: Code or modules specific to your project.

Here’s an example following PEP 8 conventions:

```python
import os
import glob

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from my_module import my_function
```

### Whitespace

* Add two blank lines before top-level function and class definitions
* Add a single blank line before method definitions within a class
* Add single blank lines to group blocks of related code within functions and methods.
* Add a single blank line between code and a single-line comment.
* Comments: Add a space after the `#` sign and capitalize the first letter of a comment


```python
import numpy as np


# Two blank lines above a function definition
def my_function():
    # Process data
    data = pd.readcsv("pyos-data.csv")
    data["values"] = data["values"] * 2

    # One line to break up code into related chunks
    # e.g. processing is separate from plotting
    plt.plot(values)


# Two lines before a class definition
class MyClass:
    
    # One line before a method definition
    def my_method(): ...
```


[^bugs_exist]: If they are not buggy
