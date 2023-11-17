import math
import unittest

from leonardo import GoldenSequence


class TestGoldenSequence(unittest.TestCase):
    golden_ratio = (1 + math.sqrt(5)) / 2

    def test_call(self):
        g0 = GoldenSequence(0)
        g0_successor = g0()
        self.assertEqual(g0_successor, 0)

        g1 = GoldenSequence(1)
        g1_successor = g1()
        self.assertAlmostEqual(g1_successor, self.golden_ratio)

        g17 = GoldenSequence(17)
        g17_successor = g17()
        self.assertAlmostEqual(g17_successor, 17 * self.golden_ratio)

        g = GoldenSequence()
        self.assertNotEqual(g, g0)
        self.assertEqual(g, g1)
        self.assertNotEqual(g, g17)
