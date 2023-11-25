import itertools
from types import NotImplementedType


class GeometricSequence:
    def __init__(self, common_ratio: float, scale_factor: float = 1):
        self.common_ratio = common_ratio
        self.scale_factor = scale_factor

    def __call__(self, n: int = 1) -> float:
        return self.scale_factor * (self.common_ratio**n)

    def __getitem__(self, subscript) -> list[float]:
        if isinstance(subscript, int):
            return [self(subscript)]

        if subscript.start is None:
            raise TypeError("sequence requires pre-determined start")
        start = subscript.start

        if subscript.step is not None and subscript.stop is None:
            raise TypeError("sequence with step needs pre-determined stop")
        stop = subscript.stop

        if subscript.step == 0:
            raise ValueError("slice step cannot be zero")
        step = subscript.step or 1

        return [self(index) for index in range(start, stop, step)]

    def __iter__(self):
        for index in itertools.count():
            yield self(index)

    def __eq__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, GeometricSequence):
            return NotImplemented
        return (
            self.common_ratio == other.common_ratio
            and self.scale_factor == other.scale_factor
        )
