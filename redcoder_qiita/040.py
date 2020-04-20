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


def rec(day, cur, prev, D, N, S):
    if day >= N:
        print(S)
        return 1

    ret = 0
    if day in D:
        nxt = D[day]
        if not (nxt == prev and nxt == cur):
            ret += rec(day + 1, nxt, cur, D, N, S + '-' + str(nxt+1))
    else:
        for nxt in range(3):
            if nxt == prev and nxt == cur:
                continue
            ret += rec(day + 1, nxt, cur, D, N, S + '-' + str(nxt+1))

    return ret


def main():
    MOD = 10000
    N, K = MI()
    D = {}
    # Days, Number, Repeat
    dp = make3(0, N, 3, 3)

    for i in range(K):
        a, b = MI()
        D[a-1] = b-1

    if 0 in D:
        dp[0][D[0]][1] = 1
        # dp[0][(D[0]+1)%3][0] = 1
        # dp[0][(D[0]+2)%3][0] = 1
    else:
        dp[0][0][1] = 1
        dp[0][1][1] = 1
        dp[0][2][1] = 1

    # for n in dp[0]:
    #    print(n)

    for i in range(1, N):
        if i in D:
            for j in [(D[i]+1)%3, (D[i]+2)%3]:
                for k in range(1, 3):
                    dp[i][D[i]][1] += dp[i-1][j][k]
                    dp[i][D[i]][1] %= MOD
            dp[i][D[i]][2] += dp[i-1][D[i]][1]
            dp[i][D[i]][2] %= MOD
        else:
            for j in range(3):
                for k in range(3):
                    if k + 1 < 3:
                        dp[i][j][k+1] += dp[i-1][j][k]
                        dp[i][j][k+1] %= MOD
                    dp[i][(j+1)%3][1] += dp[i-1][j][k]
                    dp[i][(j+1)%3][1] %= MOD
                    dp[i][(j+2)%3][1] += dp[i-1][j][k]
                    dp[i][(j+2)%3][1] %= MOD
        # for n in dp[i]:
        #     print(n)
        # print()

    ans = sum([sum(d) for d in dp[-1]])
    print(ans % MOD)
    # print(rec(0, -1, -1, D, N, 'S'))

if __name__ == '__main__':
    main()
