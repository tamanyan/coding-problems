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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    HOUSE = 's'
    FISH = 'g'
    BLOCK = '#'
    ROAD = '.'
    H, W = map(int, input().split())
    graph = [None] * H
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False for i in range(W)] for i in range(H)]
    house_pos = None
    ans = 'No'

    for i in range(H):
        graph[i] = list(input())

        for j in range(W):
            if graph[i][j] == BLOCK:
                visited[i][j] = True
            elif graph[i][j] == HOUSE:
                house_pos = (i, j)
                visited[i][j] = True

    stack = deque([house_pos])
    while len(stack) > 0:
        p = stack.pop()

        for d in options:
            i = p[0] + d[0]
            j = p[1] + d[1]

            if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] == ROAD:
                visited[i][j] = True
                stack.append((i, j))
            elif i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] == FISH:
                ans = 'Yes'
                visited[i][j] = True

    print(ans)


if __name__ == '__main__':
    main()
