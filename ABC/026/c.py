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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat)


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

show_flg = False
# show_flg = True


def main():
    N = I()
    dp = [0] * N
    max_dp = [0] * N
    min_dp = [10**9] * N
    B = [0] * N

    for i in range(1, N):
        B[i] = I() - 1

    for i in range(N-1, -1, -1):
        if max_dp[i] == 0:
            dp[i] = 1
        else:
            dp[i] = max_dp[i] + min_dp[i] + 1
        max_dp[B[i]] = max(max_dp[B[i]], dp[i])
        min_dp[B[i]] = min(min_dp[B[i]], dp[i])

    print(dp[0])


if __name__ == '__main__':
    main()
