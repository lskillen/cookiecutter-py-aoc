"""Advent of Code: {{cookiecutter.year}} - Run All The Things."""
from __future__ import annotations

import argparse
import contextlib
import importlib
import inspect
import os
import sys
import time
from collections.abc import Generator
from typing import Any, Callable

import psutil
import pytest
from rich.console import Console
from rich.table import Table
from rich_argparse import RichHelpFormatter

from . import utils


def generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="{{cookiecutter.project_slug}}",
        description="Advent of Code: {{cookiecutter.year}} (@{{cookiecutter.author_github_handle}})",
        epilog="Ho Ho Ho!",
        formatter_class=RichHelpFormatter
    )
    parser.add_argument(
        "days", type=str, default="all", nargs="?", help="The days to execute, split by commas (default: all)"
    )
    parser.add_argument("--redact", default=False, action="store_true", help="Redact the solution values.")
    parser.add_argument("--example", default=False, action="store_true", help="Use example inputs.")
    parser.add_argument("--test", default=False, action="store_true", help="Execute tests (same as running 'pytest')")
    return parser


@contextlib.contextmanager
def timer() -> Generator[Callable[[], tuple[Any, Any]]]:
    """Capture an inner block's execution time in nanoseconds, and cpu time."""
    # Initialize cpu counters
    cpu = psutil.cpu_times_percent()
    t1 = t2 = time.perf_counter_ns()

    def _timer() -> tuple[Any, Any]:
        t = t2 - t1
        return t, cpu

    yield _timer
    t2 = time.perf_counter_ns()
    cpu = psutil.cpu_times_percent()


def ns_to_s(ns: float | int) -> float:
    """Convert nanoseconds to seconds."""
    return round(ns / 1000000000.0, 6)


def yes_no(value: bool) -> str:
    """Convert boolean to a yes/no."""
    return "yes" if value else "no"


def format_cpu(cpu: Any) -> str:
    return f"user {cpu.user}%, sys {cpu.system}%"


def maybe_redact(value: str, redact: bool) -> str:
    """Maybe redact a value if asked to."""
    return "[dim grey]<redact>[/dim grey]" if redact else value


def run() -> None:
    parser = generate_parser()
    args = parser.parse_args(sys.argv[1:])

    days = [str(s).zfill(2) for s in (range(1, 26) if args.days == "all" else args.days.split(","))]

    if args.test:
        # Execute pytest, but only with the days specified
        pytest.main([
            f"{{cookiecutter.project_slug}}/{day}.py" for day in days
            if os.path.exists(f"{{cookiecutter.project_slug}}/{day}.py")
        ])
        return

    # Import all modules and read all inputs, upfront
    modules = {}
    inputs = {}
    for day in days:
        with contextlib.suppress(ImportError):
            modules[day] = importlib.import_module(f".{day}", __package__)
            inputs[day] = utils.read_input(day)

    table = Table(title="Advent of Code: {{cookiecutter.year}} (@{{cookiecutter.author_github_handle}})", row_styles=["", "dim"])
    table.add_column("day", justify="right", style="bold cyan", no_wrap=True)
    table.add_column("p1", style="magenta")
    table.add_column("p2", style="green")
    table.add_column("cpu", justify="left", style="red")
    table.add_column("sloc (chr)", justify="right", style="yellow")
    table.add_column("t (seconds)", justify="right", style="blue")
    table.add_column("gold (t<1)", justify="right", style="gold3")

    total_seconds = 0.0
    for day, module in modules.items():
        with timer() as t_day:
            p1, p2 = module.solve(data=inputs[day] if not args.example else None)
        if p1 == 0 and p2 == 0 and args.days == "all":
            # Ignore uncompleted days, unless explicitly mentioned
            continue
        t, cpu = t_day()
        day_seconds = ns_to_s(t)
        total_seconds += day_seconds
        source = inspect.getsource(module)
        sloc = source.count("\n")
        chars = len(source)
        table.add_row(
            day,
            str(maybe_redact(p1, args.redact)),
            str(maybe_redact(p2, args.redact)),
            format_cpu(cpu),
            f"{sloc} ({chars})",
            f"{day_seconds:.6f}".ljust(8, "0"),
            yes_no(day_seconds < 1),
        )

    table.add_row("total", "", "", "", "", f"{total_seconds:.6f}".ljust(8, "0"), yes_no(total_seconds < 1))

    console = Console()
    console.print(table)


if __name__ == "__main__":  # pragma: no cover
    run()
