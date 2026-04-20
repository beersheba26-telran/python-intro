import numpy as np
import time
import sys
N = 1000_000_000
grn = np.random.default_rng()
start = time.perf_counter()
ar: np.array = grn.random(N, dtype=np.float32)
end = time.perf_counter()
print(f"time for creating {N} float numbers in numpy array is {(end -start):.3f} sec")
print (f"size of numpy array is {sys.getsizeof(ar)}")
