
import sys
import heapq
import math
import itertools

INF = float("inf")


def dis(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    N = int(input())
    x = [0] * N
    y = [0] * N

    for i in range(N):
        x[i], y[i] = map(int, input().split())

    ans = 0
    data = [i for i in range(0, N)]
    routes = list(itertools.permutations(data))
    for route in routes:
        # print(route)
        for i in range(0, len(route) - 1):
            # print(x[i], y[i], x[i+1], y[i+1])
            test = dis(x[route[i]], y[route[i]], x[route[i+1]], y[route[i+1]])
            # print(test)
            ans += test

    print(ans / len(routes))


if __name__ == '__main__':
    main()
