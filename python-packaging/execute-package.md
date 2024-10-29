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

# Execute a python package

In [Execute a Python script][#Execute_a_Python_script] you learned of the two primary ways to execute a stand-alone Python script.
There are two other ways to execute Python as commands, both of which work for code that has been formatted as a package.

## Executable modules

We have seen how The `python` command can be passed a file for execution, but it can alternatively be passed
the name of a module, exactly as would be used after an `import`. In this case, Python will look up the module
referenced in its installed packages, and when it finds the module, will execute it as a script.

This execution mode is performed with the `-m` flag, as in `python -m site`. It can be used in place of a file
path, but cannot be used in combination with a path, as there can only be one executing module.

:::{tip}
These commands both do the same thing, but one is much more portable, and easier to remember

```bash
python ./.venv/lib/python3.12/site-packages/pip/__main__.py
```

```bash
python -m pip
```
:::

On your own or in small groups:

Install the `my_program.py` module from the last lesson, and then try to get the same greeting as before using `-m`.


### Executable packages

The `-m` flag as described above only works for Python modules (files), but does not work for Python (sub-)packages (directories). This means that we cannot execute a command using only the name of our package when it is structured to use directories

Once our package grows, the top-level name `my_program` turns into a directory
```
project/
└── src/
    └── my_program/
        ├── __init__.py
        └── greeting.py
```

Which can't be executed
```bash
python -m my_program
python: No module named my_program.__main__; 'my_program' is a package and cannot be directly executed
```

Initially Python seems to be telling us that names of directories, including out top-level package name,
cannot be directly executes. But actually there is another lead in the error message that gives us the hint to make it work.

Earlier you learned that the `if __name__ == "__main__":` can protect parts of your script from executing
when it is imported, making that conditional only change the file's behavior as a script. There is a very
similar concept that can be used on whole packages.

Any package that contains a [`__main__.py` module](https://docs.python.org/3/library/__main__.html#module-__main__)
can be executed directly from the `python` command, without reference to any specific module files.

:::{note}
The `__main__.py` file typically doesn't have an `if __name__ == "__main__":` conditional in it, as its execution
is already separated out from the rest of the package.
:::

Try to create a `__main__.py` module in your package that will execute with the `python -m my_program`. (don't forget to
(re)install your package after creating this file!)

## Entrypoints

The final way to make Python code executable directly from the command line is to include a special entrypoint
into the package metadata. Entrypoints are a general purpose plug-in system for Python packages, but the
[`console_scripts`](https://packaging.python.org/en/latest/specifications/entry-points/#use-for-scripts)
entry is specifically targeted at creating executable commands on systems that install the package.

In `pyproject.toml` this specific entrypoint is configured as such

```toml
[project.scripts]
shiny = "my_program.greetings:shiny_hello"
```

In the above example `shiny` is the name of the command that will be made available after installation, `my_program` is the name of
your top-level package import, `greetings` is the name of the sub-package (optional, or may be
repeated as necessary to access the correct sub-package), and `shiny_hello` is the function that will be called.

The target of each `scripts` definition should always be one function within your package, which will be directly executed (without parameters)
when the command is invoked in the shell. The target function can live anywhere; it does not have to be in a `__main__.py` or under a `if __name__ == "__main__":`.

## Further exploration

On your own or in small groups:

- What might be the advantages of making a package executable over providing a script entrypoint?
- What are some disadvantages?
- Review the Pros section from [Executable _comparisons][Executable_comparisons]
  - Any similarities between executable packages and executable scripts?
  - Any similarities between scripts and executable scripts?
