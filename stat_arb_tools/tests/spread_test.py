import unittest
from pandas import read_csv
from numpy import delete
from stat_arb_tools import calcSpread, calcSpreadReturn, calcDist
from stat_arb_tools import zNorm

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

class TestCalcDist(unittest.TestCase):
    def test_female_births(self):
        data = read_csv('stat_arb_tools/tests/test_data/daily-total-female-births.csv', header=0)
        arr = delete(data.values, [0], axis=1).ravel()
        zArr = zNorm(arr)
        self.assertEqual(0, calcDist(zArr, zArr))

    def test_tech_stocks(self):
        appleData = read_csv('stat_arb_tools/tests/test_data/aapl_20080601_20131231.csv', header=0)
        appleList = delete(appleData.values, [0], axis=1).ravel()
        zAppleList = zNorm(appleList)

        googData = read_csv('stat_arb_tools/tests/test_data/goog_20080601_20131231.csv', header=0)
        googList = delete(googData.values, [0], axis=1).ravel()
        zGoogList = zNorm(googList)

        self.assertEqual(round(757.9458835107689, 4), round(calcDist(zAppleList, zGoogList), 4))

if __name__ == '__main__':
    unittest.main()
