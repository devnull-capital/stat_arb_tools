import unittest
from pandas import read_csv
from numpy import delete
from stat_arb_tools import calcSpread, calcSpreadReturn

class TestCalcSpread(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(0, calcSpread(1, 1, 1))
        self.assertEqual(-1, calcSpread(0, 1, 1))
        self.assertEqual(1, calcSpread(1, 0, 1))
        self.assertEqual(1, calcSpread(1, 1, 0))
        self.assertEqual(-5, calcSpread(3, 4, 2))

class TestCalcSpreadReturn(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(0, calcSpreadReturn(1, 1, 1))
        self.assertEqual(-1, calcSpreadReturn(0, 1, 1))
        self.assertEqual(-0.625, calcSpreadReturn(3, 4, 2))

if __name__ == '__main__':
    unittest.main()
