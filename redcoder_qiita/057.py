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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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


def dijkstra(cost, start, goal):
    n = len(cost)
    dist = [IINF] * n
    visited = [False] * n
    dist[start] = 0

    while True:
        v = -1

        for i in range(n):
            if not visited[i] and v == -1:
                v = i
            elif not visited[i] and dist[i] < dist[v]:
                v = i

        if v == -1:
            break

        visited[v] = True

        for i in range(n):
            dist[i] = min(dist[i], dist[v] + cost[v][i])

    return dist


def main():
    N, K = MI()
    cost = [[IINF] * N for i in range(N)]
    ans = []

    for i in range(K):
        op = LI()
        if op[0] == 0:
            data = op[1:]
            s = data[0] - 1
            g = data[1] - 1
            ret = dijkstra(cost, s, g)
            # print(ret)
            if ret[g] == IINF:
                ans.append(-1)
            else:
                ans.append(ret[g])
        else:
            data = op[1:]
            i = data[0] - 1
            j = data[1] - 1
            cost[i][j] = min(data[2], cost[i][j])
            cost[j][i] = min(data[2], cost[j][i])

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
