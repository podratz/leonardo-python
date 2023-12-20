from typing import cast, overload

from ..geometry import Angle
from .arithmeticsequence import ArithmeticSequence


class AngleSequence(ArithmeticSequence):
    """An arithmetic sequence of angles."""

    def __init__(self, angle: Angle) -> None:
        super().__init__(common_difference=angle.radians, initial_term=angle.radians)

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
