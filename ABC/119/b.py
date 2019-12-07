
from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time
from fractions import gcd
#import random


def divisor(n):
    """
    n の約数をリストで返す
    :param int n:
    :rtype: list of int
    """
    ret = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret

def MI(): return map(int, input().split())


def main():
    N = int(input())
    BTC = 380000.0
    ans = 0

    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'BTC':
            ans += x * BTC
        else:
            ans += x

    print(ans)


if __name__ == '__main__':
    main()
