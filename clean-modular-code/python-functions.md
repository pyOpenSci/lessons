---
title: "Introduction to Writing Functions in Python"
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
# Write Efficient Modular Code Using Functions

Three strategies for eliminating repetition and improving the efficiency of your code:

1. loops,
2. conditional statements, and
3. functions.

Here you will learn how writing functions in **Python** can help you to execute a specific task while also making your code more maintainable.

A function is a reusable block of code that performs a specific task. Functions receive inputs to which code is applied and return outputs (or results) of the code.

`input parameter –> function does something –> output results`

For example:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
x = 5
# The print statement is a function that provides output.
print(x)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Functions can help you to both eliminate repetition and improve efficiency in your code through modularity.

Modularity means that code is separated into independent units that can be reused and even be combined to complete a longer chain of tasks.

:::{figure} /images/clean-code/functions-for-all-things.png
:alt: You can implement strategies such as loops and functions in your code to replace tasks that you are performing over and over. Source: Francois Michonneau.
:target: /images/clean-code/functions-for-all-things.png

You can use loops and functions in your code to replace repeating tasks.  
Source: Francois Michonneau.
:::

## The benefits of functions

* Modularity: Functions only need to be defined once in a workflow. Functions that you write for specific tasks can be used over and over, without needing to redefine the function again. A function that you write for one **Python** workflow can also be reused in other workflows especially if you make your code installable.

* Fewer variables: When you run a function, the intermediate variables (i.e. placeholders) that it creates are not stored as explicit variables unless you specify otherwise. This saves memory and keeps your **Python** environment cleaner.

* Better documentation: Well-documented functions help other users understand the steps of your processing and helps your future self to understand previously written code.

* Easier to maintain and edit your code: Because a function is only defined once in the workflow, you can simply just update the original function definition. Then, each instance in which you call that function in your code (i.e. when same task is performed) is automatically updated.

* Tests & checks: Writing functions allows you you to your code to handle issues and edge cases in your code. It also can make it easier to write tests for your code.

### Write modular functions and code

A well-defined function only does one thing, but it does it well and often in various contexts. Often, the operations contained in a good function are generally useful for many tasks.

Take, for instance, the **numpy** function called `mean()`, which computes mean values from a **numpy** array.

This function only does one thing (i.e. computes a mean); however, you may use the `np.mean()` function many times in your code on multiple **numpy** arrays because it has been defined to take any **numpy** array as an input.

For example:
<!-- #endregion -->

```python
import numpy as np
arr = np.array([1, 2, 3])

# Calculate mean of input array
np.mean(arr)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
The `np.mean()` function is modular, and it can be easily combined with other functions to accomplish various tasks.

When you write modular functions, you can reuse them for other workflows and projects. Some people even write their own **Python** packages for personal and professional use that contain custom functions for tasks that they have to complete regularly.

### Variables produced in functions are discarded after the function runs

When coding tasks step by step, you are likely creating many intermediate variables that are not needed again but are
stored in your computer's memory.

By using functions, these intermediate variables are confined to the function’s local scope. Once the function finishes executing, the variables created within the function are discarded making your code cleaner and more efficient  

## Reasons why functions improve code readability

### Functions help you document your code  

Ideally, your code is easy to understand and is well-documented with **Python** comments (or **Markdown** in **Jupyter Notebook**). However, what might seem clear to you now might not be clear 6 months from now, or even 3 weeks from now.

Well-written functions help you document your workflow if:

* They have clear docstrings that outline the function's inputs and outputs.
* They use descriptive names that clearly describe the task that the function performs.

### Expressive function names make code self-describing

When writing your own functions, you should name functions using verbs and/or clear labels to indicate what the function does (i.e. `in_to_mm` for converting inches to millimeters).

This makes your code more expressive (or self-describing), and in turn, makes it easier to read for you, your future self, and your colleagues.

### Modular code is easier to maintain and edit

If all your code is written line by line (with repeated code in multiple parts of your document) it can be challenging to maintain and edit.

Imagine having to fix one element of a line of code that is repeated many times. You will have to find and replace that code to implement the fix in EVERY INSTANCE it occurs in your code!

Repeated code cause you to duplicated comment. So how do you keep the duplicated comments in sync?

A comment that is misleading because the code changed is worse than no comment.

Organizing your code using functions from the beginning allows you to explicitly document the tasks that your code performs, as all code and documentation for the function is contained in the function definition.

### Functions and tests  

While you will not learn about testing in this lessons, note that functions are also very useful for testing.

As your code gets longer and more complex, it is more prone to mistakes. For example, if your analysis relies on data that gets updated often, you may want to make sure that all the columns in your spreadsheet are present before performing an analysis. Or, that the new data are not formatted in a different way.

Changes in data structure and format could cause your code to not run. Or, in the worse case scenario, your code may run but return the wrong values!

If all your code is made up of functions (with built-in tests to ensure that they run as expected), then you can control the input to the function and test that the output returned is correct for that input. It is something that would be difficult to do if all of your code is written line by line with repeated steps.

## Summary of writing modular code with functions

It is a good idea to learn how to:

1. Modularize your code into generalizable tasks using functions.
2. Write functions for parts of your code that include repeated steps.
3. Document your functions clearly, specifying the structure of the inputs and outputs with clear comments about what the function can do.
<!-- #endregion -->
