"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

"""

import unittest


def snail(snail_map):
    res = []
    n = len(snail_map)
    if n < 2:
        return snail_map[0]
    while len(snail_map):
        res += snail_map.pop(0)
        for i in range(0, len(snail_map)):
            res.append(snail_map[i].pop(-1))
        if snail_map:
            res += snail_map.pop(-1)[::-1]
        for i in range(len(snail_map), 0, -1):
            res.append(snail_map[i - 1].pop(0))

    return res


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        src = [[]]
        dst = []
        self.assertEqual(snail(src), dst)
        src = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
        dst = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(snail(src), dst)
        src = [[1, 2, 3],
               [8, 9, 4],
               [7, 6, 5]]
        dst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(snail(src), dst)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
