from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, product, combinations_with_replacement
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
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True


def main():
    N, M = MI()

    # graph = [[1] * (M+2) for i in range(N+2)]
    # for i in range(1, N+1):
    #     for j in range(1, M+1):
    #         for v in product([0, -1, 1], repeat=2):
    #             graph[v[0] + i][v[1] + j] = 1 - graph[v[0] + i][v[1] + j]

    # ans = 0
    # for i in range(1, N+1):
    #     for j in range(1, M+1):
    #         if graph[i][j] == 0:
    #             ans += 1

    # print(ans)

    if N == 1 and M == 1:
        print(1)
    elif M == 1 or N == 1:
        print(max(N, M) - 2)
    else:
        print((M - 2) * (N - 2))


if __name__ == '__main__':
    main()
