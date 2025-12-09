"""
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

"""

import unittest


def strip_comments(strng, markers):
    s = "\n"
    parts = strng.split(s)
    res = []
    for p in parts:
        idx = len(p)
        for i, c in enumerate(p):
            if c in markers:
                idx = i
                break
        res.append(p[:idx].rstrip())

    return s.join(res)


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEquals(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
                          'apples, pears\ngrapes\nbananas')
        self.assertEquals(strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
        self.assertEquals(strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
