import unittest

from leonardo.shapes.triangle import Triangle


class TestTriangle(unittest.TestCase):
    def test_triangle(self) -> None:
        triangle = Triangle()
        self.assertIsNot(triangle, None)


if __name__ == "__main__":
    unittest.main()
