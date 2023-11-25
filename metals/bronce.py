import math

from .metal import Metal


class Bronce(Metal):
    """A class to simplify working with the bronce mean."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The bronce ratio that approximates to 3.303."""
        return (3 + math.sqrt(13)) / 2
