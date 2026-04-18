import re
import regular_expressions
from unittest import TestCase
from arithmetic_check import checkArithmeticExpr

class TestSimplifyArithmeticExpr(TestCase):
    def test_true_cases(self):
        simplifyArithmeticExprRX = regular_expressions.arithmeticRegex()
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "1+2"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "3-4"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "5*6"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "7/8"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "9+1.0-11*9/3"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "12*13/14"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "15+16*17"))

    def test_false_cases(self):
        simplifyArithmeticExprRX = regular_expressions.arithmeticRegex()
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "+1"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "2-"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "*3"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "/4"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "5++6"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "7--8"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "9**10"))
        self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "11//12"))

    def test_with_parentheses_true(self):
        self.assertTrue(checkArithmeticExpr, "(1+2)")
        self.assertTrue(checkArithmeticExpr, "3-(4*5)")
        self.assertTrue(checkArithmeticExpr, "(6/7)+8")
        self.assertTrue(checkArithmeticExpr, "9*(10-11)")
        self.assertTrue(checkArithmeticExpr, "12/(13+14)")
        self.assertTrue(checkArithmeticExpr, "12/((13-1)+(8*9))")

    def test_with_parentheses_false(self):
        self.assertFalse(checkArithmeticExpr("(1+)2"))
        self.assertFalse(checkArithmeticExpr("3-4(*5)"))
        self.assertFalse(checkArithmeticExpr("(6/7+)8"))
        self.assertFalse(checkArithmeticExpr("((1+2)"))  # нет закрывающей
        self.assertFalse(checkArithmeticExpr(")(1+2)"))  # нарушен порядок
        self.assertFalse(checkArithmeticExpr("(1+2))("))  # сломанный баланс