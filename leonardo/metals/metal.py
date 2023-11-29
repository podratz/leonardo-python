import math
from abc import ABC, abstractmethod
from functools import total_ordering
from types import NotImplementedType
from typing import Self

from ..utils.angle_sequence import AngleSequence
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

    def __init__(self, magnitude: float = 1.0) -> None:
        self.magnitude = float(magnitude)

    def __getitem__(self, subscript) -> list[float]:
        return type(self).sequence(scale_factor=self.magnitude)[subscript]

    def __call__(self, n: int = 1) -> float:
        [item] = self[n]
        return item

    def __next__(self) -> Self:
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
