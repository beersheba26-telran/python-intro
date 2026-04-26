from unittest import TestCase

from words import Words
_words:list[str] = ["apple", "Application", "Apricot", "approach", "ALL"]

class TestWords(TestCase):
    
    def setUp(self):
       self.words = Words()
       for word in _words:
           self.words.addWord(word)
    def test_add_word (self):
        with self.assertRaises(ValueError):
            self.words.addWord("Apple") 
            
    def test_words_with_prefix (self):
        self.assertEqual(["apple", "Application",  "approach"], self.words.wordsStratsWith("app")) 
        self.assertEqual(["apple", "Application"], self.words.wordsStratsWith("appl")) 
        self.assertEqual(["apple", "Application", "approach", "Apricot" ], self.words.wordsStratsWith("ap")) 
        self.assertEqual(["ALL","apple", "Application", "approach", "Apricot" ], self.words.wordsStratsWith("a")) 
              