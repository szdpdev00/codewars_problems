"""
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
representation being returned. Valid decimal values for RGB are 0 - 255
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

"""

import unittest


def rgb(r, g, b):
    return "".join([f"{min(max(x, 0), 255):02X}" for x in [r, g, b]])


class TestProblem(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def baseTest(self):
        self.assertEqual(rgb(0, 0, 0), "000000")
        self.assertEqual(rgb(1, 2, 3), "010203")
        self.assertEqual(rgb(-20, 275, 125), "00FF7D")


def run():
    suite = unittest.TestSuite()
    suite.addTest(TestProblem("baseTest"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
