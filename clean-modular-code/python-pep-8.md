---
jupytext:
  formats: ipynb,md:myst
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

# Use PEP 8 To Write Easier-to-Read Code

:::{admonition} What you will learn
:class: tip

* Describe the benefits of using code styles guides.
* Explain the PEP 8 style guide and how it helps promote code readability.
* Describe key components of the PEP 8 style guide, including naming conventions and white space.
* List tools to help you apply the PEP 8 style guide to your code.  

:::

## What is Python PEP 8 code style?

Code syntax standards refer to rules associated with how code is formatted. These rules include things like:

* How to space code elements in a script,
* How to format and create comments, and
* Naming conventions for variables, functions, and classes

## Why use code standards when writing Python code

Code standards help make your code more readable. Consider this page that you are reading right now. Some conventions are followed that most of us are familiar with (but may not even think about). These conventions include:  

* Capitalize the first letter of a sentence.
* Capitalize the first letter of someone's name.
* Add a space after the end of a sentence.
* Add a space after each word.

These conventions lead to text that you can read easily, like this:

`This is a sentence. And another sentence with a Name and a location like Florida, USA.`

Now imagine reading a book with no spacing, no capitalization and that doesn't follow the regular English language writing conventions. This book would be difficult to read. Take the example below:  

`this is a sentence.and another sentence with a name.this
text could go on forever. whatwouldhappenifweneverusedspaces?`

Code style standards, just like any other language standard, are designed to make code easier to read and understand.

Below, you will learn about the PEP 8 standard for the **Python** scientific programming language. This is the standard used by many **Python** users.

## About the PEP 8 standard for Python

PEP 8 is the style guide that is widely used in the **Python** community. This guide includes rules about naming objects, spacing rules and even how the code is laid out.  

**Python** is developed and maintained by an open source community, and thus, it is not possible to make code standards mandatory. Rather, community members choose to adopt PEP 8 recommendations whenever possible to contribute code that can easily be read and used by the greater community of users.

PEP 8 covers many aspects of code readability, including:

* naming conventions
* use of comments
* line lengths
* use of white space

## PEP 8 naming conventions

The text in this section is summarized from the <a href="https://www.python.org/dev/peps/pep-0008/#naming-conventions" target="_blank">PEP 8 Style Guide published by the Python Software Foundation</a>.

:::{tip}

**Terminology Teview**

First, let's review some terminology associated with naming conventions.

* **Lowercase letter:** `b`

* **Uppercase letter:** `B`

* **lowercase:** `this is all lowercase words`

* **snake case:** when words are separated by underscores: `lower_case_with_underscores`

* **Uppercase:** All words are all uppercase letters: `UPPERCASE`

* **Snake case** upper case: `UPPER_CASE_WITH_UNDERSCORES`

* **CamelCase:** Every word is capitalized so they visually stand out: `CapitalizedWords`. This is sometimes also referred to as CapWords or StudlyCaps.

  * Note: When using acronyms in CamelCase, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.

* **mixedCase:** (differs from CapitalizedWords by initial lowercase character!)

* **Capitalized_Words_With_Underscores:** This approach is not recommended. Use one convention and stick with it.

:::

### Use snake_case and all lower case for variable names

It is recommended that you use standard naming conventions in your code. We suggest that you use **snake_case** and all lowercase letters in your code for variable and function names. Like this:

```python
variable_one
variable_two
```

### Use CamelCase or CapsCase for class names

While regular variables and functions should use **snake_case**, PEP 8
suggests that you use `CamelCase` for class definitions.

```python
class PlotBasicObject(object):
```

### Avoid using single character letters that could be confused with numbers  

Avoid using the characters:

* 'l' (lowercase letter el),
* 'O' (uppercase letter oh), or
* 'I' (uppercase letter eye)

as single-character variable names.

These characters can be difficult to distinguish from numbers when
using certain font families.

For example, the letter `l` looks similar to the number `1`. 

## Comments and PEP 8 

Documentation is an important part of writing great code. Below are some
of the important PEP 8 conventions associated with documentation.

### 1. Python comments should have a space after the `#` sign with the first word capitalized

Following <a href="https://www.python.org/dev/peps/pep-0008/#comments" target="_blank">the PEP8 style guide</a>, single-line comments should
start with the `#` sign followed by a space. The first word of the comment should be capitalized. Like this:

`# This is a PEP 8 conforming comment`

The comment below does NOT conform to PEP 8 standards

`#this comment does not conform to PEP 8 standards`

### 2. Multi-line function comments (docstrings) 

Multi-line comments are most commonly used when creating docstrings. A docstring is the text that follows a function definition. This text helps you or someone using a function understand what the function does.

Following <a href="https://www.python.org/dev/peps/pep-0008/#documentation-strings" target="_blank">the PEP8 style guide</a>, you create a function docstring using three quotes `"""`. The first line of text following the quotes should be a short, concise description of what the function does.

Below that, you can add as much text as you'd like that provides more detail about what the function does.  

example:

```python
def calculate_sum(rainfall, time="month"):

"""Returns a single sum value of all precipitation. 

This function takes a Pandas DataFrame with time series as the index, 
and calculates the total sum, aggregated by month. 
"""
# Code here 

return the_total_sum
```

## Line Length

PEP 8 guidelines suggest that both code and comment lines should all be 79 characters wide (or less). This standard is common in other languages, such as **R**.

:::{tip}
Most text editors allow you to set up guides to see how long your code is. You can then use these guides to create line breaks in your code.
:::


## Python PEP 8 rules for white space

Some of the white space rules have already been discussed above. These including adding a single space after a comment `# Comment here`.

There are also rules associated with spacing throughout your code. These include:

* **Add a blank line before a single-line comment (unless it is the first line of a cell in Jupyter Notebook)** Blank lines help to break up code visually . Consider reading this page: If all of the text was mashed together in one long paragraph, it would be more difficult to read. However, when you break the text up into related paragraphs, it becomes a lot easier to read.

```python

# Perform some math
a = 1+2
b = 3+4
c = a+b 

# Read in and plot some 
review_timeseries = pd.readcsv("pyos-data.csv")
review_timeseries.plot()
```

The code below is more difficult to read as the spacing does not break up the text.

```python
# Perform some math and do some things 
a=1+2
b=3+4
c=a+b 
data=pd.readcsv("pyos-data.csv")
data.plot()
```

* **Break up sections of code with white space:** As you are writing code, it's always good to consider readability and to break up sections of code accordingly. Breaking up your
code becomes even more important when you start working in Jupyter Notebooks which offer individual cells where you can add Markdown and code.

```python
# Process some data here 
data=pd.readcsv("pyos-data.csv")

# Plot data - notice how separating code into sections makes it easier to read
fig, ax = plot.subplots()
data.plot(ax=ax)
plt.show()
```

## Summary -- PEP 8 and Python

The text above provides a broad overview of some of the PEP 8 guidelines and conventions for writing **Python** code. 

:::{important}
This page is not fully inclusive of all of the PEP 8 standards.
:::


+++

## Tools for applying PEP 8 format to your code

Many different tools can help you write code that is PEP 8 compliant. A tool that checks the format of your code is called a linter.

Some linters will reformat your code so that it matches the standards. 

* [Black](https://black.readthedocs.io/en/stable/) has been a popular tool in the scientific Python ecosystem for several years.
* More recently, many people are moving to [ruff which now provides Jupyter support.](https://docs.astral.sh/ruff/configuration/#jupyter-notebook-discovery). Ruff is a perfect tool for you to use if you are developing your code in `.py` files.


:::{note}
Ruff doesn't currently work well with Jupyter / JupyText and myst markdown notebooks. But it can be easily configured into a .precommit workflow, which is used alongside Git and GitHub and will be applied every time you make a commit to a GitHub repo.
::::

The pyOpenSci community has been slowly adopting Ruff because it can run many code formatters with a single configuration file, making it a convenient and easy-to-use tool. 

:::{admonition} Linter vs. code formatter
:class: tip

A code formatter is a tool that helps you modify your code to follow code standards. A linter checks your code and tells you if things need to be fixed, but it generally won't fix them for you.  

Ruff is both a linter and code formatter which is why we like to use it when developing both software and .py file based workflows. 
:::

+++ {"editable": true, "slideshow": {"slide_type": ""}}
