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
- **Clickable project links** — add a `link` field to any project and it becomes a clickable hyperlink in the PDF.
- **Special character safe** — fields like company names, skill categories, and project names support `&`, `_`, `%`, and other special characters automatically.
- **GitHub Action** — automate resume generation on every push. Always have an up-to-date PDF in your repo.
- **Supports all profiles** — students, working professionals, and researchers are all first-class citizens.

---

## 🚀 Quickstart

```yaml
# config.yml
basic_details:
  name: Jane Doe
  email: jane@example.com
  phone: "+1 555 000 0000"
  linkedin: "https://linkedin.com/in/janedoe"
  github: "https://github.com/janedoe"

summary: >
  Full-stack engineer with 5 years of experience building scalable web applications.

education:
  - institution: University of California, Berkeley
    location: Berkeley, CA
    degree: B.S. Computer Science
    year: 2019
    gpa: "3.9/4.0"

work:
  - company: Acme Corp
    role: Senior Engineer
    location: San Francisco, CA
    start: Jan 2021
    end: Present
    achievements:
      - Led migration to microservices, reducing latency by 40%
      - Mentored a team of 4 junior engineers
    technologies:
      - Python
      - Kubernetes

projects:
  - name: My Project
    link: "https://github.com/janedoe/my-project"  # optional — becomes a clickable link in the PDF
    start: Mar 2023
    end: Present
    description:
      - Built an open-source CLI tool with 200+ GitHub stars
    technologies:
      - Python
      - Docker

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
codeurcv run config.yml
# → resume.pdf
```

---

## 💻 Usage

```bash
codeurcv run config.yml                    # generate PDF (outputs resume.pdf in current directory)
codeurcv run config.yml -o ./output        # specify output directory
codeurcv run config.yml -n john-doe        # custom output filename
codeurcv run config.yml -t minimalist      # choose template
codeurcv templates                         # list available templates
codeurcv --version
```

---

## 📦 Installation

```bash
pip install codeurcv
```

### Dependencies

`codeurcv` requires two external tools to generate PDFs:

#### Pandoc

Pandoc is a universal document converter used to process Markdown fields.

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

## 🖼️ Templates

| Name | Description |
|------|-------------|
| `minimalist` | Clean minimalist resume style |

```bash
codeurcv run config.yml --template minimalist
```

---

## 📖 Local Setup

See [SETUP.md](SETUP.md) for full developer setup instructions.

---

## ⚡ GitHub Action

Automate resume generation on every push using the official GitHub Action.

```yaml
- uses: crackedngineer/codeurcv-action@v1
  with:
    config-path: config.yml
    out-dir: output
    template: minimalist
    filename: john-doe-resume
```

→ [codeurcv-action on GitHub](https://github.com/crackedngineer/codeurcv-action) · [View on Marketplace](https://github.com/marketplace/actions/codeurcv-action)

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) — contributions are welcome!

---

## 📜 License

[MIT](LICENSE) © codeurcv contributors
