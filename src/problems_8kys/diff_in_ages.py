"""
https://www.codewars.com/kata/5720a1cb65a504fdff0003e2/train/python

At the annual family gathering, the family likes to find the oldest living family member’s age
and the youngest family member’s age and calculate the difference between them.

You will be given an array of all the family members' ages, in any order.
The ages will be given in whole numbers, so a baby of 5 months, will have an ascribed ‘age’ of 0.
Return a new array (a tuple in Python) with [youngest age, oldest age, difference between the youngest and oldest age].

"""

import unittest


def difference_in_age(ages):
    ages.sort()
    y = ages[0]
    o = ages[-1]
    diff = o - y
    return y, o, diff


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(difference_in_age([10, 2, 84]), (2, 84, 82))


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
