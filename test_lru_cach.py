from unittest import TestCase

from lru_cache import LruCache
numbers = [1, 20, 10]
class TestLruCache(TestCase):
    cache:LruCache[int, int]
    def setUp(self):
        self.cache = LruCache(3)
        for num in numbers:
            self.cache.add(num, num ** 2)
    def test_add_exceeding_maxsize(self):
        self.cache.add(5, 25)
        self.assertEqual(25, self.cache.access(5))
        with self.assertRaises(KeyError):
            self.cache.access(1)
    def test_access_ordering(self):
        self.assertEqual(1, self.cache.access(1))
        self.assertEqual(400, self.cache.access(20))
        self.cache.add(5, 25)
        self.assertEqual(25, self.cache.access(5))
        self.assertEqual(1, self.cache.access(1))
        self.assertEqual(400, self.cache.access(20))
        with self.assertRaises(KeyError):
            self.cache.access(10)
    def test_square_braces_access(self):
        self.assertEqual(400, self.cache[20])   # access
    def test_square_braces_add(self):
        self.cache[5] = 25
        with self.assertRaises(KeyError):
            self.cache[1]
    def test_square_braces_update(self):
        self.cache[20] = 40
        self.assertEqual(40, self.cache[20]) 
        self.assertEqual(1, self.cache[1] )     
    def test_iterable(self):
        current: int = 0
        for key in self.cache:
            self.assertEqual(numbers[current], key) 
            current += 1      
    def test_clear(self) :
        self.cache.clear()
        self.assertEqual(0, len([n for n in self.cache]))    
              
           