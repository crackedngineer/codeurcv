<div align="center">

# 📄 codeurcv

**Turn a simple YAML or JSON file into a professional resume — instantly.**

[![PyPI version](https://badge.fury.io/py/codeurcv.svg)](https://badge.fury.io/py/codeurcv)
[![Python](https://img.shields.io/pypi/pyversions/codeurcv)](https://pypi.org/project/codeurcv/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Action](https://img.shields.io/badge/GitHub%20Action-available-blue?logo=github)](https://github.com/marketplace/actions/codeurcv)

Whether you're a student, working professional, or researcher — write your details once, get a polished PDF resume every time.

</div>

---

## ✨ Features

- **Simple input format** — describe your resume in a human-readable `.yml` or `.json` file. No LaTeX knowledge required.
- **Premium templates for free** — choose from a curated set of professionally designed resume templates.
- **GitHub Action** — automate resume generation on every push. Always have an up-to-date PDF in your repo.
- **Supports all profiles** — students, working professionals, and researchers are all first-class citizens.

---

## 🚀 Quickstart

```yaml
# resume.yml
basic_details:
  name: Jane Doe
  email: jane@example.com
  phone: "+1 555 000 0000"
  location: San Francisco, CA
  linkedin: linkedin.com/in/janedoe
  github: github.com/janedoe

summary: >
  Full-stack engineer with 5 years of experience building scalable web applications.

education:
  - institution: University of California, Berkeley
    degree: B.S. Computer Science
    year: 2019

work:
  - company: Acme Corp
    role: Senior Engineer
    start: Jan 2021
    end: Present
    highlights:
      - Led migration to microservices, reducing latency by 40%
      - Mentored a team of 4 junior engineers

skills:
  - category: Languages
    featured: 
        - Python
        - TypeScript
        - Go
  - category: Tools
    featured: 
        - Docker
        - Kubernetes
        - PostgreSQL
```

```bash
codeurcv generate example/config.yml
# → resume.pdf
```

---

## 📦 Installation

```bash
pip install codeurcv
```

### Dependencies

`codeurcv` requires two external tools to generate PDFs:

#### Pandoc

Pandoc is a universal document converter used to process templates.

| Platform | Command |
|----------|---------|
| Windows | `winget install --id JohnMacFarlane.Pandoc` or `choco install pandoc` |
| macOS | `brew install pandoc` |
| Debian/Ubuntu | `sudo apt install pandoc` |
| Fedora/RHEL | `sudo dnf install pandoc` |
| Arch/Manjaro | `sudo pacman -S pandoc` |

→ [Full Pandoc installation guide](https://pandoc.org/installing.html)

#### pdflatex (TeX Live / MiKTeX)

pdflatex is the LaTeX engine used to render the final PDF.

| Platform | Command |
|----------|---------|
| Windows | `winget install --id MiKTeX.MiKTeX` or `choco install miktex` |
| macOS | `brew install --cask mactex` |
| Debian/Ubuntu | `sudo apt install texlive-latex-base` |
| Fedora/RHEL | `sudo dnf install texlive-latex` |
| Arch/Manjaro | `sudo pacman -S texlive-basic` |
| openSUSE | `sudo zypper install texlive-latex` |

→ [TeX Live installation guide](https://www.tug.org/texlive/acquire.html) · [MiKTeX for Windows](https://miktex.org/download)

---

## ⚙️ GitHub Action

Automate your resume build on every push — the PDF is always up to date in your repository.

```yaml
# .github/workflows/resume.yml
name: Build Resume

on:
  push:
    paths:
      - "resume.yml"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Resume
        uses: crackedngineer/codeurcv@v1
        with:
          input: resume.yml
          output: resume.pdf

      - name: Commit PDF
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add resume.pdf
          git commit -m "chore: update resume" || echo "No changes"
          git push
```

---

## 🖼️ Templates

| Name | Best For |
|------|----------|
| `classic` | All-purpose, clean single column |
| `modern` | Tech roles, sidebar layout |
| `academic` | Researchers, publications-focused |
| `minimalist` | Design roles, typography-forward |

```bash
codeurcv generate resume.yml --template minimalist
```

---

## 📖 Local Setup

See [SETUP.md](SETUP.md) for full developer setup instructions.

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — contributions are welcome!

---

## 📜 License

[MIT](LICENSE) © codeurcv contributors