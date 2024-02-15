import math

from ..geometric_primitives import GeometricRatio
from .metal import Metal


class Gold(Metal):
    """A class to work with the golden ratio."""

    @classmethod
    def ratio(cls) -> GeometricRatio:
        """The golden ratio which approximates to 1.618."""
        return GeometricRatio((1 + math.sqrt(5)) / 2)
