import math
import os
import sys
from collections import deque
# from fractions import gcd
input = sys.stdin.readline

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    graph = [[] for i in range(N+1)]
    colors = [-1] * (N + 1)
    init = -1
    display_order = []

    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        display_order.append(v-1)

    q = deque()
    q.append((1, 0))
    visited = [False] * (N + 1)
    visited[1] = True

    while len(q) != 0:
        idx, color = q.popleft()
        nxt = graph[idx]
        cnt = 1
        # print('visiting', nxt)
        for e in nxt:
            if colors[e] == -1 and not visited[e]:
                if cnt == color:
                    cnt += 1
                    colors[e] = cnt
                    q.append((e, cnt))
                    visited[e] = True
                    cnt += 1
                else:
                    colors[e] = cnt
                    q.append((e, cnt))
                    visited[e] = True
                    cnt += 1

    print(max(colors))
    # print(*colors)
    # print(*display_order)
    for i in display_order:
        # print(i)
        print(colors[i+1])
    # for i in range(2, len(colors)):
    #     print(colors[i])


if __name__ == '__main__':
    main()
