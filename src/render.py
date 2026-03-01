import re
import subprocess
import yaml
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from constants import TEMPLATE_DIR, DEFAULT_CONFIG_FILE


def md_to_latex(text):
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "latex"],
        input=text,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    # Use re.sub for regex replacement.
    # The 'r' prefix ensures raw strings for correct backslash handling.
    return re.sub(r"{}".format(find), r"{}".format(replace), s)

def fetch_template(type: str = "minimalist"):
    template_path = Path(TEMPLATE_DIR) / f"{type}.tex"
    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")
    return template_path

def convert_to_pdf(tex_file: Path, output_dir: Path):
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run pdflatex command
    result = subprocess.run(
        ["pdflatex", "-output-directory", str(output_dir), str(tex_file)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("Error during PDF conversion:")
        print(result.stderr)
        raise RuntimeError("PDF conversion failed")
    
    print(f"PDF generated successfully at: {output_dir / tex_file.with_suffix('.pdf').name}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Render a resume from a YAML config.")
    parser.add_argument("-f","--filename", nargs="?", help="Config file path", default=DEFAULT_CONFIG_FILE)
    parser.add_argument("--out_dir", nargs="?", default="output", help="Directory to save the rendered resume")
    args = parser.parse_args()

    # output directory
    output_dir = Path(args.out_dir)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load YAML
    with open(args.filename) as f:
        data = yaml.safe_load(f)
    
    template_path = fetch_template(data.get("template", "minimalist"))
    if template_path:
        print(f"Using template: {template_path}")

    # Output file name
    output_file_name = data.get("filename", "resume")
    output_file_path = output_dir / f"{output_file_name}.tex"

    # Formatting resume Data
    data["summary"] = md_to_latex(data["summary"])
    for job in data["work"]:
        job["achievements"] = [md_to_latex(item) for item in job["achievements"]]
    for project in data["projects"]:
        project["description"] = [md_to_latex(item) for item in project["description"]]

    # Load LaTeX template
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        block_start_string="((*",
        block_end_string="*))",
        variable_start_string="(((",
        variable_end_string=")))",
        comment_start_string="((#",
        comment_end_string="#))",
    )
    env.filters["regex_replace"] = regex_replace
    template = env.get_template(template_path.name)

    # Render
    output = template.render(**data)

    # Save final LaTeX
    with open(output_file_path, "w") as f:
        f.write(output)

    # Convert to PDF
    convert_to_pdf(output_file_path, output_dir)


if __name__ == "__main__":
    main()
