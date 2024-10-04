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

# Part 3 - Tests & Checks for your code

In part 1, you took some code and worked to make it cleaner using expressive variable names. In part 2, you focused on making your code more DRY ("Don't Repeat Yourself"). 

In this section you will learn how to build in checks to your workflow to handle data processing "features". Messy data rarely are perfect when processing. you will most often find unusual data entries and values that you don't expdect. writing robust code that can handle unexpected values will make your code...

Using functions is a great first step to handleing messy data because they rpovide a modular unit that you can test outside of the workflow for the edge cases that you may encounter. Also, because you have funtions you can add elements to them to handle unexpected processing features as you build out your workflow. 

You will learn about using:

* conditional statements
* try/except blocks

## Making checks Pythonic 
The mantra of the zen of python includes :
“Easier to Ask for Forgiveness than Permission”)

this means...

```{code-cell} ipython3
def clean_title(title):
    """Notice that this function checks explicetiy to see if it's a list and then it proesses the data.
    """
    if isinstance(title, list):
        return title[0]
    return title
```

## More "pythonic" - ask for forgiveness 

easier to ask for forgiveness

```{code-cell} ipython3
def clean_title(title):
    """
    It's more pythonic to try first and then ask for forgiveneess later. 
    If you are writing tests this also makes your code easier to test. 
    """
    try:
        return title[0]
    except (TypeError, IndexError):
        return title
```

### Applying functions to dataframe values - .apply 

The `.apply()` function in pandas allows you to apply any function to rows or columns in a `pandas.DataFrame`. For example, You can use it to perform operations on specific column or row values. When you use .apply(), you can specify whether you want to apply the function across columns (axis=0, the default) or across rows (axis=1). For example, if you want to apply a function to each row of a DataFrame, you would use df.apply(your_function, axis=1). This function is especially useful for applying logic that can’t be easily achieved with built-in pandas functions, allowing for more flexibility in data processing.

You can use `.apply` in pandas as an efficient replacement for `for loops` to process row and column values in a df.

```{code-cell} ipython3

```

Examine the code below. 

1. Identify what areas of the code are redundant.
2. Create pseudo code of the steps that are repeatied each time
3. identify sections of the code that could be combined into functions
4. When you are done with the above, refactor the code so that it is cleaner and more modular.

```{code-cell} ipython3
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
    str
        Formatted date string.
    """
    return f"{date_parts[0]}-{date_parts[1]:02d}-{date_parts[2]:02d}"


def clean_title(value):
    """A function that removes a value contained in a list."""
    return value[0]


def process_published_date(date_parts):
    """Parse a date provided as a list of values into a proper date format.

    Parameters
    ----------
    date_parts : str or int
        The elements of a date provided as a list from CrossRef

    Returns
    -------
    pd.datetime
        A date formatted as a pd.datetime object.
    """

    date_str = (
        f"{date_parts[0][0]}-{date_parts[0][1]:02d}-{date_parts[0][2]:02d}"
    )
    return pd.to_datetime(date_str, format="%Y-%m-%d")


columns_to_keep = [
    "publisher",
    "DOI",
    "type",
    "author",
    "is-referenced-by-count",
    "title",
    "published.date-parts",
]

current_dir = Path(__file__).parent
data_dir = current_dir / "data"

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
