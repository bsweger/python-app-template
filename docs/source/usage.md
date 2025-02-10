# Using Pyprefab

## pyprefab CLI

By design, pyprefab requires only a few pieces of information to create the
boilerplate for a Python package.

```sh
>>> pyprefab --help

Usage: pyprefab [OPTIONS] NAME

🐍 Create Python package boilerplate 🐍

╭─ Arguments ───────────────────────────────────────────────────────────────╮
│ *    name      TEXT  Name of the project [required]                       │
╰───────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────╮
│ *  --author       TEXT Project author [required]                          │
│ *  --description  TEXT Project description [required]                     │
│ *  --dir          PATH Directory that will contain the project [required] │
│    --docs              Include Sphinx documentation files                 │
│    --help              Show this message and exit.                        │
╰───────────────────────────────────────────────────────────────────────────╯
```

### Example CLI use

To create a Python package named `holodeck` in a directory named
`trek/code/holodeck`:

```sh
>>> pyprefab holodeck --author rbarclay \
>>> --description "personal holodeck programs" \
>>> --dir trek/code/holodeck

╭────────────── Project Created Successfully ────────────────╮
│ Created new project holodeck in trek/code/holodeck         │
│ Author: rbarclay                                           │
│ Description: personal holodeck programs                    │
╰────────────────────────────────────────────────────────────╯
```

The pyprefab command above creates scaffolding for the new `holodeck` package,
with the following files in `trek/code/holodeck`:

```sh
.
├── .github
│   └── workflows
│       ├── ci.yaml
│       ├── publish-pypi-test.yaml
│       └── publish-pypi.yaml
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.md
├── pyproject.toml
├── src
│   └── holodeck
│       ├── __init__.py
│       └── app.py
└── test
    └── test_app.py
```

:::{caution}
If the `--dir` option points to a non-empty directory, pyprefab will overwrite
the existing contents (after prompting you).
:::

### Optional project documentation

Pass the `--docs` option to pyprefab to include Sphinx-based documentation files
with the new package.

```sh
>>> pyprefab holodeck --author rbarclay \
>>> --description "personal holodeck programs" \
>>> --dir /users/becky/code/trek/code/holodeck \
>>> --docs
```

 This option adds a `docs` directory to the code base:

```sh
.
├── .github
│   └── workflows
│       ├── ci.yaml
│       ├── publish-pypi-test.yaml
│       └── publish-pypi.yaml
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.md
├── docs
│   └── source
│       ├── CHANGELOG.md
│       ├── CONTRIBUTING.md
│       ├── README.md
│       ├── _static
│       │   └── custom.css
│       ├── conf.py
│       ├── index.rst
│       └── usage.md
├── pyproject.toml
├── src
│   └── holodeck
│       ├── __init__.py
│       └── app.py
└── test
    └── test_app.py
```

### Interactive mode

If you don't explicitly pass the `--author`, `--description`, `--dir` options,
pyprefab will prompt for them:

```sh
>>> pyprefab holodeck --docs
Project author: rbarclay
Project description: personal holodeck programs
Project directory: trek/code/holodeck/docs

╭──────────── Project Created Successfully ─────────────╮
│ Created new project holodeck in trek/code/holodeck    │
│ Author: rbarclay                                      │
│ Description: personal holodeck programs               │
│ Documentation: trek/code/holodeck/docs                │
╰───────────────────────────────────────────────────────╯
```

## Creating a dev environment for the new package

Follow the steps below to create a development environment for Python packages
generated by pyprefab.

These directions use `uv`, but you can use your preferred tooling.

1. `cd` to the directory of the new Python package

2. Create a virtual environment and install the project dependencies:

    ```sh
    uv sync
    ```

3. Test the project setupt:

    ```sh
    uv run <your_package_name>
    ```

    You should see log output stating that the project has been set up correctly.

    For example:

    ```sh
    2025-01-13 02:29:08 [info] project_test successfully created.
    ```

    You can also run the tests:

    ```sh
    uv run pytest
    ```

### Previewing documentation

If your project includes the optional Sphinx documentation, make sure you can
build and preview the docs before updating them:

```sh
uv run --group docs sphinx-autobuild docs/source docs/_build/html
```

The output of the above command provides a URL for viewing the documentation
via a local server (usually http://127.0.0.1:8000).

```sh
The HTML pages are in docs/_build/html.
[sphinx-autobuild] Serving on http://127.0.0.1:8000
[sphinx-autobuild] Waiting to detect changes...
```

### Adding the project to git

To create a new git repository for the project (this is optional):

```sh
git init
git add .
git commit -am "Initial commit"
```

:::{tip}
If you use [pre-commit](https://pre-commit.com/), pyprefab's boilerplate
includes a baseline `pre-commit-config.yaml` configuration. To use it, make
sure the project has been added to git (see above) and install the pre-commit
hooks: `pre-commit install`
:::
