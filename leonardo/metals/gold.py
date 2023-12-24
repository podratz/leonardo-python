import math

from .metal import Metal


class Gold(Metal):
    """A class to work with the golden ratio."""

    @classmethod
    def ratio(cls) -> float:
        """The golden ratio which approximates to 1.618."""
        return (1 + math.sqrt(5)) / 2
