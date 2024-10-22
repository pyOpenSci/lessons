---
layout: single
title: 'Write Python Functions: Modular Code'
excerpt: "A function is a reusable block of code that performs a specific task. Learn how to write functions in Python to eliminate repetition and improve efficiency in your code."
last_modified: '{:%Y-%m-%d}'.format(datetime.now())
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

(write-functions)=
## How to write a Python function  

:::{tip}
## What you will learn 
* Describe the components needed to define a function in **Python**.
* Write and execute a custom function in **Python**.
:::

To define a function in Python, you need:
- The `def` keyword to start the function definition.
- A function name that follows [PEP 8 guidelines](../python-expressive-code.md) for naming.
- Input parameters (optional), defined inside parentheses `()`.
- A `return` statement that specifies the output of the function.
- A docstring that explains what the function does and defines the function's inputs and outputs. We suggest that you use numpy style docstrings for scientific Python code.
- 

### An example Python function

An example Python function with two input variables is below:

```python
def add_numbers(a, b):
    """A function that adds two numbers together"

    Parameters
    ----------
    a: int
    b: int 

    """

    return a + b

# Try out the function
add_numbers(1,2)
```

<!-- #region -->
## How to define functions in Python

Several components are needed to define a function in **Python**, including the `def` keyword, function name, parameters (inputs), and the `return` statement, which specifies the function's output. 

```python
def function_name(parameter):
    some code here    
    return output
```

### `def` keyword and function Name

In **Python**, function definitions begin with the keyword **`def`** to indicate the start of a definition for a new function. The function name follows this keyword. 

```python
def function_name():
```

The function name is the name you use when calling the function (e.g. `print()`). 


You can think of functions as inline documentation. Function names should be concise but descriptive of what the function does. 

### Input Parameter(s)

The input parameter is the required information you pass to the function to run successfully. The function will take the value or object provided as the input parameter and use it to perform some task.

In **Python**, the required parameters are provided within parenthesis `()`, as shown below.

```python
def function_name(parameter):       
```    

You can define an input parameter for a function using a placeholder variable, such as `data`, which represents the value or object that will be acted upon in the function. 


```python
def function_name(data):
```   

You can define a function using multiple parameters. 


```python
def add_numbers(num_1, num_2):
```  


### Return Statement

In **Python**, function definitions should have a `return` statement to specify the output that will be returned by the function. 


```python
def function_name(data):
    some code here    
    return output
```


Like with loops and conditional statements, the code lines executed by the function, including the `return` statement, are provided on new lines after a colon `:` and are indented once to indicate that they are part of the function.

The `return` statement can return one or more values or objects and can follow multiple lines of code as needed to 
complete the task (i.e., code to create the output that will be returned by the function). 


### Python Numpy-style docstrings 

Python functions should always contain a docstring, or a multi-line documentation comment, that provides details about the function, including the specifics of the input parameters and the returns (e.g. type of objects, additional description) and any other important documentation about how to use the function. 

There are many docstring formats, but we suggest that you use [numpy style](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) as a default for the scientific Python ecosystem. 


```python
def function_name(data):
    """Docstrings describe the function's behavior.
   
    Docstrings identify the parameters (inputs) that the function 
    can take and the return (output) provided by the function,
    as shown below. 
    
    Parameters
    ----------
    input : type
        Description of input.
    
    Returns
    ------
    output : type
        Description of output.
    """
    # Add some code here
    
    return output
```

While a docstring is not required for the function to work in **Python**, good documentation will save you time in the future when you need to use this code again. It also helps others understand how to use your function.

:::{tip}
You can learn more about different types of docstrings in our [Python packaging guide](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/document-your-code-api-docstrings.html#three-python-docstring-formats-and-why-we-like-numpy-style). focused on docstrings.  
:::


<!-- #endregion -->

```python
def mm_to_in(mm):
    """Convert input from mm to inches"""   
    inches = mm / 25.4    
    return inches
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Call custom Python functions

Now that you have defined the function `add_num()`, you can call it as needed to convert units. 

Below is an example call to this function, specifying a single value variable represented by `mm` in the function.
<!-- #endregion -->

Notice that the output is provided but you have not actually changed the original values of `precip_jan_mm`.  

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Local function variables

In Python, variables defined inside a function are called **local variables**. These variables exist only while the function runs and are specific to that function. Once the function completes, the local variables are discarded, meaning they can’t be accessed from outside the function. This helps keep the function’s operations isolated and prevents interference with other parts of your workflow. 

For example, if you define a variable `result` inside a function, it won't conflict with another variable named `result` in your main code. If you need to access a value outside the function, you can use a `return` statement to pass the result back to the main program. This keeps your code clean, modular, and easy to manage!

<!-- #endregion -->

```python
def calculate_square(number):
    result = number * number  # 'result' is a local variable
    return result

# Call the function
square_of_5 = calculate_square(5)
print(square_of_5)


```

```python editable=true slideshow={"slide_type": ""} tags=["Raise Exception"]
# The following line will raise an error because 'result' is in the local scope of the function
print(result)  # NameError: name 'result' is not defined
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Determining Appropriate Inputs to Functions

Can the function `mm_to_in()` to take a list as an input? Look again at the code that the function executes. 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
## Call `help` on a custom function

Just like you can call `help()` on a function provided by a **Python** package such as **pandas** (e.g. `help(pd.DataFrame)`, you can also call `help()` on custom functions.  
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Call help on mean function from pandas
import numpy as np
help(np.mean)
```

```python editable=true slideshow={"slide_type": ""}
# Call help on your custom function
help(add_numbers)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Notice that when you call `help()` on custom functions, you will see the docstring that was provided in the function definition.  

The `help()` results for `np.mean` are simply longer because the docstring contains more information, such as sections for Notes and Examples. 

Combining related function calls into a single line of code allows you to write code that is much more efficient and less repetitive, assisting you in writing DRY code in **Python**. 

Congratulations! You have now written and executed your first custom functions in **Python** to efficiently modularize and execute tasks as needed.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->

<!-- #endregion -->