
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


show_flg = False
# show_flg = True


def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main():
    N = MI()
    a = LI()
    a = sorted(a, reverse=True)
    mx = a[0]

    if mx % 2 == 0:
        target = mx // 2
        mn = 10**9
        ans = -1
        for i in range(1, len(a)):
            if mn > abs(target - a[i]):
                ans = a[i]
                mn = abs(target - a[i])
        print(a[0], ans)
    else:
        target1 = mx // 2
        target2 = mx // 2 + 1
        mn = 10**9
        ans = -1
        for i in range(1, len(a)):
            if mn > abs(target1 - a[i]):
                ans = a[i]
                mn = abs(target1 - a[i])
            if mn > abs(target2 - a[i]):
                ans = a[i]
                mn = abs(target2 - a[i])
        print(a[0], ans)


if __name__ == '__main__':
    main()
