from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time
from fractions import gcd
#import random


def I(): return int(input())


def MI(): return map(int, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def show_arr(arr):
    if show_flg:
        print(*arr, sep='\n')


YN = ['Yes', 'No']
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


# show_flg = False
show_flg = True


def main():
    W = I()
    N, K = MI()
    A = [0] * N
    B = [0] * N
    dp = [[0 for i in range(K+1)]
            for i in range(W+1)]

    for i in range(N):
        A[i], B[i] = MI()

    for i in range(N):
        dp_tmp = [[0 for i in range(K+1)]
                   for i in range(W+1)]
        for w in range(W+1):
            for k in range(K+1):
                if w >= A[i] and k == 0:
                    dp_tmp[w][k] = max(dp[w - A[i]][k], dp[w][k])
                elif w >= A[i] and k <= K:
                    dp_tmp[w][k] = max(dp[w - A[i]][k-1] + B[i], dp[w][k])
                else:
                    dp_tmp[w][k] = dp[w][k]
        # show_arr(dp_tmp)
        # print("====")
        dp = dp_tmp
        # show_arr(dp)

    # show_arr(dp)
    print(dp[W][K])


if __name__ == '__main__':
    main()
