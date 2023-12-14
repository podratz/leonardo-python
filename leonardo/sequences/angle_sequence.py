import math
from typing import cast

from .arithmetic_sequence import ArithmeticSequence


class AngleSequence(ArithmeticSequence):
    """An arithmetic sequence that revolves."""

    def __init__(self, angle: float, degrees=False, revolves=False) -> None:
        super().__init__(common_difference=angle, initial_term=0.0)
        self.degrees = degrees
        self.revolves = revolves

    @property
    def _divisor(self) -> float:
        return 360 if self.degrees else math.tau

    def __getitem__(self, subscript: int | slice) -> float | list[float]:
        item = super().__getitem__(subscript)
        if isinstance(subscript, int):
            angle = cast(float, item)
            item = angle if self.revolves else angle % self._divisor
        return item
