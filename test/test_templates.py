import subprocess

from typer.testing import CliRunner

from pyprefab.cli import app  # type: ignore

# tomllib is not part of the standard library until Python 3.11
try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore


def test_pyproject(tmp_path):
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
    assert result.exit_code == 0
    with open(tmp_path / 'pyproject.toml', 'rb') as f:
        pyproject = tomllib.load(f)
        assert pyproject.get('project', {}).get('name') == 'transporter_logs'
        assert pyproject.get('project').get('authors')[0].get('name') == "Miles O'Brien"
        assert pyproject.get('project').get('description') == "An app for parsin' transporter logs"


def test_build(tmp_path):
    """Files created should build a valid python package."""
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
    assert result.exit_code == 0

    # pyprefab output should be a valid Python package
    result = subprocess.run(
        ['python', '-m', 'build', '--sdist', '--wheel'], capture_output=True, cwd=tmp_path, text=True
    )

    assert result.returncode == 0
