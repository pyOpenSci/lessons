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
(pep8-code-format)=
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

* Readable sentence:
    * This is a sentence.
* Unformatted sentence:
    * thisisasentence.withoutspacesitgetsconfusing.


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

Notice that adding docstrings, spacing to the code, and a few comments makes it easier to read. When code is easier to read, it 
then becomes easier to understand and, in the long term, maintain and contribute to.

[Expressive variable names](python-expressive-code) will make this code even more clear.

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

(tools-code-style)=
## Tools for Consistent Code Style

It may seem overwhelming to remember hundreds of different rules from style guides like [PEP 8](https://peps.python.org/pep-0008/), [pydocstyle](https://pypi.org/project/pydocstyle/), and others --- the good news is that you don't have to! There are tools called code linters and formatters that can apply consistent code formatting. 

You'll learn about those next.

:::{tip}
Code format tools are "[static analysis](https://en.wikipedia.org/wiki/Static_analysis)" tools. Static analysis tools are called “static” because they analyze your code without executing it. They review the source code to find errors, enforce coding standards, and improve readability, helping you catch potential issues before running your code.
:::


### Linters & formatters

**Code linters and formatters** are static analysis tools that identify and automatically apply code format standards for you.

#### About code linters 

[**Linters**](https://en.wikipedia.org/wiki/Lint_(software)) analyze your code against a set of rules (such as PEP 8 rules). They will identify those rule violations and suggest how to fix them. Linters will check for stylistic problems and logical problems like incorrect syntax and unreachable code (code that will never actually execute in your workflow). 

For example, have a look at the code below. You can runa linter on the code to identify the *errors*. The linter will suggest how to fix those errors but it will not actually apply the suggestions.

```python
n_legs = {"cat": 4, "snake": 0, "centipede": 100}
for animal, legs in n_legs:
    print(f"An {animal} has {legs} legs")
```

An example of a linter run on a `.py` file in the terminal. 
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

A linter can also check for *stylistic* rules. For instance, you may 
want to keep naming conventions consistent, following PEP8 guidelines, in your code. 

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

You'll learn more about naming conventions next.

#### About code formatters 

Code **formatters** are tools that identify issues, reformat and *change* your code according to a specific style. Formatters should[^bugs_exist] only make changes to your code that don't affect its logical structure or how it runs (its behavior). 

For example, you can apply a code formatter to the rather unfortunate function above and 
it will automatically clean it up. See below:

:::::{tab-set}
::::{tab-item} Unformatted

```python
# Unformatted code
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
# Code after the Black formatter has been run on it
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


Linters are primarily designed to analyze and point out issues in your code, such as style violations, logical errors, or bad practices. While some linters can suggest code fixes, their main purpose is to highlight problems rather than automatically fix them.

Formatters, on the other hand, are designed to modify your code automatically to adhere to a set style guide. They focus on layout and formatting (like indentation and line spacing).

However, some tools blur these lines: certain linters can auto-correct minor issues, and some formatters will identify and fix common coding errors as they reformat your code. So, the distinction is really more about their intended purpose—linting focuses on analysis and error detection while formatting focuses on consistent styling.


### Common code style tools

#### For `.py` files

If you are writing .py files, popular tools like **Black** or **Ruff** are useful for cleaning up your code:

- **[Black](https://black.readthedocs.io/en/stable/)**: An opinionated code formatter that automatically reformats code and generally adheres to PEP 8 guidelines.
- **[Ruff](https://docs.astral.sh/ruff/configuration/#jupyter-notebook-discovery)**: A linter and formatter that also supports import sorting.

Both Black and Ruff tools can be run manually or integrated into a workflow. 

Some people configure formatters like Ruff and/or Black in an IDE (like VSCode, PyCharm, or Spyder) to format your code every time you save a `.py` file.

If you use version control platforms like Git and GitHub, you can use Ruff and Black with **pre-commit hooks** to check your code passes style checks before you make a commit. 

:::{admonition} What is a pre-commit hook?
:class: tip
Pre-commit hooks are automated checks that run every time you try to make a commit in Git. They help catch issues by running tools like Black or Ruff before your code is officially saved in your project, ensuring consistent and clean code from the start.
:::

#### Code format in Jupyter Notebooks

Code formatters can also be used in Jupyter Notebooks. One popular way to format Jupyter notebooks using Jupyter Lab is the [Jupyter Lab codeformatter extension](https://jupyterlab-code-formatter.readthedocs.io/). This code formatter tool is an extension that adds a convenient button to your Jupyter Lab interface. You can use that button to format code cells in your Notebook. 

This tool is set up in the Binder connected to these lessons if you want to check it out. 

:::{note}
Ruff doesn’t fully support Jupyter/MyST markdown notebooks yet but can be integrated into a pre-commit workflow for GitHub repositories.
:::

There are also command-line tools that you can use to run Black and Ruff on Jupyter Notebooks, such as [**nbQA**](https://nbqa.readthedocs.io/en/latest/index.html). 

### How to integrate code formatters and linters into your workflow 

As you may have noticed above, there are different ways to integrate code formatters and linters into your workflows. The approach that you take will depend on the tools that you regularly use. A few approaches are discussed below:  

- **Manually**: You can choose to run these tools on-demand in your favorite terminal (shell) to check and format your code. This approach gives you control over when the tools are run, but it also requires you to run the formatters and periodically update your code.
- **Pre-commit hook**: Pre-commit hooks are great tools to use if you typically commit code to Git. Pre-commit hooks enforce code-style checks before every commit that you make to a repository.

:::{tip}
Pre-commit hooks can be  added to your .git directory in your repo or you can use a a tool such as [`pre-commit`](https://pre-commit.com/) to run them.
:::

- **IDE integration**: You can also set up your favorite IDE (VSCode, Spyder, PyCharm) to automatically format your code in your editor every time you save a file.

:::{tip}
If you're curious about setting up formatters in your IDE, check out instructions for setting up [ruff](https://docs.astral.sh/ruff/editors/setup/) and [black](https://black.readthedocs.io/en/stable/integrations/editors.html).
:::

- **Continuous Integration**: If you use a platform like GitHub or GitLab, then you can also set up and enforce code style on each commit and on pull requests (or merge requests) submitted to a repository. If you use GitHub, then you'd set these up using [GitHub actions](https://black.readthedocs.io/en/stable/integrations/github_actions.html).


Using these tools ensures that your code remains consistent, readable, and compliant with PEP 8 without you having to memorize all the rules.


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
