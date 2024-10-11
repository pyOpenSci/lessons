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

# Activity 3: Tests & Checks for your code

* In [activity 1](../activity-1/clean-code-activity-1), you took some code and made it cleaner using expressive variable names and docstrings to document the module. 
* In [activity 2](../activity-2/clean-code-activity-2), you made your code more DRY ("Don't Repeat Yourself") using documented functions and conditionals. 

In this activity, you will build checks into your workflow to handle data processing "features". 

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Real world data processing & workflows and edge cases 

Real-world data rarely can be imported without "work arounds". You will often find unusual data entries and values you don't expect. Sometimes, these values are documented - for example, a 9999 may represent a missing value in a dataset. Other times, there are typos and other errors in the data that you need to handle. These unusual values or instances in a dataset or workflow are sometimes called "edge cases".  

Writing robust code that handles unexpected values will make your code run smoothly and fail gracefully. This type of code, which combines functions (or classes) and checks within the functions that handle messy data, will make your code easier to maintain over time. 

:::{tip}
Using functions, classes, and methods (functions within a class) is a great first step in handling messy data. A function or method provides a modular unit you can test outside of the workflow for the edge cases you may encounter. Also, because a function is a modular unit, you can add elements to handle unexpected processing features as you build your workflow.

Once you have these functions and methods, you can add checks using conditional statements and try/except blocks that anticipate edge cases and errors that you may encounter when processing your data. 
:::

## Manage the unexpected 

In this activity, you will apply the following strategies to make your code more robust, maintainable & usable:

* **[Fail fast with useful error messages](fail-fast)**: Failing fast is a software engineering term that means allowing your 
  code to stop early when something goes wrong, ensuring that errors are caught 
  and communicated clearly. This helps the user quickly understand what went 
  wrong and where.
* Use **[conditional statements](../checks-conditionals/python-conditionals)** 
  to check for specific conditions before executing certain parts of your code, 
  which can help catch issues early.
* **[Try/except blocks](../checks-conditionals/python-function-checks)** allow 
  you to handle potential errors by attempting an operation and catching any 
  exceptions if they occur, providing useful feedback without crashing the 
  entire program.

When you can, try to use a [Pythonic approach](pythonic-checks) to catch errors early. This means asking for forgiveness later (often using try/except blocks) vs using conditional statements to check the state or type of an object.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This works but is less Pythonic as it's a look before you leap approach
def clean_title(title):
    """Notice that this function checks explicitly to see if it's a list and then processes the data.
    """
    if isinstance(title, list):
        return title[0]
    return title
```

## More "pythonic" - ask for forgiveness 

easier to ask for forgiveness

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This is the preferred way to catch an error 
def clean_title(title):
    """
    Attempts to return the first character of the title.
    Raises the same error with a friendly message if the input is invalid.
    """
    try:
        return title[0]
    except IndexError as e:
        raise IndexError(f"Oops! You provided a title in an unexpected format. I expected the title to be provided in a list and you provided a {type(title)}.") from e

# Example usage:
title = ""
print(clean_title(title))  # This will raise an IndexError with the friendly message
```

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["hide-output", "hide-cell"]}

:::{tip}
### Applying functions to DataFrame values--`.apply` 

The `.apply()` function in pandas allows you to apply any function to rows or columns in a `pandas.DataFrame`. For example, You can use it to perform operations on specific column or row values. When you use `.apply()`, you can specify whether you want to apply the function across columns `(axis=0)` (the default) or across rows `(axis=1)`. For example, if you want to apply a function to each row of a DataFrame, you would use `df.apply(your_function, axis=1)`. This function is especially useful for applying logic that can’t be easily achieved with built-in pandas functions, allowing for more flexibility in data processing.

You can use `.apply` in pandas to efficiently replace `for loops` to process row and column values in a `pandas.DataFrame`.

:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### What's changed in your workflow?

:::{warning}
You have a new data file to open in your list of `.json` files in this activity. This file has some unexpected "features" that your code needs to handle gracefully to process all of the data.
:::

The code below is an example of what your code might look like after completing activity 2. You can choose to work with this code, or you can use the code that you completed in activity 2. 
Your goal is to make the code below run on the data provided in the activity-3 `data/` directory.

The code below will fail. You will need to do the following:

1. Use a debugger to determine why it's failing.
2. Add try/except blocks and/or conditional statements to your functions that handle various exceptions.

Your end goal is to make the code below run. 

:::{tip}
* If you are using Jupyter, then you might [find this page helpful when setting up debugging.](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html)
* VSCODE has a nice visual debugger that you can use.

:::


Important: It is ok if you can't get the code to run fully by the end of this workshop. If you can:

1. identify at least one of the data processing "bugs" (even if you can't fix it) and/or
2. fix at least one bug

You can consider your effort today as a success!

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["raises-exception"]}

## TODO: double check this is the right code from activity 2 - there are clear errors that i just fixed. but it needs to actually run

```python
# Note that this code has no checks or tests in the functions provided. You will need to add them to make the code run. 

import json
from pathlib import Path

import pandas as pd


def load_clean_json(file_path, columns_to_keep):
    """
    Load JSON data from a file. Drop unnecessary columns and normalize
    to DataFrame.

    Parameters
    ----------
    file_path : Path
        Path to the JSON file.
    columns_to_keep : list
        List of columns to keep in the DataFrame.

    Returns
    -------
    dict
        Loaded JSON data.
    """

    with file_path.open("r") as json_file:
        json_data = json.load(json_file)
    normalized_data = pd.json_normalize(json_data)

    return normalized_data.filter(items=columns_to_keep)


def format_date(date_parts: list) -> str:
    """
    Format date parts into a string.

    Parameters
    ----------
    date_parts : list
        List containing year, month, and day.

    Returns
    -------
    pd.datetime
        A date formatted as a pd.datetime object.
    """
    date_str = f("{date_parts[0]}-{date_parts[1]:02d}-{date_parts[2]:02d}")
    return pd.to_datetime(date_str, format="%Y-%m-%d")


def clean_title(value):
    """A function that removes a value contained in a list."""
    return value[0]

columns_to_keep = [
    "publisher",
    "DOI",
    "type",
    "author",
    "is-referenced-by-count",
    "title",
    "published.date-parts",
]

data_dir = Path("data")

all_papers_list = []
for json_file in data_dir.glob("*.json"):
    papers_df = load_clean_json(json_file, columns_to_keep)

    papers_df["title"] = papers_df["title"].apply(clean_title)
    papers_df["published_date"] = papers_df["published.date-parts"].apply(
        process_published_date
    )

    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)

print("Final shape of combined DataFrame:", all_papers_df.shape)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} On your own 1
:class: attention

Ideas for on your own welcome!
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} On your own 2
:class: attention
Ideas welcome?
:::

I want to have them move their code into a module if possible during this workshop but we could also kick that off in the day 2 workshop.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
