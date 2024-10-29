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

# Code workflow logic

## Execute a Python script

There are two primary ways to execute a Python script.

You are may already be familiar with the `python` command, and that it can take the name of a Python file and execute it

```bash
python my_program.py
```

When Python reads a file in this way, it executes all of the "top-level" commands that are not indented.
This is similar, but not identical, to the behavior of copying this file and pasting it line-by-line into an interactive
Python shell (or notebook cell).

The other way a Python script may be executed is to associate the file with a launch command.

### Non-Windows executables

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

### Windows executables

If your Windows machine has Python registered as the default application associated with `.py` files, then any Python
scripts can be run as commands. However, only one Python can be registered at a time, so all Python scripts run this
way will use the same Python environment.

Additionally, most Windows Python installs come with the [Python Launcher](https://docs.python.org/3/using/windows.html#python-launcher-for-windows)
which, in addition to allowing specifying the version of Python to run, can also read shebang lines and emulate some of that behavior.
This allows for shebang lines to be re-used between Linux, macOS, and Windows systems. However, on Windows the command must still
be prefaced with another command (`py`).

```bash
py my_program.py
# ✨ Hello from Python ✨
```

:::{tip}
While all Python files should end in a `.py`, this naming is necessary for Windows to associate a script with Python, as opposed
to Linux where `.py` is a convention and the shebang associates the file with Python.

While there is no in-source format that can tell Windows what to do with a Python code file, executing a
Python file with a shebang on Windows also does not cause any issues. Python just sees the whole line as
a comment and ignores it!

Because of these differences it is best practice to use both a shebang and `.py` for all Python scripts.
:::

## Executable comparisons

### Pros of passing a file to `python`:
- don't need execute permissions
- works on every system
- explicit about what you expect to happen

### Pros of inserting a shebang to the file:
- file is associated with specific python
  - don't have to remember which
- don't have to use the `python` command
  - don't have to even remember it is a Python script


# Share code

## Execute a python package

In [Code Workflow Logic][Code Workflow Logic] you learned of the two primary ways to execute a stand-alone Python script.
There are two other ways to execute Python as commands, both of which work for code that has been formatted as a package.

### Entrypoints

There is a special `entrypoint` a package can specify in its configuration which will direct installers to create an
executable command. Entrypoints are a general purpose plug-in system for Python packages, but the
[`console_scripts`](https://packaging.python.org/en/latest/specifications/entry-points/#use-for-scripts)
entry is specifically targeted at creating executable commands on systems that install the package.

The target of a `scripts` definition should be one function within your package, which will be directly executed
when the command is invoked in the shell. A `scripts` definition in your `pyproject.toml` looks like:

```toml
[project.scripts]
COMMAND = "my_package.my_module:my_function"
```

where `COMMAND` is the name of the command that will be made available after installation, `my_package` is the name of
your top-level package import, `my_module` is the name of any sub-modules in your package (optional, or may be
repeated as necessary to access the correct sub-module), and `my_function` is the function that will be called
(without parameters) when the command is invoked.

Scripts defined in project configuration, such as `pyproject.toml`, do not need to exist as independent files in
the package repository, but will be created by installation tools, such as `pip`, at the time the package is
installed, in a manner customized to the current operating system.

### Executable modules

The final way to make Python code executable directly from the command line is to include a
[`__main__` module](https://docs.python.org/3/library/__main__.html#module-__main__) in your package. Any package that
contains a `__main__` module and is installed in the current Python environment can be execute as a module
directly from the `python` command, without reference to any specific files.
```
python -m my_package
```

Try to create a `__main__.py` module in your package that will execute with the above command. (don't forget to
(re)install your package after creating this file!)

#### Further exploration

On your own or in small groups:

- What might be the advantages of making a packaged executable over providing script entrypoints?
- What are some disadvantages?
- Review the Pros section from [Executing Scripts][Executing Scrips]
  - Any similarities between executable packages and executable scripts?

#### More about main

You just learned that the `__main__` module allows a package to be executed directly from the command line with
`python -m`, but there is another purpose to the `__main__` name in Python. Any Python script that is executed
directly, by any of the methods you have learned to run Python code from the shell, will be given the name `__main__`
which identifies it as the first Python module loaded. This leads to the convention `if __name__ == "__main__":`, which 
you may have seen used previously.

This conditional is often used at the bottom of modules, especially modules that
are expected to be executed directly, to separate code that is intended to execute as part of a command from code that
is intended to execute as part of an import.

Try to create a single Python script that contains a `if __name__ == "__main__":` which makes the file print different
messages when it is executed from when it is imported from other Python code.
