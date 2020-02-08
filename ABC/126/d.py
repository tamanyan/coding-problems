from collections import deque

# BFS

def main():
    # BLACK = 1
    WHITE = 0
    # EDGE = 0
    # WEIGHT = 1
    N = int(input())
    graph = [[] for i in range(N+1)]
    colors = [-1] * (N + 1)

    for i in range(N-1):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    q = deque()
    q.append(1)
    colors[1] = WHITE
    visited = [False] * (N + 1)
    visited[1] = True

    while len(q) != 0:
        n = q.popleft()

        for v, w in graph[n]:
            if visited[v]:
                continue

            if w % 2 == 0:
                colors[v] = colors[n]
            else:
                colors[v] = 1 - colors[n]

            visited[v] = True
            q.append(v)

    for i in colors[1:]:
        print(i)


if __name__ == '__main__':
    main()
