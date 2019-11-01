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
    a, b, x = list(map(int, input().split()))

    h = x / float(a ** 2)
    remain = b - h
    ans = math.degrees(math.atan2(remain, a/2))
    limit = math.degrees(math.atan2(h, a/2))
    # limit = x / float(a ** 2)
    # # limit_degree = math.degrees(math.atan2(limit, a))
    # print(limit + h < b)
    # print(limit)

    if ans <= limit:
        print(ans)
    else:
        # x = b * a * t / 2
        t = 2 * x / (b * a)
        deg = math.degrees(math.atan2(b, t))
        print(deg)


if __name__ == '__main__':
    main()
