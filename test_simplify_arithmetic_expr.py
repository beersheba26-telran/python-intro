import re
import regular_expressions
from unittest import TestCase

class TestSimplifyArithmeticExpr(TestCase):
    def test_simplify_arithmetic_expr(self):
        simplifyArithmeticExprRX = regular_expressions.arithmeticRegex()
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "1+2"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "3-4"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "5*6"))
        self.assertTrue(re.fullmatch(simplifyArithmeticExprRX, "7/8"))
        #self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "9+10-11"))
        #self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "12*13/14"))
        #self.assertFalse(re.fullmatch(simplifyArithmeticExprRX, "15+16*17"))