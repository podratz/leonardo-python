import unittest

from leonardo.geometric_primitives.geometric_ratio import GeometricRatio
from leonardo.metals.gold import Gold


class TestGeometricRatio(unittest.TestCase):
    def setUp(self) -> None:
        self.phi = float(Gold.ratio())

    def test_ratio_default(self) -> None:
        ratio = GeometricRatio()
        self.assertEqual(ratio, 1)

    def test_ratio_string_rounding(self) -> None:
        ratio = GeometricRatio(self.phi)
        ratio_str = str(ratio)
        self.assertEqual(ratio_str, "1.618")

    def test_ratio_float_conversion(self) -> None:
        ratio = GeometricRatio(self.phi)
        self.assertEqual(float(ratio), self.phi)

    def test_ratio_int_conversion(self) -> None:
        ratio = GeometricRatio(self.phi)
        ratio_rounded = int(ratio)
        self.assertEqual(ratio_rounded, 1)

    def test_pow(self) -> None:
        ratio = GeometricRatio(self.phi)
        ratio_pow = ratio**2
        phi_pow = self.phi**2
        self.assertEqual(ratio_pow, phi_pow)

    def test_repr_float(self) -> None:
        ratio = GeometricRatio(self.phi)
        ratio_repr = repr(ratio)
        self.assertEqual(ratio_repr, repr(self.phi))

    def test_multi_args(self) -> None:
        ratio = GeometricRatio(1, self.phi**2)
        self.assertEqual(ratio, self.phi)


if __name__ == "__main__":
    unittest.main()
