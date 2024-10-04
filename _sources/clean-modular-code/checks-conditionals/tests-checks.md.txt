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

+++ {"id": "d8b23008", "editable": true, "slideshow": {"slide_type": ""}}

# Tests, Checks & Failing Gracefully

:::{todo}
2. Add a section using dictionaries as examples (maybe where I talk about list comprehensions), as this will avoid key errors.
3. add a section on different types of Python errors to think about
::: 

Adding tests and checks to your Python code, in the form of:

* try-except blocks, and
* conditional statements,

helps you write code that can: 

* Better handle errors and edge cases gracefully, and
* Provide useful output about why things are going wrong for a user of your code.

Tests and checks allow your code to either continue processing when it encounters an issue or fail in a controlled and graceful way. They can also provide useful error messages that help users debug the problem. 

Adding checks to your code is crucial for maintaining robust, reliable code.

## What you will learn here  

In this interactive lesson, you will learn how to create a workflow that: 

1. Incorporates the clean code best practices you learned in the previous lessons, including following Pep 8 style standards, writing expressive code, and making your code DRY and modular.
2. Adds tests and checks using Python `try/except` blocks to capture common errors in the code.

By the end of this lesson, you will have a script that runs a workflow combined with a small module that contains functions that you can use to create a Python package. 


### Types of checks

You can add checks to your workflow that either:

1. continue processing the code even when it encounters a problem or
2. fail gracefully in a way that you can see what went wrong

Below you will develop a workflow that parses software and journal paper DOI (Digital Object Identifiers) in URL format and returns reference information for each published entity. 

Most of the DOIs on this page represent pyOpenSci packages that have also been reviewed by the [Journal of Open Source Software](https://joss.theoj.org/).

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Some common errors that you will see 

Python has dozens of specific errors that can be raised when code fails to run. Understanding what the error codes mean is helpful for both troubleshooting code and also adding checks to your code to address specific errors. 

Below are a few of the common errors that Python can raise.
	
### TypeError

Occurs when an operation is applied to an object of an inappropriate type.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Example: Trying to add a number and a string
1 + 'string'  # This will raise a TypeError
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### ValueError

- **Raised when** a function receives an argument of the right type but an invalid value.
- **Example:** `int('abc')` (trying to convert an invalid string to an integer).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
int('abc') 
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### KeyError

- **Raised when** a dictionary key is not found.
- **Example:** `my_dict['nonexistent_key']` (trying to access a key that doesn’t exist in the dictionary).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Example: Accessing a nonexistent key in a dictionary
my_dict = {"a": 1, "b": 2}
my_dict['nonexistent_key']
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### IndexError:

- **Raised when** an invalid index is used to access a list or tuple.
- **Example:** `my_list[10]` (trying to access the 11th element of a list with fewer elements).

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
my_list = [1, 2, 3]
my_list[10] 
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### AttributeError:

Raised when an object does not have a specific attribute or method.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
my_string = "Hello"
my_string.nonexistent_method()
```

```{code-cell} ipython3
---
editable: true
id: 1f1c256a
slideshow:
  slide_type: ''
---
import pandas as pd
from habanero import Crossref
```

+++ {"id": "69cfa634"}

The **.csv file** that you read in contains a list of doi urls.

```{code-cell} ipython3
---
editable: true
id: '80167539'
slideshow:
  slide_type: ''
---
# Open the data
file_path = "doi_urls.csv"
doi_df = pd.read_csv(file_path)
doi_df.head(2)
```

+++ {"id": "58d03c6f", "editable": true, "slideshow": {"slide_type": ""}}

In this lesson, you will build a workflow around citable published software. You will use a pre-created dataset that contains cross-ref citations for open source software reviewed by the Journal of Open Source Software (JOSS). 

:::{important}
All the data used in this lesson can be accessed using Python using the Habanero package. However, you will be using a pre-processed dataset containing some "features" that you will have to work around to successfully process your data. 
:::

## About DOI's

:::{admonition} What is a DOI?
A DOI, or [Digital Object Identifier](https://www.doi.org/), is a unique identifier that references a paper. A DOI acts as a URL, resolving to a specific location—in this case, the location is associated with citation information for a scientific paper or Python package that has been accepted into a journal such as the [Journal of Open Source Software (JOSS)](https://joss.theoj.org/).

In this lesson, you use cross-ref DOIs, which resolve to the cross-ref database. Cross-ref also lets you see what other publications have cited for that specific DOI. 
:::

```{code-cell} ipython3
---
editable: true
id: d3738f2a
slideshow:
  slide_type: ''
---
doi_df["doi_url"][0]
```

+++ {"id": "37ef78f8"}

## Create a workflow that processes a list of DOi's 

In this lesson, you will process a list of DOIs contained in a .csv file for pyOpenSci-accepted packages that both pyOpenSci and JOSS have also accepted through our software peer review partnership. 


### Workflow goals 
Your goal is to process all of the URLs in the citation file and get both the author(s) and titles of the reference. You then want to return the following values:

1. the authors of the paper
2. the paper title
3. the number of references the paper has

Like any URL, not all DOIs will resolve properly. 

You will use Pandas to read the .csv file with the DOI. You will then use the [habanero](https://habanero.readthedocs.io/en/latest/) package to parse that cross-ref DOI and return metadata about the published item. 

Below you open the data for a single DOI. Notice that the citation data for that DOI is to Python and stored as a `Dictionary.`

There is a lot of information to process. Luckily, for your work today, you only need to process a few items in this dataset.

```{code-cell} ipython3
---
editable: true
id: 38b2d444
slideshow:
  slide_type: ''
---
cr = Crossref()
# Grab a single doi
url = doi_df["doi_url"][0]
# View reference information for that DOI
ref_dict = cr.works(ids=url)
ref_dict.keys()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
ref_dict["message"]["title"]
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
ref_dict["message"]
```

```{code-cell} ipython3
author_count = len(ref_dict["message"]["author"])
author_count
```

+++ {"id": "495d50c1"}

You can access the specific reference information including journal title, year, author using the `["reference"]` key.

```{code-cell} ipython3
:id: 0b8f76ce-0368-42cf-8299-cb7bd5513664

# View first reference for this citation
ref_dict["message"]["reference"][0]
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
citation_count = len(ref_dict["message"]["reference"])
print(f"The package has {citation_count} citations and {author_count} authors.")
```

+++ {"id": "fc58802d"}

## Process all DOI URLs in the .csv file 

Next, creat a workflow that processes each DOI in your dataframe of DOIs.

```{code-cell} ipython3
---
editable: true
id: 307e4899
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Without the function, your code would look like this:
cr = Crossref()
all_refs = []
for adoi in doi_df["doi_url"]:
    #print(adoi)
    ref_info = cr.works(ids=adoi)
    all_refs.append(all_refs.append(ref_info["message"].get("reference", [])))

all_refs
```

+++ {"id": "bede9522"}

*Oops looks like you have a point of failure.*

## Some issues:

1. Once you hit a point of failure, processing stops.
2. You are not sure where it fails or why

+++ {"id": "c0b639c0"}

## When Workflows Fail
Sometimes your code may fail in certain scenarios. Having checks in place in your code to catch these points of failure can be useful for many reasons:

1. If your workflow is big, it's often time consuming to start over
2. If your workflow is big, it can be challening to identify where the point of failure is and what is causing it.

+++ {"id": "fc26a6b8"}

If you are using LLM's to help you code, you may find that the LLM can't correctly guess the types of errors that you may encounter with downloaded data such as the DOI reference data that you are working with here. However, it can help you create checks for issues that you find in the data if you wish to use it that way. 

Here, you receive a `KeyError` in your code that tells you that the 
The "reference" key for the DOI data can not be found for at least one of your DOIs. 

How can you troubleshoot this?

:::{dropdown}  Tips to troubleshoot your KeyError

There are a few different ways that you can troubleshoot this problem. 

1. A simple way is to add a print statement to your loop to identify what URL it's failing on. You can then look at the data and add a workaround.
2. You can add a breakpoint in your code if you work in an IDE with a debugger. This breakpoint will allow you to identify where the error is occurring.
3. You can add a try/except statement to print out the error but allow your code to keep running. You will learn more about try/except statements below.
4. Add a conditional statement to your look that catches a url with a missing reference key and sets the reference count to `None`.

* debugger in JupyterLab
* debugger using vscode

For this lesson, if you are not already familiar with a debugger, you can add a print statement or an iterator to determine what URL it's failing on. 
:::

## LLM's and error messages 

In some cases, particularly with Python, LLMs can be particularly useful for troubleshooting long error messages.

```{code-cell} ipython3
---
editable: true
id: 01c7443e
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# This returns a key error
url = doi_df["doi_url"][5]
ref_dict = cr.works(ids=url)
# View first reference in dics
ref_dict["message"]["reference"]
```

+++ {"id": "9d67f470"}

## Check To See if the Key Exists

```{code-cell} ipython3
:id: e665aec2

# Does the reference exist in the data?
"reference" in ref_dict["message"].keys()
```

+++ {"id": "0caf5a2b"}

## Write a Function that Checks that the Reference Exists in the Data

```{code-cell} ipython3
:id: 3fa84306

# This will return True if the reference exists, false if not
def check_reference_data(doi):
    """Checks to see if a specific doi has a list of references associated with it

    Parameters
    ----------
    doi : string
        DOI string for a reference

    Returns
    -------
        Boolean : True if exists, False if not
    """

    response = cr.works(ids=doi)
    return "reference" in response["message"].keys()
```

```{code-cell} ipython3
---
editable: true
id: 8c4fea64
slideshow:
  slide_type: ''
---
# Your code is easier to read with a function
cr = Crossref()

for adoi in doi_df["doi_url"]:
    print(adoi)
    print(check_reference_data(adoi))
```

+++ {"id": "b2d59037"}

Your workflow is failing. A
404 error which means that the URL for the doi is bad.

`404 Client Error: Not Found for url: https://api.crossref.org/works/https://doi.org/10.5066/P9MR4XN4`

+++ {"id": "b88e90bb"}

To handle this error, you can consider implementing a try/except block:

* Try will attempt to run something and if it fails, it moves on to the except statement.
* Let's add a try/except statement that returns None is the DOI url can't be accessed

[A Good Carpentry Lesson on try/except](https://mq-software-carpentry.github.io/python-testing/03-exceptions/)

+++ {"id": "f85981c7"}

```
# This is formatted as code
```

A try/except allows  you to try a function or some code
If it doesn't run properly, you can then tell it what  to return instead

```{code-cell} ipython3
:id: 658886e5

try:
    response = cr.works(ids="bad url here")
    print("Great - it runs with a good doi url.")
except:
    # If the function fails to get a return for the DOI, return None
    print("Oops, it didn't work out as planned, did it?")
```

+++ {"id": "d7c26087"}

Here your code runs as planned

```{code-cell} ipython3
:id: 0a9bce89

try:
    response = cr.works(ids=doi_df["doi_url"][2])
    print("Great - it runs with a good doi url.")
except:
    # If the function fails to get a return for the DOI, return None
    print("Oops, it didn't work out as planned, did it?")
```

+++ {"id": "970f0748"}

Add your try/except block to your function

```{code-cell} ipython3
:id: 711c9564

# Add try/except to your function
def check_reference_data_err(doi):
    """
    Checks to see if a specific doi has a list of
    references associated with it
    """

    try:
        response = cr.works(ids=doi)
    except:
        # If the function fails to get a return for the DOI, return None
        return None
    # Otherwise return true or false
    return "reference" in response["message"].keys()
```

+++ {"id": "92315aa6"}

This check in your code allows the code to
continue to run even when it encounters an error!

```{code-cell} ipython3
:id: 09e1bbfc

for adoi in doi_df["doi_url"]:
    print(check_reference_data_err(adoi))
```

+++ {"id": "9e2f519c"}

*italicized text*## Problem: Your Workflow Fails Quietly

What if you wanted to catch and print out the error so that you can
better troubleshoot? For instance, what doi is it failing on?


Notice that below you "catch" the error thrown and print it. What this means
is that you can keep running your code, and the error will be printed bu
it will NOT halt processing.

+++ {"id": "b8ae5d1f"}

## Two options

1. Catch the exception as a generic exception and print out the return.
2. Catch the specific exception (this is more advanced - don't worry about it for now)

```{code-cell} ipython3
:id: fb80796b

# Add an exception that captures the error
def check_reference_data_try_err(doi):
    """Checks to see if a specific doi  has a list of references associated with it"""
    try:
        response = cr.works(ids=doi)
    except Exception as err:
        # Print the error message
        print(err)
        # If the function fails to get a return for the Doi, return None
        return None
    return "reference" in response["message"]
```

```{code-cell} ipython3
:id: 84c4d129

for adoi in doi_df["doi_url"]:
    print(check_reference_data_try_err(adoi))
```

+++ {"id": "db044d20"}

Now, your function returns a 404 error.
But what if the URL was actually NOT a url at all?
Is your code robust enough to tell you that?

```{code-cell} ipython3
:id: dc48062d

# This returns a 404 but there is no URL in the string "Cookies"
check_reference_data_try_err("Cookies")
```

```{code-cell} ipython3
:id: a19f5601

# Mess up one of the url's in your pdf
doi_df["doi_url"][11] = "cookies!"
doi_df
```

+++ {"id": "4d6b4a22"}

##  Test that the URL Begins with "http"

Above you are assuming that the user has provided your function with a URL
however, you could also begin your function with a test to ensure that
the doi provided is in fact a URL.

```{code-cell} ipython3
:id: 1ff93fbe

doi="cake"
if doi.startswith("http"):
    print("Great - this is a proper url")
else:
    print("Sorry, human. I don't see a proper url here.")
```

+++ {"id": "6e5a9408"}

Here you provide a URL:

```{code-cell} ipython3
:id: 431d0b6b

doi="https://www.pyopensci.org"
if doi.startswith("http"):
    print("Great - this is a proper url")
else:
    print("Sorry, human. I don't see a proper url here.")
```

+++ {"id": "4d7c5a1c"}

Add this check to your function. Below the function will now
return a different value if the URL is bad.

```{code-cell} ipython3
:id: a9408f19

# Add an exception that captures the error
def check_reference_data_try_err(doi):
    """Checks to see if a specific doi  has a list of references associated with it"""

    if doi.startswith("http"):
        try:
            response = cr.works(ids=doi)
        except Exception as err:
            print(err)
            # If the function fails to get a return for the Doi, return None
            return None
    else:
        return "Missing Valid URL - " + doi
    return "reference" in response["message"]
```

```{code-cell} ipython3
:id: 3444331e

# Let's try out the final function
for adoi in doi_df["doi_url"]:
    print(check_reference_data_try_err(adoi))
```

+++ {"id": "bfc7f989"}

## On Your Own Challenge
Run the code cell below.
Answer the following questions:

1. What happens when you run the cell below?
2. What could you do to address the issue below?

If you have time, try out some solutions in this notebook.

```{code-cell} ipython3
:id: 473da2a3

check_reference_data_try_err(123)
```

```{code-cell} ipython3
:id: bbb20ca1

# Your answer here
```

```{code-cell} ipython3
# Initialize Crossref API client
cr = Crossref()

# Define the ISSN of JOSS
joss_issn = "2475-9066"

# Fetch DOIs of articles published in JOSS
results = cr.works(filter={"issn": joss_issn}, limit=100) 
#results
```

+++ {"id": "39f64c05-7d33-4123-8781-034c94f3dffc"}

https://github.com/lwasser/usgs-citations

+++

The problem here with LLM's is that they will often provide answers that are only partially correct. The code below was provided on 12 Sept 2024 by ChatGPT 4o. 

There are parts of it that are good - for instance, it

1. DRY:
2. create a function to gather data for a single doi
3. Uses a loop to iterate over the list of URLs
4. Tests & Checks: provides a nice try/except statement within the get_

It also 
* doesn't run
* suggests that you visbalize the data using a internal chatgpt tool.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

```python
# this is what chatgpt provides - 12 Sept 2024

import pandas as pd
from habanero import Crossref

# Initialize the Crossref client
cr = Crossref()

# Function to fetch paper details using habanero
def get_paper_details(doi):
    try:
        # Query CrossRef for the DOI
        result = cr.works(ids=doi)
        
        # Extract the required information
        authors = [f"{author['given']} {author['family']}" for author in result['message']['author']]
        title = result['message']['title'][0]
        references = result['message'].get('reference-count', 'N/A')  # Some papers may not have this info
        
        return authors, title, references
    
    except Exception as e:
        print(f"Error fetching data for DOI {doi}: {e}")
        return None, None, None

# Load the CSV file
df = pd.read_csv('doi_urls.csv')

# Initialize a list to store the results
results = []

# Process each DOI
for doi in df['DOI']:
    authors, title, references = get_paper_details(doi)
    results.append({
        'DOI': doi,
        'Title': title,
        'Authors': authors,
        'Reference Count': references
    })

# Create a new DataFrame from the results
results_df = pd.DataFrame(results)

# Display the results - this is using a internal openai tool :) 
import ace_tools as tools; tools.display_dataframe_to_user(name="Paper Details", dataframe=results_df)
```
