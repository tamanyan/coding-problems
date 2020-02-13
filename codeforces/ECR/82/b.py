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
    n, g, b = MI()
    atleast = (n + 1) // 2

    low = 0
    high = 10**19
    ans = 0

    while high - low > 1:
        mid = (low + high) // 2
        terms = mid // (g + b)
        remain = mid % (g + b)
        count = g * terms + min(remain, g)
        print(mid, terms, remain, count, atleast)
        if count <= atleast:
            low = mid + 1
        else:
            high = mid - 1
            ans = mid

    print(low, high, ans)
    print(max(n, ans))


def main():
    T = I()

    for i in range(T):
        solve(T)


if __name__ == '__main__':
    main()
