"""
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

"""

import unittest


def even_or_odd(number):
    if number & 1 == 1:
        return "Odd"
    return "Even"


class TestProblem(unittest.TestCase):
    def setUp(self):
        self.even = "Even"
        self.odd = "Odd"

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(even_or_odd(1), self.odd)
        self.assertEqual(even_or_odd(2), self.even)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
