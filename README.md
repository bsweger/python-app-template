# python_app

A Python template for personal use. The package itself doesn't do much, but I keep it up to date as my Python workflow
and tooling preferences evolve.

## Installing and running the package (no development)

To install this package via pip:

```bash
pip install git+https://github.com/bsweger/python-app-template.git
```

To run it:
```bash
hello_world
```

## Setup for local development

The steps below are for setting up a local development environment. This process entails more than just installing the package,
because we need to ensure that all developers have a consistent, reproducible environment.

The assumption is that app developers will be using a Python virtual environment that:

- is based on the Python version specified in [.python-version](.python-version).
- contains the dependency versions specified in the "lockfile" (in this case [requirements/requirements-dev.txt](requirements/requirements-dev.txt)).
- contains the package installed in ["editable" mode](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode).


1. Clone this repository
2. Change to the repo's root directory:

    ```bash
    cd python-app-template
    ```
3. Make sure the correct version of Python is currently active, and create a Python virtual environment:

    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:

    ```bash
    # MacOs/Linux
    source .venv/bin/activate

    # Windows
    .venv\Scripts\activate
    ```
5. Install the package dependencies and install the package in editable mode:

    ```bash
    python -m pip install -r requirements/requirements-dev.txt && python -m pip install -e .
    ```

6. Run the test suite to confirm that everything is working:

    ```bash
    python -m pytest
    ```

## Development workflow

Because the package is installed in "editable" mode, you can run the code as though it were a normal Python package, while also
being able to make changes and see them immediately. This is especially helpful when importing package components (because you
can avoid mucking with the Python path).

### Updating dependencies

Prerequisites:
- ['uv'](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started)

**Note:** using [`pipx`](https://pipx.pypa.io/stable/) (instead of pip) to install `uv` is a handy way to ensure that uv is available for all of the Python environments on your machine.

The "lockfile" for this project is simply an annotated requirements.txt that is generated by [uv](https://github.com/astral-sh/uv) (uv is a replacement for pip-compile, which
could also be used). There's also a requirements-dev.txt file that contains dependencies needed for development (_e.g._, pytest).

While it's possible to use `pip freeze` to generate a detailed lockfile without a third-party tool like uv, the output of `pip freeze` doesn't distinguish between direct and indirect dependencies or provide any information about why each dependency is included. This probably doesn't matter
for a small project, but on a large project, understanding the dependency graph is critical for resolving conflicts.

Additionally, uv (and pip-compile) are able to use the list of high-level dependencies in `pyproject.toml` to generate a detailed requirements.txt file, which is a good workflow for keeping everything in sync.

To add a dependency to the project:

1. Add the dependency to the `[dependencies]` section of `pyproject.toml` (or to the `dev` section of `[project.optional-dependencies]`, if it's a development dependency). Don't pin a specific version, since that will make it harder for people to install the package.
2. Generate updated requirements files:

    ```bash
    uv pip compile pyproject.toml -o requirements/requirements.txt && uv pip compile pyproject.toml --extra dev -o requirements/requirements-dev.txt
    ```
3. Update project dependencies:

    **Note:** This package was originally developed on MacOS. If you have trouble installing the dependencies. `uv pip sync` has a [`--python-platform` flag](https://github.com/astral-sh/uv?tab=readme-ov-file#multi-platform-resolution) that can be used to specify the platform.

    ```bash
    # note: requirements-dev.txt contains the base requirements AND the dev requirements
    #
    # using pip
    python -m pip install -r requirements/requirements-dev.txt
    #
    # alternately, you can use uv to install the dependencies: it is faster and has a
    # a handy sync option that will cleanup unused dependencies
    uv pip sync requirements/requirements-dev.txt

## Opinionated notes on Python tooling

The Python ecosystem is overwhelming! Current opinionated preferences, subject to change:

- To install and manage various versions of Python: [pyenv](https://github.com/pyenv/pyenv) + a local .python-version file
- To install Python packages that are available from anywhere on the machine, regardless of which Python environment is activated: [pipx](https://pipx.pypa.io/stable/)
- To create and manage Python virtual environments: [venv](https://docs.python.org/3/library/venv.html).
    - I like having the environment packages right there in the project directory
    - Everything single third-party tool for managing virtual environments (_e.g._, poetry, PDM, pipenv) does _too much_ and gets in my way
- To generate requirements files from `pyproject.toml`: ['uv'](https://github.com/astral-sh/uv?tab=readme-ov-file#getting-started). I don't usually recommend things this new, but it's orders of magnitude faster than `pip-compile`.
- To install dependencies: uv again (again, mostly due to speed; good old pip is another fine option)
- Logging: [structlog](https://www.structlog.org/en/stable/). I recently stopped fighting Python's built-in logging module and haven't looked back.
- Linting and formatting: [ruff](https://github.com/astral-sh/ruff) because it does both and is fast.

This is a test of the ruleset.
