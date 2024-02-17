import unittest

from leonardo.geometric_primitives.geometric_ratio import GeometricRatio
from leonardo.metals.metal import Metal


class DoubleMetal(Metal):
    @classmethod
    def ratio(cls) -> GeometricRatio:
        return GeometricRatio(2)


class TestMetal(unittest.TestCase):
    # Init

    def test_default_init_is_1(self) -> None:
        d = DoubleMetal()
        self.assertEqual(d.magnitude, 1)

    def test_init_with_0(self) -> None:
        d = DoubleMetal(0)
        self.assertEqual(d.magnitude, 0)

    def test_init_with_negative_3_point_5(self) -> None:
        d = DoubleMetal(-3.5)
        self.assertEqual(d.magnitude, -3.5)

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

    def test_metallic_rectangle_of_height_negative_3_point_5(self) -> None:
        dneg15 = DoubleMetal(-3.5)
        dneg15_rectangle = dneg15.rectangle()
        self.assertEqual(dneg15_rectangle.height, -3.5)
        self.assertEqual(dneg15_rectangle.width, -7)

    def test_get_metallic_rectangles(self) -> None:
        d = DoubleMetal()
        rects = d.rectangles[:3]
        self.assertEqual(rects[0].width, rects[0].height)
        self.assertEqual(rects[1].width, rects[0].height * 2)
        self.assertEqual(rects[2].width, rects[0].height * 4)


if __name__ == "__main__":
    unittest.main()
