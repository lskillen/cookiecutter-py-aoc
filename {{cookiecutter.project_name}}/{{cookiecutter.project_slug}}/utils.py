"""Advent of Code: {{cookiecutter.year}} - Utilities."""

import pathlib


def read_input(day) -> list[str]:
    """Read input for a day in."""
    path = pathlib.Path(__file__).parent.resolve()
    with open(f"{path}/input/{day}.txt") as f:
        return f.readlines()


def read_example(example: str) -> list[str]:
    """Read example input for a day in."""
    return example.strip().split("\n")
