import unittest
from pandas import read_csv
from numpy import delete
from stat_arb_tools import calcSigmaHat, calcEffectiveStandardDeviation, calcBetaHat

class TestCalcSigmaHat(unittest.TestCase):
    def test_female_births(self):
        data = read_csv('stat_arb_tools/tests/test_data/daily-total-female-births.csv', header=0)
        arr = delete(data.values, [0], axis=1).ravel()
        betaHat = calcBetaHat(arr, arr)

        sigmaHat = calcSigmaHat(arr, arr, betaHat)
        self.assertEqual(0.0, sigmaHat)

    def test_tech_stocks(self):
        appleData = read_csv('stat_arb_tools/tests/test_data/aapl_20080601_20131231.csv', header=0)
        appleList = delete(appleData.values, [0], axis=1).ravel()

        googData = read_csv('stat_arb_tools/tests/test_data/goog_20080601_20131231.csv', header=0)
        googList = delete(googData.values, [0], axis=1).ravel()

        betaHat = calcBetaHat(appleList, googList)

        sigmaHat = calcSigmaHat(appleList, googList, betaHat)
        self.assertEqual(round(0.13820923793111195, 4), round(sigmaHat, 4))

class TestCalcEffectiveStandardDeviation(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(round(1.5811388300842, 4), round(calcEffectiveStandardDeviation(1, 1, 1), 4))
        self.assertEqual(round(0, 4), round(calcEffectiveStandardDeviation(0, 1, 1), 4))
        self.assertEqual(round(1.1858541225631, 4), round(calcEffectiveStandardDeviation(3, 4, 1), 4))

if __name__ == '__main__':
    unittest.main()
