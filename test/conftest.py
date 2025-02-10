import pytest
from typer.testing import CliRunner

from pyprefab.cli import app  # type: ignore


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
            'An app for parsin\' "transporter logs"',
            '--dir',
            tmp_path,
            '--docs',
        ],
    )
    return tmp_path, result
