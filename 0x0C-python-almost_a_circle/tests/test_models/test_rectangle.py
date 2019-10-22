#!/usr/bin/python3
"""
Class RectangleTest -
for testing models/rectangle.py

"""


import unittest
import os
import io
import contextlib
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ unit tests for the rectangle class """
    def test_height(self):
        r_h = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r_h.height, 2)

    def test_width(self):
        r_w = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r_w.width, 10)

    def test_x(self):
        r_x = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(r_x.x, 1)

        r_x = Rectangle(10, 2)
        self.assertEqual(r_x.x, 0)

    def test_y(self):
        r_y = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(r_y.y, 1)

        r_y = Rectangle(10, 2)
        self.assertEqual(r_y.y, 0)

    def test_err_type(self):
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

        with self.assertRaises(TypeError) as e:
            r_x = Rectangle(10, 2, "0")
            self.assertEqual(
                "x must be an integer",
                str(e, exception))

        with self.assertRaises(TypeError) as e:
            r_y = Rectangle(10, 2, 0, "0")
            self.assertEqual(
                "y must be an integer",
                str(e, exception))

    def test_err_dimen_val(self):
        """ check no dimension value is less than or equal to 0 """
        with self.assertRaises(ValueError) as e:
            r_h = Rectangle(2, 0)
            self.assertEqual(
                "height must be > 0",
                str(e.exception))

        with self.assertRaises(ValueError) as e:
            r_h = Rectangle(2, -2)
            self.assertEqual(
                "height must be > 0",
                str(e.exception))

        with self.assertRaises(ValueError) as e:
            r_w = Rectangle(0, 2)
            self.assertEqual(
                "width must be > 0",
                str(e.exception))

        with self.assertRaises(ValueError) as e:
            r_w = Rectangle(-2, 2)
            self.assertEqual(
                "width must be > 0",
                str(e.exception))

    def test_err_coord_val(self):
        """ check no coordinate value is less than  0 """
        with self.assertRaises(ValueError) as e:
            r_x = Rectangle(2, 2, -2, 0)
            self.assertEqual(
                "x must be >= 0",
                str(e.exception))

        with self.assertRaises(ValueError) as e:
            r_y = Rectangle(2, 2, 0, -2)
            self.assertEqual(
                "y must be >= 0",
                str(e.exception))

    def test_area(self):
        """ test the area function """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(4, 3, 0)
        self.assertEqual(r2.area(), 12)

        r3 = Rectangle(6, 3, 1, 2)
        self.assertEqual(r3.area(), 18)

        r4 = Rectangle(4, 2, 0, 0, 12)
        self.assertEqual(r4.area(), 8)

    def test_dimen_display(self):
        r = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Rectangle(2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "##\n##\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Rectangle(1, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "#\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Rectangle(1, 5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "#\n#\n#\n#\n#\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Rectangle(5, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "#####\n"
        self.assertEqual(f.getvalue(), r_result)

    def test_coord_display(self):
        r = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = " ###\n ###\n"
        self.assertEqual(f.getvalue(), r_result)

        r = Rectangle(3, 2, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        r_result = "###\n###\n"
        self.assertEqual(f.getvalue(), r_result)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        r.update(89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r.update(89, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r.update(89, 2, 3)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/1")

        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 1/1")

        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/1")

        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_dictionary(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r_result = {'x': 1, 'y': 1, 'width': 1, 'id': 1, 'height': 1}
        self.assertEqual(r.to_dictionary(), r_result)

        r_ptr_bool = r.to_dictionary() is r
        self.assertEqual(r_ptr_bool, False)

if __name__ == '__main__':
    unittest.main()
