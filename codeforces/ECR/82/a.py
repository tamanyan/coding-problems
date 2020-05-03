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
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def solve(T):
    s = S()
    ans = 0
    trail_zero = 0
    first = None

    if len(s) == 1:
        print(0)
        return

    for i in range(len(s)):
        if first is None and s[i] == '1':
            first = i
        elif first is not None and s[i] == '0':
            ans += 1

    for i in range(len(s)-1, -1, -1):
        if s[i] == '0':
            trail_zero += 1
        elif s[i] == '1':
            break

    if ans != 0:
        print(ans - trail_zero)
    else:
        print(0)


def main():
    T = I()

    for i in range(T):
        solve(T)


if __name__ == '__main__':
    main()
