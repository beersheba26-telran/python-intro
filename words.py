from sortedcontainers import SortedKeyList


class Words: 
    __words: SortedKeyList[str]
    __lower: set[str]
    def __init__(self):
        self.__words = SortedKeyList(key=str.lower)
        self.__lower=set()
    def addWord(self, word:str):
        '''
        adds new word
        throw ValueError in the case word exists
        in collection case should be kept, but "Apple" and "apple" considered as equaled words
        '''
        if word.lower() in self.__lower:
            raise ValueError(f"{word} already exists")
        self.__lower.add(word.lower())
        self.__words.add(word)
        
    def wordsStratsWith(self, prefix: str)->list[str]:
        '''
        returns all words beginning from the given prefix
        '''
        left: int = self.__words.bisect_left(prefix)
        right: int = self.__words.bisect_right(prefix + chr(0x10ffff))
        return self.__words[left:right]
            