import pytest
import source.shapes as shapes

# Parameters and values as a list of tuples
@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("length, expected_perimeter", [(2, 8), (4, 16), (5, 20)])
def test_multiple_square_perimeters(length, expected_perimeter):
    assert shapes.Square(length).perimeter() == expected_perimeter