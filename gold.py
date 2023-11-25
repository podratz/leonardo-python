import math

from .metal import Metal


class Gold(Metal):
    """A class to simplify working with the golden mean."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The golden ratio that approximates to 1.618."""
        return (1 + math.sqrt(5)) / 2
