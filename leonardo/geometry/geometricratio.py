class GeometricRatio:
    """Wrapper that provides more appropriate interface to geometric ratios."""

    def __init__(self, value: int | float = 1):
        self.value = value

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

    def __repr__(self) -> str:
        return repr(self.value)
