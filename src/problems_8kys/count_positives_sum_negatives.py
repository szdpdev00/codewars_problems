"""
https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element
is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""

import unittest


def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positive = [x for x in arr if x > 0]
    negative = [x for x in arr if x < 0]
    return [len(positive), sum(negative)]


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(
            count_positives_sum_negatives(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
            ),
            [10, -65],
        )


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
