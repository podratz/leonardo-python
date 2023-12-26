import math
import unittest

from leonardo.geometry import Angle


class TestAngle(unittest.TestCase):
    def test_init(self) -> None:
        angle1 = Angle(fraction=1.23)
        self.assertEqual(angle1.fraction, 1.23)

        angle2 = Angle(degrees=90.0)
        self.assertAlmostEqual(angle2.fraction, 0.25)

        angle3 = Angle(radians=math.pi)
        self.assertAlmostEqual(angle3.fraction, 0.5)

        empty_kwargs = {}
        self.assertRaises(ValueError, Angle, **empty_kwargs)

        double_kwargs = {"param1": 1.0, "param2": 2.0}
        self.assertRaises(ValueError, Angle, **double_kwargs)

        wrong_kwargs = {"other_measure": 3.0}
        self.assertRaises(KeyError, Angle, **wrong_kwargs)

    def test_radians(self) -> None:
        angle0 = Angle(fraction=0)
        self.assertEqual(angle0.radians, 0)

        angle90 = Angle(radians=math.pi / 2)
        self.assertEqual(angle90.radians, 1 * math.tau / 4)

        angle180 = Angle(radians=math.pi)
        self.assertEqual(angle180.radians, 2 * math.tau / 4)

        angle270 = Angle(radians=3 * math.pi / 2)
        self.assertEqual(angle270.radians, 3 * math.tau / 4)

        angle360 = Angle(radians=math.tau)
        self.assertEqual(angle360.radians, 4 * math.tau / 4)

    def test_from_degrees(self) -> None:
        angle0 = Angle(degrees=0)
        self.assertEqual(angle0.radians, 0)

        angle90 = Angle(degrees=90)
        self.assertEqual(angle90.radians, 1 * math.tau / 4)

        angle180 = Angle(degrees=180)
        self.assertEqual(angle180.radians, 2 * math.tau / 4)

        angle270 = Angle(degrees=270)
        self.assertEqual(angle270.radians, 3 * math.tau / 4)

        angle360 = Angle(degrees=360)
        self.assertEqual(angle360.radians, 4 * math.tau / 4)


if __name__ == "__main__":
    unittest.main()
