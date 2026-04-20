from unittest import TestCase
from sortings import bsearch
class TestBsearch(TestCase):
    listTested = [10,20, 30, 40]
    def test_key_found(self):
        self.assertEqual(0, bsearch(self.listTested, 10))
        self.assertEqual(3, bsearch(self.listTested, 40))
        self.assertEqual(1, bsearch(self.listTested, 20))
    def test_key_not_found(self) :
        self.assertEqual(-1, bsearch(self.listTested, 5))
        self.assertEqual(-3, bsearch(self.listTested, 25))
        self.assertEqual(-5, bsearch(self.listTested, 50))  
    