from abc import ABC, abstractmethod

from ..utils.geometric_sequence import GeometricSequence


class Metal(ABC):
    """A class to simplify working with the metallic means."""

    def __init__(self, scale_factor: float = 1.0) -> None:
        self._scale_factor = scale_factor

    @property
    @classmethod
    @abstractmethod
    def ratio(cls) -> float:
        """A metallic ratio."""
        raise NotImplementedError

    def __getitem__(self, subscript) -> list[float]:
        return type(self).sequence(scale_factor=self._scale_factor)[subscript]

    @classmethod
    def sequence(cls, scale_factor: float = 1.0) -> GeometricSequence:
        """A series of numbers following the metallic ratio in growth."""
        return GeometricSequence(common_ratio=cls.ratio, scale_factor=scale_factor)
