from unittest import TestCase
from count_occurrences import count_occurrences
class TestCountOccurrences(TestCase):
    def test_counts_occurrences(self):
        strings = ["lmn","ab", "a", "ab","aa","aa","lmn","lmn"]
        expected = [("lmn",3), ("aa",2), ("ab",2), ("a", 1)]
        self.assertEqual(expected, count_occurrences(strings) )