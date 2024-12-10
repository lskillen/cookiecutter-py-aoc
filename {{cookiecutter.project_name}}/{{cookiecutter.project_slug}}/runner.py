"""Advent of Code: {{cookiecutter.year}} - Run All The Things."""
from __future__ import annotations

import argparse
import ast
import contextlib
import dataclasses
import functools
import importlib
import inspect
import operator
import os
import sys
import textwrap
import time
import tracemalloc
from dataclasses import dataclass, field
from typing import Any, Callable

import psutil
import pytest
from rich.console import Console
from rich.table import Table
from rich_argparse import RichHelpFormatter

from . import utils


@dataclass
class PerfCounter:
    """Capture an inner block's execution time in nanoseconds, and cpu time."""

    trace_memory: bool = False
    elapsed: float = 0.0  # nanoseconds
    memory: float = 0.0  # max memory usage in bytes
    idle: float = 0.0
    iowait: float = 0.0
    irq: float = 0.0
    steal: float = 0.0
    system: float = 0.0
    user: float = 0.0

    __t1: float = 0.0
    __t2: float = 0.0
    __cpu: Any = field(default_factory=lambda: psutil.cpu_times_percent())
    __mem: float = 0.0

    def __enter__(self) -> PerfCounter:
        self.__t1 = self.__t2 = time.perf_counter_ns()
        self.__cpu = psutil.cpu_times_percent()  # Only for marking start
        if self.trace_memory:
            tracemalloc.start()
            tracemalloc.take_snapshot()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if self.trace_memory:
            tracemalloc.take_snapshot()
            self.memory = tracemalloc.get_traced_memory()[1]
        self.__t2 = time.perf_counter_ns()
        self.__cpu = psutil.cpu_times_percent()  # psutil handles delta
        self.elapsed = self.__t2 - self.__t1
        self.idle = self.__cpu.idle
        self.iowait = self.__cpu.iowait
        self.irq = self.__cpu.irq
        self.steal = self.__cpu.steal
        self.system = self.__cpu.system
        self.user = self.__cpu.user
        tracemalloc.stop()

    def __add__(self, other: PerfCounter) -> PerfCounter:
        return self.__operator__(operator.add, other)

    def __sub__(self, other: PerfCounter) -> PerfCounter:
        return self.__operator__(operator.sub, other)

    def __truediv__(self, other: PerfCounter | int | float) -> PerfCounter:
        return self.__operator__(operator.truediv, other)

    def __floordiv__(self, other: PerfCounter | int | float) -> PerfCounter:
        return self.__operator__(operator.floordiv, other)

    def __operator__(self, op: Callable, other: PerfCounter | int | float) -> PerfCounter:
        return PerfCounter(**{
            key: op(
                getattr(self, key),
                getattr(other, key) if isinstance(other, PerfCounter) else other,
            )
            for key in dataclasses.asdict(self)
            if not key.startswith("_")
        })


def generate_parser() -> argparse.ArgumentParser:
    """Generate the argument parser."""
    parser = argparse.ArgumentParser(
        prog="{{cookiecutter.project_slug}}",
        description="Advent of Code: {{cookiecutter.year}} (@{{cookiecutter.author_github_handle}})",
        epilog="Ho Ho Ho!",
        formatter_class=RichHelpFormatter,
        add_help=False,
    )
    parser.add_argument(
        "days",
        type=str,
        default="all",
        nargs="?",
        help="the days to execute, split by commas (default: all)",
    )
    parser.add_argument(
        "-h", "--help", action="store_true", help="show this help message and exit."
    )
    parser.add_argument(
        "-d",
        "--debug-path",
        default=None,
        nargs="?",
        help="debug the file path (and only execute *that* day)",
    )
    parser.add_argument(
        "-e", "--example", default=False, action="store_true", help="use example inputs."
    )
    parser.add_argument(
        "-m",
        "--memory",
        default=False,
        action="store_true",
        help="capture memory usage per day (note: this impacts performance!).",
    )
    parser.add_argument(
        "-p",
        "--profile",
        nargs="?",
        const=10,
        type=int,
        help="execute tests multiple times (default: 10) to get better performance statistics."
        "",
    )
    parser.add_argument(
        "-s",
        "--suppress-output",
        default=False,
        action="store_true",
        help="suppress the results output.",
    )
    parser.add_argument(
        "-r",
        "--redact",
        default=False,
        action="store_true",
        help="redact the solution values.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        default=False,
        action="store_true",
        help="disables output, colours and any interactive elements.",
    )
    parser.add_argument(
        "-t",
        "--test",
        default=False,
        action="store_true",
        help="execute tests (same as running 'pytest')",
    )
    return parser


def ns_to_s(ns: float | int) -> float:
    """Convert nanoseconds to seconds."""
    return round(ns / 1000000000.0, 6)


def yes_no(value: bool) -> str:
    """Convert boolean to a yes/no."""
    return ":star:" if value else "-"


def maybe_redact(value: str, redact: bool) -> str:
    """Maybe redact a value if asked to."""
    return "[dim grey]<redact>[/dim grey]" if redact else value


def purify_source(source: str) -> str:
    """Strip comments and other unneeded parts from source code."""
    return ast.unparse(ast.parse(source))


def run() -> None:  # noqa: C901
    """Execute the runner."""
    parser = generate_parser()
    args = parser.parse_args(sys.argv[1:])
    console = Console(force_interactive=False if args.quiet else None)

    if args.help:
        parser.print_help()
        return

    if args.debug_path:
        args.days = os.path.basename(args.debug_path.rstrip(".py"))

    days = [
        str(int(s)).zfill(2)
        for s in (range(1, 26) if args.days == "all" else args.days.split(","))
    ]

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

    if args.suppress_output:
        for day, module in modules.items():
            module.solve(data=inputs[day] if not args.example else None)
        return

    star = ":glowing_star:"
    tree = ":christmas_tree:"
    author = "{{cookiecutter.author_github_handle}}"
    table = Table(
        title=" ".join(
            textwrap.dedent(
                f"""
            {tree}{star}{tree}
            [link=https://adventofcode.com][b red]Advent of Code[/b red][/link]:
            [link=https://adventofcode.com/2024][yellow]2024[/yellow][/link]
            [green]by[/green]
            [magenta][link=https://github.com/{author}/]@{author}[/link][/magenta]
            {tree}{star}{tree}
            """
            ).splitlines()
        ),
        title_style="on navy_blue",
        caption_style="on navy_blue",
        row_styles=["", "bold"],
    )
    table.add_column("day", justify="right", style="bold cyan", no_wrap=True)
    table.add_column("p1", style="magenta")
    table.add_column("p2", style="green")
    table.add_column("cpu", justify="left", style="red")
    if args.memory:
        table.add_column("mem", justify="left", style="red")
        table.caption = (
            "[b u red]* Warning: Timings skewed due to memory profiling.[/b u red]"
        )
    table.add_column("sloc", justify="right", style="yellow")
    table.add_column("chars", justify="right", style="yellow")
    table.add_column("t/seconds", justify="right", style="blue")
    table.add_column("t<1", justify="center", style="not dim bold gold3")

    total_seconds = 0.0
    total_sloc = 0
    total_chars = 0

    def _add_row(
        day: str | None,
        p1: int | None,
        p2: int | None,
        pc: PerfCounter | None,
        sloc: int,
        chars: int,
        seconds: float,
    ) -> None:
        """Add a row to the table."""
        row = [
            f"[link=https://adventofcode.com/2024/day/{int(day)}]{day}[/link]"
            if day
            else "total",
            maybe_redact(str(p1), args.redact) if p1 is not None else "",
            maybe_redact(str(p2), args.redact) if p2 is not None else "",
            f"user {pc.user:0.2f}%, sys {pc.system:0.2f}%" if pc else "",
        ]

        if pc and args.memory:
            row.append(f"{pc.memory / (1024 * 1024):0.2f} MiB")

        row.extend([
            str(sloc),
            str(chars),
            f"{seconds:.6f}".ljust(8, "0"),
            yes_no(seconds < 1) + (" *" if args.memory else ""),
        ])

        table.add_row(*row)

    with console.status("[bold green]Solving ...") as status:
        for day, module in modules.items():
            counters = []
            once = not args.profile
            max_attempts = 1 if once else args.profile
            for _ in range(max_attempts):
                attempt = "" if once else f"(profiling {_ + 1} of {max_attempts})"
                with PerfCounter(trace_memory=args.memory) as pc:
                    counters.append(pc)
                    status.update(f"[bold green]Solving day {day} {attempt}...")
                    p1, p2 = module.solve(data=inputs[day] if not args.example else None)
            pc = functools.reduce(operator.add, counters) / len(counters)
            if p1 == 0 and p2 == 0 and args.days == "all":
                # Ignore uncompleted days, unless explicitly mentioned
                continue
            day_seconds = ns_to_s(pc.elapsed)
            source = purify_source(inspect.getsource(module))
            sloc = source.count("\n") + 1
            chars = len(source)

            _add_row(day, p1, p2, pc, sloc, chars, day_seconds)

            total_seconds += day_seconds
            total_sloc += sloc
            total_chars += chars

    # Add the total row
    _add_row(None, None, None, None, total_sloc, total_chars, total_seconds)

    console.print()
    console.print(table)
    console.print()


if __name__ == "__main__":  # pragma: no cover
    run()
