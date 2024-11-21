# Assignment 1 for Numerical Algorithms

## Generating assignment outputs

For this assignment we need to submit the Jupyter notebook (executed, with cell output),
as well as a PDF version of the same thing. Since committing notebooks with cell output 
to git can result in all sorts of issues, particularly in collaborative work, we've set 
up a process to automatically generate these outputs using GitHub Actions. 

Whenever the main branch is updated on GitHub, this triggers a GitHub Action which will
run the [hw1.ipynb](hw1.ipynb) notebook. The result is then converted into PDF format
using nbconvert. Both the executed notebook and PDF are exported, and can be downloaded
from the GitHub repo, by navigating to `Actions` -> `<top workflow run>` -> 
`Artifacts/results`.

## Getting started

This repository uses _uv_ to manage Python and its dependencies, and _pre-commit_ to run
automatic code linting & formatting.

1. Install [uv](https://github.com/astral-sh/uv)

2. Navigate to this project directory

3. Install pre-commit:

```zsh
# We can use uv to install pre-commit!
uv tool install pre-commit --with pre-commit-uv --force-reinstall

# Check that pre-commit installed alright (should say 3.8.0 or similar)
pre-commit --version

# After installing pre-commit, you'll need to initialise it.
# This installs all pre-commit hooks, the scripts which run before a commit.
pre-commit install

# It's a good idea to run pre-commit now on all files.
pre-commit run --all-files
```

4. Run code:

```zsh
uv run <PATH-TO-PYTHON-FILE>
```

## Adding new packages with uv

It's simple to add a Python package to the project with uv using `uv add`.
For instance, to install numpy and scipy, and add them to the dependency graph, run:

```zsh
uv add numpy scipy
```

To remove a package dependency, e.g., scipy, run:

```zsh
uv remove scipy
```

## Running JupyterLab with uv

uv can also be used to run Jupyter, the same way as we run Python scripts:

```zsh
# If Jupyter Lab isn't already installed, add it as a dependency
uv add jupyterlab

# Start a JupyterLab server
uv run jupyter lab
```


## Pre-commit hooks

I've included a couple of pre-commit hooks 
(see [.pre-commit-config.yaml](.pre-commit-config.yaml)) which will be executed every 
time we commit code to git. Two of these hooks come from the 
[ruff](https://github.com/astral-sh/ruff) Python linter:
- `ruff`: lints Python code to ensure it adheres to the PEP8 standards. Includes a bunch of nice things like automatic sorting of imports by name and type.
- `ruff format`: formats Python code in a consistent manner, including removing excess whitespace, swapping tabs for spaces, and a _tonne_ of other things.

These should help to keep code tidy and consistent, with no extra effort on our part. 

The third hook is from the [nbstripout](https://github.com/kynan/nbstripout) project,
and will remove the cell outputs from every notebook before committing. This is good 
practice and helps to avoid merge conflicts, especially when collaborating on notebooks.

All of the hooks should run automagically if you've followed the setup instructions for
[installing pre-commit with uv](#getting-started).
