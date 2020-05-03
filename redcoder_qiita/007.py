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


def S(): return input()


def MI(): return map(int, input().split())


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
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def modinv(a):
    return pow(a, MOD - 2, MOD)


def cmb(n, r):
    p = 1
    c = 1
    for i in range(r):
        p *= (n - i)
        c *= (i + 1)
        p = p % MOD
        c = c % MOD
    return p * modinv(c) % MOD


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    N = I()
    p = [None] * N

    for i in range(N):
        x, y = MI()
        p[i] = (x, y)

    s = set(p)
    ans = 0

    for i in range(N):
        x1, y1 = p[i]
        for j in range(i+1, N):
            x2, y2 = p[j]
            dx, dy = x2 - x1, y2 - y1
            ndx = - dy * math.sin(math.radians(90))
            ndy = dx * math.sin(math.radians(90))
            # print(x1, y1, x2, y2, ndx, ndy)
            if (x1 + ndx, y1 + ndy) in s and (x2 + ndx, y2 + ndy) in s:
                ans = max(ans, ndx ** 2 + ndy ** 2)

    print(int(ans))


if __name__ == '__main__':
    main()
