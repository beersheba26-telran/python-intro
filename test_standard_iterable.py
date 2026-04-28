from unittest import TestCase
class TestStandardIterable(TestCase):
    numbers: list[int]
    def setUp(self):
        self.numbers = [10, 20, 30, 40,50]
    def test_iterable(self):
        self.assertEqual(5, len([num for num in self.numbers]))
        self.assertEqual(5, len([num for num in self.numbers]))
    def test_iterator(self) :
        it = iter(self.numbers) 
        it_numbers = []
        try:
            while True:
                it_numbers.append(next(it)) 
        except StopIteration:
            pass
        self.assertListEqual(self.numbers, it_numbers)         