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

# Combine HTML files
with open(output_file, "w") as outfile:
    # Write the HTML header
    outfile.write("<html>\n<head>\n<title>Shapes and Main Documentation</title>\n")
    outfile.write(
        '<link rel="stylesheet" type="text/css" href="styles.css">\n'
    )  # Link to your CSS file
    outfile.write("</head>\n<body>\n")
    outfile.write("<h1>Shapes and Main Documentation</h1>\n")

    # Read and append each generated HTML file
    for module in modules:
        module_file = f"{module.split('.')[-1]}.html"  # Get the last part of the module name for the file
        if os.path.exists(module_file):
            with open(module_file, "r") as infile:
                # Skip the header and body tags of each file
                lines = infile.readlines()
                outfile.writelines(lines[1:])  # Skip the first line (header)
        else:
            print(f"Warning: {module_file} not found.")

    # Write the closing body and html tags
    outfile.write("</body>\n</html>")

print(f"Combined documentation written to {output_file}")
