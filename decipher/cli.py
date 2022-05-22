import logging

import click

from decipher import main


@click.group()
@click.option("--log-level", "-l", default="debug")
@click.version_option()
def cli(log_level):
    logging.basicConfig(level=log_level.upper())


@cli.command("rune")
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"), default="-")
def rune(input, output):
    """Decipher a single rune documentation markdown file."""
    output.write(main.run(input.read()))


@cli.command("all-runes")
@click.argument("output", type=click.File("w"), default="-")
def all_runes(output):
    """Decipher all pre-defined rune documentation markdown files in a directory."""
    output.write(main.run_for_all_rune_files())
