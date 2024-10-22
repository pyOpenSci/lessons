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

(clean-code-activity-3)=
# Activity 3: Tests & Checks for your code

* In [activity 1](../activity-1/clean-code-activity-1), you made your code cleaner and more usable using [expressive variable names](python-expressive-code) and docstrings to document the module. 
* In [activity 2](../activity-2/clean-code-activity-2), you made your code more DRY ("Don't Repeat Yourself") using [functions](write-functions) and [conditionals](conditionals). 

In this activity, you will build checks into your workflow using [try/except](try-except) blocks added to functions to handle some "features" found in the JOSS, CrossRef citation data.

:::{note}
A data feature, as defined here, represents unexpected values that may be found in real-world data. You will rarely find that your data can be processed without some cleaning steps! 
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Real world data processing & workflows and edge cases 

Real-world data can rarely be imported without cleanup steps. You will often find unusual data values you don't expect. Sometimes, these values are documented--for example, a `9999` may represent a missing value in a dataset. And sometimes, that missing value is documented for you. Yay! 

Other times, the data contains undocumented typos and other errors that you need to handle in your code. In this activity, you will see these unusual values referred to as data "edge cases."  

Writing robust code that handles unexpected values will make your code run smoothly and fail gracefully. This type of code, which combines functions (or classes) and checks within the functions that handle messy data, will make your code easier to maintain.

### Strategies for handling messy data

There are several strategies that you can employ to handle unusual data values. In this activity, you will apply the following strategies to make your code more robust, maintainable & usable:

* **[conditional statements](../../code-workflow-logic/python-conditionals)** 
  to check for specific conditions before executing code. This allows you to create different pathways for code to execute based on specific conditions.
* **[Try/except blocks](../../code-workflow-logic/python-function-checks)** allow 
  you to handle potential errors by attempting an operation and catching any 
  exceptions if they occur, providing useful feedback.Sometimses, you may want the program to end on an error. In other cases, you may want to handle it in a specific way.
* **[Fail fast with useful error messages](fail-fast)**: Failing fast is a software engineering term that means allowing your 
  code to stop when something goes wrong, ensuring that errors are caught 
  and communicated promptly. This helps the user quickly understand the error, what went 
  wrong, and where.

:::{tip}
As you make decisions about adding checks to your code, weigh the value of using [Pythonic approach](pythonic-checks) vs. literal checks (look before you leap) to address potential errors in your code. This means asking yourself if the code should ask for forgiveness later or check an object's state or type before proceeding.
:::

<!-- Based on some of Carol's comments, maybe we focus less on what is Pythonic and more on the critical thinking element surrounding when to use conditionals vs. a try/except approach. I don't think that is clear yet in these lessons.
 -->
 
### Functions, classes, and methods are a tool

Using functions and class methods is a great first step in handling messy data. A function or method provides a modular unit you can test outside the workflow for the edge cases you may encounter. Also, because a function is a modular unit, you can add elements to handle unexpected processing features as you build your workflow.

Once you have these functions and methods, you can add checks using conditional statements and [try/except](try-except) blocks that anticipate edge cases and errors you may encounter when processing your data. 

<!-- Consider if this last paragraph might belong in the function checks lesson vs. here. 

## Clean up your workflow

The code below is an example of what your code might look like after completing [Activity 2](activity-2). Notice that the code below fails when run.
 
:::{admonition} What's changed in the data?
:class: tip

In this workflow, you have a new set of data files to open in your list of `.json` files. The first file, has some unexpected "features" that your code needs to handle gracefully to process all of the data successfully.

:::

-->

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["raises-exception"]}

## Activity 3, part 1: Find the data & fail fast when it's missing

If you are processing specific data in your workflow, then ensuring your code can successfully find the data is your first (and possibly most important) goal. 

**Consider:** How does your code handle and tell a user that it can't find the data that you want it to open?

If your code doesn't [fail fast](fail-fast) with a useful error message, and it continues to run and fails later, it will potentially confuse a user. The error that will likely be raised later will likely not alert the user that the issue is actually missing data vs something else. 

This will then mislead someone when trying to troubleshoot your code. 

### Activity 3 part 1 code example 

Consider the code below. Note that the code below has an incorrect `/data` directory path that doesn't exist. Notice that the error that is thrown after running the code is not a [`FileNotFounderror`](file_error). 

Instead, it raises a [`ValueError`](value_error): `ValueError: No objects to concatenate`), which is much less useful to a user (who could be your future self).


:::{admonition} Group work
:class: warning

In small groups, consider the code and answer the following questions together.

Questions:

* Does the code fail fast?
* What type of error do you want Python to throw when it can't find a data file? Use Google, LLMs, or our [tests and checks](common-exceptions) lesson to help figure this out. 
* Does the code handle the actual error gracefully?
* How can you make the code better handle missing data files?

:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
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
    return pd.json_normalize(json_data)

# Notice that this is bad data dir
# What happens when your code runs?
data_dir = Path("bad-bad-data")

all_papers_list = []
for json_file in data_dir.glob("*.json"):
    papers_df = load_clean_json(json_file, columns_to_keep)
    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Activity 3, part 2: Add checks to the `format_date` function

The code below creates a `pd.DataFrame` with the first 15 publications in the JOSS sample `data.json` file. This is the first of 3 files you must process in your workflow.

Your first task is to process and format the `published_date` column in the data to make it a `pandas.datetime` object. Having a date in a `datetime` format will allow you to do time-related analysis on your data, such as counting publications by month and year! The expected CrossRef published date should be:

```json
"published": {
      "date-parts": [
        [
          2022,
          11,
          27
        ]
      ]
    }
```

However, the date is not always formatted as expected in the above sample data.

For this activity, focus on adding checks to the `format_date` function. **IMPORTANT:** Use the sample data provided below for your troubleshooting exercise. This will allow you to focus on fixing only one function rather than trying to troubleshoot the entire workflow!  


:::{admonition} Activity 2: Part 2
:class: warning 

In small groups, do the following:

1. Evaluate the `published_date` field in the data created below and answer the question: 

* Do you see any unusually-formatted values that may be responsible for making your code above fail?

2. Once you have a list of issues you observe in the data, address them by modifying the `format_date` function below.
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["hide-output", "hide-cell"]}

###  Format dates with `pandas.datetime`

Let's work on formatting dates so there is a consistent format in our dataframe. Python has a [string formatting language](https://docs.python.org/3/library/string.html#formatspec) that defines useful characters for formatting.


What Does `02d` Mean?

* `d`: This part of the format code means you’re expecting an integer. It tells Python to format the value as a decimal (whole number).
* `02`: The `02` means the number should be padded with leading zeros if necessary, so the total width is 2 digits. For example:

* `1` becomes `01`
* `5` becomes `05`
* `12` stays as `12` (no padding needed)

This is especially useful for formatting months or days, which often require a `MM-DD` format (e.g., 01-05 for January 5th).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import pandas as pd

# Manually recreate data for the first 15 crossref entries
joss_pubs = [
    {
        "title": ["bmiptools: BioMaterials Image Processing Tools"],
        "published_date": [["2022", "11", "27"]],
        "citations": 2
    },
    {
        "title": [["QuasinormalModes.jl: A Julia package for computing discrete eigenvalues of second order ODEs"]],
        "published_date": [2022, "5", 25],
        "citations": 2
    },
    {
        "title": ["CWInPy: A Python package for inference with continuous gravitational-wave signals from pulsars"],
        "published_date": [[2022, 9, "29"]],
        "citations": 3
    },
    {
        "title": ["Nempy: A Python package for modelling the Australian National Electricity Market dispatch procedure"],
        "published_date": [[""]],
        "citations": 2
    },
    {
        "title": ["Spectral Connectivity: a python package for computing spectral coherence and related measures"],
        "published_date": [[]],  # No date available
        "citations": 3
    },
    {
        "title": ["SEEDPOD Ground Risk: A Python application and framework for assessing the risk to people on the ground from uncrewed aerial vehicles (UAVs)"],
        "published_date": [["2022", "3", ""]],
        "citations": 1
    },
    {
        "title": ["DIANNA: Deep Insight And Neural Network Analysis, explainability in time series"],
        "published_date": [[2022, 12, 15]],
        "citations": 1
    },
    {
        "title": [["diman: A Clojure Package for Dimensional Analysis and Unit Checking"]],
        "published_date": [[2022, 1]],
        "citations": 0
    },
    {
        "title": ["PERFORM: A Python package for developing reduced-order models for flow simulation"],
        "published_date": [[9999]],
        "citations": 3
    },
    {
        "title": ["TLViz: Visualising and analysing tensor decompositions"],
        "published_date": [[2022, 11, 25]],
        "citations": 2
    },
    {
        "title": ["ALUES: R package for Agricultural Land Use Evaluation System"],
        "published_date": [[2022, 5, 12]],
        "citations": 1
    },
    {
        "title": [["Spiner: Performance Portable Routines for Generalized SpMV and Triangular Solvers"]],
        "published_date": [[2022, 7, 5]],
        "citations": 0
    },
    {
        "title": ["pyndl: Naïve Discriminative Learning in Python"],
        "published_date": [[2022, 12, 15]],
        "citations": 0
    },
    {
        "title": ["HostPhot: global and local photometry of galaxies"],
        "published_date": [[2022, 8, 15]],
        "citations": 1
    },
    {
        "title": ["QMKPy: A Python Testbed for the Quadratic Multichannel Kalman Filter"],
        "published_date": [[2022, 11, 2]],
        "citations": 0
    }
]

joss_pubs_df = pd.DataFrame(joss_pubs)
joss_pubs_df.head(15)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
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
    # A print statement might help you identify the issue
    print(f"The input value is: {date_parts}")
    date_str = (
        f"{date_parts[0][0]}-{date_parts[0][1]:02d}-{date_parts[0][2]:02d}"
    )
    return pd.to_datetime(date_str, format="%Y-%m-%d")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
joss_pubs_df["published_date"][0]
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Format date fails on row 3
format_date(joss_pubs_df["published_date"][2])
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Format date runs fine on row 14
format_date(joss_pubs_df["published_date"][13])
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### How to apply functions to DataFrame values: `pandas.apply()` 

The `pandas.apply()` method allows you to apply any function to rows or columns in a `pandas.DataFrame`. For example, you can use it to perform operations on specific column or row values. When you use `.apply()`, you can specify whether you want to apply the function across columns `(axis=0)` (the default) or across rows `(axis=1)`. 

For example, if you want to apply a function to each row of a DataFrame, you would use `df.apply(your_function, axis=1)`. This function is especially useful for applying logic that can’t be easily achieved with built-in pandas functions, allowing for more flexibility in data processing.

You can use `.apply` in pandas to efficiently replace `for loops` to process row and column values in a `pandas.DataFrame`.

```python
# Apply the format_date function to every row in the published_date column
joss_pubs_df['published_date'].apply(format_date)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{tip}
* If you are using Jupyter, then you might [find this page helpful when setting up debugging.](https://jupyterlab.readthedocs.io/en/stable/user/debugger.html)
* VSCODE has a nice visual debugger that you can use.
:::

Important: It is ok if you can't get the code to run fully by the end of this workshop. If you can:

1. identify at least one of the data processing "bugs" (even if you can't fix it) and/or
2. fix at least one bug

You can consider your effort today as a success! 

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Activity 3, part 3 

<!-- This activity might be simpler than the date one?  -->

:::{admonition} Activity 3.3

Your goal in this activity is to generate a list of all package names 
found in the example CrossRef data. Below is a `clean_title` function 
and a small workflow that parses through all titles in the sample data. 

However, the function isn't working as expected. Add checks to 
the `clean_title` function to ensure it correctly extracts the title of each 
package in each publication. 

:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
joss_pubs_df["title"].head(15)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def clean_title(title):
    """Get package name from a crossref title string.

    Parameters
    ----------
    title : str
        The title string containing a package name followed by a colon and description.

    Returns
    -------
    str
        The package name before the colon.

    """
    
    return title[0].split(':')
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Add checks to the clean_title function to make sure this code runs
all_titles = []
for a_title in joss_pubs_df["title"]:
    all_titles.append(clean_title(a_title))
all_titles
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
a = joss_pubs_df["title"][0]
a[0].split(':')
#joss_pubs_df["title"][0]
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# The title value in the first row of the df
print(joss_pubs_df["title"][0])
print(type(joss_pubs_df["title"][0]))
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# The title value unnested from the list
print(joss_pubs_df["title"][0][0])
print(type(joss_pubs_df["title"][0][0]))
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
print(f"The value is {joss_pubs_df['title'][0]}")
get_title(joss_pubs_df["title"][0])
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
clean_title(joss_pubs_df["title"][1])
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## On your own

:::{admonition} On Your Own 1 

If you complete all the activities above, your challenge is fixing the 
workflow below so it runs. To do this you can use the results of the functions that you worked on above. 
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Full code snippet
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
        A date formatted as a `pd.datetime` object.
    """
    date_str = (
        f"{date_parts[0][0]}-{date_parts[0][1]:02d}-{date_parts[0][2]:02d}"
    )
    return pd.to_datetime(date_str, format="%Y-%m-%d")


def clean_title(value):
    """Removes a value contained in a list.

    Parameters
    ----------
    value : list
        A list containing one or more elements.

    Returns
    -------
    Any
        The first element of the list `value`.
    """
    print("hi", value)
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
for json_file in sorted(data_dir.glob("*.json")):
    print(json_file)
    papers_df = load_clean_json(json_file, columns_to_keep)
    papers_df["published_date"] = papers_df["published.date-parts"].apply(
        format_date
    )
    papers_df["title"] = papers_df["title"].apply(clean_title)


    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)

print("Final shape of combined DataFrame:", all_papers_df.shape)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
