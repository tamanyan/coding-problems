import math
from itertools import accumulate
from collections import Counter
import itertools
import functools


N = int(input())

strings = []
for i in range(N):
    strings.append(input())


strings = [''.join(sorted(i)) for i in strings]
c = Counter(strings)
count = 0
for i in c.values():
    if i > 1:
        count += (i * (i - 1)) / 2
print(int(count))
# print(functools.reduce(lambda a, b: a + b - 1, c.values()))