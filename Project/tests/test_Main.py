#!python
# coding: utf-8

"""
Tests for Main.py
"""

import unittest
# other imports


class TestCase1(unittest.TestCase):
    """
    Small description of test case
    """

    def setUp(self):
        """initialize whatever is necessary to run all tests in this class"""

    def test_situation_1(self):
        self.assertFalse('function_to_test(args)')

    def test_situation_2(self):
        self.assertTrue('function_to_test(args)')


class TestCase2(unittest.TestCase):
    """
    Small description of test case
    """
    def test_situation_3(self):
        self.assertEquals('function_to_test(args)', 'output')


if __name__ == '__main__':
    unittest.main()
