"""Advent of Code: {{cookiecutter.year}} - Day #DAY."""
from __future__ import annotations

from . import utils


EXAMPLE = """
EXAMPLE
""".strip()


def read_data(data: list[str] | None = None) -> list[str]:
    """Read the data."""
    return data or utils.read_example(EXAMPLE)


def solve(data: list[str] | None = None) -> tuple[int, int]:
    """
    Solve the problem.

    You can write docstests here too:

    >>> solve()
    (0, 0)
    """
    data = read_data(data=data)  # noqa: F841 (delete this)
    p1, p2 = 0, 0
    return p1, p2


def test_solve() -> None:
    assert solve() == (0, 0)
