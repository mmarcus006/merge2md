#!/usr/bin/env python3
"""
Demo script to convert franchise directory project files.
"""
from pathlib import Path
from merge2md import convert_and_merge

# Franchise directory files
files = [
    Path("/Users/miller/Downloads/franchise_directory_project/comparison_framework.md"),
    Path("/Users/miller/Downloads/franchise_directory_project/database_schema_design.md"),
    Path("/Users/miller/Downloads/franchise_directory_project/fdd_research_summary.md"),
    Path("/Users/miller/Downloads/franchise_directory_project/franchise_profile_architecture.md"),
    Path("/Users/miller/Downloads/franchise_directory_project/implementation_and_monetization.md"),
    Path("/Users/miller/Downloads/franchise_directory_project/README.md"),
    Path("/Users/miller/Downloads/franchise_directory_project/todo.md"),
]

# Convert and merge
output = convert_and_merge(
    files,
    output=None,  # Will use Downloads/merged.md (or merged_1.md, etc.)
    title="Franchise Directory Project Documentation",
    show_notification=True
)

print(f"✅ Files merged successfully to: {output}") 
 