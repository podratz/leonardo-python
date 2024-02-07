from dataclasses import dataclass


@dataclass
class Ratio:
    """Wrapper that provides more semantic interface to mathematical ratio concept."""

    value: int | float = 1

    def __eq__(self, value: object) -> bool:
        return self.value == value

    def __str__(self) -> str:
        return f"{self.value:.3f}"
