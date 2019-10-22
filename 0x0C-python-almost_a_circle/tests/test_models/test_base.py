#!/usr/bin/python3
"""
Class BaseTest -
for testing models/base.py

"""


import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    """ unit tests for the base class """
    def test_incrementation(self):
        """ sees if object id increments """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)
    def test_inputs(self):
        """ checks for various valid inputs """
        b_int = Base(12)
        self.assertEqual(b_int.id, 12)

        b_neg_int = Base(-12)
        self.assertEqual(b_neg_int.id, -12)

        b_str = Base("string")
        self.assertEqual(b_str.id, "string")

        b_list = Base([1, 2, 3])
        self.assertEqual(b_list.id, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
