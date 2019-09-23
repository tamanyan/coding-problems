import math
from itertools import accumulate


K, X = list(map(int, input().split()))

print(' '.join([str(i) for i in range(X - K + 1, X + K)]))