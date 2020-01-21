
import sys
import heapq
import math

INF = float("inf")


def main():
    N = int(input())
    ans = N

    for i in range(1, 10**6+1):
        if N % i == 0:
            ans = min(ans, (i - 1) + (N // i - 1))

    print(ans)


if __name__ == '__main__':
    main()
