import unittest

from leonardo.geometry.ratio import Ratio
from leonardo.metals.gold import Gold


class TestRatio(unittest.TestCase):
    def setUp(self) -> None:
        self.phi = Gold.ratio()

    def test_ratio_default(self) -> None:
        ratio = Ratio()
        self.assertEqual(ratio, 1)

    def test_ratio_string_rounding(self) -> None:
        ratio = Ratio(self.phi)
        ratio_str = str(ratio)
        self.assertEqual(ratio_str, "1.618")


if __name__ == "__main__":
    unittest.main()
