import math


class AngleSequence:
    def __init__(self, angle: float, degrees=False, revolves=False) -> None:
        self.angle = angle
        self.degrees = degrees
        self.revolves = revolves

    @property
    def _divisor(self) -> float:
        return 360 if self.degrees else math.tau

    def __getitem__(self, subscript) -> list[float]:
        if isinstance(subscript, int):
            new_angle = self.angle * subscript
            new_angle = new_angle if self.revolves else new_angle % self._divisor
            return [new_angle]
        elif isinstance(subscript, slice):
            raise NotImplementedError()
        else:
            raise TypeError(
                f"Type of subscript must be a slice or int, but {subscript} was found."
            )
