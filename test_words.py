from unittest import TestCase

from words import Words
_words:list[str] = ["apple", "Application", "Apricot", "approach", "ALL", "app"+chr(0x10ffff)]

class TestWords(TestCase):
    
    def setUp(self):
       self.words = Words()
       for word in _words:
           self.words.addWord(word)
    def test_add_word (self):
        with self.assertRaises(ValueError):
            self.words.addWord("Apple") 
            
    def test_words_with_prefix (self):
        self.assertEqual(["apple", "Application",  "approach","app"+chr(0x10ffff)], self.words.wordsStratsWith("app")) 
        self.assertEqual(["apple", "Application"], self.words.wordsStratsWith("appl")) 
        self.assertEqual(["apple", "Application", "approach","app"+chr(0x10ffff), "Apricot" ], self.words.wordsStratsWith("ap")) 
        self.assertEqual(["ALL","apple", "Application", "approach", "app"+chr(0x10ffff),"Apricot" ], self.words.wordsStratsWith("a")) 
    def test_wotrd_with_max_chr(self) :
        self.words.addWord(chr(0x10ffff))
        self.assertEqual([chr(0x10ffff)], self.words.wordsStratsWith(chr(0x10ffff)))
                 