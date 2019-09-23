import math
from itertools import accumulate


A, B, C = list(map(int, input().split()))

print(max(-(A - B - C), 0))
