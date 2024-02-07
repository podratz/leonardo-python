import math
from dataclasses import dataclass
from types import NotImplementedType
from typing import Self


@dataclass
class Angle:
    fraction: float = 0

    def __init__(self, **kwargs: float) -> None:
        if len(kwargs) != 1:
            raise TypeError(f"Angle() takes exactly one argument ({len(kwargs)} given)")

        key, value = kwargs.popitem()
        match key:
            case "fraction":
                self.fraction = value
            case "degrees":
                self.fraction = value / 360
            case "radians":
                self.fraction = value / math.tau
            case _:
                raise KeyError(f"key '{key}' is invalid")

    @classmethod
    def zero(cls) -> Self:
        return cls(fraction=0.0)

    # Properties

    @property
    def fraction_canonic(self) -> float:
        return self.fraction % 1

    @property
    def radians(self) -> float:
        return self.fraction * math.tau

    @property
    def radians_canonic(self) -> float:
        return self.radians % math.tau

    @property
    def degrees(self) -> float:
        return self.fraction * 360

    @property
    def degrees_canonic(self) -> float:
        return self.degrees % 360

    @property
    def complex(self) -> complex:
        real = math.cos(self.radians)
        imag = math.sin(self.radians)
        return complex(real, imag)

    # Arithmetic

    def __add__(self, other: object) -> NotImplementedType | Self:
        if isinstance(other, Angle):
            cls = type(self)
            fraction = self.fraction + other.fraction
            return cls(fraction=fraction)
        return NotImplemented

    def __iadd__(self, other: object) -> NotImplementedType | None:
        if isinstance(other, Angle):
            self.fraction += other.fraction
        return NotImplemented

    def __mul__(self, other: object) -> NotImplementedType | Self:
        if isinstance(other, int | float):
            cls = type(self)
            fraction = self.fraction * other
            return cls(fraction=fraction)
        return NotImplemented

    def __imul__(self, other: object) -> NotImplementedType | None:
        if isinstance(other, int | float):
            self.fraction *= other
        return NotImplemented

    # Coalescing

    def __str__(self) -> str:
        return f"{self.degrees:.2f}\u00B0"
