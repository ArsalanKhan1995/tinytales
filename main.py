import math
import random
import sys
import timeit
from radix import radixsort
start_time = timeit.default_timer()
def digits(number, base=10):
    assert number >= 0
    if number == 0:
        return [0]
    l = []
    while number > 0:
        l.append(number % base)
        number = number // base
    return l

a = digits(3**1000)
b = radixsort(a)
acc = 0
for i in b:
    acc += i
print(acc)

elapsed = timeit.default_timer() - start_time
print(elapsed)
