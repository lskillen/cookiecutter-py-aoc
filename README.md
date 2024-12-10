<p align="center">

![cookiecutter_py_aoc_logo](https://github.com/user-attachments/assets/f9922402-7a6b-44de-8281-e94e97434f80)

</p style = "margin-bottom: 2rem;">

---

[![Build status](https://img.shields.io/github/actions/workflow/status/lskillen/cookiecutter-py-aoc/main.yml?branch=main)](https://github.com/lskillen/cookiecutter-py-aoc/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11_%7C_3.12_%7C_3.13-blue?labelColor=grey&color=blue)](https://github.com/lskillen/cookiecutter-py-aoc/blob/main/pyproject.toml)
[![License](https://img.shields.io/github/license/lskillen/cookiecutter-py-aoc)](https://img.shields.io/github/license/lskillen/cookiecutter-py-aoc)

This is a modern [cookiecutter](https://github.com/cookiecutter/cookiecutter) project for generating a skeleton Python-based [Advent of Code](https://adventofcode.com) toolkit. Ready for you to fill out and solve the puzzles each year in Python. You bring the brains; I'll bring the brawny... templates. Features included:

- A fully containerized + devcontainer setup with Python 3.10 ready to go.
- Performance measuring CLI for executing your daily solutions in swagger-y style.
- Delightful [rich](https://github.com/Textualize/rich)-based colour highlighting.
- [uv](https://docs.astral.sh/uv/) for dependency management.
- Pre-commit hooks with [pre-commit](https://pre-commit.com/).
- Formatting with [ruff](https://github.com/charliermarsh/ruff) and [prettier](https://prettier.io/).
- Type checking with [mypy](https://mypy.readthedocs.io/en/stable/).
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/).
- Profiling with [Austin](https://github.com/P403n1x87/austin) and the [Austin VSCode Extension](https://github.com/P403n1x87/austin-vscode).
- Containerization with [Docker](https://www.docker.com/).
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers).
- Made with lurve. :heart:

Example of the CLI in action:

<p align="center">

![AoC Runner - In Action](https://github.com/user-attachments/assets/2457f365-497e-4da9-aa01-58f851f4a579)

</p style = "margin-bottom: 2rem;">

Example of the Austin-based profiling in action:

<p align="center">

![Austin Profiling - In Action](https://github.com/user-attachments/assets/33ab8a78-4475-44b6-9804-61b5ac7faf8b)

</p style = "margin-bottom: 2rem;">

---

## Quickstart

Note: For the best experience, it's recommended to use a combination of [Docker Desktop](https://www.docker.com/products/docker-desktop/) plus [VSCode](https://code.visualstudio.com/) because with a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers), you can do everything from within VSCode itself.

On your local machine, navigate to the directory in which you want to create a project directory, and run the following command with [uv installed](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uvx cookiecutter https://github.com/lskillen/cookiecutter-py-aoc.git
```

or if you don't have `uv` installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/lskillen/cookiecutter-py-aoc.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then, navigate your newly created project directory and follow the `README.md` instructions to complete your project setup. Happy Advent of Coding!

P.S. If you like what you use or use the project, send me some love with a star on GitHub (but it's optional!) ⭐

## Acknowledgements

This project is partially based on [Audrey
Feldroy](https://github.com/audreyfeldroy)\'s great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
repository.

It's also _heavily_ based on [Florian Maas](https://github.com/fpgmaas)' awesome [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv) repository.

Thank you to both so that we may AoC with joy!

## Author

Created by [Lee Skillen](https://github.com/lskillen); I build other things, including [Cloudsmith](https://cloudsmith.com).
