import unittest
from arithmetic_evaluation import evaluateArithmeticExpr


class TestEvaluation(unittest.TestCase):
    def test_evaluate(self):
        values = [
            ('1+1', 2),
            ('1+2*3', 7),
            ('(1+2)*3', 9),
            ('2*3+4*5', 26),
            ('2*(3+4)*5', 70),
            ('10-6/2', 7),
            ('(10-6)/2', 2),
            ('(2+3)*(4+5)', 45),
            ('(2+3)*(4+5*2)', 70),
            ('100/10/2', 5),
            ('50-10*2+5', 35),
            ('50-(10*2)+5', 35),
            ('(50-10)*(2+5)', 280),
            ('3+4*2/(1+1)', 7),
        ]
        for input, expected in values:
            self.assertEqual(evaluateArithmeticExpr(input), expected)


    def test_invalid(self):
        invalid = [
            '1+',
            '+1',
            '1++2',
            '1*/2',
            '(1+2',
            '1+2)',
            '(1+)',
            '()*3',
        ]
        for expr in invalid:
            with self.assertRaises(ValueError):
                evaluateArithmeticExpr(expr)