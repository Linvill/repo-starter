import os
import sys
import subprocess
from pathlib import Path

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
for d in [".devcontainer", ".github/workflows", "data", "docs", "tests"]:
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

# 9. Install pre-commit hooks
subprocess.run(["uv", "run", "pre-commit", "install"], check=True)

print(f"✅ Project successfully bootstrapped in ./{project_name}!")