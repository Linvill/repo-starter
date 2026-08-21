# repo-starter
# 🚀 Enterprise Data Science & Machine Learning Project Bootstrapper

This repository contains a standardized, high-performance Data Science project architecture and automated bootstrapper script (`init_project.py`). It bridges the gap between exploratory data analysis and production software engineering by integrating modern tooling for package management, data versioning, automated linting, containerization, and interactive documentation.

---

## 📋 Table of Contents

- [🎯 Architecture & Design Philosophy](#-architecture--design-philosophy)
- [⚡ Quick Start & Remote Bootstrapping](#-quick-start--remote-bootstrapping)
- [🏗️ Generated Repository Hierarchy & Directory Layout](#️-generated-repository-hierarchy--directory-layout)
- [🛠️ Toolchain Selection Rationale](#️-toolchain-selection-rationale)
- [🐍 Complete Bootstrapper Code (`init_project.py`)](#-complete-bootstrapper-code-init_projectpy)
- [⚡ Developer Lifecycle & Workflows](#-developer-lifecycle--workflows)
  - [1. Environment Activation & Dependency Management (`uv`)](#1-environment-activation--dependency-management-uv)
  - [2. Data & Model Artifact Tracking (DVC)](#2-data--model-artifact-tracking-dvc)
  - [3. Code Quality, Formatting & Testing](#3-code-quality-formatting--testing)
  - [4. Interactive Documentation (`MkDocs`)](#4-interactive-documentation-mkdocs)
  - [5. Containerized Development (`VS Code / Cursor`)](#5-containerized-development-vs-code--cursor)
- [🔧 Troubleshooting & Cross-Platform Execution](#-troubleshooting--cross-platform-execution)

---

## 🎯 Architecture & Design Philosophy

Machine learning projects frequently suffer from technical debt due to loose organizational standards. This template enforces industry best practices:

* **Strict Environment & Lockfile Reproducibility:** Eliminates the "works on my machine" paradigm using `uv.lock` and isolated Docker devcontainers.
* **Decoupled Code and Data Storage:** Git handles code versioning; DVC handles large binary files, dataset tracking, and model artifacts.
* **High-Throughput Tooling:** Replaces legacy, slow Python tooling (`pip`, `conda`, `black`, `flake8`) with lightning-fast, Rust-backed alternatives (`uv`, `ruff`).
* **Source Package Standard:** Utilizes the `src/` layout pattern to prevent implicit imports, force proper package installations, and streamline test execution.
* **Cross-Platform Compatibility:** Avoids shell-dependent line ending bugs (`\r\n` CRLF issues in Bash on Windows) by driving execution through cross-platform Python scripts.

---

## ⚡ Quick Start & Remote Bootstrapping

You can generate a brand-new, fully initialized repository directly from your terminal using Python—without needing to manually clone or store bootstrapper scripts locally.

### One-Liner Execution (Remote Script)

Run this command in **Cmder**, **PowerShell**, or **Bash** to pull `init_project.py` directly from GitHub and construct your new workspace:

```cmd
python -c "import urllib.request; exec(urllib.request.urlopen('[https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/init_project.py').read](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/init_project.py').read)())" my-new-project
