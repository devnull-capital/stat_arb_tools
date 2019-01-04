import unittest
from stat_arb_tools import calcKellyCritereon, calcSimpKellyCritereon

class TestCalcKellyCritereon(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(5.0, calcKellyCritereon(1, 0.9, 0.2))
        self.assertEqual(round(-1.1111111111111112, 4), round(calcKellyCritereon(0, 0.9, 0.9), 4))
        self.assertEqual(round(-7.777777777777778, 4), round(calcKellyCritereon(0.2, 0.1, 0.9), 4))
        self.assertEqual(round(0.6666666666666666, 4), round(calcKellyCritereon(0.7, 0.6, 0.6), 4))

class TestCalcSimpKellyCritereon(unittest.TestCase):
    def test_random_numbers(self):
        self.assertEqual(round(0.88, 4), round(calcSimpKellyCritereon(0.9, 0.2), 4))
        self.assertEqual(round(-0.9, 4), round(calcSimpKellyCritereon(0, 0.9), 4))
        self.assertEqual(round(0.12, 4), round(calcSimpKellyCritereon(0.2, 0.1), 4))
        self.assertEqual(round(0.52, 4), round(calcSimpKellyCritereon(0.7, 0.6), 4))
