#!/usr/bin/env python3
"""Merge Abenteuer-Schmiede module-help.csv into BMAD help.csv."""

import csv
import sys
import os

def merge_help(bmad_root):
    help_path = os.path.join(bmad_root, "_config", "help.csv")
    module_help = os.path.join(os.path.dirname(__file__), "..", "assets", "module-help.csv")

    if not os.path.exists(module_help):
        print(f"Module help CSV not found: {module_help}")
        sys.exit(1)

    # Read module help entries
    with open(module_help, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        new_rows = list(reader)

    # Read existing BMAD help (or create new)
    existing_ids = set()
    existing_rows = []
    if os.path.exists(help_path):
        with open(help_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            existing_header = next(reader)
            for row in reader:
                existing_ids.add(row[0])
                existing_rows.append(row)

    # Merge: only add rows that don't exist yet
    added = 0
    for row in new_rows:
        if row[0] not in existing_ids:
            existing_rows.append(row)
            added += 1

    # Write back
    with open(help_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(existing_rows)

    print(f"Merged {added} new entries into BMAD help.csv.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge-help-csv.py <bmad-root-path>")
        sys.exit(1)
    merge_help(sys.argv[1])
