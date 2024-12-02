from __future__ import annotations

import os
import pathlib


def main() -> None:
    path = pathlib.Path(__file__).parent.resolve()
    os.system(f"cookiecutter {path}")  # noqa: S605
