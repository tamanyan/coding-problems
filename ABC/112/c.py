
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
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True


def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    h = [0] * N

    for i in range(N):
        x[i], y[i], h[i] = MI()

    for cx in range(101):
        for cy in range(101):
            H = set()
            ZH = set()
            for i in range(N):
                if h[i] == 0:
                    ZH.add(abs(x[i] - cx) + abs(y[i] - cy))
                else:
                    H.add(h[i] + abs(x[i] - cx) + abs(y[i] - cy))

            if len(H) == 1 and len(ZH) == 0:
                print(cx, cy, H.pop())
                return
            elif len(H) == 1 and len(ZH) > 0:
                ans = H.pop()
                if ans > min(ZH):
                    continue
                print(cx, cy, ans)
                return
            elif len(H) == 0 and len(ZH) > 0:
                a = ZH.pop()
                for i in list(ZH):
                    a = min(a, ZH.pop())
                print(cx, cy, a)
                return


if __name__ == '__main__':
    main()
