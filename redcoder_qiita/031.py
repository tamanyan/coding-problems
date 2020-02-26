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


def bfs(graph, initial, visited, H, W):
    odd_options = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 1)]
    even_options = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]
    q = deque([initial])
    conn = 0
    number_of_cells = 1

    while len(q) != 0:
        p = q.popleft()

        options = even_options if p[0] % 2 == 0 else odd_options
        # print(p, options)
        for d in options:
            i = p[0] + d[0]
            j = p[1] + d[1]

            if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] == 1:
                visited[i][j] = True
                conn += 1
                number_of_cells += 1
                q.append((i, j))
            elif i >= 0 and i < H and j >= 0 and j < W and visited[i][j] and graph[i][j] == 1:
                conn += 1

    return number_of_cells, conn


def bfs_pond(graph, initial, visited, H, W):
    odd_options = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 1)]
    even_options = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]
    q = deque([initial])
    area = 0
    keep_visited = [[visited[i][j] for j in range(W)] for i in range(H)]
    visited[initial[0]][initial[1]] = True

    while len(q) != 0:
        p = q.popleft()

        options = even_options if p[0] % 2 == 0 else odd_options

        # print(initial, p, [(p[0] + d[0], p[1] + d[1]) for d in options])
        for d in options:
            i = p[0] + d[0]
            j = p[1] + d[1]

            if i < 0 or i >= H or j < 0 or j >= W:
                # print('return', initial)
                return keep_visited, 0

            if not visited[i][j] and graph[i][j] == 0:
                visited[i][j] = True
                q.append((i, j))
                # print('enqueue', initial, i, j)
            elif graph[i][j] == 1:
                # print('area', initial, i, j)
                area += 1
    return visited, area


def main():
    W, H = MI()
    graph = [None] * H
    visited = [[False for i in range(W)] for i in range(H)]

    for i in range(H):
        graph[i] = LI()

        for j in range(W):
            if graph[i][j] == 'S':
                pass

    ans = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                number_of_cells, conn = bfs(graph, (i, j), visited, H, W)
                ans += number_of_cells * 6 - conn
                # print(i, j, number_of_cells, conn)

    area = 0
    visited = [[False for i in range(W)] for i in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 0 and not visited[i][j]:
                visited, ret_area = bfs_pond(graph, (i, j), visited, H, W)
                area += ret_area
                # print(i, j, area)

    print(ans - area)


if __name__ == '__main__':
    main()
