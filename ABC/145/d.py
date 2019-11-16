import math
import os
import sys
# from fractions import gcd
input = sys.stdin.readline

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


def main():
    X, Y = list(map(int, input().split()))

    if (X + Y) % 3 != 0:
        print(0)
        return

    n = int((2 * Y - X) / 3)
    m = int(Y - 2 * n)
    # print(n, m)
    # print(cmb(n+m, min(n, m)))

    for i in range(2, m + n + 1):
        g1.append((g1[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
        g2.append((g2[-1] * inverse[-1]) % MOD)

    print(cmb(m+n, min(n, m), MOD))


if __name__ == '__main__':
    main()
