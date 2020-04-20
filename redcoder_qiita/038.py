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


def make4(initial, L, M, N, O):
    return [[[[initial for i in range(O)]
                for n in range(N)]
                for m in range(M)]
                for l in range(L)]


def make3(initial, L, M, N):
    return [[[initial for n in range(N)]
                for m in range(M)]
                for l in range(L)]


def debug(table, *args):
    ret = []
    for name, val in table.items():
        if val in args:
            ret.append('{}: {}'.format(name, val))
    print(' | '.join(ret), file=sys.stderr)


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


# LCS
def main():
    N = I()
    X = []
    Y = []

    for i in range(N):
        x = S()
        y = S()
        if len(x) > len(y):
            X.append(x)
            Y.append(y)
        else:
            X.append(y)
            Y.append(x)

    for i in range(N):
        x = X[i]
        y = Y[i]
        dp = [[0] * (len(y) + 1) for i in range(len(x) + 1)]
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            # print(dp[i])
        print(dp[-1][-1])


if __name__ == '__main__':
    main()
