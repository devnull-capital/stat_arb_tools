import unittest
from pandas import read_csv
from numpy import delete
from stat_arb_tools import calcBetaHat, calcHedgeRatio

class TestCalcBetaHat(unittest.TestCase):
    def test_female_births(self):
        data = read_csv('stat_arb_tools/tests/test_data/daily-total-female-births.csv', header=0)
        arr = delete(data.values, [0], axis=1).ravel()
        self.assertEqual(1, calcBetaHat(arr, arr))

    def test_tech_stocks(self):
        appleData = read_csv('stat_arb_tools/tests/test_data/aapl_20080601_20131231.csv', header=0)
        appleList = delete(appleData.values, [0], axis=1).ravel()

        googData = read_csv('stat_arb_tools/tests/test_data/goog_20080601_20131231.csv', header=0)
        googList = delete(googData.values, [0], axis=1).ravel()

        self.assertEqual(round(0.1479640618306254, 4), round(calcBetaHat(appleList, googList), 4))

class TestCalcHedgeRatio(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(1.5, calcHedgeRatio(1, 1))
        self.assertEqual(0, calcHedgeRatio(0, 1))
        self.assertEqual(1, calcHedgeRatio(1, 0))
        self.assertEqual(9, calcHedgeRatio(3, 4))

if __name__ == '__main__':
    unittest.main()
