"""
https://www.codewars.com/kata/69138048ff69ef74385d5941/train/python

You are tasked with a variant of the "look-and-write" sequence.
The sequence is built iteratively according to the following rules.
Start with the sequence "11". After looking at the current sequence, for each digit 0–9,
check how many times it appears.
For every digit that occurs at least once, append its count followed by the digit to the end of the sequence.
The new sequence is formed by adding all these pairs in order to the current sequence.

Your task is to compute the length of the sequence after n looks on the sequence.

Input: n, the number of times you look at the sequence (0 ≤ n ≤ 7*10^5) for Javascript, for Python: (0 ≤ n ≤ 2*10^5)

Output: An integer representing the length of the sequence after n looks

Examples:

n = 1

Start with "11". Then, for the first look, it’s "11" + there are two 1s, so "21".
Concatenating gives "1121", and the length is 4.

n = 3

Start with "11". Then, for the first look, it’s "11" + there are two 1s, so "21".
Concatenating gives "1121". For the second look, there are three 1s and one 2,
so concatenate "1121" + "31" + "12" → "11213112".
For the last look, in "11213112" there are five 1s, two 2s, and one 3,
so concatenate "11213112" + "51" + "22" + "13" → "11213112512213". The length is 14.
"""

import unittest


def look_and_write(n):
    s = "11"
    last_pos = 0
    a = [0] * 10
    for i in range(n):
        for j in range(last_pos, len(s)):
            a[int(s[j])] += 1
        last_pos = len(s)
        for j in range(10):
            if a[j] == 0:
                continue
            s = s + str(a[j]) + str(j)
        print(s)
        print(";".join(map(str, a)))
        print(f"{i + 1} - {len(s)}")
    return len(s)


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(look_and_write(0), 2)
        self.assertEqual(look_and_write(1), 4)
        self.assertEqual(look_and_write(3), 14)
        self.assertEqual(look_and_write(8000), 456426)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
