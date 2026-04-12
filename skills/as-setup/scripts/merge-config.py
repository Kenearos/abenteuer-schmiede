#!/usr/bin/env python3
"""Merge Abenteuer-Schmiede config into BMAD _config/config.yaml.

Called by: BMAD module installer (npx bmad-method install)
When:      During module installation, NOT during as-setup workflow
Purpose:   Adds default Abenteuer-Schmiede config variables to the
           central BMAD config so agents can read project settings.
Idempotent: Yes — skips if 'abenteuer-schmiede:' block already exists.

Usage:
    python merge-config.py <bmad-root-path>

Example:
    python merge-config.py /path/to/my-project

This appends the following YAML block to _config/config.yaml:

    abenteuer-schmiede:
      abenteuer_name: ""
      setting: ""
      epoche: ""
      spieleranzahl: "3-4"
      erfahrungsstufe: "Durchschnittlich (300-600 AP)"
      abenteuer_typ: "Gemischt"
      geschaetzte_dauer: "Mittel (4-6 Abende)"
      sprache: "Deutsch"

These values are populated by the as-setup workflow (skills/as-setup/SKILL.md)
when the user starts a new adventure project.
"""

import sys
import os

def merge_config(bmad_root):
    config_path = os.path.join(bmad_root, "_config", "config.yaml")

    if not os.path.exists(config_path):
        print(f"BMAD config not found at {config_path}")
        sys.exit(1)

    as_config = """
# --- Abenteuer-Schmiede Module ---
abenteuer-schmiede:
  abenteuer_name: ""
  setting: ""
  epoche: ""
  spieleranzahl: "3-4"
  erfahrungsstufe: "Durchschnittlich (300-600 AP)"
  abenteuer_typ: "Gemischt"
  geschaetzte_dauer: "Mittel (4-6 Abende)"
  sprache: "Deutsch"
"""

    with open(config_path, "r") as f:
        content = f.read()

    if "abenteuer-schmiede:" in content:
        print("Abenteuer-Schmiede config already present. Skipping.")
        return

    with open(config_path, "a") as f:
        f.write(as_config)

    print("Abenteuer-Schmiede config merged into BMAD config.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge-config.py <bmad-root-path>")
        sys.exit(1)
    merge_config(sys.argv[1])
