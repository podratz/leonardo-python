from types import NotImplementedType
from typing import Self, cast, overload

from ..geometry import Angle
from .arithmeticsequence import ArithmeticSequence


class AngleSequence(ArithmeticSequence):
    """An arithmetic sequence of angles."""

    def __init__(self, angle: Angle, start: Angle = Angle.zero) -> None:
        super().__init__(common_difference=angle.radians, initial_term=start.radians)

    @overload
    def __getitem__(self, subscript: int) -> Angle:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[Angle]:
        ...

    def __getitem__(self, subscript: int | slice) -> Angle | list[Angle]:
        item = super().__getitem__(subscript)
        if isinstance(subscript, int):
            radians = cast(float, item)
            return Angle.from_radians(radians)
        if isinstance(subscript, slice):
            list_of_angles = cast(list[Angle], item)
            return list_of_angles

    def __add__(self, other: object) -> NotImplementedType | Self:
        if isinstance(other, Angle):
            cls = type(self)
            angle = Angle.from_radians(self.common_difference)
            start = Angle.from_radians(self.initial_term + other.radians)
            return cls(angle=angle, start=start)
        return NotImplemented

    def __iadd__(self, other: object) -> NotImplementedType | None:
        if isinstance(other, Angle):
            self.initial_term += other.radians
        return NotImplemented
