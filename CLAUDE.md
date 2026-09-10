# CLAUDE.md

This file provides guidance to Claude (Copilot, Claude Code, or the GitHub Copilot CLI) when working with code and tasks in this repository.

**Also see:** `.cursorrules` — the canonical AI instruction file (tool-agnostic, used by Cursor, Copilot, Claude Code).

## What this repository is

This is a **data science project starter template** (`repo-starter`). It contains `init_project.py`, which bootstraps new ML/data science projects with complete directory structure, tooling, and AI guidance.

**Not a finished project** — it's a template engine. When cloned and run, it generates a new project folder with:
- Python package setup via `uv` (fast Python package manager)
- Git + pre-commit hooks (linting & formatting)
- DVC (data version control)
- MkDocs (documentation site)
- Testing framework (pytest)
- Dev container configuration (VS Code)
- **AI instruction files** (`.cursorrules` + `CLAUDE.md`) — every generated project is AI-ready

## How to work with this repo

### AI instruction generation

`init_project.py` now generates **two AI guidance files** in every new project:

1. **`.cursorrules`** — canonical, tool-agnostic instruction file (picked up by Cursor, Copilot, Claude Code, and emerging LLM tooling)
2. **`CLAUDE.md`** — Anthropic-specific companion file (lighter, project-context summary)

This means **every generated project is AI-aware from day one**. When you or any AI assistant enters that project folder, the Copilot CLI or IDE will automatically load the guidance.
- Creates a new project directory by name (default: `my-ml-project`)
- Sets up git, uv, and dependencies (dvc, ruff, pytest, mkdocs, pre-commit)
- Scaffolds `.devcontainer/devcontainer.json` (hardcoded)
- Generates `mkdocs.yml` and `docs/index.md` templates
- Installs pre-commit hooks
- Initializes DVC

**When making changes to `init_project.py`:**
- Keep the script concise and idempotent where possible
- Use hardcoded config strings (YAML, JSON) inline for simplicity — they're intentionally embedded
- Update both AI instruction templates (`.cursorrules` + `CLAUDE.md`) if you change tooling, structure, or defaults
- Test the output by running: `python init_project.py test-project` and inspect the generated structure
- Verify AI instruction files are correctly generated and contain project-specific context
- Add comments to non-obvious subprocess calls or config choices

### Key design choices (do not change without discussion)

- **uv for package management** — faster than pip, PEP 621 compliant, lockfile support
- **ruff for linting & formatting** — single tool replaces flake8, black, isort
- **DVC for data versioning** — integrates with git, S3-ready
- **MkDocs Material theme** — professional docs, Obsidian-style links via mkdocstrings
- **Pre-commit hooks** — enforce linting before commit
- **Dev container** — reproducible environment, Python 3.12

### Documentation

- **This file** (`CLAUDE.md`) — AI assistant guidance
- **No formal README yet** — consider creating `README.md` if you want users to understand the template without running code
- **Inline comments in `init_project.py`** — explain any complex subprocess calls or config logic

### Testing & validation

When you make changes to `init_project.py`:
1. Run it: `python init_project.py test-output`
2. Check the generated directory structure is correct
3. Verify key files exist: `.devcontainer/devcontainer.json`, `mkdocs.yml`, `.pre-commit-config.yaml`, `pyproject.toml`
4. Optionally run `cd test-output && uv sync` to validate the environment setup
5. Clean up: `rm -rf test-output`

### Conventions

- **Python version:** 3.12 (defined in `.devcontainer/devcontainer.json`)
- **Naming:** generated projects use kebab-case (e.g., `my-ml-project`)
- **Config format:** YAML for MkDocs, JSON for dev container (as generated)
- **Dependency versions:** pinned in `init_project.py` (e.g., `ruff-pre-commit` v0.9.0). Update sparingly; test each change.

### When to ask for clarification

- Should we add new tools (e.g., black, mypy, docker)?
- Should dependencies be in `init_project.py` as hardcoded versions or read from a `requirements.txt` or `constraints.txt`?
- Should the generated project include example code or remain a blank scaffold?
- Is the dev container image appropriate for the target users (e.g., add CUDA for ML)?

## Useful commands (for you, as you work)

```bash
# Test the bootstrapper
python init_project.py new-test-project

# Inspect what was generated
ls -la new-test-project/
cat new-test-project/pyproject.toml
cat new-test-project/mkdocs.yml

# Validate the environment works
cd new-test-project
uv sync --locked
uv run pytest tests/

# Clean up after testing
cd ..
rm -rf new-test-project
```

## Co-evolution

This `CLAUDE.md` should grow as conventions change. If you and I agree on new guidelines (new tools, naming patterns, testing approaches), I'll update this file to keep it in sync with `init_project.py` and actual practice.
