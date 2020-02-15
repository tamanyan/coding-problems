
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


YN = ['Yes', 'No']
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


# show_flg = False
show_flg = True


def main():
    N, M = MI()
    ab = [None] * M

    for i in range(M):
        a, b = MI()
        ab[i] = [a, b]

    ab = sorted(ab, key=lambda v: v[1])
    bridges = [ab[0]]
    # print(ab)

    for i in range(1, M):
        if bridges[-1][1] <= ab[i][0]:
            bridges.append(ab[i])

    print(len(bridges))


if __name__ == '__main__':
    main()
