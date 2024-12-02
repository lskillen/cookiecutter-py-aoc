from __future__ import annotations

import pathlib
import os

from cookiecutter.main import cookiecutter


def main() -> None:
    path = pathlib.Path(__file__).parent.resolve()
    os.system(f"cookiecutter {path}")
