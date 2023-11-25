from abc import ABC, abstractmethod

from ..geometric_sequence import GeometricSequence


class Metal(ABC):
    """A class to simplify working with the metallic means."""

    @property
    @classmethod
    @abstractmethod
    def ratio(cls) -> float:
        """A metallic ratio."""
        raise NotImplementedError

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """A series of numbers following the metallic ratio in growth."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)
