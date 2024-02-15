from types import NotImplementedType
from typing import Self, cast, overload

from ..geometric_primitives import Angle
from .arithmetic_sequence import ArithmeticSequence


class AngleSequence:
    """An arithmetic sequence of angles."""

    def __init__(self, angle: Angle, start: Angle = Angle.zero()) -> None:
        self.sequence = ArithmeticSequence(
            common_difference=angle.radians, initial_term=start.radians
        )

    @overload
    def __getitem__(self, subscript: int) -> Angle:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[Angle]:
        ...

    def __getitem__(self, subscript: int | slice) -> Angle | list[Angle]:
        item = self.sequence[subscript]
        if isinstance(subscript, int):
            radians = cast(float, item)
            return Angle(radians=radians)
        if isinstance(subscript, slice):
            list_of_angles = cast(list[Angle], item)
            return list_of_angles

    def __add__(self, other: object) -> NotImplementedType | Self:
        if isinstance(other, Angle):
            cls = type(self)
            angle = Angle(radians=self.sequence.common_difference)
            start = Angle(radians=self.sequence.initial_term + other.radians)
            return cls(angle=angle, start=start)
        return NotImplemented

    def __iadd__(self, other: object) -> NotImplementedType | None:
        if isinstance(other, Angle):
            self.sequence.initial_term += other.radians
        return NotImplemented
