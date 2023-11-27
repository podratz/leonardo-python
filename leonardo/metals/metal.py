from abc import ABC, abstractmethod
from functools import total_ordering
from types import NotImplementedType

from ..utils.geometric_sequence import GeometricSequence


@total_ordering
class Metal(ABC):
    """A class to simplify working with the metallic means."""

    @property
    @classmethod
    @abstractmethod
    def ratio(cls) -> float:
        """A metallic ratio."""
        raise NotImplementedError

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """A series of numbers following the metallic ratio in growth."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)

    def __init__(self, scale_factor: float = 1.0) -> None:
        self._scale_factor = scale_factor

    def __getitem__(self, subscript) -> list[float]:
        return type(self).sequence(scale_factor=self._scale_factor)[subscript]

    def __call__(self, n: int = 1) -> float:
        [item] = self[n]
        return item

    def __eq__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, Metal):
            return NotImplemented
        return (
            type(self).ratio == type(other).ratio
            and self._scale_factor == other._scale_factor
        )

    def __lt__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._scale_factor < other._scale_factor

    def __repr__(self) -> str:
        cls = self.__class__
        return "{}({})".format(cls.__name__, self._scale_factor)
