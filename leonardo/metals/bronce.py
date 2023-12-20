import math

from .metal import Metal


class Bronce(Metal):
    """A class to work with the bronce ratio."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The bronce ratio which approximates to 3.303."""
        return (3 + math.sqrt(13)) / 2
