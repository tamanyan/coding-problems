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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def modinv(a):
    return pow(a, MOD-2, MOD)


def main():
    n, k = MI()
    ans = 1
    a = 1
    b = 1

    for i in range(n+(n-1)):
        ans *= (i + 1)
        ans %= MOD

    for i in range(n):
        a *= (i + 1)
        a %= MOD

    for i in range(n-1):
        b *= (i + 1)
        b %= MOD

    # print(ans, a, b)
    print(ans * modinv((a * b % MOD)) % MOD)


if __name__ == '__main__':
    main()
