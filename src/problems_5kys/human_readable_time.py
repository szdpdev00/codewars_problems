"""
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

Description:

Write a function, which takes a non-negative integer (seconds) as input and returns the time
in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""

import unittest


def make_readable(seconds):
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return f"{h:02}:{m:02}:{s:02}"


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(make_readable(0), "00:00:00")
        self.assertEqual(make_readable(3599), "00:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
