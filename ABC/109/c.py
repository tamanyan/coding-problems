
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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_n(a, n):
    ans = a[0]
    for i in range(1, n):
        ans = gcd(ans, a[i])
    return ans


def main():
    N, X = MI()
    x = LI()
    x.append(X)
    x.sort()
    d = []

    for i in range(1, N+1):
        d.append(x[i] - x[i-1])

    print(gcd_n(d, len(d)))


if __name__ == '__main__':
    main()
