
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
IINF = 10**9
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True

# dfs


def dfs(graph):
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    W = len(graph)
    H = len(graph[0])
    ans = 0
    start = []
    ans = IINF

    for x in range(len(graph)):
        for y in range(len(graph[x])):
            start.append((x, y))

    for p in start:
        visited = [[False] * 10 for i in range(10)]
        # visited[p[0]][p[1]] = True
        prev = graph[p[0]][p[1]]
        graph[p[0]][p[1]] = 'o'
        number_of_island = 0

        for x in range(len(graph)):
            for y in range(len(graph[x])):
                if graph[x][y] == 'x' or visited[x][y] is True:
                    continue

                stack = [(x, y)]

                while stack != []:
                    v = stack.pop()
                    visited[v[0]][v[1]] = True

                    for op in options:
                        n = (v[0] + op[0], v[1] + op[1])

                        if n[0] >= 0 and n[0] < W and n[1] >= 0 and n[1] < H:
                            f = graph[n[0]][n[1]]
                            if visited[n[0]][n[1]] is False and f == 'o':
                                stack.append(n)

                number_of_island += 1

        ans = min(ans, number_of_island)
        graph[p[0]][p[1]] = prev

    return ans


def main():
    graph = [[0] * 10 for i in range(10)]

    for i in range(10):
        graph[i] = list(input())

    print('YES' if dfs(graph) == 1 else 'NO')


if __name__ == '__main__':
    main()
