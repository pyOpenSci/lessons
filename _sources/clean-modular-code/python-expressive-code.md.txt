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

```{raw-cell}
---
editable: true
raw_mimetype: ''
slideshow:
  slide_type: ''
---
---
title: 'Make Your Code Easier to Read By Using Expressive Variable Names in Python'
excerpt: "Expressive variable names refer to function and variable names that describe what the variable contains or what the function does. Using expressive names makes your code easier to understand. Learn how to create expressive names for objects in your Python code."
authors: ['Leah Wasser', 'Jenny Palomino']
---
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Make Your Code Easier to Read Using Expressive Variable Names in Python

:::{admonition} Learning Objectives

* Learn how using expressive names can help you write clean and readable code.
* Create expressive names for objects in your **Python** code.
* Describe the PEP 8 recommendations for Python object names.
:::

## Why use expressive names?

Expressive names describe the contents of the object itself. So for example you probably expect a directory called `data` to contain data within it.

:::{figure} /images/clean-code/open-science-expressive-file-names.png
:alt: "File and directory names that clearly indicate the type of information stored within that file or directory are the most useful or expressive to your colleagues or your future self as they allow you to quickly understand the structure and contents of a project directory."

Compare the list of file names on the LEFT to those on the right - which ones are easier to quickly understand? File and directory names that clearly indicate the type of information stored within that file or directory are the most useful or expressive to your colleagues or your future self as they allow you to quickly understand the structure and contents of a project directory. Source: Jenny Bryan, Reproducible Science Curriculum.
:::

Expressive code is also important for naming variables and functions in your **Python** code because it will make your code easier to understand for someone skimming it, just as it makes it easier for someone to understand a file directory structure.

Expressive code is another part of clean coding - that is, writing code that is easier for you, your future self, and for someone else to look at and understand. After you've been programming for a while, you will begin to see that consistently formatted code is much easier for your eye to scan and quickly understand.

:::{figure} /images/clean-code/clean-code-expressive-variable-names-basmati-rice.png
:alt: "alt here."

This container clearly contains cookies, yet it's labeled "rice." This might be confusing to someone who is looking for rice in your kitchen! Consider this when writing code. It's easier for someone to understand your code without running it when your code variables describe the objects that they contain. Source: Jenny Bryan, Reproducible Science Curriculum.
::


:::{tip}
The <a href="https://www.python.org/dev/peps/pep-0008/" target="_blank">the PEP 8 Style Guide</a> suggests that all objects (variables, functions and methods) in your code are named using meaningful words.
:::

## Best practices for naming objects

PEP 8 style guide has a suite of recommendations that focus on making Python code more readable. Below are some of the PEP 8 guidelines related to expressive object names.  

1. **Keep object names short:** this makes them easier to read when scanning through code.

2. **Use meaningful names:** A meaningful or expressive variable name will be  eaiser for someone to understand. For example: `precip` is a more useful name that tells us something about the object compared to `x` or `a`.

3. **Do not start names with numbers** Objects that start with a number are NOT VALID in **Python**.

4. **Avoid names that are existing functions in Python:** e.g., `if`, `else`, `for`, see <a href="https://www.programiz.com/python-programming/keywords-identifier" target="_blank">here</a> for more reserved names.

A few other notes about object names in **Python**:

* **Python** is case sensitive (e.g., `weight_kg` is different from `Weight_kg`).
* Avoid existing function names (e.g. `mean`), though you can combine these with other words to create a more descriptive name (e.g. `precip_mean`).
* Use nouns for variable names (e.g. `weight_kg`), and verbs for function names (e.g. `convert_kg_lb`).
* Avoid using dots in object names - e.g. `precip.boulder` - dots have a special meaning in **Python** (for methods - the dot indicates a function that is connected to a particular **Python** object) and other programming languages.
  * Instead, use underscores `precip_boulder`.

## Recommendations for naming conventions

### Best practices for directory and file names

We suggest that you use directory and file names that contain words that describe the contents of the file or directory, separated using dashes - like this:

`lower-case-with-dashes`

Directory and files names should be kept as short and concise as possible, while also clearly indicating what is contained within the directory or file.

### Best practices for Python variable names

For variables, we suggest that you use `lowercase` for short variable names and `lower_case_with_underscores` for longer and more descriptive variable names. Variable names should be kept as short and concise as possible while also clearly indicating the kind of data or information contained in the variable.

Examples include:

* **precip**: to indicate a simple variable (either single value or data structure without temporal or spatial variation in coverage)
* **boulder_precip**: to indicate the location of the data collection
* **max_precip**: to indicate the result of a summary statistic
* **precip_2002**: to indicate a particular year of data included
* **precip_2002_2013**: to indicate the particular years of data included
* **precip_2000_to_2010**: to indicate a range of years of data included
* **precip_in** or **precip_mm**: to indicate the measurement units

The variable names should be driven by the overall goals and purpose of the code in which they are being used.

For example, in some cases, it may be more important to distinguish the units of measurement, the location, or the year or range of years covered by the data. Use your best judgment and modify variable names as needed.  

### Best practices for naming Python functions and methods

Following PEP 8 guidelines, function names should be formatted using  
`words_separated_by_underscores`. The words that you use to name your function should clearly describe the function's intent (what the function does). Ideally this name is a very specific name that describes what the function does. For example, if you write a function that removes hyphens from some text a name like `remove_hyphens` might be appropriate.  

```python
## This function name is less expressive 
text_edit()

# This function name is more expressive
remove_hyphens()
```

## Example function

The function below is designed to convert a temperature provided
in a numeric format in degrees Fahrenheit to Kelvin.

```python

def fahr_to_kelvin(fahr):
    """Convert temperature in Fahrenheit to kelvin.
    
    Parameters:
    -----------
    fahr: int or float
        The temperature in Fahrenheit.
    
    Returns:
    -----------
    kelvin : int or float
        The temperature in kelvin.
    """
    kelvin = ((fahr - 32) * (5 / 9)) + 273.15
    return kelvin

```

Consider the list of function names below for the above function, which of these names are the most expressive and why?

```python
f()
my_func()
t_funk()
f2k()
convert_temperature()
fahr_to_kelvin()
```

:::{tip}
PEP 8 suggests that class names should use `mixedCase`.
:::
