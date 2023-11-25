import math

from .metal import Metal


class Silver(Metal):
    """A class to simplify working with the silver mean."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The silver ratio that approximates to 2.414."""
        return (2 + math.sqrt(8)) / 2
