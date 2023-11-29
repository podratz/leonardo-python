import math
import unittest
from typing import cast

from leonardo.metals import Gold
from leonardo.utils import GeometricSequence


class TestGoldSequence(unittest.TestCase):
    def setUp(self) -> None:
        self.golden_ratio = (1 + math.sqrt(5)) / 2
        self.g = Gold()

    def test_call(self):
        g0 = Gold(0)
        g0_successor = g0()
        self.assertEqual(g0_successor, 0.0)

        g1 = Gold(1)
        g1_successor = g1()
        self.assertAlmostEqual(g1_successor, self.golden_ratio)

        g17 = Gold(17)
        g17_successor = g17()
        self.assertAlmostEqual(g17_successor, 17.0 * self.golden_ratio)

        self.assertNotEqual(self.g, g0)
        self.assertEqual(self.g, g1)
        self.assertNotEqual(self.g, g17)

    def test_getitem(self):
        g_neg1 = 1.0 / self.golden_ratio
        self.assertEqual(cast(float, self.g[-1]), g_neg1)

        g0 = 1.0
        self.assertEqual(cast(float, self.g[0]), g0)

        g1 = self.golden_ratio
        self.assertEqual(cast(float, self.g[1]), g1)

        g_neg6_neg2 = [self.golden_ratio**n for n in range(-6, -2)]
        self.assertListEqual(cast(list[float], self.g[-6:-2]), g_neg6_neg2)

        g_neg2_3 = [self.golden_ratio**n for n in range(-2, 3)]
        self.assertListEqual(cast(list[float], self.g[-2:3]), g_neg2_3)

        g_3_7 = [self.golden_ratio**n for n in range(3, 7)]
        self.assertListEqual(cast(list[float], self.g[3:7]), g_3_7)

        g_2_neg3_neg1 = [self.golden_ratio**n for n in range(2, -3, -1)]
        self.assertListEqual(cast(list[float], self.g[2:-3:-1]), g_2_neg3_neg1)

        self.assertRaises(
            TypeError, GeometricSequence.__getitem__, self.g, slice(None, 5, 1)
        )

        self.assertRaises(
            TypeError, GeometricSequence.__getitem__, self.g, slice(2, None, 1)
        )

        self.assertRaises(
            ValueError, GeometricSequence.__getitem__, self.g, slice(2, 5, 0)
        )


if __name__ == "__main__":
    unittest.main()
