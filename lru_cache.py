from functools import lru_cache
import time


@lru_cache(maxsize=4)
def long_square(x: int)->int:
    time.sleep(2)
    return x ** 2
args = [1,2, 3, 4,  1]
for arg in args:
    start = time.perf_counter()
    print (long_square(arg))
    end = time.perf_counter()
    print(f"first call of function takes with argument {arg}", end - start, "sec")
    print(long_square(arg))
    print(f"second call of function takes {arg}", time.perf_counter() - end, "sec")