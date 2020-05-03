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


def f(H, S, x):
    N = len(H)
    t = []

    for i in range(N):
        t.append((x - H[i]) / S[i])

    t.sort()
    # print(t, x, H, S, all(i <= t[i] for i in range(N)))
    # print(t, x)

    for i in range(N):
        if i > t[i]:
            return False

    return True


# 二分探索 ok ng
def main():
    N = I()
    H = []
    S = []
    MAX = 10**19
    # print(A)
    # print(C)

    for i in range(N):
        h, s = MI()
        H.append(h)
        S.append(s)
        MAX = max(MAX, H[i] + S[i] * (N - 1))

    s = 0
    t = MAX
    ok = t
    ng = s

    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if f(H, S, mid):
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == '__main__':
    main()
