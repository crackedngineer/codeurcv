# Local Development Setup

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — fast Python package manager
- [pandoc](https://pandoc.org/installing.html)
- [pdflatex](https://www.tug.org/texlive/) (via TeX Live or MiKTeX)

---

## 1. Clone the repo

```bash
git clone https://github.com/crackedngineer/codeurcv.git
cd codeurcv
```

## 2. Install Python dependencies

```bash
uv sync
```

This creates a virtual environment and installs all dependencies from `pyproject.toml`.

## 3. Install system dependencies

**pandoc**

| Platform | Command |
|----------|---------|
| Windows | `winget install --id JohnMacFarlane.Pandoc` |
| macOS | `brew install pandoc` |
| Debian/Ubuntu | `sudo apt install pandoc` |
| Fedora | `sudo dnf install pandoc` |
| Arch | `sudo pacman -S pandoc` |

**pdflatex**

| Platform | Command |
|----------|---------|
| Windows | `winget install --id MiKTeX.MiKTeX` |
| macOS | `brew install --cask mactex` |
| Debian/Ubuntu | `sudo apt install texlive-latex-base` |
| Fedora | `sudo dnf install texlive-latex` |
| Arch | `sudo pacman -S texlive-basic` |

Verify both are available:
```bash
pandoc --version
pdflatex --version
```

## 4. Install codeurcv in editable mode

```bash
uv pip install -e .
```

## 5. Run it

```bash
codeurcv generate examples/config.yml
```

---

## Running Tests

```bash
uv run pytest
```

## Linting & Formatting

```bash
uv run ruff format .
uv run ruff check .
uv run mypy src/
```

---

## Project Structure

```
.
├── CHANGELOG.md
├── CONTRIBUTING.md
├── pyproject.toml
├── README.md
├── release-please-config.json
├── SETUP.md
├── codeurcv/
│   ├── examples/
│   ├── src/
│   │   └── codeurcv/
│   │       ├── __init__.py
│   │       ├── __main__.py       # CLI entry point
│   │       ├── cli.py            # Typer commands
│   │       ├── core/
│   │       │   ├── constants.py
│   │       │   ├── dependency_checker.py
│   │       │   ├── logger.py
│   │       │   ├── markdown_converter.py
│   │       │   ├── plugin_loader.py
│   │       │   ├── renderer.py
│   │       │   ├── schema.py
│   │       │   ├── settings.py
│   │       │   └── template_loader.py
│   │       └── plugins/
│   │           ├── __init__.py
│   │           ├── base.py
│   │           └── minimalist/
│   │               ├── __init__.py
│   │               ├── plugin.py
│   │               └── template.tex
│   │      
│   └── tests/
├── example/
│   └── config.yml
```