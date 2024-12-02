#!/usr/bin/env python
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def run():
    # Generate days (and inputs) from template
    project_slug = "{{cookiecutter.project_slug}}"
    prefix_path = os.path.join(PROJECT_DIRECTORY, project_slug)
    template_path = os.path.join(prefix_path, "template.py")

    for n in range(1, 26):
        day = str(n).rjust(2, "0")
        day_path = os.path.join(prefix_path, f"{day}.py")

        # Create the file
        shutil.copyfile(template_path, day_path)

        # Replace the day variable
        with open(day_path, "r") as f:
            contents = f.read()
        contents = contents.replace("#DAY", day)
        with open(day_path, "w") as f:
            f.write(contents)

        # Generate empty input file
        with open(os.path.join(prefix_path, "input", f"{day}.txt"), "w") as f:
            f.write("")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    remove_file(template_path)


if __name__ == "__main__":
    run()
