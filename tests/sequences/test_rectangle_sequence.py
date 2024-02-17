import unittest

from leonardo.geometric_primitives.geometric_ratio import GeometricRatio
from leonardo.sequences.rectangle_sequence import RectangleSequence
from leonardo.shapes.rectangle import Rectangle


class TestRectangleSequence(unittest.TestCase):
    def setUp(self) -> None:
        self.double_ratio = GeometricRatio(2)
        self.rect = Rectangle(3, 2)
        self.rectangle_seq = RectangleSequence(self.double_ratio, self.rect)
        return super().setUp()

    def test_rectangle_scaling(self) -> None:
        rectneg, rect0, rect1, rect2 = self.rectangle_seq[-1:3]

        self.assertEqual(rectneg.width, self.rect.width / 2)
        self.assertEqual(rectneg.height, self.rect.height)

        self.assertEqual(rect0.width, self.rect.width)
        self.assertEqual(rect0.height, self.rect.height)

        self.assertEqual(rect1.width, self.rect.width * 2)
        self.assertEqual(rect1.height, self.rect.height)

        self.assertEqual(rect2.width, self.rect.width * 4)
        self.assertEqual(rect2.height, self.rect.height)

    def test_rectangle_sequence_default_base(self) -> None:
        rect1, rect2 = self.rectangle_seq[:3]

        self.assertEqual(rect1.width, self.rect.width * 2)
        self.assertEqual(rect1.height, self.rect.height)

        self.assertEqual(rect2.width, self.rect.width * 4)
        self.assertEqual(rect2.height, self.rect.height)


if __name__ == "__main__":
    unittest.main()
