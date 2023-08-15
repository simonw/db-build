import click
import pathlib
import sqlite_utils
from sqlite_utils.utils import TypeTracker, rows_from_file


@click.command()
@click.argument(
    "database",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "paths",
    type=click.Path(exists=True, file_okay=True, dir_okay=True, allow_dash=True),
    nargs=-1,
)
def cli(database, paths):
    "Build a SQLite database from files and directories"
    db = sqlite_utils.Database(database)
    paths = [pathlib.Path(path) for path in paths]
    for path in paths:
        if path.suffix == ".csv":
            with path.open("rb") as fp:
                rows, _ = rows_from_file(fp)
                tracker = TypeTracker()
                db[path.stem].insert_all(tracker.wrap(rows))
