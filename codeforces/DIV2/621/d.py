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


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    n, m, k = MI()
    a = LI()
    graph = [[] for i in range(n+1)]
    visited = [False] * (n + 1)
    is_special = {}
    not_change = False

    for i in a:
        is_special[i] = True

    for i in range(m):
        x, y = map(int, input().split())
        if x in is_special and y in is_special:
            not_change = True
        graph[x].append(y)
        graph[y].append(x)

    dist = [-1] * (n + 1)
    dist = [-1] * (n + 1)
    q = deque()
    visited[1] = True
    dist[1] = 0
    visited_special = []

    if 1 in is_special:
        q.append((1, [1]))
    else:
        q.append((1, []))

    while len(q) != 0:
        edge, nodes = q.popleft()
        nxt = graph[edge]

        for i, e in enumerate(nxt):
            if visited[e] is False:
                _nodes = None
                if e in is_special:
                    _nodes = nodes + [e]
                else:
                    _nodes = nodes
                q.append((e, _nodes))
                dist[e] = dist[edge] + 1
                visited[e] = True
                if e == n:
                    visited_special = _nodes
                    q = deque()
                    break

    if not_change:
        print(dist[-1])
    else:
        distances = []
        # print(visited_special)
        a = visited_special
        if len(visited_special) >= 2:
            for i in range(len(a)-1):
                distances.append(abs(dist[a[i+1]] - dist[a[i]]))
            print(dist[-1] - max(min(distances) - 1, 0))
        else:
            print(dist[-1])


if __name__ == '__main__':
    main()
