
import sys
from collections import deque

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    BLACK = '#'
    WHITE = '.'
    H, W = map(int, input().split())
    graph = [None] * H
    # w_score = [[0 for i in range(W)] for i in range(H)]
    # h_score = [[0 for i in range(W)] for i in range(H)]
    options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = [[False for i in range(W)] for i in range(H)]
    initial = []

    for i in range(H):
        graph[i] = list(input())

        for j in range(W):
            if graph[i][j] == BLACK:
                initial.append((i, j))
                visited[i][j] = True

    # print(visited)
    # print(graph)

    q = deque()
    q.append(initial)
    ans = 0
    while len(q) != 0:
        n = q.popleft()
        # print(ans, n)

        items = set()
        for p in n:
            for d in options:
                i = p[0] + d[0]
                j = p[1] + d[1]

                if i >= 0 and i < H and j >= 0 and j < W and not visited[i][j] and graph[i][j] == WHITE:
                    visited[i][j] = True
                    graph[i][j] = BLACK
                    items.add((i, j))
                # else:
                #     print(i, j)

        if len(items) > 0:
            ans += 1
            q.append(items)

    print(ans)


if __name__ == '__main__':
    main()
