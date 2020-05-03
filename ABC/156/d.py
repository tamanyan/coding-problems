from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
import sys
import bisect
import string
import math
import time


def I(): return int(input())


def MI(): return map(int, input().split())


def S(): return input()


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def modinv(a):
    return pow(a, MOD-2, MOD)


def cmb(n, r):
    p = 1
    c = 1
    for i in range(r):
        p *= (n - i)
        c *= (i + 1)
        p = p % MOD
        c = c % MOD
    return p * modinv(c) % MOD


def main():
    n, a, b = MI()
    first = cmb(n, a)
    second = cmb(n, b)
    ans = pow(2, n, MOD) - 1
    print((ans - first - second) % MOD)


if __name__ == '__main__':
    main()
