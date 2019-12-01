
from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time
from fractions import gcd
#import random


def I(): return int(input())


def MI(): return map(int, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['Yes', 'No']
MOD = 10**9+7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


# show_flg = True
show_flg = False

g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブルル


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


def cmbx(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main():
    N = int(input())
    A = list(MI())
    X = 0
    Y = 0
    Z = 0
    X = 1

    for i in range(1, N):
        if A[i] == X:
            X += 1
        elif A[i] == Y:
            Y += 1
        elif A[i] == Z:
            Z += 1

    print('Z,Y,Z', X, Y, Z)
    # X = 3
    # Y = 2
    # Z = 2

    for i in range(2, (X + Y + Z) * 2):
        g1.append((g1[-1] * i) % MOD)
        inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
        g2.append((g2[-1] * inverse[-1]) % MOD)

    print(cmb(X + Y + Z, X, MOD))
    print(cmb(Y + Z, Y, MOD))
    print((cmb(X + Y + Z, X, MOD) * cmb(Y + Z, Y, MOD)) % MOD)
    print((cmbx(X + Y + Z, X) * cmbx(Y + Z, Y)) % MOD)


if __name__ == '__main__':
    main()
