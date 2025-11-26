"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""

import unittest


def move_zeros(lst):
    t = [x for x in lst if x]
    return t + [0] * (len(lst) - len(t))


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
        )

        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

        self.assertEqual(move_zeros(
            [0, 0]),
            [0, 0]
        )

        self.assertEqual(move_zeros(
            [0]),
            [0]
        )

        self.assertEqual(move_zeros(
            []),
            []
        )

def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
