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


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


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


# 範囲を考慮に入れる
def main():
    N, D, K = MI()
    L = []
    R = []
    S = []
    T = []

    for i in range(D):
        l, r = MI()
        L.append(l)
        R.append(r)

    for i in range(K):
        s, t = MI()
        S.append(s)
        T.append(t)

    ans = []

    for i in range(K):
        lower = S[i]
        upper = S[i]
        for j in range(D):
            if R[j] >= lower and L[j] <= lower or R[j] >= upper and L[j] <= upper:
                lower = min(L[j], lower)
                upper = max(R[j], upper)

            if lower <= T[i] and upper >= T[i]:
                ans.append(j + 1)
                break

    for i in ans:
        print(i)



if __name__ == '__main__':
    main()
