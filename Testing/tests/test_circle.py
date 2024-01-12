import pytest
import source.shapes as shapes
import math

class TestCircle:
    def setup_method(self, method):
        '''Runs before tests'''
        # print(f'Setting up {method}')
        print(f"Initialize circle with raidus 10")
        self.circle = shapes.Circle(radius=10)

    def teardown_method(self, method):
        '''Runs after tests'''
        # print(f"Tearing down {method}")
        print(f"Deleting circle")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected