from multiprocessing import Pool
import time

def loop():
    start = time.time()
    p = Pool(5)
    p.map(f, lst)
    print(f"MultiThreding: {round(time.time() - start, 2)}")

    start = time.time()
    [f(i) for i in lst]
    print(f"List Comprehension: {round(time.time() - start, 2)}")

    start = time.time()
    for i in lst:
        f(i)
    print(f"Normal Loop: {round(time.time() - start, 2)}")

    start = time.time()
    list(map(f, lst))
    print(f"Map: {round(time.time() - start, 2)}")


lst = list(range(10000))
def f(x):
    x**x
loop()
# MultiThreding: 2.34
# List Comprehension: 5.87
# Normal Loop: 6.78
# Map: 7.26


lst = list(range(10000))
def f(x):
    str(x**x)
loop()
# MultiThreding: 31.71
# List Comprehension: 99.71
# Normal Loop: 100.22
# Map: 100.37