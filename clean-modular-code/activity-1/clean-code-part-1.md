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

# Clean, Modular Code: Part 1

Below is some code that processes cross-ref citation data for JOSS publications. The data were pulled directly from the cross-ref API but then modified to support this workshop.

## Your goal 
Your goal  is to take the code below and turn it into a script that has the following characteristics:

* The code uses clean, expressive naming conventions
* the code follows the PEP 8 style guide
* The code uses expressive names wherever possible
* The code is DRY - elements in it aren't repeated.
* The code uses principles of modularity.


### If you want to use an LLM to support your learning 

These cleanup steps are all things that a LLn LLM can support you in doing. But remember that if you are using LLMs, they likely will not always give you the right answer—especially on the first, second, even sometimes the third try. 

If you are using an LLM, 

* provide it with descriptive, leading prompts that allow it to better perform the task.
* Be sure to closely check it's work -

The data used in this part of the workshop hasn't been modified; the code below should run. 

Your job is to make it cleaner and more maintainable.

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
