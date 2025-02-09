"""Snapshot tests for pyprefab templates."""

import pytest

# tomllib is not part of the standard library until Python 3.11
try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore


def test_changelog(cli_output, snapshot):
    """Location and contents of CHANGELOG.md are correct."""
    project_path, cli_result = cli_output
    with open(project_path / 'CHANGELOG.md', 'r') as f:
        changelog = f.read()
    assert changelog == snapshot


def test_contributing(cli_output, snapshot):
    """Location and contents of CHANGELOG.md are correct."""
    project_path, cli_result = cli_output
    with open(project_path / 'CONTRIBUTING.md', 'r') as f:
        contributing = f.read()
    assert contributing == snapshot


@pytest.mark.parametrize(
    'docs_file',
    [
        'conf.py',
        'index.rst',
        'CHANGELOG.md',
        'CONTRIBUTING.md',
        'README.md',
        'usage.md',
    ],
)
def test_docs_dir(cli_output, snapshot, docs_file):
    """Documentation contents are correct."""
    project_path, cli_result = cli_output
    with open(project_path / 'docs' / 'source' / docs_file, 'r') as f:
        file = f.read()
    assert file == snapshot


def test_readme(cli_output, snapshot):
    """Location and contents of README.md are correct."""
    project_path, cli_result = cli_output
    with open(project_path / 'README.md', 'r') as f:
        readme = f.read()
    assert readme == snapshot


def test_pyproject(cli_output, snapshot):
    """Location and content of pyproject.toml are correct."""
    project_path, cli_result = cli_output
    with open(project_path / 'pyproject.toml', 'rb') as f:
        pyproject = tomllib.load(f)
    assert pyproject == snapshot
