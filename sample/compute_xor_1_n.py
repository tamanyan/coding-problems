from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time
from fractions import gcd
#import random


def I(): return int(input())


def MI(): return map(int, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False

# XOR 高速


def brute_force(N):
    ans = 1

    for i in range(2, N+1):
        ans ^= i

    return


def compute_xor(N):
    #  if n is multiple of 4
    if N % 4 == 0:
        return N

    # If n % 4 gives remainder 1
    if N % 4 == 1:
        return 1

    # If n%4 gives remainder 2
    if N % 4 == 2:
        return N + 1

    # If n%4 gives remainder 3
    return 0


def main():
    N = I()

    print(compute_xor(N))


if __name__ == '__main__':
    main()
