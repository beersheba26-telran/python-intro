import unittest
from arithmetic_evaluation import evaluateArithmeticExpr


class TestEvaluation(unittest.TestCase):
    def test_evaluate(self):
        values = [
            ('1+1', 2)
        ]
        for input, expected in values:
            self.assertEqual(evaluateArithmeticExpr(input), expected)