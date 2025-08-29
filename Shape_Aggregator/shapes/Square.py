from shapes.Shape import Shape


class Square(Shape):
    """Class representing a square shape."""

    def __init__(self, side: float) -> None:
        """Initialize a square with a given side length.

        Args:
            side (float): The length of the side of the square.
        """
        self.side = side

    def area(self) -> float:
        """Calculate the area of the square.

        Returns:
            float: The area of the square, calculated as side squared.
        """
        return self.side**2


# Register the Square shape in the shape registry
Square.register_shape()
