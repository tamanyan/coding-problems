from collections import deque

# BFS

def main():
    # BLACK = 1
    WHITE = 0
    EDGE = 0
    WEIGHT = 1
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
    while len(q) != 0:
        parentIdx = q.popleft()
        parent = graph[parentIdx]
        # print(u+1, [i + 1 for i in q])
        for v, e in enumerate(parent):
            if not visited[e[EDGE]]:
                q.append(e[EDGE])
                visited[e[EDGE]] = True
                if e[WEIGHT] % 2 == 0:
                    colors[e[EDGE]] = colors[parentIdx]
                else:
                    colors[e[EDGE]] = 1 - colors[parentIdx]
                # print(colors)

    for i in range(1, len(colors)):
        print(colors[i])


if __name__ == '__main__':
    main()
