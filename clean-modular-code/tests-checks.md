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

+++ {"id": "d8b23008"}

## Tests, Checks & Failing Gracefully

You can add checks to your workflow to allow the workflow to either:

1. continue processing even when it encounters
2. fail gracefully in a way that you can see what went wrong

+++ {"id": "83b37457"}

## Tools Needed to Run This Noteboook

`conda install -c conda-forge habanero`

```{code-cell} ipython3
:id: 1f1c256a

import pandas as pd
import habanero
```

+++ {"id": "69cfa634"}

The **.csv file** that you read in contains a list of doi urls.

```{code-cell} ipython3
:id: '80167539'

# Read in the data
file_path = "doi_urls.csv"
doi_df = pd.read_csv(file_path)
doi_df.head(2)
```

+++ {"id": "58d03c6f"}

## About DOI's

A DOI is a unique identifier (Digital Object Identifier) that is used to reference work.

You will add a DOI to a GitHub Repo using Zenodo.org xxxx.

```{code-cell} ipython3
:id: d3738f2a

doi_df["doi_url"][0]
```

+++ {"id": "37ef78f8"}

## Your Task

Your task here is to process a list of DOI's that you have recieved. The dois in this csv file represent DOIs for all packages that have been acceppted by both pyOpenSci and JOSS as a part of our software peer review partnership. 


* **Short Term Goal:** automate accessing reference information for each url in the **.csv** file.
* **Long Term Goal:** create a small "database" containing the reference information associated with each DOI

However, like any URL, all DOI's may resolve properly. 
TO begin, explore the data. The output below is a large
block of JSON. It will be read into **Python** as a `Dictionary`.

```{code-cell} ipython3
:id: 38b2d444

cr = habanero.Crossref()
# Grab a single doi
url = doi_df["doi_url"][0]
# View reference information for that DOI
cr.works(ids=url)
```

+++ {"id": "495d50c1"}

You can access the specific reference information including journal title, year, author using the `["reference"]` key.

```{code-cell} ipython3
:id: 0b8f76ce-0368-42cf-8299-cb7bd5513664

ref_dict = cr.works(ids=url)

# View first reference in dictionary
ref_dict["message"]["reference"][0]
```

+++ {"id": "fc58802d"}

## Automate Your Workflow with a Loop

> Add blockquote

```{code-cell} ipython3
:id: 307e4899

# Without the function your code would look like this:
cr = habanero.Crossref()
all_refs = []
for adoi in doi_df["doi_url"]:
    #print(adoi)
    ref_info = cr.works(ids=adoi)
    all_refs.append(ref_info["message"]["reference"])

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

It looks like you are getting a `KeyError`. This means
that reference information is not returned in your
habanero call.

```{code-cell} ipython3
:id: 01c7443e

# This returns a key error
url = doi_df["doi_url"][3]
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
:id: 8c4fea64

# Your code is easier to read with a function
cr = habanero.Crossref()

for adoi in doi_df["doi_url"]:
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

doi="https://www.earthdatascience.org"
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

+++ {"id": "39f64c05-7d33-4123-8781-034c94f3dffc"}

This data was manually copied from this repo (which i have since forked)
I will either recreate what max did or maybe he already has the code somewhere.

https://github.com/earthlab/usgs-citations
