from datetime import datetime

from marko import Markdown

from decipher.helper import clean_markdown, extract_rune_name, parse_as_tag
from decipher.template import template
from decipher.vimdoc_renderer import VimDocRenderer


def run(text):
    _, metadata, content = text.split("+++", maxsplit=3)
    rune, name = extract_rune_name(metadata)
    rune_tag = parse_as_tag(rune)
    name_tag = parse_as_tag(name)
    temp = template.get_heading(level=1)
    heading = temp.substitute(
        name_upper=name.upper(),
        name_tag=name_tag,
        rune_tag=rune_tag,
    )
    content = clean_markdown(content)
    markdown = Markdown(renderer=VimDocRenderer)
    return heading + markdown(content).replace("\n>", ">")


def run_for_all_rune_files():
    file_names = (
        "bar.md",
        "buc.md",
        "cen.md",
        "col.md",
        "dot.md",
        "fas.md",
        "ket.md",
        "lus.md",
        "mic.md",
        "sig.md",
        "tis.md",
        "wut.md",
        "zap.md",
        "terminators.md",
    )
    temp = template.get_header()
    output = temp.substitute(today=datetime.today().strftime("%Y-%m-%d"))
    for name in file_names:
        with open(name, "r") as file:
            output = output + "\n\n" + run(file.read())
    return output
