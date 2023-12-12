#!/usr/bin/python3
"""
This is a test case file
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This is the test case for the Base file"""

    def test_base_constructor_with_id(self):
        """Tests the base constructor"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_with_argument(self):
        """Tests with argument"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_id_after_argument(self):
        """Tests after argument"""
        b4 = Base()
        self.assertEqual(b4.id, 3)


if __name__ == '__main__':
    unittest.main()
