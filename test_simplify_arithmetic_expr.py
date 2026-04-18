import re
import regular_expressions
from unittest import TestCase

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
