from asyncio import subprocess

import yaml
from jinja2 import Environment, FileSystemLoader

def md_to_latex(text):
    result = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "latex"],
        input=text,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()
    

# Load YAML
with open("resume.yml") as f:
    data = yaml.safe_load(f)
    
# Formatting resume Data
for job in data["work"]:
    job["achievements"] = [
        md_to_latex(item) for item in job["achievements"]
    ]

# Load LaTeX template
env = Environment(
    loader=FileSystemLoader("."),
    block_start_string="((*",
    block_end_string="*))",
    variable_start_string="(((",
    variable_end_string=")))",
    comment_start_string="((#",
    comment_end_string="#))",
)
template = env.get_template("template.tex")

# Render
output = template.render(**data)

# Save final LaTeX
with open("output/resume.tex", "w") as f:
    f.write(output)