import math

from .metal import Metal


class Silver(Metal):
    """A class to work with the silver ratio."""

    @classmethod
    def ratio(cls) -> float:
        """The silver ratio which approximates to 2.414."""
        return (2 + math.sqrt(8)) / 2
