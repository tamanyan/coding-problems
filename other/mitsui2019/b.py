
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


def main():
    N = int(input())

    # print(math.floor(N * 1.08))

    for i in range(100000):
        if N == int(i * 1.08):
            print(i)
            return

    print(':(')


if __name__ == '__main__':
    main()
