import unittest

from leonardo.geometry.geometricratio import GeometricRatio
from leonardo.metals.metal import Metal


class SimpleMetal(Metal):
    @classmethod
    def ratio(cls) -> GeometricRatio:
        return GeometricRatio(2)


class TestMetal(unittest.TestCase):
    def test_metal(self) -> None:
        metal = SimpleMetal()
        self.assertIsNot(metal, None)

    def test_rectangle(self) -> None:
        metal = SimpleMetal(1)
        rectangle = metal.rectangle()
        self.assertEqual(rectangle.height, 1)
        self.assertEqual(rectangle.width, 2)

    def test_rectangle_zero(self) -> None:
        metal = SimpleMetal(0)
        rectangle = metal.rectangle()
        self.assertEqual(rectangle.height, 0)
        self.assertEqual(rectangle.width, 0)

    def test_rectangle_two(self) -> None:
        metal = SimpleMetal(3)
        rectangle = metal.rectangle()
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.width, 6)


if __name__ == "__main__":
    unittest.main()
