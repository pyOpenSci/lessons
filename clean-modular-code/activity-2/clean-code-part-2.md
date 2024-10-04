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

# Part 2 - Functions & DRY code

In part 1, you took some code and worked to make it cleaner using expressive variable names. In part 2, you will focus on making the code more DRY. 

Remember that DRY refers to "Don't Repeat Yourself". 

You are welcome to use the script you worked on in part 1. Or you can use the cleaned-up script below. 

## Remember the strategies

* Write functions for a task that is performed over and over.
    * Then clearly document what the document does to help your future self or another user understand its intent.
* REMOVE - part 3 Create loops that iterate over repetitive tasks.
* Use conditional statements to control if and when code is executed.
* Use `os` or `pathlib` to create paths to ensure that your code runs across operating systems


## To begin - identify the parts of this code that are redundant 

Create pseudocode (or text) describing the process steps represented in the code below. How could the code be organized differently and more efficiently? 

What tools could make the code more DRY?

## Reproducibility: will this code run on other machines?

One big challenge when considering the reproducibility of workflows is ensuring that your code runs seamlessly on different machines or environments. One key issue is file paths. Hard-coded paths, like "data/part-1-data.json", can lead to errors if the directory structure on another machine differs from your setup. Paths should be constructed dynamically, using tools like Python’s pathlib or environment variables to ensure flexibility across different systems.

+++

### Applying functions to dataframe values - .apply 

The `.apply()` function in pandas allows you to apply any function to rows or columns in a `pandas.DataFrame`. For example, You can use it to perform operations on specific column or row values. When you use .apply(), you can specify whether you want to apply the function across columns (axis=0, the default) or across rows (axis=1). For example, if you want to apply a function to each row of a DataFrame, you would use df.apply(your_function, axis=1). This function is especially useful for applying logic that can’t be easily achieved with built-in pandas functions, allowing for more flexibility in data processing.

You can use `.apply` in pandas as an efficient replacement for `for loops` to process row and column values in a df.

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

Examine the code below. 

1. Identify what areas of the code are redundant.
2. Create pseudo code of the steps that are repeatied each time
3. identify sections of the code that could be combined into functions
4. When you are done with the above, refactor the code so that it is cleaner and more modular.

```{code-cell} ipython3
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

## On your own 1

If you get through the above activity with time to spare, here are a few additional tasks that you can work on. 

1. In this file, the package titles can be found in the title column, as follows:

"package-name: title here." 

Add a component to the code that pulls the package name out from the title column and creates a new column called `package-name`.

1. Then, create a workflow that calculates how many packages in that list are pyOpenSci packages.

to complete this, you will need the `pyos-joss-accepted-packages.csv` file, which has a list of all pyOpenSci packages that have also gone through JOSS review. 

+++

## On your own 2

Create a new workflow that calculates how many packages were submitted to JOSS each month.
