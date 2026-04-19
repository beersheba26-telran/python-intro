from unittest import TestCase
from arithmetic_evaluation import evaluation


class TestArithmeticNMulDivNoParenthesesEval(TestCase):
    def test_right_expr_no_mul_div(self):
        expr: str = "2.23 + 3.12 - 10 + 100.54 -20 +0"
        self.assertAlmostEqual(2.23 + 3.12 - 10 + 100.54 -
                               20 + 0, evaluation(expr), places=2)
    def test_right_expr_no_prefernces(self):
        expr: str = "2.23 *4 / 3.12 * 10 / 2* 100.54 -20 +40"
        self.assertAlmostEqual(2.23 *4 / 3.12 * 10 / 2* 100.54 -20 +40, evaluation(expr), places=2)
    def test_right_expr_preferences(self):
        expr: str = "2.23 +4 / 3.12 * 10 / 2* 100.54 -20 +40" 
        self.assertAlmostEqual(2.23 +4 / 3.12 * 10 / 2* 100.54 -20 +40, evaluation(expr), places=2)
    def test_right_full_expr(self):
         expr: str = "((2.23 +4) / 3.12) * (10 / 2)* 100.54 -(20 -40) + (40 -20)"  
         self.assertAlmostEqual(((2.23 +4) / 3.12) * (10 / 2)* 100.54 -(20 -40)+ (40 -20), evaluation(expr), places=2)     
    def test_wrong_expr(self):
        with self.assertRaises(ValueError):
            evaluation("2,23 + 20")
