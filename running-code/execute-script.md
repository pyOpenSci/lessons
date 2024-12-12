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

(execute-script)=
# How to Execute a Python Script

There are two primary ways to execute a Python script.

The first way to execute a Python script is to use the  `python` command. The `python` command takes the name of a Python file and executes the file from a command in your shell, like this:

```bash
python my_program.py
```

When Python reads a file in this way, it executes all of the "top-level" commands that are not indented.
This is similar, but not identical, to the behavior of copying this file and pasting it line-by-line into an interactive
Python shell (or a Jupyter notebook cell).

```python
def report_error():
  print("An error has occured")

print("\N{Sparkles} Hello from Python \N{Sparkles}")
```

Note that only one line is printed when this script is run. The `report_error` function only runs if you call it directly in the file. 

```bash
my_program.py
# ✨ Hello from Python ✨
```

### 2. Associate the file with a launch command

The other way a Python script may be executed is to associate the file with a launch command. The way in which
this association is done depends on what operating system you are running.

###  MAC / Linux / Non-Windows executables

On Linux or Mac systems, the Python file can itself be turned into a command. By adding a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))
as the first line in any Python file, and by giving the file [executable permissions](https://docs.python.org/3/using/unix.html#miscellaneous) the
file can be directly invoked without a `python` command.

```python
#!/usr/bin/env python
# The above line is a shebang, and can take the place of typing python on the command line
# This comment is below, because shebangs must be the first line!

def shiny_hello():
    print("\N{Sparkles} Hello from Python \N{Sparkles}")

shiny_hello()
```

```bash
my_program.py
# ✨ Hello from Python ✨
```

:::{tip}
Shebangs are a feature of [POSIX](https://en.wikipedia.org/wiki/POSIX). POSIX represents some level of compatibility between systems.
Linux, macOS, all BSDs, and many other operating systems are fully- or mostly-POSIX compliant.

Windows is not natively POSIX compliant. However, some "modes" inside of Windows are, such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/about)
(Windows Subsystem for Linux), gitbash, or some VSCode terminals.
:::

## Windows executables

If your Windows machine has Python registered as the default application associated with `.py` files, then any Python
scripts can be run as commands. However, only one Python can be registered at a time, so all Python scripts run this
way will use the same Python environment.

Additionally, most Windows Python installs come with the [Python Launcher](https://docs.python.org/3/using/windows.html#python-launcher-for-windows). This launcher allows you to specify the version of Python to run and also can read shebang lines and emulate some of that behavior.
This allows you to reuse shebang lines between Linux, macOS, and Windows systems. However, on Windows, the command must still
be prefaced with another command (`py`).

```bash
py my_program.py
# ✨ Hello from Python ✨
```

:::{tip}
All Python files should end in a `.py`. The `.py` is required for Windows to associate a script with Python. In comparison, on Linux and Mac machines, `.py` is a recommended best practice; the shebang (`!`) associates the file with Python.

 For simplicity and reproducibility, which ensures that your code runs consistently across machines, you should always just include the `.py` extension in your Python files~

Windows doesn’t rely on a shebang (`#!`) to determine how to execute a Python file; instead, it treats the shebang line in a Python file as a comment and ignores it. However, including a shebang in your script doesn’t cause any issues on Windows because Python just reads the line as
a comment and ignores it!

Because of these differences between Mac/Linux and Windows, it is best practice to use both a shebang in your .py files and to add the `.py` extension for all Python scripts.
:::

## Comparing passing files to Python vs the "shebang" (`#!`) execution approach  

There are pros and cons of using the two approaches above to executive Python files. 

### Pros of passing a file to `python`:
- don't need execute permissions
- works on every system
- explicit about what you expect to happen

### Pros of inserting a shebang to the file:
- file is associated with specific python
  - don't have to remember which
- don't have to use the `python` command
  - don't have to even remember it is a Python script


## Separating script from import behavior

Sometimes a Python file that is useful to execute is also useful to import. You may want to use `shiny_hello`
in another Python file. But right now, the `my_program.py` does all its script behavior even when it is imported. Consider

```python
import my_program

def guess_my_number():
    my_program.shiny_hello()
    print("Was your number 42?")

guess_my_number()
# ✨ Hello from Python ✨
# ✨ Hello from Python ✨
# Was your number 42?
```

You may not have expected it to print the hello twice, but it did. This is because `my_program` is set to
_always_ call `shiny_hello`, and now `guess_my_number` also calls it. That's two times. How can we make
`my_program` only call `shiny_hello` when it is used as a script?

You may have already seen the answer, without realizing what it was doing. `my_program` needs a conditional that checks if is is in "script mode" or "import mode" and that conditional is `if __name__ == "__main__":`.

This conditional is  most often included at the bottom of modules  that are expected to be executed
directly. This conditional separates code that is intended to execute as part of a command or script from code that is intended to
execute as part of an import within another script.

```python
#!/usr/bin/env python
# The above line is a shebang and can take the place of typing python on the command line
# This comment is below, because shebangs must be the first line!

def shiny_hello():
    print("\N{Sparkles} Hello from Python \N{Sparkles}")

# By calling shiny_hello within this conditional, it will only run when this file is run as a script. It will 
# not run if you import it into another script. 
if __name__ == "__main__":
    shiny_hello()
```

```bash
my_program.py
# ✨ Hello from Python ✨
```

```python
import my_program

def guess_my_number():
    my_program.shiny_hello()
    print("Was your number 42?")

guess_my_number()
# ✨ Hello from Python ✨
# Was your number 42?
```

:::{note} Why did that work?

All Python modules (individual files) have a `__name__` attribute, which is usually the same as the name used to import the module.

```python
import os
print(os.__name__)
# 'os'
```

This attribute is available within a module by using a global `__name__`. So in the `os.py` module, `__name__`
also gives the value `'os'`.

Importantly, this name is changed for the *first user-module* executed by Python. When you pass a file to
`python`, that is the first user-module executed. For this module, and only when it is the first, the `__name__`
is changed to the string `'__main__'`. This answers the question for every module used in a Python program, "am I the main module?".
:::
