# {{cookiecutter.project_name}} by @{{cookiecutter.author_github_handle}}

{{cookiecutter.project_description}}

- **GitHub Repository**: <https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/>

## Getting Started

### 1. Create a New Repository

First, [create a repository on GitHub](https://github.com/new).

- Template: None (you don't need one!)
- Owner: "{{cookiecutter.author_github_handle}}"
- Repository Name: "{{cookiecutter.project_name}}"
- Description: "{{cookiecutter.project_description}}"
- Visibility: Up to you. :)

You can leave the rest because we'll initialize these automatically in the next step.

Next, you can _either_ execute the following in the root directory:

```bash
bash setup.sh
```

... or follow the rest of this README to do it manually. :)

**Note:** *Don't* blindly trust script files; go and look at it first. These are the exact instructions from this `README.md`, but in a single script.

### 2. Initialize the Repository

Then, run the following commands:

```bash
git init -b main
git add .
git commit -m "init: {{cookiecutter.project_description}}"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main --force
```

**Note:** Only pass `--force` the first time you initialize; not _every_ time!

**Note:** This assumes you're authenticating via `ssh` and you're [already setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### 3. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 4. Run the pre-commit hooks

Initially, the CI/CD pipeline might fail due to formatting issues. To resolve those run:

```bash
pre-commit run -a
```

Or, if you're outside of the devcontainer:

```bash
uv run pre-commit run -a
```

### 5. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add -u
git commit -m 'fix: formatting'
git push origin main
```

You are now ready to solve Advent of Code in style, with extra swagger!

## Devcontainer

If you're using devcontainers, just execute `code .` from the project directory, and you're _almost_ ready.

When it loads, make sure you hit "Reopen in Container" in VSCode (at the bottom-right):

![VSCode: Reopen in Container](https://github.com/user-attachments/assets/07da7773-8bd3-45b8-9f43-508f88b6c80f)

Yes, you have to do this everytime (but there are some shortcuts, like installing and using the [devcontainer CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli)).

## Project Structure

Within your project folder, i.e., {{cookiecutter.project_name}}/{{cookiecutter.project_slug}}, you've got a python file for each day you need to solve, such as `01.py`, as well as a corresponding input file, such as `input/01.txt`.

You can update the code to solve the puzzle and put your input in the text file as per Advent of Code (feel free to skip checking it in if you want; a nice way to do that is to add `{{cookiecutter.project_name}}/{{cookiecutter.project_slug}}/input/*` to your `.gitignore` file).

You've also got the following:

- `{{cookiecutter.project_name}}/{{cookiecutter.project_slug}}/runner.py`: The CLI; check it out for arguments, or execute just the project with `-h`.
- `{{cookiecutter.project_name}}/{{cookiecutter.project_slug}}/utils.py`: A utility file to get you started, but feel free to flesh it out. :)

## Executing the CLI

The CLI will:

- Run your solution for all days or the days you specify (comma-separated list).
- Provide the answers you generated, either example or real, for each day.
- Provide CPU and timing information for each day.
- Tell you whether it was a "golden" solution, i.e., it took less than one second.
- Tell you whether _all_ together are "golden"; i.e., _all_ took less than one second.

If you're in the devcontainer, just run the following:

```
python -m {{cookiecutter.project_name}}
```

Or, if you're outside of the devcontainer:

```
uv run python -m {{cookiecutter.project_name}}
```

### Redacting Output

If you'd like to redact the output (e.g., for sharing just timings elsewhere), execute the CLI with `--redact`.

## Executing Tests

If you'd like to execute your tests, you can pass `--test` to the CLI or execute `pytest`.

If you're in the devcontainer, just run the following:

```
pytest
```

Or, if you're outside of the devcontainer:

```
uv run pytest
```

## Attribution / Where Can I Get My Own?

For everyone else who isn't @{{cookiecutter.author_github_handle}}: This repository was created using [lskillen/cookiecutter-py-aoc](https://github.com/lskillen/cookiecutter-py-aoc), for a rockin' around the tree good time, developing Advent of Code solutions using Python+uv+ruff+mypy+pytest. Go there and find out how to get your own; yes, that means _you_!
