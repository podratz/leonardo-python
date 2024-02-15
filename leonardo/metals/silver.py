import math

from ..geometric_primitives import GeometricRatio
from .metal import Metal


class Silver(Metal):
    """A class to work with the silver ratio."""

    @classmethod
    def ratio(cls) -> GeometricRatio:
        """The silver ratio which approximates to 2.414."""
        return GeometricRatio((2 + math.sqrt(8)) / 2)
