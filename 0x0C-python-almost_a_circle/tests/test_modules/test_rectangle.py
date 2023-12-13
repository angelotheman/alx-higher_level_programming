#!/usr/bin/python3
"""
This is the test file for the rectangle class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the rectangle only"""

    def test_constructor_with_default_values(self):
        """Tests the constructor with different values"""
        r = Rectangle(1, 1)

        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_constructor_with_custom_values(self):
        """Tests with custom values"""
        r = Rectangle(5, 10, 2, 3, 7)
        
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 7)

    def test_constructor_with_negative_values(self):
        """Checks if code raises exception when negative values are passed"""
        with self.assertRaises(ValueError):
            r = Rectangle(-2, 8)

        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, -1, 2)

    def test_constructor_with_non_integer_values(self):
        """Checks for non integer values"""
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 5)

        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, "invalid", 2)

    def test_setter_with_non_integer_values(self):
        """Checks setter methods for non integer values"""
        r = Rectangle(3, 4)

        with self.assertRaises(TypeError):
            r.width = "invalid"


if __name__ == '__main__':
    unittest.main()
