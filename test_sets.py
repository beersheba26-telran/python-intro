from unittest import TestCase
from sets import remove_repeated, max_negative_representive
class SetsTest(TestCase):
    def test_remove_repeated(self):
        lst = [23, 45, -10, 23, 48, 23]
        self.assertEqual([23, 45, -10, 48], remove_repeated(lst))
        
    def test_max_positive_with_negative_representive(self) :
        ar1 = [100, 10, 1000, -1] 
        ar2 = [100, 1, 10, 1000, -1]  
        ar3 = [100, 1, -100, -1, -1000, 1000]
        self.assertEqual(-1, max_negative_representive(ar1))
        self.assertEqual(1, max_negative_representive(ar2))
        self.assertEqual(1000, max_negative_representive(ar3))