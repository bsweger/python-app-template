from typer.testing import CliRunner

from pyprefab.cli import app  # type: ignore


def test_pyprefab_cli(tmp_path):
    runner = CliRunner()
    result = runner.invoke(
        app,
        ['pytest_project', '--author', 'Py Test', '--directory', tmp_path],
    )
    assert result.exit_code == 0

    # project directory populated with tesmplate output should contain
    # two folders: src and test
    dir_count = 0
    dir_names = []
    for child in tmp_path.iterdir():
        if child.is_dir():
            dir_names.append(child.name)
            dir_count += 1
    assert dir_count == 3
    assert '.github' in dir_names
    assert 'src' in dir_names
    assert 'test' in dir_names
