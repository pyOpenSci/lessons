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

# Write Flexible Functions for Messy Data

When dealing with messy or unpredictable data, using functions is an excellent first step in creating a robust and maintainable data processing workflow. Functions provide modular units that can be tested independently, allowing you to handle various edge cases and unexpected scenarios effectively.

## Function benefits

Using functions in your data processing pipeline offers several advantages:

1. **Modularity**: Functions encapsulate specific tasks, making your code more organized and easier to understand.
2. **Testability**: You can test functions individually, outside of the main workflow, to ensure they handle different scenarios correctly.
3. **Flexibility**: As you build out your workflow, you can easily add elements to functions to handle new processing requirements or edge cases.
4. **Reusability**: Well-designed functions can be reused across different parts of your project or even in other projects.

Your goal is to identify detect and data processing or workflow problems immediately when they occur, rather than allowing
them to propagate through your code. This approach saves time and makes
debugging easier, providing clearer, more useful error outputs (known as stack traces).

When working with messy data, you'll often encounter edge cases - unusual or unexpected data that can break your processing pipeline. Functions allow you to implement robust error handling and data validation.

(fail-fast)=

## Fail fast strategy

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

In the example below, you use a [conditional statement](python-conditionals) to check to see if the file exists; if it doesn't, then it returns None. In this case the code will fail quietly and the user doesn't understand that there is an error.

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

1. It's pythonic: it asks for forgiveness later by using a try/except
2. it fails quickly - as soon as it tries to open the file. The code won't continue to run after this step fails.
3. it raises a clean, useful error that the user can undersatnd

The code anticipates what will happen if it can't find the file. Here you can raise a `FileNotFoundError` and provide a useful message to the user.

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
        raise FileNotFoundError(f"Oops! I couldn't find the file located at: {file_path}. Please check to see if it exists")

# Raises an error immediately if the file doesn't exist
file_data = read_file("nonexistent_file.txt")
```

Notice that the code below doesn't throw an error. This code is allowed to fail quietly.
This will be problematic for a user as their code will run but they will have no output and will have to carefully debug the code in order to figure out where the problem is.

```{code-cell} ipython3
from pathlib import Path

def read_file(file_path):
    """
    Reads the content of a single file and returns it.
    Handles errors if the file cannot be read.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred while reading {file_path}: {e}"

# Example usage
directory_path = Path("data")
files = list(directory_path.glob("*.json"))
for file in files:
    file_data = read_file(file)
    print(f"Content of {file.name}:")
    print(file_data)
print("All done--I didn't fail but I should have failed quickly")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

[Using functions](python-functions) is a great first step in creating a robust
and maintainable data processing workflow. Functions provide modular units that
can be tested independently, allowing you to handle various edge cases and
unexpected scenarios effectively. However, adding checks to your functions
is the next step towards making your code more robust and maintainable over time.

(pythonic-checks)=

## Make Checks Pythonic

Python has a unique philosophy regarding handling potential errors or
exceptional cases. This philosophy is often summarized by the acronym EAFP:
"Easier to Ask for Forgiveness than Permission." When combined with the **fail
fast** approach, your code can be flexible and resilient to the messy
realities of data processing.

### EAFP vs. LBYL

There are two main approaches to handling potential errors:

- **LBYL (Look Before You Leap)**: Check for conditions before making calls or
  accessing data.
- **EAFP (Easier to Ask for Forgiveness than Permission)**: Assume the operation
  will succeed and handle any exceptions if they occur.

Pythonic code generally favors the EAFP approach, which allows for **failing
fast** when an error occurs, providing useful feedback without unnecessary
checks.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# LBYL approach - manually check that the user provides a int
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

- It’s often faster, avoiding redundant checks when operations succeed.
- It’s more readable, separating the intended operation and error handling.

## Any Check is a Good Check

As long as you consider edge cases, you're writing great code! You don’t need to worry about being “Pythonic” immediately, but understanding both approaches is useful regardless of which approach you chose.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Try/Except blocks

Try/except blocks help you catch and handle errors that might happen while your code is running. This is useful for tasks that might fail, like converting data types or working with data that’s missing or incorrect.

A try/except block looks like this:

```python
try:
    # code that might cause an error
except SomeError:
    # what to do if there's an error
```

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

This function attempts to convert a value to an integer, returning None and a message if the conversion fails.

## Make checks Pythonic

Python has a unique philosophy regarding handling potential errors or exceptional cases. This philosophy is often summarized by the acronym EAFP: "Easier to Ask for Forgiveness than Permission."

### EAFP vs. LBYL

There are two main approaches to handling potential errors:

**LBYL (Look Before You Leap)**: Check for conditions before making calls or accessing data.
**EAFP (Easier to Ask for Forgiveness than Permission)**: Assume the operation will succeed and handle any exceptions if they occur.

Pythonic code generally favors the EAFP approach.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# LBYL approach - manually check that the user provides a int
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

- It’s often faster, avoiding redundant checks when operations succeed.
- It’s more readable, separating the intended operation and error handling.

## Any Check is a Good Check

As long as you consider edge cases, you're writing great code! You don’t need to worry about being “Pythonic” immediately, but understanding both approaches is useful regardless of which approach you chose.

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Common Python exceptions

Python has dozens of specific errors that can be raised when code fails to run. Below are a few common ones that you may encounter in the activity 3.

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
int("abc")
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

### IndexError

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

### AttributeError

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

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## FileNotFoundError

A `FileNotFoundError` occurs in Python when the code attempts to open or access a file that does not exist at the specified path.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
with open("data/nonexistent_file.json", "r") as file:
    data = file.read()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

By catching this exception, you can

1. Raise a kinder and more informative message.
2. Direct the user toward the next steps
3. FUTURE: write tests for this step of the workflow (if you are creating a package!) that make sure that it handles a bad file path properly.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [raises-exception]
---
from pathlib import Path

file_path = Path("data") / "nonexistent_file.json"
try:
    with open(file_path, "r") as file:
        data = file.read()
except FileNotFoundError as fe:
    raise FileNotFoundError(f"Oops! it looks like you provided a path to a file that doesn't exist. You provided: {file_path}. Make sure the file path exists. ")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

If you don't raise the error but instead provide a print statement, you can provide a simple, clean output without the full "stack" or set of Python messages that provides the full "tracking" or traceback of where the error originated.

The challenge with not raising a FileNotFound error is that it will be a bit trickier to test the output.

- you could do `sys.exit` too... bbut i've ru into issues with that in the past (i wish i could remember what they were ) .

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
file_path = Path("data") / "nonexistent_file.json"
try:
    with open(file_path, "r") as file:
        data = file.read()
except FileNotFoundError as fe:
    print(f"Oops! it looks like you provided a path to a file that doesn't exist. You provided: {file_path}. Make sure the file path exists. ")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
