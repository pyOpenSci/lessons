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

* How to follow the PEP 8 style guide to write Python code that’s easy to read and understand.
* Best practices for naming variables, using comments, and formatting code.
* Tools to help you apply PEP 8 to your code automatically.

:::

## Why code style and Python PEP 8 matters 

Just like good grammar makes text easier to read, PEP 8 helps make your code easier to understand. It enforces rules on naming variables, capitalization, formatting code, and structuring your script. Well-formatted code also makes it easier for you to share code, given it will be easier for others to understand.  

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
 avg_precip=pd.Series(precip_list).mean()
 if avg_precip<100:
  return'Low'
 elif avg_precip>=100 and avg_precip<=150:
  return'Medium'
 else:
  return'High'
data={'location':['Station1','Station2','Station3','Station4'],'year':[2021,2021,2021,2021],'monthly_precipitation':[[50.0,70.0,90.0,80.0],[100.0,110.0,120.0,130.0],[150.0,160.0,170.0,180.0],[200.0,210.0,220.0,230.0]],'start_date':["2021-01-01","2021-01-01","2021-01-01","2021-01-01"]}
df=pd.DataFrame(data)
df['start_date']=pd.to_datetime(df['start_date'])
df['precipitation_category']=df['monthly_precipitation'].apply(classify_precipitation)
df
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Notice that by adding docstrings, spacing to the the code.... 

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Built-in libraries are imported first
from datetime import datetime
import pandas as pd

# Function to classify precipitation levels
def classify_precipitation(precip_list):
    """Classify average monthly precipitation into low, medium, or high.

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


# Sample data for precipitation values (in mm) for different locations
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
df['start_date'] = pd.to_datetime(df['start_date'])

# Classify precipitation levels based on ranges
df['precipitation_category'] = df['monthly_precipitation'].apply(classify_precipitation)

df
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## How to Apply PEP 8 Code Style Standards

It may seem overwhelming to remember all the PEP 8 rules, but tools called **code formatters** can automatically apply these standards for you.

### For `.py` Files

Use popular tools like **Black** or **Ruff**:

- **[Black](https://black.readthedocs.io/en/stable/)**: Automatically reformats code according to PEP 8.
- **[Ruff](https://docs.astral.sh/ruff/configuration/#jupyter-notebook-discovery)**: A linter and formatter that also supports import sorting with **isort**.

Both tools can be run manually or integrated into **pre-commit hooks** with Git to check your code before each commit. You can also configure them in your IDE (like VSCode, PyCharm, or Spyder) to format your code every time you save.


:::{note}
Ruff doesn’t fully support Jupyter/MyST markdown notebooks yet but can be integrated into a pre-commit workflow for GitHub repositories.
:::


### For Jupyter Notebooks

For Jupyter Notebooks, try:
- **Notebook extensions**: Add extensions to your interface to format cells automatically.
- **nbQA**: A command-line tool that applies Black or Ruff to Jupyter Notebooks via the CLI.

### Running These Tools
These tools can be used in the following ways:
- **Manually**: Run on-demand to check and format your code.
- **Pre-commit hook**: Enforce code style checks before every commit.
- **IDE integration**: Automatically format code in your editor.

Using these tools ensures your code remains consistent, readable, and compliant with PEP 8, without memorizing all the rules.

:::{admonition} Linter vs. Code Formatter
:class: note

- **Linter**: Checks your code and highlights issues but doesn’t automatically fix them.
- **Code Formatter**: Automatically reformats your code according to style rules.

Ruff acts as both a linter and formatter, making it ideal for `.py` file workflows.
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}


## Why use code standards when writing Python code

Code standards make your code more readable and easier to maintain, just like writing conventions make text easier to read. Think about how we capitalize the first word of a sentence or add spaces between words—without those conventions, text would be hard to follow. Similarly, code with inconsistent formatting is difficult to understand and debug.
  
For example:

* Readable sentence: This is a sentence.
* Unformatted sentence: thisisasentence.withoutspacesitgetsconfusing.

Using code standards like PEP 8 helps avoid such confusion, making code clearer and more professional.

### Some PEP 8 rules to remember 

There is a style guide devoted to Python pep 8 standards that you can read [here](https://www.python.org/dev/peps/pep-0008/#naming-conventions). However, below are a handful of PEP 8 Rules that you can consider following when writing code. 

* Naming Conventions: Use **snake_case** for variables/functions and **CamelCase** for class names.

```python
# This is a class definition
class MyClass:
    """A class to process data and calculate statistics."""

    # This is a function 
    def calculate_average(self, data_list):
        """Calculate the average of a list of numbers."""
        total_sum = sum(data_list)
        count = len(data_list)
        return total_sum / count

# Example variable names and function call
data_processor = DataProcessor()
numbers = [10, 20, 30, 40, 50]
average_value = data_processor.calculate_average(numbers)

print(f"The average value is: {average_value}")
```

* Line Length: Limit all lines to 79 characters for better readability.

:::{tip}
Most text editors allow you to set up guides to see how long your code is. You can then use these guides to create line breaks in your code.
:::

* Comments: Add a space after the `#` sign and capitalize the first letter of a comment:

`# This is a PEP 8 conforming comment`

* White Space: Add space between sections of code to improve clarity.
* Avoid using single-character letters that could be confused with numbers  (ie the letter `l` looks similar to the number one  `1` 
* Add a blank line before a single-line comment (unless it is the first line of a cell in Jupyter Notebook)

```python
a = 1 

# Here is a commment
b = 2 

```

* **Break up sections of code with white space:** Breaking up your
code becomes even more important when you start working in Jupyter Notebooks which offer individual cells where you can add Markdown and code.

```python
# Process some data here 
data=pd.readcsv("pyos-data.csv")

# Plot data - notice how separating code into sections makes it easier to read
fig, ax = plot.subplots()
data.plot(ax=ax)
plt.show()
```

## PEP 8 naming conventions

:::{seealso}
For the entire pep-8 style guide see: <a href="https://peps.python.org/pep-0008/" target="_blank">PEP 8 Style Guide published by the Python Software Foundation</a>.

:::

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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Best practices for importing libraries

### Import Python libraries at the top of your code

It’s good practice to import all required libraries at the top of your **Python** script or in the first cell of a **Jupyter Notebook**. This helps anyone understand what packages are needed to run your code. It also follows PEP 8 conventions.

### Organize your imports into groups

PEP 8 recommends organizing imports in the following order:

1. **Standard Library Imports**: These built-in modules come with Python, such as `os` and `glob`. You can find the full list [here](https://docs.python.org/3/library/index.html).
2. **Third-Party Imports**: Libraries that you install via `pip`, like `numpy` and `pandas`.
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

### Why organize imports?

Organizing your imports this way ensures your code is readable and follows widely accepted practices. Importing libraries at the top also makes it easier to debug and see which dependencies are required to run the code.
