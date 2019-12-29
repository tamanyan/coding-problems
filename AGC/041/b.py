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


YN = ['Yes', 'No']
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True


def check(x, N, M, V, P, A):
    if (N - x) <= P:
        return True

    if V <= x + P:
        return (A[x] + M) >= A[N-P]

    x_score = A[x] + M
    total_v = (V - x - P) * M
    show('x =', x, 'A[x] =', A[x], 'x_score =', x_score, 'total_v =', total_v)

    if A[N-P] > x_score:
        return False

    for i in range(x+1, N-P+1):
        show('i = ', i, 'A[i] =', A[i], 'total_v =', total_v,
             '(x_score - A[i]) =', (x_score - A[i]))
        total_v -= min(M, (x_score - A[i]))

    show('total_v =', total_v)
    if total_v <= 0:
        return True
    else:
        return False


def main():
    N, M, V, P = MI()
    A = LI()
    A.sort()

    if(check(0, N, M, V, P, A)):
        print(N)
        return

    r = N - 1
    l = 0
    while r-l > 1:
        mid = (l+r) // 2
        # print('brefore l =', l, 'mid =', mid, 'r =', r, 'A[mid] =', A[mid])
        if check(mid, N, M, V, P, A):
            r = mid
        else:
            l = mid
        # print('after l =', l, 'mid =', mid, 'r =', r, 'A[mid] =', A[mid])
    print(N - r)



if __name__ == '__main__':
    main()
