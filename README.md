# About
Repository to play with streamlit, loosely following the 30 days challenge at https://30days.streamlit.app/

# Dependency management

In my previous projects (open and closed source ones), I've been playing with virtual environments using pip and some custom designed bash scripts to run pip install and also to freeze the dependencies (especially the indirect or transitive ones) in requirements.txt files with the following hierarchy:
-  `requirements.in`: manually edited, with the package that is required for some new functionality
-  `requirements.txt`: after compilation of `requirements.in` using the following command
    > ```bash
    > pip-compile --generate-hashes --rebuild --no-strip-extras --emit-find-links ./../../requirements.in
    > ```
    a `requirements.txt` is generated and then used afterwards to run all necessary `pip install` instances
- `requirementsALL.txt`: installation of dependencies is done using 
    >```bash
    >python -m pip install -r ./../../requirements.txt
    >```
    and after installation is complete, all dependencies (direct, indirect and tooling of Python) is frozen as a file in source control system using the following command:
    >```bash
    >python -m pip freeze --all > ./../../requirementsALL.txt
    >```

All these steps are performed after the virtual environment is created so that dependencies are properly installed in virtual environment rather than on global Python environment. The detailed configuration can be seen in my sample-python-repo ([setup.sh](https://github.com/disouzam/sample-python-repo/blob/main/setup.sh))

While this process works well, I decided to understand the Poetry tool and the following resources were indeed useful:

- [Gerenciando pacotes e ambientes com Poetry - Live de Python #179 - por Eduardo Mendes](https://www.youtube.com/watch?v=ZOSWdktsKf0)
- [Python Poetry in 8 Minutes by ArjanCodes](https://www.youtube.com/watch?v=Ji2XDxmXSOM)
- [How to Create and Use Virtual Environments in Python With Poetry by ArjanCodes](https://www.youtube.com/watch?v=0f3moPe_bhk)

So this repository represents my first experience with Poetry.

## Installing Poetry

There are at least two ways to install Poetry: using pip to install in global Python environment or using PowerShell to install it (in Windows) using the following command:

```PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

For more details, see official documentation: [Python-Poetry website](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Initialization of project

To start using Poetry, it is enough to run (https://python-poetry.org/docs/basic-usage/#project-setup)

```bash
poetry new [name_of-the-project]
```

This command will prepare a folder structure for the project and also to create tests and also create a `pyproject.toml` file with project's metadata and its requirements.