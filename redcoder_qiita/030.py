from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
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

BLOCK = 'X'
ROAD = '.'
START = 'S'


def bfs(graph, initial, goal, H, W):
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([initial])
    visited = [[False for i in range(W)] for i in range(H)]
    dist = [[-1 for i in range(W)] for i in range(H)]
    visited[initial[0]][initial[1]] = True
    dist[initial[0]][initial[1]] = 0

    while len(q) != 0:
        p = q.popleft()

        for d in options:
            i = p[0] + d[0]
            j = p[1] + d[1]

            if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] != BLOCK:
                visited[i][j] = True
                q.append((i, j))
                dist[i][j] = dist[p[0]][p[1]] + 1

    return dist[goal[0]][goal[1]]


def main():
    H, W, N = MI()
    graph = [None] * H
    nums = [None] * (N + 1)

    for i in range(H):
        graph[i] = list(S())

        for j in range(W):
            if graph[i][j].isnumeric():
                nums[int(graph[i][j])] = (i, j)
            elif graph[i][j] == START:
                nums[0] = (i, j)

    ans = 0
    for i in range(N):
        ans += bfs(graph, nums[i], nums[i+1], H, W)
    print(ans)


if __name__ == '__main__':
    main()
