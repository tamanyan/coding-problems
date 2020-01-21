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
    area = x / a
    h = area / a
    remain = b - h

    if h >= b / 2:
        print(math.degrees(math.atan2(remain, a / 2)))
    else:
        a_dash = (2 * area) / b
        print(math.degrees(math.atan2(b, a_dash)))


if __name__ == '__main__':
    main()
