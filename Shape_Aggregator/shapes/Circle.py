from shapes.Shape import Shape
from math import pi


class Circle(Shape):
    """Class representing a circle shape."""

    def __init__(self, radius: float) -> None:
        """Initialize a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle, calculated as π * radius squared.
        """
        return pi * (self.radius**2)


# Register the Circle shape in the shape registry
Circle.register_shape()
