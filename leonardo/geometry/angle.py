import math
from typing import Self


class Angle:
    def __init__(self, radians: float) -> None:
        self.radians = radians

    @classmethod
    def from_mean(cls, mean: float) -> Self:
        radians = mean * math.tau
        return cls(radians)

    @classmethod
    def from_degrees(cls, degrees: float) -> Self:
        radians = degrees * math.tau / 360
        return cls(radians)

    @property
    def degrees(self) -> float:
        return self.radians * 360 / math.tau

    def __float__(self):
        return self.radians
