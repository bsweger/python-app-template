# pyprefab

Creates a new Python package from an opinioned set of templates.

## Installing pyprefab

To install this package via pip:

```bash
pip install pyprefab
```

## Generating boilerplate for a new Python package

Use pyprefab's command line interface to create a new Python package:

```bash
➜ pyprefab-create --help

 Usage: pyprefab-create [OPTIONS] NAME

 Generate a new Python project from templates.

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    name      TEXT  Name of the project [default: None] [required]                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --author                    TEXT  Project author [default: None] [required]                                                │
│    --description               TEXT  Project description                                                                      │
│    --directory                 PATH  Directory that will contain the project (defaults to current directory) [default: None]  │
│    --install-completion              Install completion for the current shell.                                                │
│    --show-completion                 Show completion for the current shell, to copy it or customize the installation.         │
│    --help                            Show this message and exit.                                                              │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For example:

```
pyprefab-create project_test --author lassie --description "this is a pet project for lassie" --directory ~/code/lassie
```

## Setting up the package's dev environment

Follow the steps below to create a development environment for the package.

These directions use `uv`, but you can use your preferred tooling.

1. `cd` to the directory of the new Python package

2. Create a virtual environment seeded with pip:

    ```script
    uv venv --seed
    ```

3. Install dependencies + project as editable module

    ```script
    uv sync
    ```

4. Test the project setupt:

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

    **Note:** `uv run` runs commands in the virtual environment created by uv
    (see step 2). Alternately, you can activate the virtual environment the
    old-fashioned way and then run commands without the `uv run` prefix:

    ```script
    source .venv/bin/activate
    <your package name>
    pytest
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
