import os
from string import Template


def get_path(name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)


def get_heading(level: int):
    path = get_path("heading-level-{0}.txt".format(level))
    with open(path, "r") as file:
        return Template(file.read())


def get_header():
    path = get_path("header.txt")
    with open(path, "r") as file:
        return Template(file.read())
