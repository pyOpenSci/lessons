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

```{raw-cell}
---
editable: true
hideCode: false
hidePrompt: false
raw_mimetype: ''
slideshow:
  slide_type: ''
---
---
layout: single
title: "Learn to Write Pseudocode for Python Programming"
excerpt: "Pseudcode can help you design data workflows by listing the individual workflow steps in plain language, so the focus is on the overall data process rather than on the specific code needed. Learn best practices for writing pseudocode for data workflows."
last_modified: 
---
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(intro-write-pseudocode)=
# Introduction to Pseudocode

:::{admonition} What you'll learn
:class: note

* Be able to approach a coding task with a modular, systematic approach. 
* Be able to write pseudocode.
:::

Writing pseudocode is a powerful tool that you can use to plan, organize, and structure your code without worrying about the syntax of a specific programming language or the specific steps. Writing pseudocode helps you focus on clearly expressing the logical steps that your code needs to perform to process your data. 

Writing pseudocode before diving into actual coding will help you write better code from the start and hopefully reduce the number of times your code gets refactored or rewritten. 

## Benefits of Pseudocode

1. **Clarifies logic**: Helps you outline your code’s structure without getting bogged down by specific syntax.
2. **Easier collaboration**: Allows you to communicate your plan for designing a workflow with people in different roles (if you are working collaboratively), in different scientific domains, or across different programming languages.
3. **Quick debugging**: You can often quickly identify problem areas or logical errors when writing pseudocode and consider how to address them before writing actual code. This will save you time!

## Using pseudocode with LLMs

LLMs (like ChatGPT) can assist in converting pseudocode into actual Python code. By writing clear pseudocode, you can prompt the LLM to generate Python code that follows your logic, helping you focus on problem-solving and testing the generated code rather than obscure syntax.

## Example: processing Crossref data from JOSS papers

You have inherited the code below; it's quite messy and hard to read

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from datetime import datetime

# Example list of papers with nested title, citations, and weird date format
ps = [
    {"title": ["P1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["P2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["P3"], "pub_date": "2021/03/15", "citations": [8]},
]

# Process each paper manually

# P1
p = ps[0]
if p["citations"]:
    pd1 = datetime.strptime(p["pub_date"], "%Y/%m/%d")
    cit1 = p["citations"][0]  # Access first element directly
    print({"tit": p["title"][0], "pd": pd1})

# P2
x = ps[1]
if x["citations"]:
    pd2 = datetime.strptime(x["pub_date"], "%Y/%m/%d")
    cit2 = x["citations"][0]  # Access first element directly
    print({"t": x["title"][0], "pd": pd2})

# P3
z = ps[2]
if z["citations"]:
    p3 = datetime.strptime(z["pub_date"], "%Y/%m/%d")
    cit3 = z["citations"][0]  # Access first element directly
    print({"ttl": z["title"][0], "pdate": p3})

# Manually calculate the mean number of citations
total_citations = cit1 + cit2 + cit3
mean_citations = total_citations / 3

print(f"Mean number of citations: {mean_citations}")
```

Before tackling the code above, break things down a bit using English rather than Python! The goal of the code above is to process citation data. In this case, you have a list of dictionaries to process. 

### Step 1: Write pseudocode

In the code above, each dictionary is processed individually. 

Ask yourself:
1. What steps are repeated in the code above?
1. Is there a better way to process the data more efficiently?

Your pseudocode might look something like this:

```md
Open a list of Python dictionary objects.
Process the data in each list:
    * Extract the date
    * Extract the number of citations
    * Store the data in some format that makes it easier to process(don't print it)
```

### Step 2: generate pseudocode that begins to consider Python syntax 

Next, you can choose whether you want to write cleaner Python code yourself or generate your code using an LLM. Below, you begin to flesh out the pseudocode, considering the types of Python data structures that might be most useful for storing the data.  

In this case, Pandas is a great option because it has a built-in mean method and handles tabular data well. 


```md
Open a list of Python dictionary objects.
Create a Python loop to process the data in each list:
* Extract the date
* Extract the number of citations
* Add the cleaned data to a list
Turn the list into a Pandas DataFrame
Calculate mean citations
```

### Step 3: refine your pseudocode further 

Now that you have pseudocode, you can begin to fill in the code gaps! 
Keep your pseudocode steps. Add the code required to perform each step.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from datetime import datetime

# Example list of papers with nested title, citations, and weird date format
pubs = [
    {"title": ["P1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["P2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["P3"], "pub_date": "2021/03/15", "citations": [8]},
]

# It's straightforward to convert a list to a DataFrame.
# Create / initialize an empty list

all_pubs = []
# Create a Python loop to process each publication the list
for pub in pubs:
    # * Extract the date and add print statements for checks
    pub_date = datetime.strptime(pub["pub_date"], "%Y/%m/%d")
    print(pub_date)
    # * Extract the number of citations
    citation_count = pub["citations"][0]
    print(citation_count)
    # * Add the cleaned data to a list
    all_pubs.append({"pub_date": pub_date, "citation_count": citation_count})
    print(all_pubs)
# Turn the list into a Pandas DataFrame
# Calculate mean publications using pandas.mean
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Based on the above, you can begin to clean up your workflow even further. You no longer need print statements.

:::{tip}
It can also be helpful to use a code formatter as you go to keep your code consistent. 
If you are working in Jupyter Lab, [Jupyter Lab code formatter is a great option.](https://jupyterlab-code-formatter.readthedocs.io/).
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from datetime import datetime

# Example list of papers with nested title, citations, and weird date format
pubs = [
    {"title": ["P1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["P2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["P3"], "pub_date": "2021/03/15", "citations": [8]},
]

all_pubs = []
for pub in pubs:
    pub_date = datetime.strptime(pub["pub_date"], "%Y/%m/%d")
    citation_count = pub["citations"][0]

    all_pubs.append({"pub_date": pub_date, "citation_count": citation_count})

# Turn the list into a Pandas DataFrame
all_pubs_df = pd.DataFrame(all_pubs)
all_pubs_df.head()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Calculate mean publications using pandas.mean
mean_citations = all_pubs_df["citation_count"].mean()
mean_citations
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

:::{dropdown}
Using the above pseudocode, ChatGPT provided the following code.
```python
from datetime import datetime
import pandas as pd

def extract_data(papers):
    """
    Extract publication date and number of citations from a list of papers.

    Parameters
    ----------
    papers : list of dict
        List of paper dictionaries containing 'title', 'pub_date', and 'citations'.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the extracted information.
    """
    processed_data = []

    for paper in papers:
        if paper["citations"]:
            pub_date = datetime.strptime(paper["pub_date"], "%Y/%m/%d")
            citations = paper["citations"][0] 
            processed_data.append({
                "title": paper["title"][0],
                "publication_date": pub_date,
                "citations": citations
            })

    return pd.DataFrame(processed_data)

# Example list of papers with nested title, citations, and date format
papers = [
    {"title": ["P1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["P2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["P3"], "pub_date": "2021/03/15", "citations": [8]},
]

# Extract the data into a DataFrame
processed_papers = extract_data(papers)

# Example of further processing or analysis (without printing)
# e.g., Calculate the mean number of citations
mean_citations = processed_papers["citations"].mean()

# Store processed data and mean citations for further analysis
processed_data_store = {
    "processed_papers": processed_papers,
    "mean_citations": mean_citations
}
```
:::

+++

### You now have a cleaner, working script!

By following the above steps, you now have a clean working workflow that you can 
adapt and refactor even further. Let's pretend that you know you will need to 
add two things to your workflow:

* You know that your data is doing to be in a JSON file, rather 
than provided to you as a Python dictionary. 
* You also know that you will need to process multiple files. 

Have a look at the code below, consider using pseudocode to identify areas that you could 
clean up even further to support a multi-file workflow.

```{code-cell} ipython3
from datetime import datetime

# Open the data in .JSON format rather than via an example 
pubs = [
    {"title": ["P1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["P2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["P3"], "pub_date": "2021/03/15", "citations": [8]},
]
# if there are multiple files, I will need a processing step for each file
all_pubs = []
for pub in pubs:
    # Could this step be a function or multiple functions that cleans the data?
    pub_date = datetime.strptime(pub["pub_date"], "%Y/%m/%d")
    citation_count = pub["citations"][0]
    all_pubs.append({"pub_date": pub_date, "citation_count": citation_count})

all_pubs_df = pd.DataFrame(all_pubs)
mean_citations = all_pubs_df["citation_count"].mean()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Add Multiple data files to your workflow

Above you begin to think about the steps associated with creating a workflow for a single list of dictionaries.  

Using pseudocode helps you think through your logic clearly, while LLMs can assist by generating Python code based on your structure. This process is especially helpful when working on tasks like processing JOSS CrossRef data, where filtering, extracting, and calculating values are essential steps.

```{code-cell} ipython3

```
