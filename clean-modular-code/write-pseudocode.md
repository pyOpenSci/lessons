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
:hideCode: false
:hidePrompt: false

---
layout: single
title: "Learn to Write Pseudocode for Python Programming"
excerpt: "Pseudcode can help you design data workflows by listing the individual workflow steps in plain language, so the focus is on the overall data process rather than on the specific code needed. Learn best practices for writing pseudocode for data workflows."
last_modified: 
---
```

# Introduction to Pseudocode

## Design an Efficient Data Workflow Using Pseudocode

:::{admonition} What you'll learn
:class: note

* Be able to approach a coding task with a modular, systematic approach. 
* Be able to write pseudocode.
:::

Pseudocode is an informal way of planning and structuring your code logic without worrying about the syntax of a specific programming language. It focuses on clearly expressing the steps a program will take to solve a problem. Writing pseudocode before diving into actual code helps clarify your thought process, spot logical gaps, and communicate your ideas to others.

## Benefits of Pseudocode
1. **Clarifies logic**: Helps you outline your program’s structure without getting bogged down by syntax.
2. **Easier collaboration**: Allows you to communicate ideas with people in different roles, in different scientific domains, or across different programming languages.
3. **Quick debugging**: Spot logical errors early before writing actual code.

## Using Pseudocode with LLMs

LLMs (like ChatGPT) can assist in converting pseudocode into actual Python code. By writing clear pseudocode, you can prompt the LLM to generate Python code that follows your logic, helping you focus on problem-solving and testing the generated code rather than obscure syntax.

## Example: Processing CrossRef Data from JOSS Papers

You have inherited the code below, it's quite messy and hard to read 



```{code-cell} ipython3
from datetime import datetime

# example list of papers with nested title, citations, and weird date format
ps = [
    {"title": ["P1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["P2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["P3"], "pub_date": "2021/03/15", "citations": [8]},
]

# process each paper manually 
# P1
p = ps[0]
if p["citations"]:
    pd1 = datetime.strptime(p["pub_date"], "%Y/%m/%d")
    a = sum(p["citations"]) / len(p["citations"])
    print({"tit": p["title"][0],"pd":pd1,"a":a})

# P2
x = ps[1]
if x["citations"]:
    pd2 = datetime.strptime(x["pub_date"], "%Y/%m/%d")
    y = sum(x["citations"]) / len(x["citations"])
    print({"t":x["title"][0],"pd":pd2,"y":y})

# P3
z = ps[2]
if z["citations"]:
    p3 = datetime.strptime(z["pub_date"],"%Y/%m/%d")
    z_avg = sum(z["citations"]) / len(z["citations"])
    print({"ttl":z["title"][0],"pdate":p3,"z_avg":z_avg})
```



### Step 1: Write Pseudocode
Suppose you want to write a Python function that processes JSON data of JOSS papers from CrossRef, filtering out papers without valid DOIs and calculating citations per month.

Here’s how you can start with pseudocode:

1. Load JSON data of JOSS papers from CrossRef.
2. Loop through each paper.

    * ✅ Check if the DOI is valid.

    * ✅ If valid, extract the number of citations and the publication date

    * ✅ Calculate the number of citations per month since the publication date.
   
3.	Store results in a list.
4.	Return the list of processed data.


+++

### Step 2: Generate Python Code Using LLMs

Now, you can prompt an LLM to convert this pseudocode into Python. Or you could begin to code up the workflow yourself. 

For the LLM, you could input:

> "Write a Python workflow that processes a list of Python dictionaries containing cross-ref citation data. for each list that loads JSON data of JOSS papers, checks for valid DOIs, calculates citations per month since the publication date, and returns the results in a list."

Based on this, the LLM might generate Python code like this:

## Add Multiple data files to your workflow

Above you begin to think about the steps associated with creating a workflow for a single list of dictionaries.  

Using pseudocode helps you think through your logic clearly, while LLMs can assist by generating Python code based on your structure. This process is especially helpful when working on tasks like processing JOSS CrossRef data, where filtering, extracting, and calculating values are essential steps.

```{code-cell} ipython3

```

By following pep8 style and using expressive names, the code becomes easier to read. Expressive naming can act like documentation,

```{code-cell} ipython3
from datetime import datetime

# Example list of papers with nested title, citations, and unusual date format
papers = [
    {"title": ["Paper 1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["Paper 2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["Paper 3"], "pub_date": "2021/03/15", "citations": [8]},
]

# Process each paper manually
# Paper 1
paper_1 = papers[0]
if paper_1["citations"]:
    pub_date_1 = datetime.strptime(paper_1["pub_date"], "%Y/%m/%d")
    avg_citations_1 = sum(paper_1["citations"]) / len(paper_1["citations"])
    print({
        "title": paper_1["title"][0],
        "pub_date": pub_date_1, 
        "citations": citations_1
    })

# Paper 2
paper_2 = papers[1]
if paper_2["citations"]:
    pub_date_2 = datetime.strptime(paper_2["pub_date"], "%Y/%m/%d")
    avg_citations_2 = sum(paper_2["citations"]) / len(paper_2["citations"])
    print({
        "title": paper_2["title"][0],
        "pub_date": pub_date_2,       
        "citations": citations_2
    })

# Paper 3
paper_3 = papers[2]
if paper_3["citations"]:
    pub_date_3 = datetime.strptime(paper_3["pub_date"], "%Y/%m/%d")
    avg_citations_3 = sum(paper_3["citations"]) / len(paper_3["citations"])
    print({
        "title": paper_3["title"][0],
        "pub_date": pub_date_3,  
        "citations": citations_3
    })
```

The above workflow has easier-to-read variable names. Unfortunately, it's also a great example of "copy pasta" code, which is repeated code. 

You could write pseudocode to identify the core steps like this:

1. Open each citation entry in a Python list. It will be in `dict` format. For each citation  
    1. Get the paper's publication date & turn it into a `datetime` object
    1. Get the total citations the paper has
    2. Add data to a pandas dataframe
2. Calculate the mean citation number for all papers

+++

The above pseudo code could be passed to a llm (with more details about how you want it to create the code). 

You could also begin to translate it into Python code like this:


1. Loop through and access each citation dictionary in the Python list. For each citation:  
    1. Get the paper's publication date & turn it into a `datetime` object
    1. Get the total citations the paper has
    2. Add data to a pandas dataframe
2. Calculate the mean citation number for all papers

```{code-cell} ipython3
from datetime import datetime

# Example list of papers with nested fields
papers = [
    {"title": ["Paper 1"], "pub_date": "2023/05/10", "citations": [5]},
    {"title": ["Paper 2"], "pub_date": "2022/04/12", "citations": [3]},
    {"title": ["Paper 3"], "pub_date": "2021/03/15", "citations": [8]},
]

# Process papers in a loop
for paper in papers:
    if paper["citations"]:
        pub_date = datetime.strptime(paper["pub_date"], "%Y/%m/%d")
        avg_citations = sum(paper["citations"]) / len(paper["citations"])
        print({
            "title": paper["title"][0],  # Cleaning step
            "pub_date": pub_date,        # Parsed datetime
            "avg_citations": avg_citations
        })
```

You have now designed a workflow using pseudocode to process several sites worth of landsat data. 

Of course, the pseudocode above is just the beginning. For each of the steps above, you need to flesh out how you can accomplish each task. 

The next lesson in this chapter focuses on data workflow best practices that can help you implement your workflow efficiently and effectively.
