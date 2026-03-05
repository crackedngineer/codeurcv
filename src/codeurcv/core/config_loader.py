import json
import yaml
from pathlib import Path

LOADERS = {
    ".yml":  yaml.safe_load,
    ".yaml": yaml.safe_load,
    ".json": json.loads,
}

def load_config(path: Path) -> dict:
    loader = LOADERS.get(path.suffix.lower())
    if loader is None:
        raise ValueError(
            f"Unsupported file type '{path.suffix}'. Use .yml, .yaml, or .json"
        )
    return loader(path.read_text())