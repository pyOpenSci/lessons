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

# Clean, Modular Code

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Part 1: 3 strategies

* Use consistent code format
* Use expressive object names
* Make your code DRY

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

### PEP 8 & consistent code format

* Generally accepted rules for code format: PEP 8
* Code Formatters: Tools to apply PEP 8 as you work!

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
#this code is not PEP8 compliant -- why?
def doStuff(a,b):print("Result:",a+b);return(a+b)
x = True
if(x):print("Messy code.");print("Oops!")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This code is PEP8 compliant -- why?
def do_stuff(number1, number2):
    print("Result:", number1 + number2)
    return number1 + number2

x = True
if x:
    print("This is nicer code.")
    print("Yay!")
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

#### Code format tools

* Jupyter code formatter (installed in this binder).
* Black
* Ruff

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

#### [Other tools to consider](tools-code-style)

* pre-commit hooks: if you use version control, they run when you commit changes
* setup VSCode (and other IDE's) to format on save®

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Expressive code

* Code can become documentation when written well.
* Use variable, function & class names that tell a user what each thing does

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

:::{figure} /images/clean-code/clean-code-expressive-variable-names-basmati-rice.png
:alt: "Image showing a large see-through Tupperware container with cookies in it but a label that says Basmati Rice."

This container clearly contains cookies, yet it's labeled "rice." This might be confusing to someone who is looking for rice in your kitchen! Consider this when writing code. It's easier for someone to understand your code without running it when your code variables describe the objects they contain. Source: Jenny Bryan, Reproducible Science Curriculum.
:::

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
# This code is PEP8 compliant -- why?
def do_stuff(number1, number2):
    print("Result:", number1 + number2)
    return number1 + number2

x = True
if x:
    print("This is nicer code.")
    print("Yay!")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# This code is PEP8 compliant -- why?
def calculate_sum(number1, number2):
    print("Result:", number1 + number2)
    return number1 + number2

is_valid = True
if is_valid:
    print("This is nicer code.")
    print("Yay!")
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## DRY code

* Don't Repeat Yourself
* use functions, loops and conditionals instead

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: slide
---
a = 5
b = 10
print(a + 2)
print(b + 2)
print(a * 2)
print(b * 2)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def process_number(x):
    print(x + 2)
    print(x * 2)

numbers = [5, 10]
for num in numbers:
    process_number(num)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

:::{admonition} Begin Activity One!
:class: tip
You are now familiar with 3 strategies for writing better, cleaner code. In the [first activity](clean-code-activity-1), you will apply these principles to example code.

Remember that this is not a test! Rather, it's a chance to think about how you write code and how others may receive it! 
:::
