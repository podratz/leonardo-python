import math
from enum import Enum, auto
from typing import Self


class Angle:
    class Measure(Enum):
        DEGREES = auto()
        RADIANS = auto()

        @property
        def unity(self) -> float:
            return 360.0 if self is self.DEGREES else math.tau

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
    def divisor(cls, measure: Measure = Measure.RADIANS) -> float:
        return 360 if measure is Angle.Measure.RADIANS else math.tau

    @classmethod
    def from_mean(cls, mean: float, measure: Measure = Measure.RADIANS):
        return cls(cls.divisor(measure) * mean)
