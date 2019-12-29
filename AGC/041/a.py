
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
    N, A, B = MI()
    diff = abs(A - B)

    if diff % 2 == 0:
        print(diff // 2)
    else:
        ans = 0
        minp = min(A, B)
        maxp = max(A, B)
        # print(N - maxp + 1, maxp, minp)
        if N - maxp + 1 > minp:
            ans += minp - 1
            B -= minp - 1
            B -= 1
            ans += 1
            A = 1
            # print(ans, A, B)
            if B == 1:
                print(ans)
            else:
                ans += abs(B - A) // 2
                print(ans)
        else:
            ans += N - maxp
            A += N - maxp
            A += 1
            ans += 1
            B = N
            # print(ans, A, B)
            if A == N:
                print(ans)
            else:
                ans += abs(B - A) // 2
                print(ans)
        # # print(minp, maxp, N - maxp)
        # else:
        #     print(max(A, B) - 1)


if __name__ == '__main__':
    main()
