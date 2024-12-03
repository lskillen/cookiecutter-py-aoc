<p align="center">
  <img width="1024" src="https://github.com/lskillen/cookiecutter-py-aoc/blob/main/static/images/cookiecutter_py_aoc_logo.png?raw=true">
</p style = "margin-bottom: 2rem;">

---

[![Build status](https://img.shields.io/github/actions/workflow/status/lskillen/cookiecutter-py-aoc/main.yml?branch=main)](https://github.com/lskillen/cookiecutter-py-aoc/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/lskillen/cookiecutter-py-aoc/blob/main/pyproject.toml)
[![License](https://img.shields.io/github/license/lskillen/cookiecutter-py-aoc)](https://img.shields.io/github/license/lskillen/cookiecutter-py-aoc)

This is a modern [cookiecutter](https://github.com/cookiecutter/cookiecutter) project for generating a skeleton Python-based [Advent of Code](https://adventofcode.com) toolkit. Ready for you to fill out and solve the puzzles each year, in Python. You bring the brains, I'll bring the brawn-y templates. Features included:

- Performance measuring CLI, for executing your daily solutions in style.
- Delightful [rich](https://github.com/Textualize/rich)-based colour highlighting.
- [uv](https://docs.astral.sh/uv/) for dependency management.
- Pre-commit hooks with [pre-commit](https://pre-commit.com/).
- Formatting with [ruff](https://github.com/charliermarsh/ruff) and [prettier](https://prettier.io/).
- Type checking with [mypy](https://mypy.readthedocs.io/en/stable/).
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- Containerization with [Docker](https://www.docker.com/).
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers).
- Made with lurve. :heart:

Example of the CLI in action:

<p align="center">
  <img width="610" src="https://github.com/lskillen/cookiecutter-py-aoc/blob/main/static/images/aoc_runner.png?raw=true">
</p style = "margin-bottom: 2rem;">

---

## Quickstart

Note: It's recommend to use a combination of [Docker Desktop](https://www.docker.com/products/docker-desktop/) plus [VSCode](https://code.visualstudio.com/) for the best experience, because with a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers), you can do everything from within VSCode itself.

On your local machine, navigate to the directory in which you want to create a project directory, and run the following command with [uv installed](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uvx cookiecutter https://github.com/lskillen/cookiecutter-py-aoc.git
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/lskillen/cookiecutter-py-aoc.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the `README.md` to complete the setup of your project. Happy Advent of Coding!

## Acknowledgements

This project is partially based on [Audrey
Feldroy](https://github.com/audreyfeldroy)\'s great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository.

It's also _heavily_ based on [Florian Maas](https://github.com/fpgmaas)' awesome [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv) repository.

Thank you, to both, so that we may AoC in joy!

## Author

Created by [Lee Skillen](https://github.com/lskillen); I build other things, including [Cloudsmith](https://cloudsmith.com).
