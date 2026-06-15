
# Function Caching in Python:-----------------------

import time

from functools import lru_cache
@lru_cache(maxsize=3)

def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("Done>>>Calling Again")
    some_work(3)
    print("Called Again!")
    some_work(10)
    print("It will be printed at after the execution of 10 second")

