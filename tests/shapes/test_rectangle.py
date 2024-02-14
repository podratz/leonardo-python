import unittest

from leonardo.shapes.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_rectangle(self) -> None:
        width = 10
        height = 20
        rectangle = Rectangle(width, height)
        self.assertEqual(rectangle.width, width)
        self.assertEqual(rectangle.height, height)

    def test_rectangle_equality(self) -> None:
        rect1 = Rectangle(10, 20)
        rect2 = Rectangle(10, 20)
        self.assertEqual(rect1, rect2)


if __name__ == "__main__":
    unittest.main()
