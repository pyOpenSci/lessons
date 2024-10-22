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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(functions-checks)=
# Write Flexible Functions to Handle Messy Data

When working with messy or unpredictable data, your goal is to write robust code to handle the unexpected. It's important to catch errors early
and handle them gracefully. [Using functions](about-functions)  is a great first step in creating
a maintainable and resilient data processing workflow. Functions provide modular
units that can be tested independently, making handling edge cases 
and unexpected scenarios easier.

Adding checks to your functions 
is the next step towards making your code more robust and maintainable over time. 

This lesson covers several strategies for making your code more robust and easier-to-use: 

1. Use [`try/except blocks`](#try-except) rather than simply allowing errors to occur.
1. [Make checks Pythonic](#pythonic-checks)
1. [Fail fast](fail-fast)

+++

The same function below assumes that the user provides a list that contains a title as a string. Notice that the output of this function is different from what you might expect. How could you fix this? 

```{code-cell} ipython3
# This function runs when provided both a list 
def clean_title(title):
    """This function checks explicitly to see if it is provided with a value that is a list. It then 
    makes a decision about how to process the function input based on 
    its type.  
    """
    return title[0]

print(clean_title(["hi, i'm a title"]))
print(clean_title("hi, i'm a title"))
```

The function below uses [conditional statements](conditionals) to check the input provided by the user. It uses a "look before you leap" approach to check to see if the input is provided in a list format.
If it isn't, it returns the title in its provided format. 

```{code-cell} ipython3
---
tags: [raises-exception]
---
def clean_title(title):
    """This function checks explicitly to see if it is provided with a value that is a list. It then 
    makes a decision about how to process the function input based on 
    it's type.  
    """
    if isinstance(title, list):
        return title[0]
    return title


print(clean_title(["hi, i'm a title"]))
print(clean_title("hi, i'm a title"))
print(clean_title(""))
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The function below uses a try/except block to handle the title. 
But again notice that in some cases the code will continue to run, but still returns an unexpected value that will surprise a user. 

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
def clean_title(title):
    """
    This function attempts to return the first character of the title.
    Raises the same error with a friendly, custom error message if the input is invalid.
    """
    try:
        return title[0]
    except IndexError as e:
        raise IndexError(f"Oops! You provided a title in an unexpected format. "
                         f"I expected the title to be provided in a list and you provided "
                         f"a {type(title)}.") from e

print(f"{clean_title(['hi, i am a title'])} ")
print(clean_title("hi, i am a title"))
print(clean_title(""))  
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

If you wish, you can shorten the amount of information returned in the error by adding `from None` when you raise the error. This will look nicer to a user, but you lose some detail in the error traceback.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
def clean_title(title):
    """
    Attempts to return the first character of the title.
    Raises the same error with a friendly message if the input is invalid.
    """
    try:
        return title[0]
    except IndexError as e:
        raise IndexError(f"Oops! You provided a title in an unexpected format. "
                         f"I expected the title to be provided in a list and you provided "
                         f"a {type(title)}.") from None 

# Run the function
print(clean_title("")) 
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(try-except)=
## Use Try/Except blocks

`try/except` blocks in Python help you handle errors gracefully instead of letting your program crash. They are used when you think a part of your code might fail, like when working with missing data, or when converting data types.

Here’s how try/except blocks work:

* **try block:** You write the code that might cause an error here. Python will attempt to run this code.
* **except block:** If Python encounters an error in the try block, it jumps to the except block to handle it. You can specify what to do when an error occurs, such as printing a friendly message or providing a fallback option.

A `try/except` block looks like this:

```python
try:
    # code that might cause an error
except SomeError:
    # what to do if there's an error
```

:::{tip}
We pulled together some of the more [common exceptions that Python can throw here](common-exceptions). 
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("Oops i can't process this so I will fail quietly with a print statement.")
        return None  # or some default value
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
convert_to_int("123")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
convert_to_int("abc") 
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

This function attempts to convert a value to an integer, returning `None` and a message if the conversion fails. However, is that message helpful to a person using your code?

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(fail-fast)=
## Fail fast strategy

Identify data processing or workflow problems immediately when they occur and throw an error immediately rather than allowing
them to propagate through your code. This approach saves time and simplifies debugging, providing clearer, more useful error outputs (stack traces).  Below, you can see that the code tries to open a file, but Python can't find the file. In response, Python throws a `FileNotFoundError`.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# Open a file (but it doesn't exist
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

file_data = read_file("nonexistent_file.txt")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

You could anticipate a user providing a bad file path. This might be especailly possible if you plan to share your code with others and run it on different computers and different operating systems.

In the example below, you use a [conditional statement](conditionals) to check if the file exists; if it doesn't, it returns None. In this case, the code will fail quietly, and the user will not understand that there is an error.

This is also dangerous territory for a user who may not understand why the code runs but doesn't work.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import os

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    else:
        return None  # Doesn't fail immediately, just returns None

# No error raised, even though the file doesn't exist
file_data = read_file("nonexistent_file.txt")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

This code example below is better than the examples above for three reasons:

1. It's **pythonic**: it asks for forgiveness later by using a try/except
2. It fails quickly - as soon as it tries to open the file. The code won't continue to run after this step fails.
3. It raises a clean, useful error that the user can understand

The code anticipates what will happen if it can't find the file. It then raises a `FileNotFoundError` and provides a useful and friendly message to the user.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Oops! I couldn't find the file located at: {file_path}. Please check to see if it exists.")

# Raises an error immediately if the file doesn't exist
file_data = read_file("nonexistent_file.txt")
```

## Customizing error messages

The code above is useful because it fails and provides a simple and effective message that tells the user to check that their file path is correct. 

However, the amount of text returned from the error is significant because it finds the error when it can't open the file. Still, then you raise the error intentionally within the except statement. 

If you wanted to provide less information to the user, you could use `from None`. From None ensure that you 
only return the exception information related to the error that you handle within the try/except block.

```{code-cell} ipython3
---
tags: [raises-exception]
---
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Oops! I couldn't find the file located at: {file_path}. Please check to see if it exists.") from None

# Raises an error immediately if the file doesn't exist
file_data = read_file("nonexistent_file.txt")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(pythonic-checks)=
## Make Checks Pythonic

Python has a unique philosophy regarding handling potential errors or
exceptional cases. This philosophy is often summarized by the acronym EAFP:
"Easier to Ask for Forgiveness than Permission." When combined with the **fail
fast** approach, your code can be flexible and resilient to the messy
realities of data processing.

### EAFP vs. LBYL

There are two main approaches to handling potential errors:

- **EAFP (Easier to Ask for Forgiveness than Permission)**: Assume the operation
  will succeed and handle any exceptions if they occur.
- **LBYL (Look Before You Leap)**: Check for conditions before making calls or
  accessing data.

Pythonic code generally favors the EAFP approach, which allows for **failing
fast** when an error occurs, providing useful feedback without unnecessary
checks.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# LBYL approach - manually check that the user provides an int

def convert_to_int(value):
    if isinstance(value, int):
        return int(value)
    else:
        print("Oops i can't process this so I will fail gracefully.")
        return None 

convert_to_int(1)
convert_to_int("a")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# EAFP approach - Consider what the user might provide and catch the error.

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("Oops i can't process this so I will fail gracefully.")
        return None  # or some default value

convert_to_int(1)
convert_to_int("a")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

The EAFP (Easier to Ask for Forgiveness than Permission) approach is more Pythonic because:

* It’s often faster, avoiding redundant checks when operations succeed.
* It’s more readable, separating the intended operation and error handling.

## Any Check is a Good Check

As long as you consider edge cases, you're writing great code! You don’t need to worry about being “Pythonic” immediately, but understanding both approaches is useful regardless of which approach you chose.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
