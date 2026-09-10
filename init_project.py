import os
import sys
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

project_name = sys.argv[1] if len(sys.argv) > 1 else "my-ml-project"
project_dir = Path(project_name)

print(f"🚀 Bootstrapping data science project: '{project_name}'...")

# 1. Create project folder and change directory
project_dir.mkdir(parents=True, exist_ok=True)
os.chdir(project_dir)

# 2. Git init & uv init
subprocess.run(["git", "init", "-q"], check=True)
subprocess.run(["uv", "init", "--package", "--name", project_name, "-q"], check=True)
subprocess.run([
    "uv", "add", "dvc", "ruff", "pytest", "mkdocs", 
    "mkdocs-material", "mkdocstrings[python]", "pre-commit", "-q"
], check=True)

# 3. Create directory layout
for d in [".devcontainer", ".github/workflows", "data", "docs", "tests", ".github/instructions"]:
    Path(d).mkdir(parents=True, exist_ok=True)

# 4. Generate .devcontainer/devcontainer.json
devcontainer_json = """{
  "name": "Python & uv Dev Environment",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "features": {
    "ghcr.io/jsburckhardt/devcontainer-features/uv:1": {}
  },
  "postCreateCommand": "uv sync --locked",
  "customizations": {
    "vscode": {
      "extensions": [
        "charliermarsh.ruff",
        "ms-python.python",
        "Iterative.dvc"
      ]
    }
  }
}"""
Path(".devcontainer/devcontainer.json").write_text(devcontainer_json, encoding="utf-8")

# 5. Initialize DVC
subprocess.run(["uv", "run", "dvc", "init", "-q"], check=True)
Path("data/.gitkeep").touch()

# 6. Configure MkDocs
mkdocs_yml = f"""site_name: {project_name} Documentation
theme:
  name: material
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
"""
Path("mkdocs.yml").write_text(mkdocs_yml, encoding="utf-8")

index_md = f"""# {project_name}

Welcome to the documentation for **{project_name}**.

## Getting Started
Run `uv sync` to set up the local virtual environment.
"""
Path("docs/index.md").write_text(index_md, encoding="utf-8")

# 7. Pre-commit config
pre_commit_yaml = """repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/iterative/dvc
    rev: v3.59.0
    hooks:
      - id: dvc-pre-commit
        additional_dependencies: ['.[s3]']
"""
Path(".pre-commit-config.yaml").write_text(pre_commit_yaml, encoding="utf-8")

# 8. Update .gitignore
gitignore = """
# Python / Tools local caches
.venv/
.dvc/cache/
site/
.pytest_cache/
.ruff_cache/
"""
with open(".gitignore", "a", encoding="utf-8") as f:
    f.write(gitignore)

# 9. Generate .cursorrules (tool-agnostic AI instructions; also picked up by Claude, Copilot, etc.)
cursorrules = """# .cursorrules

This file provides guidance to AI assistants (Cursor, Copilot, Claude Code) when working with this project.

## Project type

This is a Python **data science / ML project** using:
- **uv** for fast Python package management
- **pytest** for testing
- **ruff** for linting & formatting (single tool for all style checks)
- **DVC** for data versioning
- **MkDocs** for documentation
- **Pre-commit hooks** for automated checks before commit

## How to work with this repo

1. **Setup:** Run `uv sync --locked` to install all dependencies into the local virtual environment
2. **Development:** Use `uv run pytest` to test, `uv run ruff check --fix` to lint
3. **Pre-commit:** Hooks auto-run on `git commit`; never force-skip them
4. **Documentation:** Add docstrings (Google or NumPy style) — they feed mkdocstrings
5. **Data:** Version large files with DVC; commit `.dvc` files to git

## Code style conventions

- Use **type hints** (PEP 484)
- Keep functions small and focused
- Write docstrings on public functions/classes
- Run ruff & pytest before pushing commits

## When to ask for clarification

- Should this project use a different ML framework?
- Do you want example notebooks or starter code?
- Should we add mypy (static type checking) or other tools?
"""
Path(".cursorrules").write_text(cursorrules, encoding="utf-8")

# 10. Optionally generate CLAUDE.md (Anthropic-specific; complements .cursorrules)
claude_md = f"""# CLAUDE.md

Guidance for Claude (and Claude Code) when working with **{project_name}**.

This project was bootstrapped by `repo-starter` with a complete data science setup.

## Quick context

- **Environment:** Python 3.12, managed by `uv`
- **Testing:** `uv run pytest tests/`
- **Linting:** `uv run ruff check --fix` (replaces black, flake8, isort)
- **Docs:** MkDocs + Material theme; view with `mkdocs serve`
- **Data:** Use DVC for anything large; commit `.dvc` files to git
- **Pre-commit:** Enforced before commit; don't bypass

## When helping with code

- Assume we want clean, type-hinted Python
- Suggest tests alongside code
- Keep module responsibilities clear
- Prefer small, composable functions

For more detail, see `.cursorrules` (the canonical AI instruction file for this project).
"""
Path("CLAUDE.md").write_text(claude_md, encoding="utf-8")

# 11. Install pre-commit hooks
subprocess.run(["uv", "run", "pre-commit", "install"], check=True)

print(f"✅ Project successfully bootstrapped in ./{project_name}!")