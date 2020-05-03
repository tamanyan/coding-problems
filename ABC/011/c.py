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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def main():
    N = I()
    NG = set()
    NG.add(I())
    NG.add(I())
    NG.add(I())
    dp = [0] * (N+1)
    dp[N] = 1

    if N in NG:
        print('NO')
        return

    for i in range(100):
        dp_next = [0] * (N+1)
        for j in range(N, -1, -1):
            if dp[j] == 1:
                dp_next[j] = dp[j]

            for k in range(1, 4):
                if dp[j] == 1:
                    if j - k not in NG and j - k >= 0:
                        dp_next[j-k] = dp[j]
                # print(i, j, dp_next, dp[j])
        dp = dp_next
        # print(i, dp_next)

    print(YNU[dp[0]])


if __name__ == '__main__':
    main()
