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

(clean-code-activity-1)=
# Clean, Modular Code: Activity 1

Writing clean, modular code takes practice but is a habit worth building. Over time as you incorporate clean code strategies that improve code quality and maintainability, these strategies will become second nature. This, in turn, will make your code easier to read, maintain, and share with others. It will also make it easier for others (and your future self) to use. 

In this exercise, you'll focus on three key clean coding strategies:

1. **Use expressive names**: Assign meaningful names to all variables and functions to make your code more readable. [Learn more about expressive names.](../python-expressive-code.md)
2. **Follow PEP8 guidelines**: Adhere to [PEP8 Python code style rules](../python-pep-8.md), including proper spacing and naming conventions, to maintain a consistent and readable codebase.
3. **Identify opportunities to make your code DRY (Don't Repeat Yourself)**: In this activity, you will use pseudocode to pinpoint areas where the code can be simplified and made DRY. In the next activity, you will implement DRY best practices using loops and functions. 

By practicing these strategies, you are well on your way to writing clean, efficient, and maintainable code.

## Activity data 

Below is some code that processes cross-ref citation data for JOSS publications. The data were pulled directly from the cross-ref API but then modified with some specific features to help you learn when completing the activities.

## Your goal 
Your goal is to take the code below and turn it into a script that has the following characteristics:

* The code uses clean, expressive naming conventions
* the code follows the PEP 8 style guide

While you will implement the items below in the next activity, you will create pseudocode in this activity to identify:

* How the code could be more DRY. Are elements repeated? 
* How the code could be more modular. 

### If you want to use an LLM to support your learning 

The cleanup steps discussed above are things an LLM can help you with. However, remember that if you use LLMs, they likely will not always give you the right answer. In fact more often than not, part of the answer is wrong. This means that you need to have a keen eye to catch issues in your code.

If you are using a LLM: 

* provide it with descriptive, leading prompts that allow it to perform the task better. So you might write:

> Make the variables in the code below.

or

> Identify areas of the code below that could be more DRY. Write Pseudocode that identifies the core steps that are repeated.

:::{important}  
If you use an LLM for this activity, be sure to double-check that it works. Add anything you notice it does wrong or oddly to our workshop document.  
:::

## Your task

The workflow below should open the data stored in the data directory for this activity. It should run without issues if you have a proper Python environment setup. 

In part 1, your job is to make the code cleaner, easier to understand and more maintainable.


## Part 1 - evaluate with a partner 

To begin, look at the code. 

* Create a list of any issues that you see with it.
* What is the code supposed to do?
* Does the code run?
* What ideas do you have to make it more efficient? 

```{code-cell} ipython3
import os
import numpy as np
import json
from glob import glob 
from pathlib import Path
import numpy as np

path = "data/part-1-data.json"

with open(path, "r") as z:
    x = json.load(z)
    
import pandas as pd
a=pd.json_normalize(x)

b=['publisher', 'DOI', 'type', 'author','is-referenced-by-count', 'title', 'published.date-parts']
df=a.filter(items=b)

for i,r in df.iterrows():
    l = r["published.date-parts"][0]
    df.at[i, 'title'] = df.at[i, 'title'][0]
    s = f"{l[0]}-{l[1]:02d}-{l[2]:02d}"
    d = pd.to_datetime(s, format='%Y-%m-%d')
    df.at[i, 'published_date'] = d

df.drop("published.date-parts", axis=1, inplace=True) 
print(df.shape)

path="data/part-1-datab.json"

with open(path, "r") as z:
    x=json.load(z)

a=pd.json_normalize(x)
b=['publisher', 'DOI', 'type', 'author','is-referenced-by-count', 'title', 'published.date-parts']
df2=a.filter(items=b)

for i, r in df2.iterrows():
    l=r["published.date-parts"][0]
    df2.at[i, 'title'] = df.at[i, 'title'][0]
    s=f"{l[0]}-{l[1]:02d}-{l[2]:02d}"
    d=pd.to_datetime(s, format='%Y-%m-%d')
    df2.at[i, 'published_date']=d

df2.drop("published.date-parts", axis=1, inplace=True) 
df_combined = pd.concat([df, df2], axis=0)
df_combined.shape
```

## Part 2 

Take the code above and clean it up. Make the code:

* PEP8 compliant
* Add expressive names to make it more readable
* Add a docstring to the top of the script to help a user understand what the code does.


## Part 3

Evaluate the code to determine whether it could be more DRY. 
* Create a list of items that you notice are repeated could be cleaned up in the code
* Write pseudocode that describes what the code intends to do step by step 


## Part 4 

Once you are done with the above, if you have time, begin to clean up the code. We will discuss loops and functions in the next activity in more detail.
