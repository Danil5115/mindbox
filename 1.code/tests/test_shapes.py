import unittest
from calculator_library.shapes import Circle, Triangle
import math

# для запуска тестов, не забудьте перейти в папку 1.code
# python -m unittest discover -s tests

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 9)
    
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)
    
    def test_triangle_is_right(self):
        right_triangle = Triangle(3, 4, 5)
        not_right_triangle = Triangle(3, 3, 3)
        self.assertTrue(right_triangle.is_right())
        self.assertFalse(not_right_triangle.is_right())

if __name__ == "__main__":
    unittest.main()
