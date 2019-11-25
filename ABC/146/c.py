import math
import os
import sys
# from fractions import gcd
input = sys.stdin.readline

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    A, B, X = map(int, input().split())
    l = 0
    r = 10**9 + 1

    def f(N):
        return A * N + B * len(str(N))

    while r-l > 1:
        c = (l+r) // 2
        if f(c) <= X:
            l = c
        else:
            r = c
        print(l, r, c)

    print(l)

    # N = (X - B * d) / A
    # MAX = 18
    # digit = 0

    # for d in range(MAX+1):
    #     p = A * 10 ** d + B * d
    #     # print(d, p - X)
    #     if p - X > 0:
    #         digit = d
    #         break

    # # print(digit)
    # ans = (X - B * digit) // A
    # print(min(ans, 10**9))


if __name__ == '__main__':
    main()
