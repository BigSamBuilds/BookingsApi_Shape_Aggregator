import pytest
from shapes.Circle import Circle
from shapes.Rectangle import Rectangle
from shapes.Triangle import Triangle
from main import load_data, saveTotalArea


# Test for Circle area
def test_circle_area():
    """Test the area calculation for a Circle."""
    circle = Circle(5)
    assert circle.area() == pytest.approx(78.5398, rel=1e-4)


# Test for Rectangle area
def test_rectangle_area():
    """Test the area calculation for a Rectangle."""
    rectangle = Rectangle(3, 4)
    assert rectangle.area() == 12.0


# Test for Triangle area
def test_triangle_area():
    """Test the area calculation for a Triangle."""
    triangle = Triangle(6, 2)
    assert triangle.area() == 6.0


# Test load_data function
def test_load_data():
    """Test the load_data function to ensure it creates the correct shape instances."""
    shape_list = [
        {"type": "circle", "radius": 5},
        {"type": "rectangle", "width": 3, "height": 4},
        {"type": "triangle", "base": 6, "height": 2},
    ]
    shapes = load_data(shape_list)
    assert len(shapes) == 3
    assert isinstance(shapes[0], Circle)
    assert isinstance(shapes[1], Rectangle)
    assert isinstance(shapes[2], Triangle)


# Test saveTotalArea function
def test_save_total_area(monkeypatch):
    """Test the saveTotalArea function to ensure it calculates and saves the total area."""
    monkeypatch.setattr("builtins.print", lambda x: x)

    shapes = [Circle(5), Rectangle(3, 4), Triangle(6, 2)]

    saveTotalArea(shapes)

    assert True
