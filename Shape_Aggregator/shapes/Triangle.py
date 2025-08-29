from shapes.Shape import Shape


class Triangle(Shape):
    """Class representing a triangle shape."""

    def __init__(self, base: float, height: float) -> None:
        """Initialize a triangle with a given base and height.

        Args:
            base (float): The base length of the triangle.
            height (float): The height of the triangle.
        """
        self.base = base
        self.height = height

    def area(self) -> float:
        """Calculate the area of the triangle.

        Returns:
            float: The area of the triangle, calculated as 0.5 * base * height.
        """
        return 0.5 * self.base * self.height


# Register the Triangle shape in the shape registry
Triangle.register_shape()
