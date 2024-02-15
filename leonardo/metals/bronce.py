import math

from ..geometric_primitives import GeometricRatio
from .metal import Metal


class Bronce(Metal):
    """A class to work with the bronce ratio."""

    @classmethod
    def ratio(cls) -> GeometricRatio:
        """The bronce ratio which approximates to 3.303."""
        return GeometricRatio((3 + math.sqrt(13)) / 2)
