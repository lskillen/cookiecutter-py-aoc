"""Advent of Code: {{cookiecutter.year}} - Day #DAY."""
from __future__ import annotations

from . import utils


EXAMPLE = """
DELETE_THIS_AND_PASTE_EXAMPLE_HERE
"""


def read_data(data: list[str] | None = None) -> list[str]:
    """Read the data (describe it)."""
    return data or utils.read_example(EXAMPLE)


def solve(data: list[str] | None = None) -> tuple[int | str, int | str]:
    """Solve the problem (describe it)."""
    data = read_data(data=data)  # noqa: F841 (delete this comment)
    p1, p2 = 0, 0
    return p1, p2


def test_solve() -> None:
    assert solve() == (0, 0)
