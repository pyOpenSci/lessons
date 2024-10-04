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

# Handling Messy Data with Python Functions

## Introduction

When dealing with messy or unpredictable data, using functions is an excellent first step in creating a robust and maintainable data processing workflow. Functions provide modular units that can be tested independently, allowing you to handle various edge cases and unexpected scenarios effectively.

## Benefits of Using Functions

Using functions in your data processing pipeline offers several advantages:

1. **Modularity**: Functions encapsulate specific tasks, making your code more organized and easier to understand.
2. **Testability**: You can test functions individually, outside of the main workflow, to ensure they handle different scenarios correctly.
3. **Flexibility**: As you build out your workflow, you can easily add elements to functions to handle new processing requirements or edge cases.
4. **Reusability**: Well-designed functions can be reused across different parts of your project or even in other projects.

## Handling Edge Cases

When working with messy data, you'll often encounter edge cases - unusual or unexpected data that can break your processing pipeline. Functions allow you to implement robust error handling and data validation. Here are some techniques you can use:

+++

## Try/Except Blocks
Try/except blocks allow you to catch and handle exceptions that might occur during data processing. This is particularly useful when dealing with operations that might fail, such as type conversions or accessing nested data structures.

```{code-cell} ipython3
def safe_convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None  # or some default value

# Example usage
result = safe_convert_to_int("123")  # Returns 123
result = safe_convert_to_int("abc")  # Returns None
```

This function attempts to convert a value to an integer, returning None if the conversion fails.

## Making Checks Pythonic

Python has a unique philosophy when it comes to handling potential errors or exceptional cases. This philosophy is often summarized by the acronym EAFP: "Easier to Ask for Forgiveness than Permission".

### EAFP vs LBYL
There are two main approaches to handling potential errors:

LBYL (Look Before You Leap): Check for conditions before making calls or accessing data.
EAFP (Easier to Ask for Forgiveness than Permission): Assume the operation will succeed and handle any exceptions if they occur.

Python generally favors the EAFP approach, which often leads to cleaner and more readable code. Here's an example to illustrate the difference:

```{code-cell} ipython3
# LBYL approach
def get_value_lbyl(dictionary, key, default=None):
    if key in dictionary:
        return dictionary[key]
    else:
        return default

# EAFP approach
def get_value_eafp(dictionary, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default

# Example usage
my_dict = {"a": 1, "b": 2}
print(get_value_lbyl(my_dict, "c", 0))  # Returns 0
print(get_value_eafp(my_dict, "c", 0))  # Returns 0
```

The EAFP approach is considered more Pythonic because:

It's often faster, as it avoids redundant checks in the common case where the operation succeeds.
It's more readable and expressive, clearly showing the intended operation and the exception handling separately.
It helps avoid race conditions in certain scenarios, particularly in multi-threaded environments.
