
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
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True


def main():
    H, W = MI()
    graph = [None] * H
    ans = []

    for i in range(H):
        graph[i] = list(MI())

    q = []
    for i in range(H):
        range_w = range(W) if i % 2 == 0 else reversed(range(W))
        for j in range_w:
            q.append((i, j))

    for idx, (i, j) in enumerate(q):
        coin = graph[i][j]
        if coin % 2 == 1 and idx + 1 < len(q):
            ni, nj = q[idx+1]
            graph[i][j] -= 1
            graph[ni][nj] += 1
            ans.append([i+1, j+1, ni+1, nj+1])

    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])


if __name__ == '__main__':
    main()
