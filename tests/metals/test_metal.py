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

    def test_metallic_rectangle_of_height_negative_3(self) -> None:
        dneg3 = DoubleMetal(-3)
        dneg3_rectangle = dneg3.rectangle()
        self.assertEqual(dneg3_rectangle.height, -3)
        self.assertEqual(dneg3_rectangle.width, -6)

    def test_metallic_rectangle_of_height_negative_1(self) -> None:
        dneg1 = DoubleMetal(-1)
        dneg1_rectangle = dneg1.rectangle()
        self.assertEqual(dneg1_rectangle.height, -1)
        self.assertEqual(dneg1_rectangle.width, -2)

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

    def test_metallic_rectangle_of_height_three(self) -> None:
        d3 = DoubleMetal(3)
        d3_rectangle = d3.rectangle()
        self.assertEqual(d3_rectangle.height, 3)
        self.assertEqual(d3_rectangle.width, 6)


if __name__ == "__main__":
    unittest.main()
