import unittest

from leonardo.sequences.arithmeticsequence import ArithmeticSequence


class TestArithmeticsequence(unittest.TestCase):
    def test_arithmeticsequence(self) -> None:
        arithmeticsequence = ArithmeticSequence()
        self.assertIsNot(arithmeticsequence, None)


if __name__ == "__main__":
    unittest.main()
