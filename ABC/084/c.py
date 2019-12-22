
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


# show_flg = False
show_flg = True


def main():
    N = I()
    C = [0] * (N-1)
    S = [0] * (N-1)
    F = [0] * (N-1)

    for i in range(N-1):
        C[i], S[i], F[i] = MI()

    for i in range(0, N-1):
        ans = S[i]
        # show(ans)
        for j in range(i, N-1):
            ans = max(ans, S[j])
            diff = S[j] - ans
            ans += diff % F[j]
            ans += C[j]
            # show(j, ans)
        print(ans)
    print(0)


if __name__ == '__main__':
    main()
