"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

Alright, detective, one of our colleagues successfully observed our target person, Robby the robber.
We followed him to a secret warehouse, where we assume to find all the stolen stuff.
The door to this warehouse is secured by an electronic combination lock.
Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw
could actually be another adjacent digit (horizontally or vertically, but not diagonally).
E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs,
they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function,
that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN
with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#).
But please note that all PINs, the observed one and also the results, must be strings,
because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

"""
import itertools
import unittest


def get_pins(observed):
    digits = [
        [-1, -1, -1, -1, -1],
        [-1, 1, 2, 3, -1],
        [-1, 4, 5, 6, -1],
        [-1, 7, 8, 9, -1],
        [-1, -1, 0, -1, -1],
        [-1, -1, -1, -1, -1]
    ]
    res = []
    for l in observed:
        coords = [(r_id, c_id) for r_id, row in enumerate(digits) for c_id, col in enumerate(row) if col == int(l)]

        x, y = coords[0]
        v = 1 + 0j
        variants = [str(digits[x][y])]
        for i in range(4):
            val = digits[x + int(v.imag)][y + int(v.real)]
            v = v * 1j
            if val < 0:
                continue
            variants.append(str(val))
        res.append(variants)

    cross = list(itertools.product(*res))
    out = ["".join(x) for x in cross]

    return sorted(list(set(out)))


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        src = '8'
        dst = sorted(['5', '7', '8', '9', '0'])
        self.assertEquals(get_pins(src), dst)
        src = '11'
        dst = sorted(["11", "22", "44", "12", "21", "14", "41", "24", "42"])
        self.assertEquals(get_pins(src), dst)
        src = '369'
        dst = sorted([
                "339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
                "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
                "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"
        ])
        self.assertEquals(get_pins(src), dst)


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
