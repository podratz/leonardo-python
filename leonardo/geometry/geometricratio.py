from dataclasses import dataclass


@dataclass
class GeometricRatio:
    """Wrapper that provides more appropriate interface to geometric ratios."""

    value: int | float = 1

    def __eq__(self, value: object) -> bool:
        return self.value == value

    def __str__(self) -> str:
        return f"{self.value:.3f}"

    def __float__(self) -> float:
        return float(self.value)

    def __int__(self) -> int:
        return int(self.value)

    def __pow__(self, exp: int) -> float:
        return self.value**exp
