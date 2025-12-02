"""
https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

Create a function that takes a positive integer and returns the next bigger number that can be formed
by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1

"""

import unittest


def next_bigger(n):
    tmp = [x for x in str(n)]
    for i in range(len(str(n)) - 1, 0, -1):
        if tmp[i] <= tmp[i-1]:
            continue

        r = min([x for x in tmp[i:] if x > tmp[i-1]])
        t = [x for x in tmp[i-1:]]
        t.remove(r)
        tmp[i-1] = r
        part = sorted(t)

        cur_n = int("".join(tmp[:i]) + "".join(part))
        if cur_n > n:
            return cur_n

    return -1


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEquals(next_bigger(59884848459853), 59884848483559)
        self.assertEquals(next_bigger(12), 21)
        self.assertEquals(next_bigger(21), -1)
        self.assertEquals(next_bigger(513), 531)
        self.assertEquals(next_bigger(2017), 2071)
        self.assertEquals(next_bigger(414), 441)
        self.assertEquals(next_bigger(144), 414)
        self.assertEquals(next_bigger(1234567890), 1234567908)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
