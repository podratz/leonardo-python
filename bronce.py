import math

from leonardo import GeometricSequence


class Bronce:
    """A class to simplify working with the bronce ratio."""

    @classmethod
    @property
    def ratio(cls) -> float:
        """The bronce ratio that approximates to 3.303."""
        return (3 + math.sqrt(13)) / 2

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """The series of numbers following each other with the bronce mean."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)
