from unittest import TestCase
import re
import regular_expressions
'''
arithmetic expression with no spaces and no parenthesses 
'''
arithmeticExprPattern: re.Pattern = re.compile(regular_expressions.arithmeticExprRegex())
class TestSimplifiedArithmeticExpr(TestCase):
    def test_true_cases(self):
        self.assertTrue(arithmeticExprPattern.fullmatch("10"))
        self.assertTrue(arithmeticExprPattern.fullmatch("10/2+15-6*4/2"))
    def test_false_cases(self):
        self.assertFalse(arithmeticExprPattern.fullmatch("10&4+100"))    
        self.assertFalse(arithmeticExprPattern.fullmatch("10 10/2"))    