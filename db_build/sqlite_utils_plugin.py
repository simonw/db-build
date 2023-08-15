import sqlite_utils


@sqlite_utils.hookimpl
def register_commands(cli):
    from .cli import cli as db_build_cli

    cli.add_command(db_build_cli, name="build")
