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


def main():
    # c = I()
    n, m = MI()
    # cnt = 0
    # s = S()
    # n = len(s)

    # for i in range(n):
    #     for j in range(n):
    #         # print(s[i:j+1])
    #         if '1' in s[i:j+1]:
    #             cnt += 1

    # print(cnt)
    # n = 1
    k = n // 2
    # a = (2 * k + 2) * (2 * k + 3) // 2
    print(a)
    # a = 2 + (n * (n - 1)) * 2
    # if a % 2 == 1:
    #     a -= n
    # print(a)
    if m <= n // 2:
        inc = m * (n - 2)
        print(inc)
    else:
        r = m - n // 2
        inc = (n // 2) * (n - 2) + r
        print(inc)

    # an = (4 + (2 * (n - 1) + 2)) * n - 4
    # print(an)

    # (n - 2)


if __name__ == '__main__':
    main()
