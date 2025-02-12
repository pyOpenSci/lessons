---
title: "Why Functions Make Your Scientific Code Better"
excerpt: "A function is a reusable block of code that performs a specific task. Learn how to use functions to write DRY (Do Not Repeat Yourself) code in Python."
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
(about-functions)=
# Why write functions?

There are several strategies for making your code more modular. Here, you will learn about 
functions as one strategy that eliminates repetition in your code and also can improve the 
efficiency and maintainability of your code. 

A function is a reusable block of code that performs a specific task. Functions receive inputs to which code is applied and return outputs (or results) of the code.

`input parameters –> function does something –> output results`

:::{tip}

Functions (and classes) are the base for creating Python packages.

:::

For example:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
x = 5
# abs is a function that provides output.
abs(x)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Functions can help you to both eliminate repetition and improve efficiency by making it more modular. 


Modular code is separated into independent units that can be reused and even combined to complete a longer chain of tasks.

:::{figure} /images/clean-code/functions-for-all-things.png
:alt: You can implement strategies such as loops and functions in your code to replace tasks that you are performing over and over. Source: Francois Michonneau.
:target: /images/clean-code/functions-for-all-things.png

You can use loops and functions in your code to replace repeating tasks.  
Source: Francois Michonneau.
:::

## The benefits of functions

* **Modularity:** Functions only need to be defined once in a workflow. Functions that you write for specific tasks can be used over and over without redefining the function again. A function that you write for one **Python** workflow can also be reused in other workflows, especially if you [make your code installable](https://www.pyopensci.org/python-package-guide/tutorials/installable-code.html).

* **Fewer variables:** When you run a function, the intermediate variables that the function creates are not by default stored as explicit variables. These placeholder variables are thrown out once the function has run so it saves memory and keeps your **Python** environment cleaner.
* **Better documentation:** Well-documented functions help other users understand the steps of your processing and helps your future self to understand previously written code.
* **Easier to maintain and edit your code:** Because a function is only defined once in the workflow, you can update the original function definition. Then, each instance in which you call that function in your code (i.e., when the same task is performed) is automatically updated.
* **Tests & checks:** Writing functions allows you to handle issues and edge cases in your code. It also can make it easier to write tests for your code.

### Write modular functions and code

A well-defined function only does one thing but does it well and often in various contexts. Often, the operations in a good function are useful for many tasks.

Take, for instance, the **{mod}`numpy`** function called {func}`~numpy.mean`, which computes mean values from a **numpy** array.

This function only does one thing-- it computes a mean. However, you may use the {func}`np.mean() <numpy.mean>` function many times in your code on multiple **numpy** arrays because it has been defined to take any **numpy** array as an input.

For example:
<!-- #endregion -->

```python
import numpy as np

arr = np.array([1, 2, 3])

# Calculate mean of input array
np.mean(arr)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
The {func}`numpy.mean()` function is modular, and it can be easily combined with other functions to accomplish various tasks.

When you write modular functions, you can reuse them for other workflows and projects. Some people even write their own **Python** packages for personal and professional use that contain custom functions for tasks that they have to complete regularly.

### Variables produced in functions are discarded after the function runs

When coding tasks step by step, you are likely creating many intermediate variables that are not needed again but are
stored in your computer's memory.

These intermediate variables are confined to the function’s local scope by using functions. Once the function finishes executing, the variables created within the function are discarded, making your code cleaner and more efficient  

## Reasons why functions improve code readability

### Functions help you document your code  

Ideally, your code is easy to understand and is well-documented with **Python** comments (or **Markdown** in **Jupyter Notebook**) and expressive variable and function names. However, what might seem clear to you now might not be clear 6 months from now, or even 3 weeks from now.

Well-written functions help you document your workflow if:

* They have clear docstrings that outline the function's inputs and outputs.
* They use descriptive names that clearly describe the function's task.

### Expressive function names make code self-describing

When writing your own functions, you should name functions using verbs and/or clear labels to indicate what the function does (i.e., `in_to_mm` for converting inches to millimeters).

This makes your code more expressive (or self-describing) and, in turn, makes it easier to read for you, your future self, and your colleagues.

### Modular code is easier to maintain and edit

It can be challenging to maintain and edit if your code is written line by line (with repeated code in multiple parts of your script).

Imagine having to fix one element of a code line repeated many times. You will have to find and replace that code to implement the fix in EVERY INSTANCE it occurs in your code!

Organizing your code using functions from the beginning allows you to explicitly document the tasks that your code performs, as all code and documentation for the function is contained in the function definition.

### Functions and tests  

Functions are also useful for testing.

As your code gets longer and more complex, it is more prone to mistakes. For example, if your analysis relies on data that gets updated often, you may want to make sure that all data are up-to-date before performing an analysis. Or that the new data are not formatted in a different way.

Changes in data structure and format could break your code. In the worst-case scenario, your code may run but return the wrong values.

If all your code is composed of functions (with built-in tests and checks to ensure that they run as expected), then you can control the input to the function and test that the output returned is correct for that input. It is something that would be difficult to do if all of your code is written line by line with repeated steps.

## Summary

It is a good idea to learn how to:

1. Modularize your code into generalizable tasks using functions.
2. Write functions for parts of your code that include repeated steps.
3. Document your functions clearly, specifying the structure of the inputs and outputs with clear comments about what the function can do.
<!-- #endregion -->
