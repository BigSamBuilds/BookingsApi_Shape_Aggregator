from shapes.Shape import Shape


class Rectangle(Shape):
    """Class representing a rectangle shape."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize a rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle, calculated as width * height.
        """
        return self.width * self.height


# Register the Rectangle shape in the shape registry
Rectangle.register_shape()
