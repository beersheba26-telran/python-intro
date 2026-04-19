from unittest import TestCase
from arithmetic_check import checkArithmeticExpr
class TestArithmeticExpr(TestCase):
    def test_true_cases(self):
        self.assertTrue(checkArithmeticExpr("10 "))
        self.assertTrue(checkArithmeticExpr("10/2+15-6*4/2"))
        self.assertTrue(checkArithmeticExpr("( 10 / ( (2+15) ) -6*4 )/ 2"))
    def test_false_cases(self):
        self.assertFalse(checkArithmeticExpr("10&4+100"))    
        self.assertFalse(checkArithmeticExpr("10 10/2")) 
        self.assertFalse(checkArithmeticExpr("( 10 / (2+15) -6*4 / 2")) 