import os
import subprocess

# List of shape classes and main module
modules = [
    "shapes.Shape",
    "shapes.Circle",
    "shapes.Rectangle",
    "shapes.Square",
    "shapes.Triangle",
    "main",
    "test",
]
output_file = "combined_shapes_and_main.html"

# Generate individual HTML files
for module in modules:
    subprocess.run(["python", "-m", "pydoc", "-w", module])

