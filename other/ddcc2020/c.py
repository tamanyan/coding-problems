from collections import deque

INF = float("inf")
IINF = 10 ** 18
MOD = 998244353


def main():
    BLACK = '#'
    WHITE = '.'
    H, W, K = map(int, input().split())
    graph = [None] * H
    # w_score = [[0 for i in range(W)] for i in range(H)]
    # h_score = [[0 for i in range(W)] for i in range(H)]
    options = [(0, -1), (0, 1)]
    visited = [[False for i in range(W)] for i in range(H)]
    ans = [[0 for i in range(W)] for i in range(H)]
    idx = 1

    for i in range(H):
        graph[i] = list(input())

    for i in range(H):
        for j in range(W):
            if graph[i][j] == BLACK:
                visited[i][j] = True
                ans[i][j] = idx

                q = deque()
                q.append((i, j))
                while len(q) != 0:
                    p = q.popleft()

                    for d in options:
                        ni = p[0] + d[0]
                        nj = p[1] + d[1]

                        if ni >= 0 and ni < H and nj >= 0 and nj < W and not visited[ni][nj] and graph[ni][nj] == WHITE:
                            visited[ni][nj] = True
                            ans[ni][nj] = idx
                            q.append((ni, nj))
                idx += 1

    for i in range(H):
        for j in range(W):
            if i == 0 and ans[i][j] == 0:
                n = 1
                while ans[i+n][j] == 0:
                    n += 1
                ans[i][j] = ans[i+n][j]
            elif ans[i][j] == 0:
                ans[i][j] = ans[i-1][j]

    for i in range(len(ans)):
        print(*ans[i])


if __name__ == '__main__':
    main()
