import subprocess

import pytest
from typer.testing import CliRunner

from pyprefab.cli import app  # type: ignore

# tomllib is not part of the standard library until Python 3.11
try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore


@pytest.fixture
def cli_output(tmp_path):
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            'transporter_logs',
            '--author',
            "Miles O'Brien",
            '--description',
            "An app for parsin' transporter logs",
            '--directory',
            tmp_path,
        ],
    )
    return tmp_path, result


def test_pyproject(cli_output):
    project_path, cli_result = cli_output
    assert cli_result.exit_code == 0
    with open(project_path / 'pyproject.toml', 'rb') as f:
        pyproject = tomllib.load(f)
        assert pyproject.get('project', {}).get('name') == 'transporter_logs'
        assert pyproject.get('project').get('authors')[0].get('name') == "Miles O'Brien"
        assert pyproject.get('project').get('description') == "An app for parsin' transporter logs"


def test_lint(cli_output):
    """Files created by CLI should lint without errors."""
    project_path, cli_result = cli_output

    result = subprocess.run(['ruff', 'check', project_path], capture_output=True, text=True)
    assert result.returncode == 0


def test_build(cli_output):
    """Files created should build a valid python package."""
    project_path, cli_result = cli_output

    # pyprefab output should be a valid Python package
    result = subprocess.run(
        ['python', '-m', 'build', '--sdist', '--wheel'], capture_output=True, cwd=project_path, text=True
    )
    assert result.returncode == 0
