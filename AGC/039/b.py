
# import sys
# input = sys.stdin.readline
# from collections import Counter
# import string
from collections import deque

INF = float('inf')

# BFS

def main():
    N = int(input())
    # N = map(int, input().split())
    graph = [[] for i in range(N)]
    # ans = [0] * (N+1)
    # visit = [False]*(N+1)

    def get_distances(s):
        q = deque()
        q.append(s)
        d = [INF] * N
        d[s] = 0
        while len(q):
            u = q.popleft()
            for v, e in enumerate(graph[u]):
                if e:
                    if d[v] > d[u] + 1:
                        d[v] = d[u] + 1
                        q.append(v)
        return d

    def get_diameter():
        dmax = 0
        for i in range(N):
            d = get_distances(i)
            print(i, d)
            dmax = max(max(d), dmax)
        return dmax

    for i in range(N):
        edges = input()
        for s in range(len(edges)):
            e = int(edges[s])
            graph[i].append(e)

    q = deque()
    q.append(0)
    color = [0] * N
    vaild = True
    color[0] = 1
    while vaild and len(q) != 0:
        u = q.popleft()
        # print(u+1, [i + 1 for i in q])
        for v, e in enumerate(graph[u]):
            # print(v, e)
            if e == 1:
                # print(v)
                if not color[v]:
                    color[v] = -color[u]
                    q.append(v)
                    # print(v+1, color)
                elif color[v] == color[u]:
                    vaild = False
                    # print('invalid')
                    break
    if vaild:
        print(get_diameter() + 1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
