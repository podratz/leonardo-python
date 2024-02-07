from math import prod


class GeometricRatio:
    """Wrapper that provides more appropriate interface to geometric ratios."""

    def __init__(self, *values: int | float) -> None:
        self._ratio = prod(values) ** (1 / len(values)) if values else 1

    def __eq__(self, value: object) -> bool:
        return self._ratio == value

    def __str__(self) -> str:
        return f"{self._ratio:.3f}"

    def __float__(self) -> float:
        return float(self._ratio)

    def __int__(self) -> int:
        return int(self._ratio)

    def __pow__(self, exp: int) -> float:
        return self._ratio**exp

    def __repr__(self) -> str:
        return repr(self._ratio)
