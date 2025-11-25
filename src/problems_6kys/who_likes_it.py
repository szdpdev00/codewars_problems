"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

Description:

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

import unittest


def likes(names):
    n = len(names)

    part1 = f"{'like' if n > 1 else 'likes'} this"
    if n == 0:
        return "no one " + part1

    part1 = f"{'others ' if n > 3 else ''}" + part1

    part1 = f"{len(names) - 2 if n > 3 else names[0 + n // 2 + n // 3]} " + part1
    if n == 1:
        return part1

    part1 = f"{names[0] if n == 2 else names[1]} and " + part1

    if n == 2:
        return part1

    return f"{names[0]}, " + part1


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(likes([]), 'no one likes this')
        self.assertEqual(likes(['Peter']), 'Peter likes this')
        self.assertEqual(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(likes(["Alex", "Jacob", "Mark", "Max"]), "Alex, Jacob and 2 others like this")
        self.assertEqual(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
