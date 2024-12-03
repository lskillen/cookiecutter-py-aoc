"""Advent of Code: {{cookiecutter.year}} - Day #DAY."""
from __future__ import annotations

from . import utils


def example() -> str:
    return """
EXAMPLE
"""


def read_data(data: list[str] | None = None) -> tuple[list[int], list[int]]:
    data = data or utils.read_example(example())


def solve(data: list[str] | None = None) -> tuple[int, int]:
    p1, p2 = 0, 0
    return p1, p2


def test_solve() -> None:
    assert solve() == (0, 0)
