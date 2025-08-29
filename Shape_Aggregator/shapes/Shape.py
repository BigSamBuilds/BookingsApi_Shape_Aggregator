from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    shape_registry = {}

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @classmethod
    def register_shape(cls):
        """Register a shape class in the shape registry.

        This method adds the shape class to the registry using its
        lowercase name as the key.
        """
        cls.shape_registry[cls.__name__.lower()] = cls

    @classmethod
    def create_shape(cls, shape_type: str, **kwargs):
        """Create an instance of a registered shape.

        Args:
            shape_type (str): The type of shape to create.
            **kwargs: Additional arguments to pass to the shape's constructor.

        Returns:
            Shape: An instance of the requested shape.

        Raises:
            ValueError: If the shape type is not registered.
        """
        shape_class = cls.shape_registry.get(shape_type.lower())
        if shape_class:
            return shape_class(**kwargs)
        raise ValueError(f"Unknown shape type: {shape_type}")
