import textwrap
from typing import Tuple

from decipher.html_table_parser import TableHTMLParser


def extract_rune_name(metadata: str) -> Tuple[str, str]:
    """Extract rune and name from metadata (font matters)"""
    for line in metadata.split("\n"):
        if line.startswith("title"):
            title_line = line
    _, title = title_line.split("=", maxsplit=1)
    title = remove_chars(title)
    *_, rune, name = title.split(" ")
    return rune, name


def remove_chars(text: str, chars: tuple = ("`", '"', "'", "(", ")")) -> str:
    for char in chars:
        text = text.replace(char, "")
    return text


def parse_as_tag(text: str) -> str:
    if "*" in text:
        # Format as code
        return "`{0}`".format(text)
    else:
        # Format as text
        return "*{0}*".format(text)


def parse_html_table(text: str) -> str:
    parser = TableHTMLParser()
    parser.feed(text)
    match parser.table:
        case [["Form", "Syntax"], *_]:
            rows_formatted = []
            for row in parser.table[1:]:
                form = row[0]
                syntax = textwrap.indent(row[1], "    ")
                rows_formatted.append(f"{form}: >\n{syntax}\n<\n")
            return "".join(rows_formatted)
        case _:
            raise ValueError("HTML is not the expected table.")
