#!/usr/bin/python3
"""
Class RectangleTest -
for testing models/rectangle.py

"""


import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    """ unit tests for the rectangle class """
    def test_id:
        """ check for consistent ids based off various inputs """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.id, 12)
    def test_height:
        pass
    def test_width:
        pass
    def test_x:
        pass
    def test_y:
        pass
    def test_err_type:
        """ checks no non-int attributes pass """
        with self.assertRaises(TypeError) as e:
            r_h = Rectangle(10, "2")
        self.assertEqual(
            "height must be an integer",
            str(e.exception))

        with self.assertRaises(TypeError) as e:
            r_w = Rectangle("10", 2)
            self.assertEqual(
                "width must be an integer",
                str(e.exception))

        with selfassertRaises(TypeError) as e:
            r_x = Rectangle(10, 2, "0")
            self.assertEqual(
                "x must be an integer",
                str(e, exception))

        with selfassertRaises(TypeError) as e:
            r_y = Rectangle(10, 2, 0, "0")
            self.assertEqual(
                "y must be an integer",
                str(e, exception))
    def test_err_dimen_val:
        """ check no dimension value is less than or equal to 0 """
        with self.assertRaise(ValueError) as e:
            r_h = Rectangle(2, 0)
            self.assertEqual(
                "height must be > 0",
                str(e.exception))

        with self.assertRaise(ValueError) as e:
            r_h = Rectangle(2, -2)
            self.assertEqual(
                "height must be > 0",
                str(e.exception))

        with self.assertRaise(ValueError) as e:
            r_w = Rectangle(0, 2)
            self.assertEqual(
                "width must be > 0",
                str(e.exception))

        with self.assertRaise(ValueError) as e:
            r_w = Rectangle(-2, 2)
            self.assertEqual(
                "width must be > 0",
                str(e.exception))
    def test_err_coord_val:
        """ check no coordinate value is less than  0 """
        with self.assertRaise(ValueError) as e:
            r_x = Rectangle(2, 2, -2, 0)
            self.assertEqual(
                "x must be >= 0",
                str(e.exception))

        with self.assertRaise(ValueError) as e:
            r_y = Rectangle(2, 2, 0, -2)
            self.assertEqual(
                "y must be >= 0",
                str(e.exception))
    def test_area:
        """ test the area function """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(4, 3, 0)
        self.assertEqual(r2.area(), 12)

        r3 = Rectangle(6, 3, 1, 2)
        self.assertEqual(r3.area(), 18)

        r4 = Rectangle(4, 2, 0, 0, 12)
        self.assertEqual(r4.area(), 8)

if __name__ == '__main__':
    unittest.main()
