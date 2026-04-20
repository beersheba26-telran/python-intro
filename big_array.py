from array import array
import random
import time
from sys import getsizeof
N:int = 100
start = time.perf_counter()
big_array:array = array("i", (random.uniform(0, 1) for _ in range(N)))
big_array.append(0.5)
print(f"running time for creating {N} random numbers is {(time.perf_counter() - start):.3f} sec")
print(f"actual size of array containing {N} float numbers is {getsizeof(big_array)}")