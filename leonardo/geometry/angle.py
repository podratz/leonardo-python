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

    @property
    def degrees_canonic(self) -> float:
        return self.degrees % 360

    @property
    def canonic(self) -> float:
        return self.radians % math.tau

    def __float__(self):
        return self.radians

    def __repr__(self):
        return f"Angle({self.radians})"
