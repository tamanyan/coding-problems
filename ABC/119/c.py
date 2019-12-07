
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


show_flg = False
# show_flg = True

A = 0
B = 0
C = 0
N = 0


def dfs(cur, L, a, b, c):
    # print(A, B, C)
    if cur == N:
        return abs(A - a) + abs(B - b) + abs(C - c) if min(a, b, c) > 0 else IINF

    ret0 = dfs(cur + 1, L, a, b, c)
    ret1 = dfs(cur + 1, L, a + L[cur], b, c) + (0 if a == 0 else 10)
    ret2 = dfs(cur + 1, L, a, b + L[cur], c) + (0 if b == 0 else 10)
    ret3 = dfs(cur + 1, L, a, b, c + L[cur]) + (0 if c == 0 else 10)

    return min(ret0, ret1, ret2, ret3)


def main():
    global A
    global B
    global C
    global N
    N, A, B, C = MI()
    L = [0] * N

    for i in range(N):
        L[i] = int(input())

    print(dfs(0, L, 0, 0, 0))


if __name__ == '__main__':
    main()
