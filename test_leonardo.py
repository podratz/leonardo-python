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

    def test_getitem(self):
        g = GoldenSequence()

        g_range_neg1 = [1/self.golden_ratio]
        self.assertListEqual(g[-1], g_range_neg1)

        g_range_0 = [1]
        self.assertListEqual(g[0], g_range_0)

        g_range_1 = [self.golden_ratio]
        self.assertListEqual(g[1], g_range_1)

        g_range_neg6_neg2 = [self.golden_ratio ** n  for n in range(-6,-2)]
        self.assertListEqual(g[-6:-2], g_range_neg6_neg2)

        g_range_neg2_3 = [self.golden_ratio ** n  for n in range(-2,3)]
        self.assertListEqual(g[-2:3], g_range_neg2_3)

        g_range_3_7 = [self.golden_ratio ** n  for n in range(3,7)]
        self.assertListEqual(g[3:7], g_range_3_7)

        g_range_2_neg3_neg1 = [self.golden_ratio ** n  for n in range(2,-3,-1)]
        self.assertListEqual(g[2:-3:-1], g_range_2_neg3_neg1)

        self.assertRaises(TypeError, GoldenSequence.__getitem__, g, slice(None, 5, 1))

        self.assertRaises(TypeError, GoldenSequence.__getitem__, g, slice(2, None, 1))

        self.assertRaises(ValueError, GoldenSequence.__getitem__, g, slice(2, 5, 0))


if __name__ == '__main__':
    unittest.main()
