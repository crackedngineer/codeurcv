# Contributing to codeurcv

Thank you for your interest in contributing! Here's everything you need to get started.

---

## Ways to Contribute

- **Bug reports** — open an issue with steps to reproduce
- **Feature requests** — open an issue describing the use case
- **New templates** — add a LaTeX template under `src/codeurcv/templates/`
- **Code improvements** — bug fixes, refactors, tests
- **Documentation** — improve the README, add examples

---

## Development Setup

See [SETUP.md](SETUP.md) for full local setup instructions.

---

## Workflow

1. Fork the repository
2. Create a branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Run tests: `uv run pytest`
5. Commit using [Conventional Commits](#commit-style)
6. Open a Pull Request against `main`

---

## Commit Style

This project uses [Conventional Commits](https://www.conventionalcommits.org/) for automated versioning and changelog generation.

| Prefix | When to use | Version bump |
|--------|-------------|--------------|
| `feat:` | New feature or template | minor |
| `fix:` | Bug fix | patch |
| `docs:` | Documentation only | none |
| `chore:` | Maintenance, deps | none |
| `feat!:` or `fix!:` | Breaking change | major |

**Examples:**
```
feat: add academic resume template
fix: handle missing optional fields gracefully
docs: add researcher quickstart example
feat!: rename template config key from type to template
```

---

## Adding a Plugin

1. Create `src/codeurcv/plugins/<name>/template.tex`
<!-- 2. Add a sample render to `tests/fixtures/<name>/` -->
2. Document the template in the README template table
3. Open a PR with a screenshot of the rendered output

---

## Code Style

- Formatter: `ruff format`
- Linter: `ruff check`
- Type checker: `mypy`

Run all checks:
```bash
uv run ruff format . && uv run ruff check . && uv run mypy src/
```

---

## Questions?

Open an issue or start a Discussion on GitHub.