import sys
import math
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    N, M = map(int, input().split())
    min_r = N
    max_l = 0

    for i in range(M):
        L, R = map(int, input().split())
        min_r = min(min_r, R)
        max_l = max(max_l, L)

    print(max(min_r - max_l + 1, 0))


if __name__ == '__main__':
    main()
