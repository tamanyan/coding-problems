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
    D, N = MI()
    T = [0] * D
    A = [0] * N
    B = [0] * N
    C = [0] * N
    dp = [-IINF] * (100 + 1)

    for i in range(D):
        T[i] = I()

    for i in range(N):
        A[i], B[i], C[i] = MI()


    for j in range(N):
        if T[0] >= A[j] and T[0] <= B[j]:
            dp[C[j]] = 0

    for i in range(1, D):
        dp_next = [-IINF] * (100 + 1)
        for c in range(100 + 1):
            for j in range(N):
                if T[i] >= A[j] and T[i] <= B[j]:
                    dp_next[C[j]] = max(dp_next[C[j]], dp[c] + abs(c - C[j]))
        dp = dp_next
        # print(*[a if a > -10**10 else '-IINF' for a in dp_next])

    print(max(dp))


if __name__ == '__main__':
    main()
