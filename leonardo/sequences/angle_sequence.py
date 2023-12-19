from typing import cast

from ..geometry import CircleMeasure
from .arithmetic_sequence import ArithmeticSequence


class AngleSequence(ArithmeticSequence):
    """An arithmetic sequence that revolves."""

    def __init__(
        self, angle: float, measure=CircleMeasure.RADIANS, revolves=False
    ) -> None:
        super().__init__(common_difference=angle, initial_term=0.0)
        self.measure = measure
        self.revolves = revolves

    def __getitem__(self, subscript: int | slice) -> float | list[float]:
        item = super().__getitem__(subscript)
        if isinstance(subscript, int) and self.revolves:
            item = cast(float, item)
            item %= self.measure.unity
        return item
