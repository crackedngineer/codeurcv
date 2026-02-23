import yaml
from jinja2 import Environment, FileSystemLoader

# Load YAML
with open("resume.yml") as f:
    data = yaml.safe_load(f)

# Load LaTeX template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("template.tex")

# Render
output = template.render(**data)

# Save final LaTeX
with open("output/resume.tex", "w") as f:
    f.write(output)