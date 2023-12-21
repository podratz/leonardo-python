import math
from abc import ABC, abstractmethod
from copy import Error, copy
from functools import total_ordering
from types import NotImplementedType
from typing import Self, overload

from ..geometry import Angle
from ..sequences import AngleSequence, GeometricSequence


@total_ordering
class Metal(ABC):
    """A class to work with metallic ratios."""

    def __init__(self, magnitude: float = 1.0) -> None:
        self.magnitude = magnitude
        """The magnitude of the metallic number."""

    # Ratio methods

    @classmethod
    @property
    @abstractmethod
    def ratio(cls) -> float:
        """The metallic ratio."""
        raise NotImplementedError

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """A sequence of numbers following the metallic ratio in growth."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)

    # Angle methods

    @classmethod
    @property
    def angle(cls) -> Angle:
        """The metallic angle."""
        fraction = 1 / (1 + cls.ratio)
        return Angle(fraction)

    @property
    def angle_adjusted(self) -> Angle:
        """The adjusted multiple of the metallic angle."""
        if not self:
            return Angle.zero
        cls = type(self)
        n = 1 + math.log(self.magnitude, cls.ratio)
        return cls.angle * n

    @classmethod
    @property
    def angle_sequence(cls) -> AngleSequence:
        """A sequence of angles following the metallic ratio in rotation."""
        return AngleSequence(cls.angle)

    @property
    def angles(self) -> AngleSequence:
        return type(self).angle_sequence + self.angle_adjusted

    # Item access

    @overload
    def __getitem__(self, subscript: int) -> float:
        ...

    @overload
    def __getitem__(self, subscript: slice) -> list[float]:
        ...

    def __getitem__(self, subscript: int | slice) -> float | list[float]:
        return type(self).sequence(scale_factor=self.magnitude)[subscript]

    def __next__(self) -> Self:
        """The next metallic number."""
        next = self[1]
        cls = type(self)
        return cls(next)

    def __call__(self, n: int = 1) -> float:
        """The (nth) next metallic value."""
        item = self[n]
        return item

    # Comparison

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

    # Arithmetic

    class ArithmeticError(Error):
        """An error type raised for invalid arithmetic operations on metallic numbers."""

    def __iadd__(self, n: int) -> Self:
        """Add the nth metallic predecessor to itself."""
        if n == 0:
            raise Metal.ArithmeticError("in-place addition with zero")
        self.magnitude += self[-n]
        return self

    def __isub__(self, n: int) -> Self:
        """Subtract the nth metallic predecessor from itself."""
        if n == 0:
            raise Metal.ArithmeticError("in-place subtraction with zero")
        self.magnitude -= self[-n]
        return self

    def __add__(self, n: int) -> Self:
        """Add the nth metallic predecessor."""
        if n == 0:
            raise Metal.ArithmeticError("addition with zero")
        metal = copy(self)
        metal.magnitude += self[-n]
        return metal

    def __sub__(self, n: int) -> Self:
        """Subtract the nth metallic predecessor."""
        if n == 0:
            raise Metal.ArithmeticError("subtraction with zero")
        metal = copy(self)
        metal.magnitude -= self[-n]
        return metal

    # Coalescing

    def __str__(self) -> str:
        return str(self.magnitude)

    def __float__(self) -> float:
        return float(self.magnitude)

    def __int__(self) -> int:
        return int(self.magnitude)

    def __bool__(self) -> bool:
        return bool(self.magnitude)

    # Debug

    def __repr__(self) -> str:
        cls = self.__class__
        return "{}({})".format(cls.__name__, self.magnitude)
