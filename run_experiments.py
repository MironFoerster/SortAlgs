import bubble, insert, merge, quick
from random import randint as rint
import threading
import copy as cp
from time import time as tm
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)

lengths = [1000, 10000, 100000, 1000000]
algs = [bubble, insert, merge, quick]
times = []

def run_all():
    for n in lengths:
        arr = [rint(0, n-1) for i in range(n)]
        times.append([])
        print(n)
        for alg in algs:
            print(alg)
            start = tm()
            alg.sort(cp.copy(arr))
            end = tm()
            secs = (end - start) / 1000
            times[-1].append(secs)
    print(times)


threading.stack_size(200000000)
thread = threading.Thread(target=run_all)
thread.start()
