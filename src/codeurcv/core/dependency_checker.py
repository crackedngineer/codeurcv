import sys
import shutil
from codeurcv.core.settings import console

INSTALL_INSTRUCTIONS = {
    "pandoc": {
        "win32": [
            ("winget", "winget install --id JohnMacFarlane.Pandoc"),
            ("choco", "choco install pandoc"),
        ],
        "darwin": [
            ("brew", "brew install pandoc"),
        ],
        "linux": [
            ("apt", "sudo apt install pandoc"),
            ("dnf", "sudo dnf install pandoc"),
            ("pacman", "sudo pacman -S pandoc"),
            ("zypper", "sudo zypper install pandoc"),
            ("emerge", "sudo emerge app-text/pandoc"),
            ("snap", "sudo snap install pandoc"),
            ("flatpak", "flatpak install flathub org.pandoc.Pandoc"),
        ],
    },
    "pdflatex": {
        "win32": [
            ("winget", "winget install --id MiKTeX.MiKTeX"),
            ("choco", "choco install miktex"),
        ],
        "darwin": [
            ("brew", "brew install --cask mactex"),
        ],
        "linux": [
            ("apt", "sudo apt install texlive-latex-base"),
            ("dnf", "sudo dnf install texlive-latex"),
            ("pacman", "sudo pacman -S texlive-basic"),
            ("zypper", "sudo zypper install texlive-latex"),
            ("emerge", "sudo emerge dev-texlive/texlive-basic"),
            ("snap", "sudo snap install texlive"),
            ("flatpak", "flatpak install flathub org.texlive.TeXLive"),
        ],
    },
}

# Maps package manager → distro label for display
PM_DISTRO_LABEL = {
    "apt":     "Debian / Ubuntu / Mint",
    "dnf":     "Fedora / RHEL / CentOS",
    "pacman":  "Arch / Manjaro",
    "zypper":  "openSUSE",
    "emerge":  "Gentoo",
    "snap":    "Snap",
    "flatpak": "Flatpak",
    "winget":  "winget",
    "choco":   "Chocolatey",
    "brew":    "Homebrew",
}


def get_available_package_managers() -> list[str]:
    managers = ["apt", "dnf", "pacman", "zypper", "emerge", "snap", "flatpak", "winget", "choco", "brew"]
    return [pm for pm in managers if shutil.which(pm) is not None]


def check_dependencies():
    missing = [t for t in ("pandoc", "pdflatex") if shutil.which(t) is None]
    if not missing:
        return

    available_pms = get_available_package_managers()
    platform = sys.platform

    console.print("\n[bold red]Missing dependencies detected:[/bold red]\n")

    for tool in missing:
        options = INSTALL_INSTRUCTIONS[tool].get(platform, INSTALL_INSTRUCTIONS[tool]["linux"])

        # Filter to only detected package managers, fallback to all if none matched
        matched = [(pm, cmd) for pm, cmd in options if pm in available_pms] or options

        console.print(f"[bold yellow]{tool}[/bold yellow] is not installed.")

        if len(matched) == 1:
            pm, cmd = matched[0]
            label = PM_DISTRO_LABEL.get(pm, pm)
            console.print(f"[dim]Install with ({label}):[/dim] [cyan]{cmd}[/cyan]")
        else:
            console.print(f"[dim]Install with one of:[/dim]")
            for pm, cmd in matched:
                label = PM_DISTRO_LABEL.get(pm, pm)
                console.print(f"[dim]{label:<28}[/dim] [cyan]{cmd}[/cyan]")

        console.print()

    raise SystemExit(1)