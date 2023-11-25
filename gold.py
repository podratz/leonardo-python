import math

from .geometric_sequence import GeometricSequence


class Gold:
    """A class to simplify working with the golden ratio."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The golden ratio that approximates to 1.618."""
        return (1 + math.sqrt(5)) / 2

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """The series of numbers following each other with the golden mean."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)
