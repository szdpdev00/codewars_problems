"""
https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

Write a function called sumIntervals/sum_intervals that accepts an array of intervals,
and returns the sum of all the interval lengths.
Overlapping intervals should only be counted once.
Intervals

Intervals are represented by a pair of integers in the form of an array.
The first value of the interval will always be less than the second value.
Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
Overlapping Intervals

List containing overlapping intervals:

[
   [1, 4],
   [7, 10],
   [3, 5]
]

The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap,
we can treat the interval as [1, 5], which has a length of 4.
Examples:

sumIntervals( [
   [1, 2],
   [6, 10],
   [11, 15]
] ) => 9

sumIntervals( [
   [1, 4],
   [7, 10],
   [3, 5]
] ) => 7

sumIntervals( [
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ) => 19

sumIntervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ) => 100000030

Tests with large intervals

Your algorithm should be able to handle large intervals.
All tested intervals are subsets of the range [-1000000000, 1000000000].

"""

import unittest
from functools import reduce


def sum_of_intervals(intervals):
    s = sorted(intervals, key=lambda x: x[0])
    res = []
    m = s[0][0]
    e = s[0][1]
    i = 1
    while i < len(s):
        n = s[i]
        if n[0] < e:
            if n[0] + (n[1] - n[0]) > e:
                e = n[1]
        else:
            res.append((m, e))
            m = s[i][0]
            e = s[i][1]
        i += 1

    res.append((m, e))

    return reduce(lambda x, y: x + y, [z[1] - z[0] for z in res])


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEquals(sum_of_intervals([(1, 5), (1, 5)]), 4)
        self.assertEquals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
        self.assertEquals(sum_of_intervals([(1, 5)]), 4)
        self.assertEquals(sum_of_intervals([(1, 5), (6, 10)]), 8)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
