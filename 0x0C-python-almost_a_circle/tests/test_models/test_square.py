#!/usr/bin/python3
"""
Class SquareTest -
for testing models/rectangle.py

"""


import unittest
import os
import io
import contextlib
from models.square import Square

class SquareTest(unittest.TestCase):
    """ unit tests for the square class """
    def test_size(self):
        r_s = Square(10, 0, 0, 1)
        self.assertEqual(r_s.size, 10)

    def test_x(self):
        r_x = Square(10, 1, 1, 1)
        self.assertEqual(r_x.x, 1)

        r_x = Square(10)
        self.assertEqual(r_x.x, 0)
    def test_y(self):
        r_y = Square(10, 1, 1, 1)
        self.assertEqual(r_y.y, 1)

        r_y = Square(10)
        self.assertEqual(r_y.y, 0)
    def test_err_type(self):
        """ checks no non-int attributes pass """
        with self.assertRaises(TypeError) as e:
            r_s = Square("10")
            self.assertEqual(
                "width must be an integer",
                str(e.exception))

        with self.assertRaises(TypeError) as e:
            r_x = Square(10, "0")
            self.assertEqual(
                "x must be an integer",
                str(e, exception))

        with self.assertRaises(TypeError) as e:
            r_y = Square(10, 0, "0")
            self.assertEqual(
                "y must be an integer",
                str(e, exception))
    def test_err_dimen_val(self):
        """ check no dimension value is less than or equal to 0 """
        with self.assertRaises(ValueError) as e:
            r_h = Square(0)
            self.assertEqual(
                "height must be > 0",
                str(e.exception))

        with self.assertRaises(ValueError) as e:
            r_h = Square(-2)
            self.assertEqual(
                "height must be > 0",
                str(e.exception))

    def test_err_coord_val(self):
        """ check no coordinate value is less than  0 """
        with self.assertRaises(ValueError) as e:
            r_x = Square(2, -2, 0)
            self.assertEqual(
                "x must be >= 0",
                str(e.exception))

        with self.assertRaises(ValueError) as e:
            r_y = Square(2, 0, -2)
            self.assertEqual(
                "y must be >= 0",
                str(e.exception))
    def test_area(self):
        """ test the area function """
        r1 = Square(2)
        self.assertEqual(r1.area(), 4)

        r2 = Square(5, 1, 2, 99)
        self.assertEqual(r2.area(), 25)
    def test_dimen_display(self):
        r = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "##\n##\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Square(1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "#\n"
        self.assertEqual(f.getvalue(), r_result)
    def test_coord_display(self):
        r = Square(2, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "\n\n  ##\n  ##\n"
        self.assertEqual(f.getvalue(), r_result)
    def test_str(self):
        r = Square(4, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Square] (12) 2/1 - 4")
    def test_update_args(self):
        r = Square(10, 10, 10, 1)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 10")

        r.update(89)
        self.assertEqual(r.__str__(), "[Square] (89) 10/10 - 10")

        r.update(89, 2)
        self.assertEqual(r.__str__(), "[Square] (89) 10/10 - 2")

        r.update(89, 2, 3)
        self.assertEqual(r.__str__(), "[Square] (89) 3/10 - 2")

        r.update(89, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (89) 3/4 - 2")
    def test_update_kwargs(self):
        r = Square(10, 10, 10, 1)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 10")

        r.update(size=1)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 1")

        r.update(x=7, y=2)
        self.assertEqual(r.__str__(), "[Square] (1) 7/2 - 1")

        r.update(y=1, size=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Square] (89) 3/1 - 2")
    def test_dictionary(self):
        r = Square(1, 1, 1, 1)
        r_result = {'x': 1, 'y': 1, 'size': 1, 'id': 1}
        self.assertEqual(r.to_dictionary(), r_result)

        r_ptr_bool = r.to_dictionary() is r
        self.assertEqual(r_ptr_bool, False)

if __name__ == '__main__':
    unittest.main()
