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


def main():
    t = I()
    for i in range(t):
        n, m = MI()
        # m: number of one
        # n: number of string
        # z: number of zero
        z = n - m
        g = m + 1
        total = (n * (n + 1)) // 2
        if z >= g:
            k = (z + (g - 1)) // g
            r = z % g
            zero_total = 0
            if r != 0:
                zero_total = ((k * (k + 1)) // 2) * r
                zero_total += ((k * (k - 1)) // 2) * (g - r)
            else:
                zero_total = ((k * (k + 1)) // 2) * g
            # print(total, zero_total, r)
            print(total - zero_total)
        else:
            k = 1
            g = z
            zero_total = ((k * (k + 1)) // 2) * g
            print(total - zero_total)


if __name__ == '__main__':
    main()
