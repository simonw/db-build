from click.testing import CliRunner
from db_build.cli import cli
import pathlib
import sqlite_utils

examples = pathlib.Path(__file__).parent / "examples"


def test_basic_csv(tmpdir):
    runner = CliRunner()
    db_path = str(tmpdir / "data.db")
    result = runner.invoke(cli, [str(db_path), str(examples / "test.csv")])
    db = sqlite_utils.Database(db_path)
    assert db.schema == (
        "CREATE TABLE [test] (\n"
        "   [county] TEXT,\n"
        "   [precinct] TEXT,\n"
        "   [office] TEXT,\n"
        "   [district] TEXT,\n"
        "   [party] TEXT,\n"
        "   [candidate] TEXT,\n"
        "   [votes] TEXT\n"
        ");"
    )
