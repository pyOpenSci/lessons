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

(clean-code-activity-1)=
# Clean, Modular Code: Activity 1

Writing clean, modular code takes practice but is a habit worth building. Over time as you incorporate clean code strategies that improve code quality and maintainability, these strategies will become second nature. Writing cleaner code will make your code easier to read, maintain, and share with others. It will also make your work easier for others (and your future self) to use. 

In this exercise, you'll focus on using three key clean code strategies:

1. [**Use expressive names**](python-expressive-code): Assign meaningful names to all variables and functions to make your code more readable.
2. [**Use a Python style guide (PEP8) for consistent syntax**](../python-pep-8): Adhere to PEP8 Python code style rules, including proper spacing and naming conventions, to maintain a consistent and readable codebase.
3. **Identify opportunities to [make your code DRY (Don't Repeat Yourself)](../python-dry-modular-code)**: In this activity, you will use pseudocode to identify areas where the code can be simplified and made DRY. In the next activity, you will implement DRY best practices using loops and functions. 

By practicing these strategies, you are well on your way to writing clean, efficient, and maintainable code.

## Activity data 

This activity begins with some code that you "inherited from a former lab mate". This code processes [cross-ref](https://www.crossref.org/) citation data for [The Journal of Open Source Software (JOSS)](https://joss.theoj.org/) publications. The data are pulled directly from the Crossref API but then modified with specific "features" to help you learn better coding practices when completing the activities.

## Your goal 

Your goal is to take the code below and turn it into a script that has the following characteristics:

* The code uses clean, expressive naming conventions
* The code follows the PEP 8 style guide

In this part of the activity, you will create pseudocode to identify:

* How the code could be more DRY. Are elements repeated? 
* How the code could be made more modular.

In the next activity, you will modify the code.

:::{admonition} If you want to use an LLM to support your learning 

The cleanup steps discussed above are things a LLM (Large Language Model) like ChatGPT and Anthropic's Claude can help you with. However, remember that LLMs often return wrong or partially wrong answers. This means that if you use LLMs, you must have a keen eye for catching issues in LLM-generated code.

If you are using a LLM: 

* provide it with descriptive, leading prompts that allow it to perform the task better. So you might write:

> Make the variable names in the code below more expressive.

or

> Identify areas of the code below that could be more DRY. Write [pseudocode](intro-write-pseudocode) that identifies the processing steps that are repeated in the code.


If you use an LLM for this activity, consider adding any odd or incorrect code it returns to our shared workshop document.  
:::

## Your task

The workflow below should open the data stored in the `/data` directory for this activity. The code should run if you have a proper Python environment setup. 

:::{admonition} Part 1: evaluate with a partner 
:class: attention

Examine the code below and address the following questions and statements. 

1. Create a list of any issues that you see with the code.
2. Write down: what is the code supposed to do?
3. Does the code run?
4. Work with your partner to create a list of improvements to make your code more efficient and easier to understand.
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import os
import numpy as np
import json
from glob import glob 
from pathlib import Path
import numpy as np

path="data/part-1-data.json"

with open(path,"r") as z:
    x=json.load(z)
    
import pandas as pd
a=pd.json_normalize(x)

b=['publisher','DOI','type','author','is-referenced-by-count','title', 'published.date-parts']
df=a.filter(items=b)

for i,r in df.iterrows():
    l=r["published.date-parts"][0]
    df.at[i, 'title']=df.at[i, 'title'][0]
    s=f"{l[0]}-{l[1]:02d}-{l[2]:02d}"
    d=pd.to_datetime(s, format='%Y-%m-%d')
    df.at[i, 'published_date']=d

df.drop("published.date-parts",axis=1,inplace=True) 
print(df.shape)

path="data/part-1-datab.json"

with open(path, "r") as z:
    x=json.load(z)

a=pd.json_normalize(x)
b=['publisher','DOI','type','author','is-referenced-by-count','title','published.date-parts']
df2=a.filter(items=b)

for i,r in df2.iterrows():
    l=r["published.date-parts"][0]
    df2.at[i, 'title'] = df.at[i, 'title'][0]
    s=f"{l[0]}-{l[1]:02d}-{l[2]:02d}"
    d=pd.to_datetime(s, format='%Y-%m-%d')
    df2.at[i, 'published_date']=d

df2.drop("published.date-parts",axis=1,inplace=True) 
df_combined = pd.concat([df,df2],axis=0)
df_combined.shape
```

:::{admonition} Part 2: refactor your code
:class: attention

We've taken the code above and copied it to a new notebook cell below for your convenience. Edit the code in that cell to make it:

* PEP8 compliant
* Add expressive names to make it more readable
* Add a docstring to the top of the script to help a user understand what the code does.

You are welcome to work in groups to complete this task!
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
"""Modify this code and make improvements. Good luck!"""
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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{dropdown} Hint 1: built-in help
If you want to look up a pandas function to get help, Jupyter Lab has built-in help.
Enter `help(pd.DataFrame.iterrows)` to see the {meth}`documentation <pandas.DataFrame.iterrows>`.
:::

:::{dropdown} Hint 2: Pandas `itterows` and `at`
What do we expect to happen in the code block with `iterrows`? Iterate through each row of the dataframe and extract the date and title. Try looking up the `at` method in pandas docs. [`at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html) accesses a single value for a row/column label pair.
:::

:::{admonition} Part 3
:class: attention

Evaluate the code to determine whether it could be more DRY. 

* Create a list of items that you notice are repeated and could be cleaned up in the code
* Write [pseudocode](intro-write-pseudocode) that describes what the code intends to do step by step

:::

:::{admonition} On your own 1
:class: tip

Begin to clean up/refactor the code above. In the next activity, we will discuss loops and functions in more detail.
:::
