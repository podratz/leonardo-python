import math
from typing import Self

from .circlemeasure import CircleMeasure


class Angle:
    def __init__(self, radians: float) -> None:
        self.radians = radians

    @classmethod
    def from_degrees(cls, degrees: float) -> Self:
        radians = degrees * math.tau / 360
        return cls(radians)

    @property
    def degrees(self) -> float:
        return self.radians * 360 / math.tau

    @classmethod
    def divisor(cls, measure: CircleMeasure = CircleMeasure.RADIANS) -> float:
        return 360 if measure is CircleMeasure.RADIANS else math.tau

    @classmethod
    def from_mean(cls, mean: float, measure: CircleMeasure = CircleMeasure.RADIANS):
        return cls(cls.divisor(measure) * mean)
