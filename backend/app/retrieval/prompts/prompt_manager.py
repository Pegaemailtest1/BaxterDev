import os
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from typing import Dict

class PromptManager:
    def __init__(self, prompt_dir: str = "prompt_templates", registry_filename: str = "prompt_registry.yaml"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.template_dir = os.path.join(current_dir, prompt_dir)
        self.registry_path = os.path.join(current_dir, registry_filename)

        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            undefined=StrictUndefined  # Raise errors for missing vars
        )
        self.registry = self._load_registry(self.registry_path)

    def _load_registry(self, path: str) -> Dict[str, str]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Prompt registry not found at: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_prompt(self, intent: str, context_vars: Dict[str, str]) -> str:
        if intent not in self.registry:
            raise ValueError(f"No template registered for intent '{intent}'")
        
        template_name = self.registry[intent]

        # Ensure context_vars is a copy to avoid modifying the caller's dictionary
        context_vars = context_vars.copy()

        # ✅ Ensure "fields" is a list (needed for template rendering)
        if "fields" not in context_vars:
            field_string = context_vars.get("field", "")
            if isinstance(field_string, str):
                context_vars["fields"] = [f.strip() for f in field_string.split(",") if f.strip()]
            else:
                context_vars["fields"] = []

        try:
            template = self.env.get_template(template_name)
            rendered = template.render(context_vars)
            if not rendered.strip():
                raise ValueError("Template rendered to empty string.")
            return rendered
        except Exception as e:
            raise RuntimeError(f"Failed to render template '{template_name}': {e}")
