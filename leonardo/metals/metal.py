import math
from abc import ABC, abstractmethod
from functools import total_ordering
from types import NotImplementedType
from typing import Self, overload

from ..utils import AngleSequence, GeometricSequence


@total_ordering
class Metal(ABC):
    """A class to simplify working with metallic numbers."""

    @classmethod
    @property
    @abstractmethod
    def ratio(cls) -> float:
        """A metallic ratio."""
        raise NotImplementedError

    @classmethod
    @property
    def mean(cls) -> float:
        """A metallic mean. (inverse of the metallic ratio)"""
        return 1 / cls.ratio

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """A series of numbers following the metallic ratio in growth."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)

    def __init__(self, magnitude: float = 1.0) -> None:
        self.magnitude = float(magnitude)

    @overload
    def __getitem__(self, subscript: int) -> float:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[float]:
        ...

    def __getitem__(self, subscript: int | slice) -> float | list[float]:
        return type(self).sequence(scale_factor=self.magnitude)[subscript]

    def __call__(self, n: int = 1) -> float:
        """The (nth) next metallic value."""
        item = self[n]
        return item

    def __next__(self) -> Self:
        """The next metallic number."""
        cls = type(self)
        next = self()
        return cls(next)

    def __eq__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, Metal):
            return NotImplemented
        return (
            type(self).ratio == type(other).ratio and self.magnitude == other.magnitude
        )

    def __lt__(self, other: object) -> NotImplementedType | bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.magnitude < other.magnitude

    def __repr__(self) -> str:
        cls = self.__class__
        return "{}({})".format(cls.__name__, self.magnitude)

    def __str__(self) -> str:
        return str(self.magnitude)

    def __float__(self) -> float:
        return float(self.magnitude)

    def __int__(self) -> int:
        return int(self.magnitude)

    def __bool__(self) -> bool:
        return bool(self.magnitude)

    @classmethod
    def angle(cls, *, degrees=False) -> float:
        """Returns the metallic angle."""
        return cls.degs if degrees else cls.rads

    @classmethod
    def angle_sequence(cls, degrees=False, revolves=False) -> AngleSequence:
        """An angle-sequence following the metallic ratio."""
        return AngleSequence(
            angle=cls.angle(degrees=degrees), degrees=degrees, revolves=revolves
        )

    @classmethod
    @property
    def rads(cls) -> float:
        """Returns the metallic angle in radians."""
        return math.tau * (1 - 1 / cls.ratio)

    @classmethod
    @property
    def degs(cls) -> float:
        """Returns the metallic angle in degrees."""
        return 360 * (1 - 1 / cls.ratio)
