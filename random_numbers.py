from typing import Iterator, Callable
import random
class RandomIntegerNumbers:
    __min: int
    __max: int
    __amount: int
    __isdistinct: bool
    __predicate: Callable[[int], bool]
    __helper: set[int]
    def __init__(self, min, max, *, amount: int = -1,isdistinct=False, predicate:
        Callable[[int], bool] = lambda num: bool(num)):
        if min >= max:
            raise ValueError(f" min {min} greater or equal max {max}")
        self.__min = min
        self.__max = max
        self.__current = 0
        self.__amount = amount
        self.__isdistinct = isdistinct
        self.__predicate = predicate
        self.__helper = set()
    def __iter__(self)->Iterator[int]:
           
        while self.__amount != self.__current:
            num = self.__getRandomNumber()
            self.__isdistinct and self.__helper.add(num)
            self.__current += 1
            yield num
    def __getRandomNumber(self) :
        while  True:
            number = random.randint(self.__min, self.__max)
            if  number not in self.__helper and self.__predicate(number):
                break
        return number;   
              