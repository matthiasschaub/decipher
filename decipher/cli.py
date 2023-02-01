import logging
from pathlib import Path

import click

from decipher import main


@click.group()
@click.option("--log-level", "-l", default="debug")
@click.version_option()
def cli(log_level):
    logging.basicConfig(level=log_level.upper())


@cli.command("run")
@click.option("--type", "-t", type=click.Choice(("rune", "stdlib")), required=True)
@click.argument("input", type=click.File("r"), required=True)
@click.argument("output", type=click.File("w"), default="-")
def rune(type, input, output):
    """Decipher a single markdown file."""
    output.write(main.run(type, input.read()))


@cli.command("run-all")
@click.option("--type", "-t", type=click.Choice(("rune", "stdlib")), required=True)
@click.argument("input", type=click.Path(path_type=Path), required=True)
@click.argument("output", type=click.File("w"), default="-")
def all_runes(type, input, output):
    """Decipher all markdown files in current directory."""
    output.write(main.run_all(type, input))
