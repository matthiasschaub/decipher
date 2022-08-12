import textwrap
from typing import Tuple
from warnings import warn

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
                rows_formatted.append(f"{form}: >\n{syntax}\n<")
            return "\n".join(rows_formatted)
        case _:
            raise ValueError("HTML is not the expected table.")


def clean_markdown(text: str) -> str:
    """Reformat markdown list which are converted to HTML table."""
    start = "{% table %}"
    end = "{% /table %}"
    i_start = text.find(start)
    i_end = text.find(end)

    if i_start == -1 and i_end == -1:
        return text
    elif i_start == -1 or i_end == -1:
        warn("Found either start or end tag for a table but not both. Skipping ...")
        return text

    replace_with = (
        ("- Form", ""),
        ("- Syntax", ""),
        ("- Tall", "Tall:\n\n"),
        ("- Wide", "Wide:\n\n"),
        ("- ```", "```"),
        ("- Irregular", "Irregular:\n\n"),
        ("\n\n", "\n"),
        ("\n  ", "\n"),
        ("---", ""),
    )

    content = text[i_start + len(start) + 1 : i_end]

    for t in replace_with:
        if content.find(t[0]) == -1:
            return text
        content = content.replace(*t)
    content = content.lstrip()
    content = content.rstrip()

    text = text.replace(text[i_start : i_end + len(end)], content)
    return clean_markdown(text)
