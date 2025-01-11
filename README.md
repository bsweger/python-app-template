# pyprefab

A Python template for personal use. The package itself doesn't do much, but I
keep it up to date as my Python workflow and tooling preferences evolve.

## Installing and running the package (no development)

To install this package via pip:

```bash
pip install git+https://github.com/bsweger/pyprefab.git
```

To run it:

```bash
hello_world
```

## Setup for local development

The instructions below outline how to set up a development environment based
on uv tooling.

Prerequisites:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

1. Clone this repository
2. Change to the repo's root directory:

    ```bash
    cd pyprefab
    ```

3. Create a Python virtual environment and install dependencies. The command
below creates a virtual environment in the `.venv` directory, installs Python
if needed, installs project dependencies (including dev dependencies), and
installs the package in
[editable mode](https://setuptools.pypa.io/en/stable/userguide/development_mode.html):

    ```bash
    uv sync
    ```

4. Run the test suite to confirm that everything is working:

    ```bash
    uv run pytest
    ```

### Updating dependencies

Use [`uv add`](https://docs.astral.sh/uv/reference/cli/#uv-add) to include a
new dependency in the project. This command will install the new dependency
into the virtual environment, add it to `uv.lock`, and update the
`dependencies` section of [`pyproject.toml`](pyproject.toml).

```bash
uv add <package-name>
```

To add a dependency to a specific group (adding a dev dependency, for example),
use the `--group` flag:

```bash
uv add <package-name> --group dev
```
