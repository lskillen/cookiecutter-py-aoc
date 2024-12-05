from __future__ import annotations

import os
import shlex
import subprocess
from datetime import datetime
from typing import Any

from tests.utils import run_within_dir


def test_bake_project(cookies: Any) -> None:
    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()


def test_using_pytest(cookies: Any, tmp_path: str) -> None:
    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Assert that project was created.
        year = datetime.now().strftime("%Y")
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == f"aoc{year}"
        assert result.project_path.is_dir()

        # Install the uv environment and run the tests.
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert subprocess.check_call(shlex.split("uv run make test")) == 0


def test_devcontainer(cookies: Any, tmp_path: str) -> None:
    """Test that the devcontainer files are created when devcontainer=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_not_devcontainer(cookies: Any, tmp_path: str) -> None:
    """Test that the devcontainer files are not created when devcontainer=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_dockerfile(cookies: Any, tmp_path: str) -> None:
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/Dockerfile")


def test_not_dockerfile(cookies: Any, tmp_path: str) -> None:
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/Dockerfile")


def test_oss_input_ignored(cookies: Any, tmp_path: str) -> None:
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "MIT license"})
        assert result.exit_code == 0
        file_path = f"{result.project_path}/.gitignore"
        with open(file_path) as f:
            contents = f.read()
            print(contents)
            assert f"{result.context['project_name']}/{result.context['project_slug']}/input/" in contents


def test_non_oss_input_allowed(cookies: Any, tmp_path: str) -> None:
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "None"})
        assert result.exit_code == 0
        file_path = f"{result.project_path}/.gitignore"
        with open(file_path) as f:
            contents = f.read()
            assert f"{result.context['project_name']}/{result.context['project_slug']}/input/" not in contents


def test_day_templates(cookies: Any, tmp_path: str) -> None:
    with run_within_dir(tmp_path):
        result = cookies.bake()
        year = datetime.now().strftime("%Y")
        for n in range(1, 26):
            day = str(n).rjust(2, "0")
            day_path = f"{result.project_path}/{result.context['project_slug']}/{day}.py"
            assert os.path.isfile(day_path)
            assert os.path.isfile(f"{result.project_path}/{result.context['project_slug']}/input/{day}.txt")
            with open(day_path) as f:
                contents = f.read()
            assert f"Advent of Code: {year} - Day {day}" in contents
