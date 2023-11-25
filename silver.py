import math

from leonardo import GeometricSequence


class Silver:
    """A class to simplify working with the silver ratio."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The silver ratio that approximates to 2.414."""
        return (2 + math.sqrt(8)) / 2

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """The series of numbers following each other with the silver mean."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)
