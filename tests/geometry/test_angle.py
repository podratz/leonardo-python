import math
import unittest

from leonardo.geometry import Angle


class TestAngle(unittest.TestCase):
    def test_radians(self) -> None:
        angle0 = Angle.from_radians(0)
        self.assertEqual(angle0.radians, 0)

        angle90 = Angle.from_radians(math.pi / 2)
        self.assertEqual(angle90.radians, 1 * math.tau / 4)

        angle180 = Angle.from_radians(math.pi)
        self.assertEqual(angle180.radians, 2 * math.tau / 4)

        angle270 = Angle.from_radians(3 * math.pi / 2)
        self.assertEqual(angle270.radians, 3 * math.tau / 4)

        angle360 = Angle.from_radians(math.tau)
        self.assertEqual(angle360.radians, 4 * math.tau / 4)

    def test_from_degrees(self) -> None:
        angle0 = Angle.from_degrees(0)
        self.assertEqual(angle0.radians, 0)

        angle90 = Angle.from_degrees(90)
        self.assertEqual(angle90.radians, 1 * math.tau / 4)

        angle180 = Angle.from_degrees(180)
        self.assertEqual(angle180.radians, 2 * math.tau / 4)

        angle270 = Angle.from_degrees(270)
        self.assertEqual(angle270.radians, 3 * math.tau / 4)

        angle360 = Angle.from_degrees(360)
        self.assertEqual(angle360.radians, 4 * math.tau / 4)


if __name__ == "__main__":
    unittest.main()
