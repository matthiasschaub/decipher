import logging
from pathlib import Path
import os
from datetime import datetime
from typing import Literal

from marko import Markdown

from decipher.helper import (
    clean_markdown,
    extract_rune_name,
    extract_title,
    parse_as_tag,
)
from decipher.template import template
from decipher.vimdoc_renderer import VimDocRendererRune, VimDocRendererStdlib


def run(type_: Literal["rune", "stdlib"], text):
    _, metadata, content = text.split("+++", maxsplit=3)
    title = extract_title(metadata)
    match type_:
        case "rune":
            rune, name = extract_rune_name(title)
            rune_tag = parse_as_tag(rune)
            head_tag = parse_as_tag(name)
            head = name.upper()
            markdown = Markdown(renderer=VimDocRendererRune)
        case "stdlib":
            rune_tag = ""
            head_tag = parse_as_tag(title)
            head = title
            markdown = Markdown(renderer=VimDocRendererStdlib)
    temp = template.get_heading(level=1)
    heading = temp.substitute(head=head, head_tag=head_tag, rune_tag=rune_tag)
    content = clean_markdown(content)
    return heading + markdown(content).replace("\n>", ">")


def run_all(type_: Literal["rune", "stdlib"], directory: Path):
    """Run for all files in current directory."""
    temp = template.get_header(type_)
    output = temp.substitute(today=datetime.today().strftime("%Y-%m-%d"))
    files = directory.glob('*.md')
    for file in files:
        if file.name in ("constants.md", "_index.md"):
            continue
        with open(file, "r") as f:
            logging.info("Reading file: " + str(file))
            output = output + "\n\n" + run(type_, f.read())
    return output
