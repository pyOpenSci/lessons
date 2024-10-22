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

(common-exceptions)=
# Common Python exceptions 

Python has dozens of specific errors that can be raised when code fails to run. Below are a few common ones that you may encounter in [Activity 3](clean-code-activity-3). 
	
## `TypeError`

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

(value_error)=
### `ValueError`

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

### `KeyError`

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

### `IndexError`

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

### `AttributeError`

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

(file_error)=
### `FileNotFoundError`

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

* you could do `sys.exit` too... bbut i've ru into issues with that in the past (i wish i could remember what they were ) .

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
