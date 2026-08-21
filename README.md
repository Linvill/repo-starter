# 🚀 repo-starter

A lightweight bootstrapper script to initialize production-ready Python Data Science and ML projects with modern, high-performance tooling.

---

## ⚡ Quick Start

Run the bootstrapper script followed by your project name:

```bash
python init_project.py my-ml-project
```

## 🛠️ Setup Steps Breakdown

* **Project Directory Initialization**: Creates the target project folder and switches the execution context into it.
* **Git & `uv` Package Setup**: Runs `git init` and `uv init --package` to set up a clean `src/` layout package with a `pyproject.toml` and `uv.lock`.
* **Dependency Installation**: Adds core tooling (`dvc`, `ruff`, `pytest`, `mkdocs`, `mkdocs-material`, `mkdocstrings[python]`, `pre-commit`) via `uv add`.
* **Folder Hierarchy**: Scaffolds standard project subdirectories (`.devcontainer/`, `.github/workflows/`, `data/`, `docs/`, and `tests/`).
* **Dev Container Configuration**: Writes `.devcontainer/devcontainer.json` targeting Python 3.12, auto-syncing dependencies (`uv sync --locked`), and enabling recommended extensions (**Ruff**, **Python**, **DVC**).
* **Data Version Control (DVC)**: Runs `dvc init` and touches `data/.gitkeep` so Git tracks folder structure while ignoring raw data files.
* **Documentation Engine**: Configures `mkdocs.yml` with the Material theme and `mkdocstrings` for docstring parsing, alongside an initial `docs/index.md`.
* **Pre-Commit Quality Gates**: Generates `.pre-commit-config.yaml` for Ruff (linting/formatting) and DVC validation, then runs `pre-commit install`.
* **Git Hygiene**: Appends build folders, tool performance caches (`.ruff_cache`, `.pytest_cache`), virtualenvs (`.venv/`), and DVC data caches (`.dvc/cache/`) to `.gitignore`.

---

## 🧰 Included Toolchain

| Tool | Purpose | Advantage |
| :--- | :--- | :--- |
| **`uv`** | Package & Environment Manager | Fast Rust-based resolver and installer replacing `pip` and `poetry`. |
| **`DVC`** | Data Version Control | Tracks datasets and model weights via lightweight Git pointer files. |
| **`Ruff`** | Linter & Code Formatter | Ultra-fast Rust tool replacing `flake8`, `black`, and `isort`. |
| **`pytest`** | Automated Testing | Industry-standard framework for running unit and integration tests. |
| **`MkDocs Material`** | Technical Documentation | Generates searchable docs sites with auto-parsed Python docstrings. |
| **`pre-commit`** | Git Hook Automation | Enforces code formatting and quality checks automatically on commit. |

---

## 🔄 Daily Workflow Commands

```bash
# Synchronize environment with lockfile
uv sync

# Add project dependencies
uv add pandas scikit-learn
uv add --dev ipykernel

# Format and lint code
uv run ruff check --fix
uv run ruff format

# Run test suite
uv run pytest

# Preview documentation locally
uv run mkdocs serve

# Track data with DVC
uv run dvc add data/raw_dataset.csv
```

## File structure
```bash
my-ml-project/
├── .devcontainer/
│   └── devcontainer.json    # Dev container settings & recommended IDE extensions
├── .github/
│   └── workflows/           # Target directory for CI/CD automation pipelines
├── .dvc/                    # DVC metadata, configuration, and cache pointers
├── data/                    # Storage for raw/processed datasets (tracked by DVC)
│   └── .gitkeep
├── docs/                    # Technical documentation sources
│   └── index.md             # Documentation home page
├── src/                     # Source package root workspace
│   └── my_ml_project/
│       └── __init__.py
├── tests/                   # Pytest test suite directory
├── .gitignore               # Ignores build artifacts, caches, virtualenvs, & raw data
├── .pre-commit-config.yaml  # Pre-commit hook rules (Ruff lint/format & DVC checks)
├── mkdocs.yml               # MkDocs engine & theme configuration file
├── pyproject.toml           # Project metadata & dependency definitions
└── uv.lock                  # Deterministic dependency lockfile
```
