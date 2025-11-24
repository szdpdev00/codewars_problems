"""
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.

"""

import unittest


def solution(number):
    if number < 4:
        return 0

    res = (x for x in range(3, number) if x % 3 == 0 or x % 5 == 0)

    return sum(res)


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(solution(10), 23)
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(13), 45)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
