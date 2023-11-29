import itertools
from types import NotImplementedType
from typing import Union, cast


class ArithmeticSequence:
    def __init__(self, common_difference: float = 1.0, initial_term: float = 0.0):
        self.common_difference = common_difference
        """The constant difference between two successive terms."""
        self.initial_term = initial_term
        """The initial term of the sequence."""

    def __getitem__(self, subscript: Union[int, slice]) -> Union[float, list[float]]:
        if isinstance(subscript, int):
            n = cast(int, subscript)
            d = self.common_difference
            a_1 = self.initial_term
            a_n = a_1 + (n - 1) * d
            return a_n
        else:
            s = cast(slice, subscript)
            sequence = [self[index] for index in range(s.start, s.stop, s.step)]
            return cast(list[float], sequence)

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
