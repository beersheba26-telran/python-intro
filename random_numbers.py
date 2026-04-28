from typing import Iterator, Callable
import random
class RandomIntegerNumbers:
    __min: int
    __max: int
    __amount: int
    __isdistinct: bool
    __predicate: Callable[[int], bool]
    __helper: set[int]
    def __init__(self, min, max, *, limit_iterations=1000, amount: int = -1,isdistinct=False, predicate:
        Callable[[int], bool] = lambda num: bool(num)):
        if min >= max:
            raise ValueError(f" min {min} greater or equal max {max}")
        self.__min = min
        self.__max = max
        self.__amount = amount
        self.__isdistinct = isdistinct
        self.__predicate = predicate
        self.__helper = set()
        self.__limit_iterations = limit_iterations
    def __iter__(self)->Iterator[int]:
        current = 0   
        while self.__amount != current:
            num = self.__getRandomNumber()
            self.__isdistinct and self.__helper.add(num)
            current += 1
            yield num
    def __getRandomNumber(self) :
        iteration = self.__limit_iterations
        while  iteration:
            number = random.randint(self.__min, self.__max)
            if  number not in self.__helper and self.__predicate(number):
                break
            iteration -= 1
        if not iteration:
            raise ValueError(f"limit iterations {self.__limit_iterations} exceeds")    
        return number;   
              