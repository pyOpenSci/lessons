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

(execute-package)=
# How to Execute a Python Package

In [How to Execute a Python Script](execute-script) you learned about two primary ways to execute a stand-alone Python script.
There are two other ways to execute Python code from the command line, both of which work for code that has been formatted as a package.

1. You can [**execute modules**](#executable-modules) using their import name
2. You can [**execute packages**](#executable-packages) using a `__main__.py` file 
3. A package can provide arbitraty command names that execute parts of themselves

## 1. Executable modules

In the [Pass your script to the Python command lesson](execute-script-pass-to-python) you learned that the `python` command can
be passed a file path for execution. Alternatively you can also pass the name of a module, exactly as would be used after an `import`.
In this case, Python will look up the module referenced in the
[currently active environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments),
and will execute it as a script.

This execution mode is performed with the `-m` flag, as in `python -m site`. It can be used in place of a file
path, but cannot be used in combination with a path, as there can only be one executing module.

:::{tip}
These commands both do the same thing, but the latter is easier to remember and much more portable, as it doesn't rely
on the local machine's file system details.

```bash
python ./.venv/lib/python3.12/site-packages/pip/__main__.py
```

```bash
python -m pip
```
:::

### Further exploration

On your own or in small groups:

* Install the `my_program.py` module from the [last lesson](execute-script-launch-command)
* Try to get the same greeting as before using `python -m my_program`.

**my_program.py** which prints out `✨ Hello from Python ✨` when executed as a script.

```python
#!/usr/bin/env python
# The above line is a shebang and can take the place of typing python on the command line
# This comment is below, because shebangs must be the first line!

def shiny_hello():
    print("\N{Sparkles} Hello from Python \N{Sparkles}")

if __name__ == "__main__":
    shiny_hello()
```

## 2. Executable packages

The `-m` flag as described above only works for Python modules (files), but does not work for Python (sub-)packages (directories).
This means that you cannot execute a command using only the name of your package when it is structured to use directories

Once your package grows, the top-level name `my_program` turns into a directory.
(See [Python Package Structure](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html)
for when and how to create a package structure).
```
project/
└── src/
    └── my_program/
        ├── __init__.py
        └── greeting.py
```

However, you can never execute a directory.
```bash
python -m my_program
python: No module named my_program.__main__; 'my_program' is a package and cannot be directly executed
```

Initially, Python seems to tell you that the directory names, including your top-level package name,
cannot be directly executed. But the error message contains the hint that you need to make this run properly.

[Earlier you learned](execute-script-name-eq-main) that `if __name__ == "__main__":` can protect parts of your
script from executing when it is imported, making that conditional change the file's behavior when used as a script.
There is a very similar concept that can be applied to Python packages.

Any package that contains a [`__main__.py` module](https://docs.python.org/3/library/__main__.html#module-__main__)
can be executed directly using the `python` command, without reference to any specific module files.

:::{note}
The `__main__.py` file typically doesn't have an `if __name__ == "__main__":` conditional in it, as its execution
is already separated out from the rest of the package.
:::

### Further exploration

- Try to separate `my_program` into a package containing two files, including one `__main__.py`
- Try to get `python -m my_program` to work as before
- Does importing `my_program` still work [as before the separation](execute-script-name-eq-main)?

```python
import my_program

def guess_my_number():
    my_program.shiny_hello()
    print("Was your number 42?")

guess_my_number()
# ✨ Hello from Python ✨
# Was your number 42?
```

:::{attention}
Don't forget to (re)install your package after creating this file!
:::

## 3. Named Commands

The final way to make Python code executable directly from the command line is to include a special [entrypoint](https://packaging.python.org/en/latest/specifications/entry-points/)
into the package metadata. Entrypoints are a general purpose plug-in system for Python packages, but the
[`console_scripts`](https://packaging.python.org/en/latest/specifications/entry-points/#use-for-scripts)
entry is specifically targeted at creating executable commands on systems that install the package.

These commands are configured in your project's [`pyproject.toml`](https://www.pyopensci.org/python-package-guide/tutorials/pyproject-toml.html#what-is-a-pyproject-toml-file) file in the [`[project.scripts]`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#creating-executable-scripts) table.

```toml
[project.scripts]
shiny = "my_program.greetings:shiny_hello"
```

In the above example `shiny` is the name of the command that will be made available in the shell after installation,
`my_program` is the name of your top-level package import, `greetings` is the name of the sub-package (optional, or may be
repeated as necessary to access the correct sub-package), and `shiny_hello` is the function that will be called.

If this package was installed, the command would be made avalibel in your shell

```bash
shiny
# ✨ Hello from Python ✨
```

The target of each `scripts` definition should always be one function within your package, which will be directly executed (without arguments)
when the command is invoked in the shell. The target function can live anywhere; it does not have to be in a `__main__.py` or under a `if __name__ == "__main__":`.

### Further exploration

On your own or in small groups:

- List some advantages of making a Python package executable over providing a script entry point.
- List some disadvantages of making a Python package executable over providing a script entry point.
- Review the Pros section from [How to Execute a Python Script](execute-script-comparison)
  - Do you see any similarities between executable packages and executable script files?
  - Do you notice any similarities between entrypoint scripts and executable script files?