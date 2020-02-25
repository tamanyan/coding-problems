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


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def solve(T):
    n = I()
    a, b, c = MI()
    ans = 10**9
    ans_set = []

    for i in range(1, 10*4+1):
        _a = abs(i - a)
        _b = b % i
        if c % (b + _b) <= c % (b - _b):
            _c = c % (b + _b)
            ans_b = b + _b
        else:
            _c = c % (b - _b)
            ans_b = b - _b
        if ans < _a + _b + _c:
            ans = _a + _b + _c
            ans_set = [i, ans_b, c - _c]

        ans = min(ans, _a + _b + _c)
    print()


def main():
    T = I()

    for i in range(T):
        solve(T)


if __name__ == '__main__':
    main()
