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

* In [activity 1](../activity-1/clean-code-activity-1), you made your code cleaner and more usable using [expressive variable names](python-expressive) and docstrings to document the module. 
* In [activity 2](../activity-2/clean-code-activity-2), you made your code more DRY ("Don't Repeat Yourself") using documented [functions](write-functions) and [conditionals](python-conditionals). 

In this activity, you will build checks into your workflow using [try/except](try-except) blocks added to functions to handle data processing "features".

:::{admonition}
A data feature, as defined here, represents unexpected values that may be found in real-world data. You will rarely find that your data can be processed without some cleaning steps! 
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Real world data processing & workflows and edge cases 

Real-world data can rarely be imported without cleanup steps. You will often find unusual data values you don't expect. Sometimes, these values are documented--for example, a `9999` may represent a missing value in a dataset. And sometimes, that missing value is documented for you. Yay! 

Other times, the data contains undocumented typos and other errors that you need to handle in your code. In this activity, you will see these unusual values referred to as data "edge cases."  

Writing robust code that handles unexpected values will make your code run smoothly and fail gracefully. This type of code, which combines functions (or classes) and checks within the functions that handle messy data, will make your code easier to maintain.

### Strategies for handling messy data

There are several strategies that you can employ to handle unusual data values. In this activity, you will apply the following strategies to make your code more robust, maintainable & usable:


* **[conditional statements](../checks-conditionals/python-conditionals)** 
  to check for specific conditions before executing code. This allows you to create different pathways for code to execute based on specific conditions.
* **[Try/except blocks](../checks-conditionals/python-function-checks)** allow 
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
 
## Functions, classes, and methods are your secret data science tool for handling messy data

Using functions and class methods is a great first step in handling messy data. A function or method provides a modular unit you can test outside the workflow for the edge cases you may encounter. Also, because a function is a modular unit, you can add elements to handle unexpected processing features as you build your workflow.

Once you have these functions and methods, you can add checks using conditional statements and [try/except](try-except) blocks that anticipate edge cases and errors that you may encounter when processing your data. 

<!-- This last paragraph might belong in the function checks lesson vs. here?  -->

## Clean up your workflow
The code below is an example of what your code might look like after completing [Activity 2](activity-2). If you run the code below, you will notice that it fails when processing the data.

Your goal


Using the `published` key in the JSON file for each publication:

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

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
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
    date_str = (
        f"{date_parts[0][0]}-{date_parts[0][1]:02d}-{date_parts[0][2]:02d}"
    )
    return pd.to_datetime(date_str, format="%Y-%m-%d")


def clean_title(value):
    """A function that removes a value contained in a list."""
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
for json_file in data_dir.glob("*.json"):
    papers_df = load_clean_json(json_file, columns_to_keep)
    papers_df["published_date"] = papers_df["published.date-parts"].apply(
        format_date
    )
    papers_df["title"] = papers_df["title"].apply(clean_title)


    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)

print("Final shape of combined DataFrame:", all_papers_df.shape)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Activity 1: Part 1

The code below creates a `pd.DataFrame` with the first 15 publications in the JOSS sample data.json file. This is the first of 3 files that you need to process in your workflow.

Your first task is to process and reformed the published_date column in the data to make it a `pandas.datetime` object.H aving a date in a useful format will allow you to do further analysis later such as counting publications by month and year! 

The function that you should focus on here is:


In small groups, do the following:

1. Evaluate the `published_date` field in the data created below and answer the question: 

* Do you see any unusually formatted values that may be responsible for making your code above fail?

:::{tip}
Using `DataFrame.head(7)` and `DataFrame.tail(number_of_rows_here)` will be helpful as you troubleshoot the data. 
:::

2. Once you have a list of issues you observe in the data, address them by modifying the `format_date` function below.

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["hide-output", "hide-cell"]}

In this activity, you will be working with Pandas `DataFrames`. You may find the `.apply` function to be particularly useful. 

### How to apply functions to DataFrame values: `pandas.apply()` 

The `pandas.apply()` method allows you to apply any function to rows or columns in a `pandas.DataFrame`. For example, you can use it to perform operations on specific column or row values. When you use `.apply()`, you can specify whether you want to apply the function across columns `(axis=0)` (the default) or across rows `(axis=1)`. 

For example, if you want to apply a function to each row of a DataFrame, you would use `df.apply(your_function, axis=1)`. This function is especially useful for applying logic that can’t be easily achieved with built-in pandas functions, allowing for more flexibility in data processing.

You can use `.apply` in pandas to efficiently replace `for loops` to process row and column values in a `pandas.DataFrame`.

:::{tip} Formatting dates with Pandas
:class: tip

What Does 02d Mean?

	•	d: This part of the format code means you’re expecting an integer. It tells Python to format the value as a decimal (whole number).
	•	02: The 02 means that the number should be padded with leading zeros if necessary, so the total width is 2 digits. For example:
	•	1 becomes 01
	•	5 becomes 05
	•	12 stays as 12 (no padding needed)

This is especially useful for formatting months or days, which often need to be in a MM-DD format (e.g., 01-05 for January 5th).
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import pandas as pd

# Manually create the data for the first 15 entries
data = [
    {
        "title": ["bmiptools: BioMaterials Image Processing Tools"],
        "published_date": [["2022", "11", "27"]],
        "citations": 2,
        "doi": "10.21105/joss.04859"
    },
    {
        "title": ["QuasinormalModes.jl: A Julia package for computing discrete eigenvalues of second order ODEs"],
        "published_date": [[2022, "5", 25]],
        "citations": 2,
        "doi": "10.21105/joss.04077"
    },
    {
        "title": ["CWInPy: A Python package for inference with continuous gravitational-wave signals from pulsars"],
        "published_date": [[2022, 9, 29]],
        "citations": 3,
        "doi": "10.21105/joss.04568"
    },
    {
        "title": ["Nempy: A Python package for modelling the Australian National Electricity Market dispatch procedure"],
        "published_date": [[""]],
        "citations": 2,
        "doi": "10.21105/joss.03596"
    },
    {
        "title": ["Spectral Connectivity: a python package for computing spectral coherence and related measures"],
        "published_date": [[]],  # No date available
        "citations": 3,
        "doi": "10.21105/joss.04840"
    },
    {
        "title": ["SEEDPOD Ground Risk: A Python application and framework for assessing the risk to people on the ground from uncrewed aerial vehicles (UAVs)"],
        "published_date": [["2022", "3", ""]],
        "citations": 1,
        "doi": "10.21105/joss.04079"
    },
    {
        "title": ["DIANNA: Deep Insight And Neural Network Analysis, explainability in time series"],
        "published_date": [[2022, 12, 15]],
        "citations": 1,
        "doi": "10.21105/joss.04493"
    },
    {
        "title": ["diman: A Clojure Package for Dimensional Analysis and Unit Checking"],
        "published_date": [[2022, 1]],
        "citations": 0,
        "doi": "10.21105/joss.03735"
    },
    {
        "title": ["PERFORM: A Python package for developing reduced-order models for flow simulation"],
        "published_date": [[9999]],
        "citations": 3,
        "doi": "10.21105/joss.03428"
    },
    {
        "title": ["TLViz: Visualising and analysing tensor decompositions"],
        "published_date": [[2022, 11, 25]],
        "citations": 2,
        "doi": "10.21105/joss.04754"
    },
    {
        "title": ["ALUES: R package for Agricultural Land Use Evaluation System"],
        "published_date": [[2022, 5, 12]],
        "citations": 1,
        "doi": "10.21105/joss.04228"
    },
    {
        "title": ["Spiner: Performance Portable Routines for Generalized SpMV and Triangular Solvers"],
        "published_date": [[2022, 7, 5]],
        "citations": 0,
        "doi": "10.21105/joss.04367"
    },
    {
        "title": ["pyndl: Naïve Discriminative Learning in Python"],
        "published_date": [[2022, 12, 15]],
        "citations": 0,
        "doi": "10.21105/joss.04515"
    },
    {
        "title": ["HostPhot: global and local photometry of galaxies"],
        "published_date": [[2022, 8, 15]],
        "citations": 1,
        "doi": "10.21105/joss.04508"
    },
    {
        "title": ["QMKPy: A Python Testbed for the Quadratic Multichannel Kalman Filter"],
        "published_date": [[2022, 11, 2]],
        "citations": 0,
        "doi": "10.21105/joss.04718"
    }
]

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

joss_pubs_df = pd.DataFrame(joss_pubs)
joss_pubs_df.tail(7)
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
    # This print statement might also help you identify the issue!
    print(date_parts)
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
df['published_date'].apply(format_date)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### What's changed in your workflow?

:::{warning}
You have a new data file to open in your list of `.json` files in this activity. This file has some unexpected "features" that your code needs to handle gracefully to process all of the data.
:::

The code below is an example of what your code might look like after completing [activity 2](../activity-2/clean-code-activity-2). You can choose to work with this code, or you can use the code that you completed in activity 2. 

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

You can consider your effort today as a success! We will work on the first element together as a group.

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["raises-exception"]}

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
    date_str = (
        f"{date_parts[0][0]}-{date_parts[0][1]:02d}-{date_parts[0][2]:02d}"
    )
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
        format_date
    )

    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)

print("Final shape of combined DataFrame:", all_papers_df.shape)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} Part 1 - What happens when your code can't find the data?
:class: attention

Let's break the code below and see how our code performs. 

* Note that the code below has a modified `/data` directory path (that doesn't exist!).

Questions:
* What type of error do you expect Python to throw? Use Google, LLMs or our [tests and checks](common-exceptions) lesson to help figure this out. 
* Does your code handle this error gracefully?
* How can we make the code handle it better?

```python
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

    # Return the pandas DataFrame, filtering out some of the columns that we don't need
    return normalized_data.filter(items=columns_to_keep)


columns_to_keep = [
    "publisher",
    "DOI",
    "type",
    "author",
    "is-referenced-by-count",
    "title",
    "published.date-parts",
]

# Break this data path by giving it a dir name that doesn't exist - what happens when your code runs?
data_dir = Path("bad-bad-data")

all_papers_list = []
for json_file in data_dir.glob("*.json"):
    papers_df = load_clean_json(json_file, columns_to_keep)
    papers_df["title"] = papers_df["title"].apply(clean_title)

    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)

print("Final shape of combined DataFrame:", all_papers_df.shape)
```

Your goal is to troubleshoot any issues associated with cleaning up the title so you can work with it later in a `pandas.DataFrame`.

:::

+++ {"editable": true, "slideshow": {"slide_type": ""}, "tags": ["hide-cell"]}

Note: we can have two groups - one that wants to work on their own and another that wants to work with the instructor together.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} Activity 3: part 1 
:class: attention

In this activity, we will work together in groups or as a whole class to add a try/except block that handles messiness when parsing titles in the cross-ref data. 

:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} On your own 1
:class: attention

If you get through the activity above and want a second challenge, try to parse the date values for each JOSS publication. Use the published key to extract the date for each publication. You may run into some data "features" when completing this activity. 

```json
"published": {
      "date-parts": [
        [
          2020,
          7,
          4
        ]
      ]
```

:::

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
