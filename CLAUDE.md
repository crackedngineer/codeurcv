# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**codeurcv** is a Python CLI tool that generates professional PDF resumes from YAML/JSON input by rendering Jinja2 LaTeX templates and compiling them with `pdflatex`.

## Commands

```bash
# Install dependencies (creates venv automatically)
uv sync

# Run the CLI
uv run codeurcv generate <config.yml> [--out DIR] [--name FILENAME] [--template TEMPLATE]
uv run codeurcv templates    # list available templates
uv run codeurcv --version

# Lint & format
uv run ruff format .
uv run ruff check .

# Type check
uv run mypy src/

# Tests
uv run pytest
```

**External system dependencies** (must be installed separately):
- `pdflatex` — compiles LaTeX → PDF
- `pandoc` — converts Markdown fields → LaTeX

## Architecture

The resume generation pipeline in `core/renderer.py` orchestrates four sequential steps:

```
YAML/JSON input
  → ConfigLoader (core/config_loader.py)           — parse YAML or JSON
  → Pydantic validation (core/schema.py)           — typed ResumeConfig models
  → Plugin.preprocess() (plugins/<name>/plugin.py)
  → TemplateLoader (core/template_loader.py)       — Jinja2 with LaTeX-safe delimiters
  → Plugin.postprocess()
  → pdflatex subprocess                            — produces final PDF
```

### Key modules

| File | Role |
|------|------|
| `cli.py` | Typer commands: `generate`, `templates`, `--version` |
| `core/renderer.py` | Central orchestrator for the full pipeline |
| `core/schema.py` | Pydantic models — `ResumeConfig`, sections (`BasicDetails`, `Job`, `Education`, `Project`, `Skill`) |
| `core/config_loader.py` | Reads `.yml`/`.yaml`/`.json` input files |
| `core/plugin_loader.py` | Discovers `TemplatePlugin` subclasses via `pkgutil.iter_modules` |
| `core/template_loader.py` | Jinja2 environment with `\VAR{}`, `\BLOCK{}` delimiters for LaTeX compatibility |
| `core/markdown_converter.py` | Calls `pandoc` subprocess to convert Markdown → LaTeX |
| `core/dependency_checker.py` | Verifies `pandoc` and `pdflatex` are installed; prints platform-specific install hints |

### Plugin system

Templates live in `src/codeurcv/plugins/<name>/`:
- `plugin.py` — subclass of `TemplatePlugin` (ABC in `plugins/base.py`) with:
  - `name`, `description` class attributes
  - `template_path()` → Path to `.tex` file
  - `preprocess(data: ResumeConfig) -> ResumeConfig`
  - `postprocess(tex_content: str) -> str`
- `template.tex` — Jinja2 template using LaTeX-safe delimiters

Plugins are auto-discovered at runtime via `pkgutil.iter_modules` — no registration needed. The only built-in template is `minimalist`.

### Schema notes

`MarkdownContent` is a custom Pydantic type that transparently converts its value from Markdown to LaTeX during field assignment (via `markdown_converter.py`). Any schema field typed as `MarkdownContent` invokes pandoc on validation.

`ResumeSection` base class adds an optional `priority` field used for ordering sections.

### Jinja2 delimiters

Standard `{{ }}` delimiters conflict with LaTeX, so the template loader uses custom delimiters:

| Purpose | Delimiter |
|---------|-----------|
| Variable | `\VAR{...}` |
| Block | `\BLOCK{...}` |
| Comment | `%# ... #%` |

### Logging & output

Each run writes a log to `logs/codeurcv_<timestamp>.log`. The renderer wraps each pipeline step in a `_step()` helper that captures errors. Rich is used for styled terminal output.

## Release process

Uses `release-please` for automated semantic versioning. Version is read at runtime via `importlib.metadata` — do not edit version strings directly.

---

<!-- code-review-graph MCP tools -->
## MCP Tools: code-review-graph

**IMPORTANT: This project has a knowledge graph. ALWAYS use the
code-review-graph MCP tools BEFORE using Grep/Glob/Read to explore
the codebase.** The graph is faster, cheaper (fewer tokens), and gives
you structural context (callers, dependents, test coverage) that file
scanning cannot.

### When to use graph tools FIRST

- **Exploring code**: `semantic_search_nodes` or `query_graph` instead of Grep
- **Understanding impact**: `get_impact_radius` instead of manually tracing imports
- **Code review**: `detect_changes` + `get_review_context` instead of reading entire files
- **Finding relationships**: `query_graph` with callers_of/callees_of/imports_of/tests_for
- **Architecture questions**: `get_architecture_overview` + `list_communities`

Fall back to Grep/Glob/Read **only** when the graph doesn't cover what you need.

### Key Tools

| Tool | Use when |
|------|----------|
| `detect_changes` | Reviewing code changes — gives risk-scored analysis |
| `get_review_context` | Need source snippets for review — token-efficient |
| `get_impact_radius` | Understanding blast radius of a change |
| `get_affected_flows` | Finding which execution paths are impacted |
| `query_graph` | Tracing callers, callees, imports, tests, dependencies |
| `semantic_search_nodes` | Finding functions/classes by name or keyword |
| `get_architecture_overview` | Understanding high-level codebase structure |
| `refactor_tool` | Planning renames, finding dead code |

### Workflow

1. The graph auto-updates on file changes (via hooks).
2. Use `detect_changes` for code review.
3. Use `get_affected_flows` to understand impact.
4. Use `query_graph` pattern="tests_for" to check coverage.
