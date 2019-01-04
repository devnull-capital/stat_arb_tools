import unittest
from pandas import read_csv
from numpy import delete
from stat_arb_tools import adf, isStationary

class TestADF(unittest.TestCase):
    def test_female_births(self):
        data = read_csv('stat_arb_tools/tests/test_data/daily-total-female-births.csv', header=0)

        res  = adf(delete(data.values, [0], axis=1).ravel())
        print(res)

        self.assertEqual(round(-4.808291253559763, 4), round(res[0], 4))
        self.assertEqual(round(5.243412990149865e-05, 4), round(res[1], 4))

class TestIsStationary(unittest.TestCase):
    def test_female_births(self):
        appleData = read_csv('stat_arb_tools/tests/test_data/aapl_20080601_20131231.csv', header=0)
        appleList = delete(appleData.values, [0], axis=1).ravel()

        googData = read_csv('stat_arb_tools/tests/test_data/goog_20080601_20131231.csv', header=0)
        googList = delete(googData.values, [0], axis=1).ravel()

        res = isStationary(appleList, googList)

        self.assertEqual(round(-1.3403293516072663, 4), round(res[0], 4))
        self.assertEqual(round(0.6105256778014359, 4), round(res[1], 4))

if __name__ == '__main__':
    unittest.main()
