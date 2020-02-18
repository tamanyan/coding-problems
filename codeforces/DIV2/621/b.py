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

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def solve(T):
    n, x = MI()
    a = LI()
    ans = 10**19

    for i in range(n):
        if x % a[i] == 0:
            ans = min(ans, x // a[i])
        else:
            if x < a[i]:
                ans = min(ans, 2)
            else:
                n = x // a[i]
                n -= 1
                ans = min(ans, n + 2)

    print(ans)
    # print(distance(0, 0, 2, math.sqrt(5)))


def main():
    T = I()

    for i in range(T):
        solve(T)


if __name__ == '__main__':
    main()
