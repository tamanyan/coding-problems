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
    W = LI()
    total = sum(W)

    if total % 2 == 1:
        print('impossible')
        return

    half = total // 2
    dp = [0] * (half+1)
    dp[0] = 1

    for i in range(N):
        dp_next = [0] * (half+1)
        for j in range(half+1):
            if dp[j] == 1:
                dp_next[j] = 1
                if j + W[i] <= half:
                    dp_next[j+W[i]] = 1
        print(i, dp_next)
        dp = dp_next

    if dp[half] == 0:
        print('impossible')
    else:
        print('possible')


if __name__ == '__main__':
    main()
