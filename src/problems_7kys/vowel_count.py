"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""

import unittest


def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for x in sentence if x in vowels)


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(get_count("hello world"), 3)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
