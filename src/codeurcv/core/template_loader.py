import importlib
import pkgutil
from typing import Dict

from codeurcv.templates.base import TemplatePlugin


def load_builtin_templates() -> Dict[str, TemplatePlugin]:
    """
    Dynamically discover built-in template plugins.
    """
    plugins = {}

    package = "codeurcv.templates"

    for _, module_name, is_pkg in pkgutil.iter_modules(
        importlib.import_module(package).__path__
    ):
        if not is_pkg:
            continue

        try:
            module = importlib.import_module(f"{package}.{module_name}.plugin")

            for attr in dir(module):
                obj = getattr(module, attr)

                if (
                    isinstance(obj, type)
                    and issubclass(obj, TemplatePlugin)
                    and obj is not TemplatePlugin
                ):
                    instance = obj()
                    plugins[instance.name] = instance

        except ModuleNotFoundError:
            continue

    return plugins
