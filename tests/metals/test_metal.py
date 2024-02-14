import unittest

from leonardo.geometry.geometricratio import GeometricRatio
from leonardo.metals.metal import Metal


class DoubleMetal(Metal):
    @classmethod
    def ratio(cls) -> GeometricRatio:
        return GeometricRatio(2)


class TestMetal(unittest.TestCase):
    def test_metal_instantiates(self) -> None:
        d = DoubleMetal()
        self.assertIsNot(d, None)

    # Rectangle

    def test_metallic_rectangle_of_height_zero(self) -> None:
        d0 = DoubleMetal(0)
        d0_rectangle = d0.rectangle()
        self.assertEqual(d0_rectangle.height, 0)
        self.assertEqual(d0_rectangle.width, 0)

    def test_metallic_rectangle_of_height_1(self) -> None:
        d1 = DoubleMetal(1)
        d1_rectangle = d1.rectangle()
        self.assertEqual(d1_rectangle.height, 1)
        self.assertEqual(d1_rectangle.width, 2)

    def test_metallic_rectangle_of_height_negative_1_point_5(self) -> None:
        dneg15 = DoubleMetal(-1.5)
        dneg15_rectangle = dneg15.rectangle()
        self.assertEqual(dneg15_rectangle.height, -1.5)
        self.assertEqual(dneg15_rectangle.width, -3)


if __name__ == "__main__":
    unittest.main()
