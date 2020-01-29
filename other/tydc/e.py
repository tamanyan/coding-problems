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
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


# ナップサック問題 大きい
def main():
    D = I()
    s = S()
    N = len(s)
    n = [int(s[i]) for i in range(N)]
    dp = [[[0 for smaller in range(2)]
                for j in range(D)]
                for i in range(N + 2)]
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(D):
            for smaller in range(2):
                lim = n[i] if smaller == 0 else 9
                for d in range(lim+1):
                    nj = (j + d) % D
                    ns = int(smaller or d < n[i])
                    dp[i+1][nj][ns] += dp[i][j][smaller]
                    dp[i+1][nj][ns] %= MOD
                    print(i, j, smaller, d)
                    for t in range(N+1):
                        print(dp[t])

    print(dp[N][0][1] + dp[N][0][0] - 1)


if __name__ == '__main__':
    main()
