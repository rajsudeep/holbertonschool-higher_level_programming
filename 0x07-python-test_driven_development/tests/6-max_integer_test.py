#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit test for max_integer """
    def test_values(self):
        """
        Returns assertions for max_integer
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7]), 7)
        self.assertEqual(max_integer([10, 100, 12, 5, 3, 2, 0]), 100)
        self.assertEqual(max_integer([0, 0, -6, -2, -3, -5]), 0)

if __name__ == '__main__':
    unittest.main()
