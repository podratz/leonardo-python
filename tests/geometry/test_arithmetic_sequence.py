import unittest

from leonardo.sequences.arithmetic_sequence import ArithmeticSequence


class TestArithmeticsequence(unittest.TestCase):
    def test_arithmetic_sequence(self) -> None:
        arithmeticsequence = ArithmeticSequence()
        self.assertIsNot(arithmeticsequence, None)


if __name__ == "__main__":
    unittest.main()
