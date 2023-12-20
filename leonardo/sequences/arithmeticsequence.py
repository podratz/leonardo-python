import itertools
from types import NotImplementedType
from typing import cast, overload


class ArithmeticSequence:
    """An arithmetic sequence."""

    def __init__(self, common_difference: float = 1.0, initial_term: float = 0.0):
        self.common_difference = common_difference
        """The constant difference between two successive terms."""
        self.initial_term = initial_term
        """The initial term of the sequence."""

    @overload
    def __getitem__(self, subscript: int) -> float:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[float]:
        ...

    def __getitem__(self, subscript: int | slice) -> float | list[float]:
        if isinstance(subscript, int):
            n = cast(int, subscript)
            d = self.common_difference
            a_1 = self.initial_term
            a_n = a_1 + (n - 1) * d
            return a_n
        elif isinstance(subscript, slice):
            s = cast(slice, subscript)
            sequence = [self[index] for index in range(s.start, s.stop, s.step)]
            return sequence
        else:
            raise TypeError(
                f"Type of subscript must be a slice or int, but {subscript} was found."
            )

    def __iter__(self):
        """Iterate this infinite arithmetic sequence."""
        for index in itertools.count():
            yield self[index]

    def __eq__(self, other: object) -> NotImplementedType | bool:
        """Return True if and only if the common differences and initial terms are the same."""
        if not isinstance(other, ArithmeticSequence):
            return NotImplemented
        return (
            self.common_difference == other.common_difference
            and self.initial_term == other.initial_term
        )
