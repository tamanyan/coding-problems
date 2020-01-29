from math import factorial
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


# show_flg = False
show_flg = True


def main():
    s = S()
    N = len(s)
    n = [int(s[i]) for i in range(N)]
    dp = [[[0 for j in range(10)]
                for smaller in range(2)]
                for i in range(N + 1)]
    dp[0][0][0] = 1

    for i in range(1, N):
        for smaller in range(2):
            for x in range(9 if smaller else n[i]):
                if x == 1:
                    dp[i+1][smaller or x < n[i]] += dp[i][smaller]
                else:
                    dp[i+1][smaller or x < n[i]] += dp[i][smaller]
                print(x, dp)

    print(dp[N][0] + dp[N][1])
    # print(C(2 * m + n - 1, 2*m) % MOD)


if __name__ == '__main__':
    main()
