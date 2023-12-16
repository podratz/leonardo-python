import math
from enum import Enum, auto
from typing import Self


class Angle:
    class Measure(Enum):
        degrees = auto()
        radians = auto()

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
    def divisor(cls, measure: Measure = Measure.radians) -> float:
        return 360 if measure is Angle.Measure.radians else math.tau

    @classmethod
    def from_mean(cls, mean: float, measure: Measure = Measure.radians):
        return cls(cls.divisor(measure) * mean)
