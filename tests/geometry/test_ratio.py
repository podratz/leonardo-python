import unittest

from leonardo.geometry.ratio import Ratio


class TestRatio(unittest.TestCase):
    def test_ratio_default(self) -> None:
        ratio = Ratio()
        self.assertEqual(ratio, 1)


if __name__ == "__main__":
    unittest.main()
