#!/bin/bash
set -euxo pipefail
git init -b main
git add .
git commit -m "init: {{cookiecutter.project_description}}"
git remote add origin git@github.com:{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
git push -u origin main --force
make install
pre-commit run -a
git add -u
git commit -m 'fix: formatting'
git push origin main
echo "Your Advent of Code toolkit is setup; you can safely delete 'setup.sh' now. :)"
