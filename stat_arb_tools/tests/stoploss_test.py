import unittest
from stat_arb_tools import calcOptimalStopLoss, calcOptimalVarStopLoss

class TestCalcOptimalStopLoss(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(0.0, calcOptimalStopLoss(1, 1, 1, 1))
        self.assertEqual(-0.5, calcOptimalStopLoss(0, 1, 1, 1))
        self.assertEqual(0.5, calcOptimalStopLoss(1, 0, 1, 1))
        self.assertEqual(-0.5, calcOptimalStopLoss(3, 4, 2, 1))

class TestCalcOptimalVarStopLoss(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual((0, 2), calcOptimalVarStopLoss(1, 1, 1))
        self.assertEqual((1, 1), calcOptimalVarStopLoss(0, 1, 1))
        self.assertEqual((1, 1), calcOptimalVarStopLoss(1, 0, 1))
        self.assertEqual((-22, 26), calcOptimalVarStopLoss(3, 4, 2))
