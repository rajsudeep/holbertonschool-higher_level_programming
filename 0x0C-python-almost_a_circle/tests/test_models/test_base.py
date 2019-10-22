#!/usr/bin/python3
"""
Class BaseTest -
for testing models/base.py

"""


import unittest
from models.base import Base
from models.rectangle import Rectangle

class BaseTest(unittest.TestCase):
    """ unit tests for the base class """
    def test_incrementation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)
    def test_inputs(self):
        b_int = Base(12)
        self.assertEqual(b_int.id, 12)

        b_neg_int = Base(-12)
        self.assertEqual(b_neg_int.id, -12)
    def test_json_conversions(self):
        r = Base.to_json_string(None)
        self.assertEqual(r, "[]")

        r = Base.to_json_string([])
        self.assertEqual(r, "[]")

        r = Rectangle(10, 7, 2, 8)
        dict = r.to_dictionary()
        json_dict = Base.to_json_string([dict])
        result = [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        self.assertEqual(len(json_dict), len(str(result)))

        input = '[{"x": 1, "y": 2, "id": 3}, \
        {"x": 2, "y": 2, "id": 2}]'
        output = [{'x': 1, 'y': 2, 'id': 3},
             {'x': 2, 'y': 2, 'id': 2}]
        self.assertEqual(Base.from_json_string(input), output)
    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
    def test_create(self):
        r = Rectangle(3, 5, 1, 1, 100)
        r_dict = r.to_dictionary()
        r_x = Rectangle.create(**r_dict)
        self.assertEqual(r is r_x, False)
    
if __name__ == '__main__':
    unittest.main()
