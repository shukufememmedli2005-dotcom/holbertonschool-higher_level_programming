#!/usr/bin/python3
"""Add all arguments to a list and save them to a JSON file."""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, else start with empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments
items.extend(sys.argv[1:])

# Save updated list
save_to_json_file(items, filename)
