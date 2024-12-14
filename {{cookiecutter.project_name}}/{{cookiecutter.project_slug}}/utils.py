"""Advent of Code: {{cookiecutter.year}} - Utilities."""
from __future__ import annotations

import pathlib

import rich
from colorhash import ColorHash
from rich.table import Table


def read_input(day: str) -> list[str]:
    """Read input for a day in."""
    path = pathlib.Path(__file__).parent.resolve()
    with open(path / f"input/{day}.txt") as f:
        return [line.rstrip() for line in f.readlines()]


def read_example(example: str) -> list[str]:
    """Read example input for a day in."""
    return example.strip().split("\n")


def get_dimensions(lines: list[str]) -> tuple[int, int]:
    """Get the dimensions of the map."""
    return len(lines[0].strip()), len(lines)


def print_sparse_grid(
    max_x: int,
    max_y: int,
    coords: dict[tuple[int, int], str],
    styles: dict[str, str] | None = None,
    default_style: str | None = None,
    empty_style: str = "dim grey",
) -> None:
    """
    Print a sparsely populated grid (i.e. size plus contents).

    For styles, see:
    https://rich.readthedocs.io/en/stable/style.html

    Example, printing a small grid with "antennas" (auto-colored) and "antinodes" (red):

    coords = dict()
    coords[3, 1] = "#"
    coords[6, 7] = "#"
    coords[4, 3] = "a"
    coords[5, 5] = "a"
    utils.print_sparse_grid(max_x=10, max_y=10, coords=coords, styles={"#": "red"})
    """
    grid = Table.grid(pad_edge=True)
    for _y in range(max_y):
        grid.add_column(justify="center", vertical="middle", ratio=1)

    styles = styles or {}
    for y in range(max_y):
        row = []
        for x in range(max_x):
            if symbol := coords.get((x, y)):
                if (style := styles.get(symbol)) is None:
                    if default_style:
                        style = default_style
                    else:
                        c = ColorHash(symbol)
                        style = f"bold {c.hex}"
                    styles[symbol] = style
                row.append(f"[{style}]{symbol}[/{style}]")
            else:
                row.append(f"[{empty_style}].[/{empty_style}]")
        grid.add_row(*row)
    rich.print()
    rich.print(grid)
