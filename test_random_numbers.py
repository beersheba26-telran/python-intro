from itertools import islice
from unittest import TestCase
from typing import Iterator
from random_numbers import RandomIntegerNumbers
class TestRandomNumbers(TestCase):
    def test_endless_iterating(self):
        randomNumbers = RandomIntegerNumbers(10, 20)
        first_100 = list(islice(randomNumbers, 100))
        self.assertEqual(100, len(first_100))
        
    def test_list_comprehansive(self):
        '''
        test for iterable
        '''
        
        size=1000
        min =10
        max = 20
        randomNumbers = RandomIntegerNumbers(min, max, amount=size)
        numbers: list[int] = list(randomNumbers)
        self.assertEqual(size, len(numbers))
        for num in numbers:
            self.assertTrue(min<=num<=max)
    def test_random_numbers_iterator(self):
        '''
        test for iterator
        '''
        randomNumbers = RandomIntegerNumbers(1, 2, amount=2)
        it: Iterator = iter(randomNumbers)
        self.assertTrue(1 <=it.__next__()<=2)
        self.assertTrue(2>=next(it) >= 1)
        with self.assertRaises(StopIteration):
            next(it)
    def test_random_numbers_distinct(self):
        for i in range(10) :
            randomNumbers = RandomIntegerNumbers(1, 3, amount=3, isdistinct=True)
            self.assertEqual(3, len(set(randomNumbers))) 
    def test_random_numbers_predicate(self) :
        for i in range(5):
            randomNumbers = RandomIntegerNumbers(1, 3, amount=3, predicate=lambda n : n % 2)
            numbers = list(randomNumbers)    
            self.assertEqual(3, len(numbers))  
            for num in  numbers:
                self.assertTrue(num % 2)  
    def test_random_numbers_predicate_distinct(self) :
        for i in range(5):
            randomNumbers = RandomIntegerNumbers(1, 200, amount=30, isdistinct=True, predicate=lambda n : n % 2)
            numbers =set(randomNumbers)    
            self.assertEqual(30, len(numbers))  
            for num in  numbers:
                self.assertTrue(num % 2)             
            
                   
            
                
            
            
        