import math
from enum import Enum, auto


class CircleMeasure(Enum):
    DEGREES = auto()
    RADIANS = auto()

    @property
    def unity(self) -> float:
        return 360 if self is CircleMeasure.DEGREES else math.tau
