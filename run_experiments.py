import numpy as np
import bubble, insert, merge, quick
from random import randint as rint
import threading
from matplotlib import pyplot as plt
import copy as cp
from time import time as tm
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)

lengths = range(10000, 100000, 10000)
algs = [bubble, insert, merge, quick]
#algs = [merge, quick]
alg_names = ["bubble", "insert", "merge", "quick"]
#alg_names = ["merge", "quick"]
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
            msecs = (end - start)
            times[-1].append(msecs)
    print(times)


threading.stack_size(200000000)
thread = threading.Thread(target=run_all)
thread.start()
thread.join()
fig, ax = plt.subplots()
times = np.array(times)
times = times.T
lengths = np.expand_dims(np.array(lengths), axis=0).repeat(4, axis=0)

for idx, alg in enumerate(alg_names):
    plt.plot(lengths[idx, :], times[idx, :], label=alg, marker="o")

ax.set_xlabel('n')
ax.set_ylabel('time')
plt.legend()
plt.savefig("time_plot.svg")