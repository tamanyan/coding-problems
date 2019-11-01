
import sys
import heapq
import math

INF = float("inf")


def main():
    N = int(input())
    ans = N

    for i in range(1, int(N ** 0.5)+1):
        if N % i == 0:
            j = N // i
            ans = min(i + j - 2, ans)

    print(ans)


if __name__ == '__main__':
    main()
