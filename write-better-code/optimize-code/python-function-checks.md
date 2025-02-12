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
# This function runs when provided both a list or a string
def clean_title(title):
    """This function always returns the first element"""
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

print(clean_title(["hi, i am a title"]))
print(clean_title("hi, i am a title"))
print(clean_title(""))  
```

```{tip} Informative Errors

Notice we included the value that caused the error in the `IndexError` message,
and a suggestion about what we expected!

Include enough detail in your exceptions so that the person reading them knows
why the error occurred, and ideally what they should do about it.
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

(try-except)=
## Use Try/Except blocks

`try/except` blocks in Python help you handle errors gracefully instead of letting your program crash. They are used when you think a part of your code might fail, like when working with missing data, or when converting data types.

Here’s how try/except blocks work:

* **try block:** You write the code that might cause an error here. Python will attempt to run this code.
* **except block:** If Python encounters an error in the try block, it jumps to the except block to handle it. You can specify what to do when an error occurs, such as printing a friendly message or providing a fallback option.

A `try/except` block looks like this[^more_forms]:

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

Identify data processing or workflow problems immediately when they occur and throw an error rather than allowing
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

You could anticipate a user providing a bad file path. This might be especially possible if you plan to share your code with others and run it on different computers and different operating systems.

In the example below, you use a [conditional statement](conditionals) to check if the file exists; if it doesn't, it returns None. In this case, the code will fail quietly, and the user will not understand that there is an error.

This is also dangerous territory for a user who may not understand why the code runs but doesn't work.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import os

def read_file_silent(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    else:
        return None  # Doesn't fail immediately, just returns None

# No error raised, even though the file doesn't exist
file_data = read_file_silent("nonexistent_file.txt")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Even if you know that it is possible for a `FileNotFoundFoundError` to be raised here, it's better to raise the exception rather than catch it and proceed silently so the person calling the function knows there is a problem they need to address.

Say for example reading the data was one step in a longer chain of analyses with other steps that take a long time in between when the data was loaded and when it was used:

```python
# The problem occurs here...
data = read_file_silent("nonexistent_file.txt")

# This file takes an hour to download...
big_file = download_file('http://example.com/big_file.exe')

# And this simulation runs overnight...
generated_data = expensive_simulation()

# We'll only realize there is a problem here, 
# and by then the problem might not be obvious!
analyze_data(data, big_file, generated_data)
```

By silencing the error, we wasted our whole day!

## Catching and Using Exceptions

If we want to raise exceptions as soon as they happen,
why would we ever want to catch them with `try`/`catch`?
Catching exceptions allows us to choose how we react to them -
and vice versa when someone else is running our code, 
raising exceptions lets them know there is a problem and gives them the opportunity to decide how to proceed.

For example, you might have many datasets to process,
and you don't want to waste time processing one that has missing data,
but you also don't want to stop the whole run because an exception happens
somewhere deep within the nest of code.
The *combination* of failing fast with error handling allows us to do that!

Here we use the `except {exception type} as {variable}` syntax to *use* the error after catching it,
and we store error messages for each dataset to analyze and display them at the end:

```{code-cell} ipython3
from rich.pretty import pprint

data = [2, 4, 6, 8, 'uh oh']

def divide_by_two(value):
    return value/2

def my_analysis(data):
    results = {}
    errors = {}
    for value in data:
        try:
            results[value] = divide_by_two(value)
        except TypeError as e:
            errors[value] = str(e)
    return {'results': results, 'errors': errors}

results = my_analysis(data)
pprint(results, expand_all=False)
```

These techniques stack! So add one more level where we imagine someone else is using our analysis code. They might want to raise an exception to stop processing the rest of their data.

```{code-cell} ipython3
---
tags: [raises-exception]
---

def someone_elses_analysis(data):
    processed = my_analysis(data)
    if processed['errors']:
        raise RuntimeError(f"Caught exception from my_analysis: {processed['errors']}")

someone_elses_analysis(data)
```


## Customizing error messages

Recall the exception from our missing file:

```{code-cell} ipython3
---
tags: [raises-exception]
---

file_data = read_file("nonexistent_file.txt")
```

### Focusing Information - Raising New Exceptions

The error is useful because it fails and provides a simple and effective message that tells the user to check that their file path is correct. But there's a lot of information there! The traceback shows us each line of code in between the place where you called the function and where the exception was raised: the `read_file()` call, the `open()` call, the bottom-level `IPython` exception. If you wanted to provide less information to the user, you could catch it and raise a *new* exception. 

If you simply raise a new exception, it is [chained](https://docs.python.org/3/tutorial/errors.html#exception-chaining) to the previous error, which is noisier, not tidier!

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
        raise FileNotFoundError(
            f"Oops! I couldn't find the file located at: {file_path}. "
            "Please check to see if it exists."
        )  # no "from" statement implicitly chains the prior error


file_data = read_file("nonexistent_file.txt")
```

Instead we can use the exception chaining syntax, `raise {exception} from {other exception}`, to explicitly exclude the original error from the traceback.


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
        raise FileNotFoundError(
            f"Oops! I couldn't find the file located at: {file_path}. "
            "Please check to see if it exists."
        ) from None  # explicitly break the exception chain


file_data = read_file("nonexistent_file.txt")
```

This code example below is better than the examples above for three reasons:

1. It's **pythonic**: it asks for forgiveness later by using a try/except
2. It fails quickly - as soon as it tries to open the file. The code won't continue to run after this step fails.
3. It raises a clean, useful error that the user can understand

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Adding Information - Using Notes

The above exception is tidy, and it's reasonable to do because we know
exactly where the code is expected to fail.

The disadvantage to breaking exception chains is that you might *not*
know what is going to cause the exception, and by removing the traceback,
you hide potentially valuable information.

To add information without raising a new exception, you can use the 
{meth}`Exception.add_note` method and then re-raise the same error:

```{code-cell} ipython3
---
tags: [raises-exception]
---
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        e.add_note("Here's the deal, we both know that file should have been there, but now its not ok?")
        raise e

# Raises an error immediately if the file doesn't exist
file_data = read_file("nonexistent_file.txt")
```

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

---

[^more_forms]: See the [python tutorial on exceptions](https://docs.python.org/3/tutorial/errors.html#enriching-exceptions-with-notes) for the other forms that an exception might take, like:

    ```python
    try:
        # do something
    except ExceptionType:
        # catch an exception
    else:
        # do something if there wasn't an exception
    finally:
        # do something whether there was an exception or not
    ```

