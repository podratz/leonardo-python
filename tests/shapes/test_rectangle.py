import unittest

from leonardo.shapes.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle(self) -> None:
        rectangle = Rectangle()
        self.assertIsNot(rectangle, None)


if __name__ == "__main__":
    unittest.main()
