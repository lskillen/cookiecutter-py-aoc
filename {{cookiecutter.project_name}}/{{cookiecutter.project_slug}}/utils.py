"""Advent of Code: {{cookiecutter.year}} - Utilities."""
from __future__ import annotations

import pathlib

import rich
from colorhash import ColorHash
from rich.console import Control
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
    styles_at: dict[tuple[int, int], str] | None = None,
    default_style: str | None = None,
    empty_style: str = "dim black",
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
    console = rich.get_console()
    console.control(Control.home())
    grid = Table.grid(pad_edge=True)
    for _y in range(max_y):
        grid.add_column(justify="center", vertical="middle", ratio=1)

    styles = styles or {}
    styles_at = styles_at or {}
    for y in range(max_y):
        row = []
        for x in range(max_x):
            if not (symbol := coords.get((x, y))):
                symbol = "."
            if (style := styles_at.get((x, y))) or (style := styles.get(symbol)):
                pass
            else:
                if symbol == ".":
                    style = empty_style
                elif default_style:
                    style = default_style
                else:
                    c = ColorHash(symbol)
                    style = f"bold {c.hex}"
                styles[symbol] = style
            row.append(f"[{style}]{symbol}[/{style}]")
        grid.add_row(*row)
    rich.print()
    rich.print(grid)


def clear_screen() -> None:
    """Clear the screen."""
    console = rich.get_console()
    console.clear()
