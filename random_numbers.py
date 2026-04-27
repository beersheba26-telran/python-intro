from typing import Iterator, Callable
import random
class RandomIntegerNumbers:
    __min: int
    __max: int
    __amount: int
    def __init__(self, min, max, *, amount: int = -1,isdistinct=False, predicate:
        Callable[[int], bool] = lambda num: bool(num)):
        if min >= max:
            raise ValueError(f" min {min} greater or equal max {max}")
        self.__min = min
        self.__max = max
        self.__current = 0
        self.__amount = amount
    def __iter__(self)->Iterator[int]:
           
        while self.__amount != self.__current:
            self.__current += 1
            num: int = self.__getRandomNumber()
            yield num
    def __getRandomNumber(self) :
        return random.randint(self.__min, self.__max)
              