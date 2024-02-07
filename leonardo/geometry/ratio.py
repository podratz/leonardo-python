from dataclasses import dataclass


@dataclass
class Ratio:
    """Wrapper that provides more semantic interface to mathematical ratio concept."""

    value: int = 1

    def __eq__(self, value: object) -> bool:
        return self.value == value
