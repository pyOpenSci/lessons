---
layout: single
title: 'Write Clean, Modular, DRY Pythonic Code'
excerpt: "Clean code refers to writing code that runs efficiently, is not redundant, and is easy for anyone to understand. Learn about the characteristics and benefits of writing clean, expressive code in Python."
authors: ['Leah Wasser']
estimated-time: "2-3 hours"
difficulty: "beginner"
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=true slideshow={"slide_type": ""} -->

(intro-clean-code)=
# Write Clean, Modular, DRY Code

:::{toctree}
:hidden:
:caption: Clean, Expressive Code
:maxdepth: 2

Intro <self>
Python Code Style <python-pep-8>
Don't Repeat Yourself <python-dry-modular-code>
Expressive Code <python-write-expressive-code>
Write Pseudocode <write-pseudocode>
:::



:::{toctree}
:hidden:
:caption: Activities
:maxdepth: 2

Activity overview <clean-code-present>
Clean Code: Activity 1 <activity-1/clean-code-activity-1>
Clean Code: Activity 2 <activity-2/clean-code-activity-2>
Clean Code: Activity 3 <activity-3/clean-code-activity-3>
:::

:::{note}
After completing this lesson, you will be able to:

* List 2-4 characteristics of writing clean code.
* Apply the PEP 8 Style Guide standards to your **Python** code.
:::

"Pythonic" code follows the conventions and best practices of the Python programming language. It emphasizes clear, concise, and readable code—the principles of Python's design philosophy. 

<!-- #region editable=true slideshow={"slide_type": ""} -->
Pythonic code also takes full advantage of Python's features which include:

* list comprehensions,
* generators, and
* context managers,
  
to write more elegant and efficient code.

## Characteristics of Pythonic code

### **It's Readable**

Pythonic code is easy to read and understand, often adhering to the **Zen of Python** (a set of guiding principles for Python’s design).

Readable code uses descriptive (expressive) variable names and adheres to PEP 8 style guidelines.
<!-- #endregion -->

```python
# The Zen of Python 
import this
```

```python editable=true slideshow={"slide_type": ""}
# Not Pythonic
import datetime

foovar = datetime.date.today().strftime("%y-%m-%d")
foovar
```

```python editable=true slideshow={"slide_type": ""}
# Pythonic
import datetime

todays_date = datetime.date.today().strftime("%y-%m-%d")
todays_date
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Compare the variable `foovar` to `todays_date`. Which variable name tells you more about the information that it contains?

### **It's Concise**

Pythonic code is concise but not at the expense of clarity. An example of concise code is to use features like list comprehensions and built-in functions.

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Non-Pythonic
result = []
for i in range(10):
   result.append(i * 2)
result
```

```python editable=true slideshow={"slide_type": ""}
# Pythonic
result = [i * 2 for i in range(10)]
result
```

Another example:

```python
# More Pythonic
languages = ["python", "julia", "rust"]

i=0
for language in(languages):
    i+=1
    print(f"{i}: {language}")
```

```python
# More Pythonic
languages = ["python", "julia", "rust"]

for index, language in enumerate(languages):
    print(f"{index}: {language}")
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Clean code is DRY & avoids repetition

Pythonic code avoids repetition. DRY (Don't Repeat Yourself) code is written in a way that avoids repetition and is well organized. This makes it easier to maintain and extend.

### Pythonic code is expressive

Pythonic code communicates the programmer's intent clearly, making it easier for others to understand the purpose of the code at a glance.

Note that the function below has an easy-to-understand name. Some people will even suggest adding a verb that explains what the function does, such as:

`convert_to_kelvin()`

<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def to_kelvin(temperature_fahr):
    return ((temperature_fahr - 32) * (5 / 9)) + 273.15
```

### Pythonic code is well-documented

Docstrings are Pythonic because they prioritize code readability and clarity. They provide clear descriptions of a function’s purpose, parameters, and return values. By embedding documentation directly in the code, docstrings make it easy for developers to understand and use functions or classes without reading the implementation details.

Documentation can mean many different things. When writing code, expressive names combined with sparsely added comments can make it easier to read.

Pythonic code reflects Python's emphasis on readability and simplicity. A well-known phrase from the **Zen of Python** is: "There should be one—and preferably only one—obvious way to do it," which is a core idea behind writing Pythonic code.

```python
def to_kelvin(temperature_fahr):
    """
    Convert the temperature from Fahrenheit to Kelvin.

    Parameters
    ----------
    temperature_fahr : float
        Temperature in Fahrenheit.

    Returns
    -------
    float
        Temperature in Kelvin.
    """
    return ((temperature_fahr - 32) * (5 / 9)) + 273.15
```

<!-- #region editable=true slideshow={"slide_type": ""} -->

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Tools to help you write better, more Pythonic code - code formatters, linters and LLMs

While the above tasks used to require manual code editing, in today's world, you can use a suite of automated tools such as linters and code formatters, combined with LLMs to help you write better, cleaner and more Pythonic code for scientific workflows.  

LLMs (Large Language Models) can be useful for writing code, however, you must be careful about how you use them because:

* ethical issues
* they are often wrong
* they make up stuff
* etc.

However, with correct prompts, an eye out for problems, and tools that will help you with your code as you write it, they can be effective tools in your dev process.

In the next lessons, you will learn more about tools and approaches to making your code more Pythonic.

You will then learn about tools that you can use to format your code and identify problem points, including:

* LLMs like:
  * GitHub Co-pilot
  * OpenAI ChatGPT
  * Google Gemini
  * Anthropic Claude

* Code formatters like:

  * black
  * ruff

<!-- #endregion -->
