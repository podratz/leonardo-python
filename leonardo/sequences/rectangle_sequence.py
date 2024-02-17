import itertools
from types import NotImplementedType
from typing import Generator, cast, overload

from ..geometric_primitives import GeometricRatio
from ..shapes import Rectangle


class RectangleSequence:
    """A sequence of rectangles."""

    def __init__(
        self,
        common_ratio: GeometricRatio,
        rectangle: Rectangle,
    ):
        """Create a geometric sequence from a common ratio and a scale factor."""
        self.common_ratio = common_ratio
        self.rectangle = rectangle

    @overload
    def __getitem__(self, subscript: int) -> Rectangle:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> Generator[Rectangle, None, None]:
        ...

    def __getitem__(
        self, subscript: int | slice
    ) -> Rectangle | Generator[Rectangle, None, None]:
        """Return the element at the given index, or the subsequence bound by the given slice."""
        if isinstance(subscript, int):
            n = cast(int, subscript)

            factor = self.common_ratio**n
            item = Rectangle(self.rectangle.width * factor, self.rectangle.height)
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

            sequence = (self[index] for index in range(start, stop, step))
            return sequence

    def __iter__(self):
        """Iterate this infinite geometric sequence."""
        for index in itertools.count():
            yield self[index]

    def __eq__(self, other: object) -> NotImplementedType | bool:
        """Return True if and only if the scale factors and common ratios are equal."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return (
            self.rectangle.width == other.width
            and self.rectangle.height == other.height
        )
