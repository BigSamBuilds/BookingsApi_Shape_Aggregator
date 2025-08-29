import json
import os
import sys
from shapes import *
import argparse


def read_file(filename: str) -> list:
    """Read a JSON file and return its contents as a list.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: The contents of the file parsed as a list.
    """
    with open(filename, "r") as data:
        return json.loads(data.read())


def load_data(shape_list: list) -> list[Shape]:
    """Load shapes from a list of dictionaries and create shape instances.

    Args:
        shape_list (list): A list of dictionaries containing shape data.

    Returns:
        list[Shape]: A list of created shape instances.
    """
    shapes = []

    for s in shape_list:
        shape_type = s.get("type")
        # Create a new dictionary without the 'type' key
        shape_params = {k: v for k, v in s.items() if k != "type"}

        try:
            # Factory method to create the shape
            shape = Shape.create_shape(shape_type, **shape_params)
            shapes.append(shape)
        except ValueError as e:
            print(e)

    return shapes


def save_total_area(shapeList: list[Shape]) -> None:
    """Calculate and save the total area of the given shapes.

    Args:
        shapeList (list[Shape]): A list of shape instances.
    """
    total_area = sum(shape.area() for shape in shapeList)

    print(f"Total area: {total_area:.1f}")

    with open("area.txt", "a") as writer:
        writer.write(f"{total_area:.1f}\n")


def main():
    parser = argparse.ArgumentParser(description="Calculate the total area of shapes.")
    parser.add_argument(
        "--file", type=str, required=True, help="Path to the JSON input file"
    )
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: The file {args.file} does not exist.")
        sys.exit(1)

    try:
        shape_data = read_file(args.file)
        shapes = load_data(shape_data)
        save_total_area(shapes)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        sys.exit(1)


if __name__ == "__main__":
    main()
