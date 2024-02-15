import itertools
from types import NotImplementedType
from typing import cast, overload

from ..geometric_primitives import GeometricRatio


class GeometricSequence:
    """A geometric sequence."""

    def __init__(self, common_ratio: GeometricRatio, scale_factor: float = 1.0):
        """Create a geometric sequence from a common ratio and a scale factor."""
        self.common_ratio = common_ratio
        self.scale_factor = scale_factor

    @overload
    def __getitem__(self, subscript: int) -> float:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[float]:
        ...

    def __getitem__(self, subscript: int | slice) -> float | list[float]:
        """Return the element at the given index, or the subsequence bound by the given slice."""
        if isinstance(subscript, int):
            n = cast(int, subscript)

            item = self.scale_factor * (self.common_ratio**n)
            return item
        else:
            s = cast(slice, subscript)
            start = s.start if s.start is not None else 1

            if subscript.stop is None:
                raise TypeError("slice stop cannot be None")
            stop = s.stop

            if subscript.step == 0:
                raise ValueError("slice step cannot be zero")
            step = s.step or 1

            sequence = [self[index] for index in range(start, stop, step)]
            return sequence

    def __iter__(self):
        """Iterate this infinite geometric sequence."""
        for index in itertools.count():
            yield self[index]

    def __eq__(self, other: object) -> NotImplementedType | bool:
        """Return True if and only if the scale factors and common ratios are equal."""
        if not isinstance(other, GeometricSequence):
            return NotImplemented
        return (
            self.common_ratio == other.common_ratio
            and self.scale_factor == other.scale_factor
        )
