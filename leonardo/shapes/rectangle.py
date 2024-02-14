class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        """Create a rectangle."""
        self.width = width
        self.height = height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height
