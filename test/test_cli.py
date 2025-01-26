from unittest.mock import patch

from typer.testing import CliRunner

from pyprefab.cli import app  # type: ignore


def test_pyprefab_cli(tmp_path):
    runner = CliRunner()
    project_dir = tmp_path / 'test_cli'
    result = runner.invoke(
        app,
        ['pytest_project', '--author', 'Py Test', '--dir', project_dir],
        input='""\n',
    )
    assert result.exit_code == 0
    assert project_dir.exists()

    # project directory populated with template output contains expected folders
    dir_count = 0
    dir_names = []
    expected_dirs = ['.github', 'src', 'test']
    for child in project_dir.iterdir():
        if child.is_dir():
            dir_names.append(child.name)
            dir_count += 1
    assert dir_count == len(expected_dirs)
    assert set(dir_names) == set(expected_dirs)


def test_invalid_project_name(tmp_path):
    """Project name must be a valid Python identifier."""
    runner = CliRunner()
    result = runner.invoke(
        app,
        ['pytest-project', '--author', 'Py Test', '--dir', tmp_path],
        input='This is a test project\n',
    )
    assert result.exit_code != 0


def test_error_cleanup(tmp_path):
    """Error when creating a project should trigger cleanup."""
    project_dir = tmp_path / 'test_error'
    with patch('pyprefab.cli.render_templates', side_effect=Exception('Test exception')):
        runner = CliRunner()
        result = runner.invoke(
            app,
            ['pytest_project', '--description', '', '--dir', project_dir],
            input='Py Test\n',
        )
    assert result.exit_code != 0
    # pyprefab should remove project directory if an error occurs
    assert project_dir.exists() is False
