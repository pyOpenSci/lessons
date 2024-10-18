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

(activity-2)=
# Activity 2 - DRY Code & Functions

In [activity 1](../activity-1/clean-code-activity-1), you took some code and made  it cleaner and easier to understand by:

* using expressive variable names, 
* following PEP8 code style guidelines, and
* creating pseudocode as a way to create a plan to clean up the code and make it easier to maintain.  

In this activity, you will make the code [DRY which stands for Don't Repeat Yourself](../python-dry-modular-code). 

You can use the script you worked on in Activity 1 here or the cleaned-up script provided below.

:::{note}
In [activity 3](../activity-3/clean-code-activity-3), you will

* Use conditional statements to control if and when code is executed.
* Add checks to your code
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## The clean code strategies 

In this activity, you will focus on the following clean code strategies:

* **Document:** Document what the code does by adding a docstring at the top of the script to help your future self, a future lab member, or another user understand your code's tasks. Use Numpy-style docstrings when possible. 
* **Modularize** Make your code more modular by adding functions that perform small, repeated tasks. Functions should also have docstrings and expressive names for added readability and usability.
* **Use Loops** Eliminate repetition by using loops that will iterate over specific tasks. In this case, you will iterate over processing several files. 
* **Create dynamic paths:** Dynamic paths ensure that your code will run on other machines regardless of operating system. To achieve this in Python, you can use `os` or `pathlib` to create paths

## To begin - identify redundant parts of this code 

Create pseudocode (or text) describing the process steps represented in the code below. How could the code be organized differently and more efficiently? 

What tools could make the code more DRY?

## Reproducibility: will your code run on other machines?

When considering workflow reproducibility, ensuring that your code runs seamlessly across different machines is important. Hard-coded paths (e.g., `data\part-1-data.json`) can cause errors. For example:

* The path `data/part-1-data.json` is a POSIX path, which works on Mac and Linux machines but will fail on Windows because Windows uses backslashes (`\`) for paths.
* Similarly, a path like `data\part-1-data.json`, written for Windows, will fail on Mac and Linux systems, which expect forward slashes (`/`) in their paths.

To avoid these issues, file paths should be constructed dynamically using tools like Python’s `pathlib`. Using `pathlib` will ensure path compatibility across different operating systems by automatically using the correct path format for the system on which your code is running.

:::{tip} 
* “POSIX” refers to a set of standards for maintaining compatibility between operating systems, and Mac systems are POSIX-compliant.
* You can also use `os.path.join` to create paths; however, using `pathlib` is a more modern and flexible approach. 
:::

```{code-cell} ipython3
import pathlib

# Dynamically generate a path so it will be correct on a Windows vs MAC vs Linux machine
path = pathlib.Path("") / "data" / "data.json"
print(path)
```

```{code-cell} ipython3
data_dir = pathlib.Path("") / "data"

# Use pathlib.path.glob to find all .json files in the 'data' directory
json_files = data_dir.glob("*.json")
for json_file in json_files:
    print(json_file)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Applying functions to `pandas.DataFrame` values - `.apply` 

The `pandas.DataFrame.apply()` function allows you to apply any function to the rows or columns of a `pandas.DataFrame`. You can use it to perform operations on specific column or row values. When using `.apply()`, you can specify whether the function should be applied across columns (`axis=0`, the default) or across rows (`axis=1`).

- To apply a function to each row of a `pandas.DataFrame`, use `df.apply(your_function, axis=1)`.
- To apply a function to a specific column across all rows, use `df["column-name"].apply(your_function)`.

The `.apply()` method in pandas is an efficient way to replace `for` loops for processing row and column values in a `DataFrame`.

In this activity, we encourage you to test out using apply as an efficient way to process data in each cell of a `DataFrame`. An example of using `.apply` is below.

```{code-cell} ipython3
import pandas as pd

# Example DataFrame
df = pd.DataFrame({"A": [1, 10, 3], "B": [4, 5, 15]})

# Function to categorize the sum of columns "A" and "B"
def categorize_sum(row):
    total = row["A"] + row["B"]
    if total > 15:
        return "high"
    else:
        return "low"

# Apply the function to each row
df["category"] = df.apply(categorize_sum, axis=1)
df
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} Activity 2: Part 1
:class: attention

Examine the code in the cell below and do the following: 

1. Identify what areas of the code are redundant.
2. Create pseudocode for the repeated steps; use that pseudocode to clean up the code. Important: Don't skip ahead and write any code yet.
:::

:::{admonition} Activity 2: Part 2
:class: attention

When you are happy with your pseudocode, refactor the code. Refactoring means improving your code’s structure and readability without changing its behavior. It makes the code cleaner, more efficient, and easier to maintain.

1. Identify sections of the code that could be combined into functions
1. When you finish the above, refactor the code so it is cleaner and more modular.

:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This is what the code could look like after part 1. In part 2, 
# you will take this code and make it more DRY.

import json
from pathlib import Path

import pandas as pd

# Use pathlib to ensure your code runs on other machines (assuming relative paths)
# Should we do this in part 2 or part 1??
file_path = Path("data") / "part-1-data.json"

# Load JSON data
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

# Normalize JSON data into a flat table
normalized_data = pd.json_normalize(json_data)

# Define columns to keep
columns_to_keep = [
    "publisher",
    "DOI",
    "type",
    "author",
    "is-referenced-by-count",
    "title",
    "published.date-parts",
]

# Filter the DataFrame by the desired columns
papers_df_1 = normalized_data.filter(items=columns_to_keep)

# Iterate through each row and extract date and title
for index, row in papers_df_1.iterrows():
    date_parts = row["published.date-parts"][0]
    papers_df_1.at[index, "title"] = papers_df_1.at[index, "title"][0]

    formatted_date = f"{date_parts[0]}-{date_parts[1]:02d}-{date_parts[2]:02d}"
    published_date = pd.to_datetime(formatted_date, format="%Y-%m-%d")

    papers_df_1.at[index, "published_date"] = published_date

# Drop the original "published.date-parts" column
papers_df_1.drop("published.date-parts", axis=1, inplace=True)

# Print the shape of the first DataFrame
print(papers_df_1.shape)

# Load and process the second JSON data
file_path_b = "data/part-1-datab.json"

with open(file_path_b, "r") as json_file_b:
    json_data_b = json.load(json_file_b)

normalized_data_b = pd.json_normalize(json_data_b)

# Filter the second DataFrame by the same columns
papers_df_2 = normalized_data_b.filter(items=columns_to_keep)

# Iterate through each row and extract date and title for the second DataFrame
for index, row in papers_df_2.iterrows():
    date_parts_b = row["published.date-parts"][0]
    papers_df_2.at[index, "title"] = papers_df_1.at[index, "title"][0]

    formatted_date_b = (
        f"{date_parts_b[0]}-{date_parts_b[1]:02d}-{date_parts_b[2]:02d}"
    )
    published_date_b = pd.to_datetime(formatted_date_b, format="%Y-%m-%d")

    papers_df_2.at[index, "published_date"] = published_date_b

# Drop the original "published.date-parts" column from the second DataFrame
papers_df_2.drop("published.date-parts", axis=1, inplace=True)

# Concatenate the two DataFrames
combined_papers_df = pd.concat([papers_df_1, papers_df_2], axis=0)

# Print the shape of the combined DataFrame
combined_papers_df.shape
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} On Your Own 1
:class: attention 


If you complete the above activity with time to spare, here are a few additional tasks you can work on. 

In the JSON data that you have been processing, the package titles can be found in the title column as follows: `"package-name: title here."` 

1. Add a processing step to the code that pulls the package name out from the title column and creates a new column called `package-name`.
1. Create a workflow that calculates how many packages in that list are pyOpenSci packages. To calculate how many are pyOpenSci packages,   you will need the `pyos-joss-accepted-packages.csv` file in the `data/` directory with the activity 2 JSON data. This .csv file lists all pyOpenSci packages that have also gone through JOSS review.
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

If you still have time, below is another challenge for you to try!

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{admonition} On Your Own 2
:class: attention 

Create a new workflow that calculates how many packages were submitted to JOSS each month. Add documented functions that process the data. 

:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{dropdown} <i class="fa-solid fa-eye"></i> TODOs-- Click to expand dropdown

Hidden content

* TODO: add drop-downs with answers to each of the OYOs.
:::
