# pyprefab

A template-driven command line interface (CLI) that creates the scaffolding
for a fully-functional, modern Python package. The goal of pyprefab is to get
you straight to writing application code by handling project startup tasks
like logging setup and creating a test harness.

The scaffolding includes:

- project files in the [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) format
- `pyproject.toml` with [dependency groups](https://packaging.python.org/en/latest/specifications/dependency-groups/#dependency-groups)
- `CHANGELOG.md`, `CONTRIBUTING.md`, `.gitignore`, and `README.md`
- automated package versioning with [setuptools-scm](https://pypi.org/project/setuptools-scm/)
- [structlog](https://www.structlog.org/)-based pre-configured logging
- a [pytest](https://docs.pytest.org)-based test harness
- a [pre-commit](https://pre-commit.com/) configuration with common plugins like
[ruff](https://docs.astral.sh/ruff/) for linting (optional)
- GitHub workflow that automatically runs code checks, tests, and a test
coverage report
- GitHub workflows to publish the package to TestPyPI and PyPI

## Quickstart

If you have `uv` installed,
[`uv tool run`](https://docs.astral.sh/uv/reference/cli/#uv-tool-run) is the
fastest way to create a new Python package with pyprefab:

```sh
uvx pyprefab <name-of-new-package>
```

Otherwise, use `pip` or `pipx` to install pyprefab:

```sh
pip install pyprefab

pyprefab <name-of-new-package>
```

## Details

### pyprefab CLI

By design, pyprefab requires only a few pieces of information to create the
boilerplate for a Python package.

```bash
➜ pyprefab --help

  Usage: pyprefab [OPTIONS] NAME

 🐍 Create Python package boilerplate 🐍

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  Name of the project                                                                                      │
│                      [required]                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --author             TEXT  Project author                                                                                  │
│                               [required]                                                                                      │
│ *  --description        TEXT  Project description                                                                             │
│                               [required]                                                                                      │
│ *  --dir                PATH  Directory that will contain the project                                                         │
│                               [required]                                                                                      │
│    --help                     Show this message and exit.                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For example:

```sh
pyprefab project_test --author lassie --description "this is a pet project for lassie" --dir ~/code/lassie
```

If you don't explicitly pass the `--author`, `--description`, and `--dir` options,
pyprefab will prompt you for them:

```sh
➜ pyprefab project_test
Project author: lassie
Project description: this is a pet project for lassie
Project directory: /Users/dogs/code/lassie
```

## Creating a dev environment for the new package

Follow the steps below to create a development environment for Python packages
generated by pyprefab.

These directions use `uv`, but you can use your preferred tooling.

1. `cd` to the directory of the new Python package

2. Create a virtual environment and install the project dependencies:

    ```script
    uv sync
    ```

3. Test the project setupt:

    ```script
    uv run <your_package_name>
    ```

    You should see a log output stating that the project has been set up correctly.

    For example:
    `2025-01-13 02:29:08 [info     ] project_test successfully created.`

    You can also run the tests:

    ```script
    uv run pytest
    ```

**Optional:**

- Add the new project to a git repository:

    ```script
    git init
    git add .
    git commit -am "Initial commit"
    ```

- If you use [pre-commit](https://pre-commit.com/), pyprefab's boilerplate
includes a baseline `pre-commit-config.yaml` configuration. To use it, make
sure the project has been added to git (see above) and run the following
command to install the pre-commit git hook scripts:

    ```script
    pre-commit install
    ```

## Contributing to pyprefab

Please refer to
[CONTRIBUTING.md](https://github.com/bsweger/pyprefab/blob/main/CONTRIBUTING.md).
