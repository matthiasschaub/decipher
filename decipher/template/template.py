import os
from string import Template
from typing import Literal


def get_path(
    file_name: str,
    directory: str = None,
) -> str:
    if directory is None:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            file_name,
        )
    else:
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            directory,
            file_name,
        )


def get_heading(level: int) -> Template:
    path = get_path("heading-level-{0}.txt".format(level))
    with open(path, "r") as file:
        return Template(file.read())


def get_header(type_: Literal["rune", "stdlib"]) -> Template:
    path = get_path("header.txt", type_)
    with open(path, "r") as file:
        return Template(file.read())
