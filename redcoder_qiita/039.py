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


# def rec(v, i, A, s):
#     ret = 0
#     if v < 0 or v > 20:
#         return 0

#     if i >= len(A) - 1:
#         if v == A[i]:
#             print(s)

#         return v == A[i] if 1 else 0

#     ret += rec(v + A[i], i + 1, A, s+'+'+str(A[i]))
#     ret += rec(v - A[i], i + 1, A, s+'-'+str(A[i]))
#     return ret


def main():
    N = I()
    A = LI()
    MAX = 20
    dp = [[0] * (MAX+1) for i in range(N-1)]
    dp[0][A[0]] = 1

    for i in range(1, N-1):
        for j in range(MAX+1):
            # dp[i+1][j] = dp[i][j]
            if j + A[i] <= MAX:
                dp[i][j+A[i]] += dp[i-1][j]
            if j - A[i] >= 0:
                dp[i][j-A[i]] += dp[i-1][j]
    print(dp[-1][A[N-1]])
    # print(rec(A[0], 1, A, str(A[0])))


if __name__ == '__main__':
    main()
