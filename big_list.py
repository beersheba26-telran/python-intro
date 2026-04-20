import random
import time
from sys import getsizeof
N:int = 100
start = time.perf_counter()
big_list: list = [random.uniform(0, 1) for _ in range(N)]
print(f"running time for creating {N} random numbers is {(time.perf_counter() - start):.3f} sec")
print(f"actual size of list containing {N} float numbers is {getsizeof(big_list)}")
