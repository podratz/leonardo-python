class Rectangle:
    """A class that encapsulates logic around the Rectangle shape."""

    def __init__(self, width: float, height: float) -> None:
        """Create a rectangle."""
        self.width = width
        self.height = height

    def __eq__(self, other: object) -> bool:
        """Test rectangle for equality."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.width == other.width and self.height == other.height

    def __repr__(self) -> str:
        """Serialize rectangle for us programmers."""
        return f"Rectangle(width={self.width}, height={self.height})"
