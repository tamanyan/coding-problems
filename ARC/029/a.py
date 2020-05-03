
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


def main():
    N = I()
    data = [0] * N
    ans = IINF

    for i in range(N):
        data[i] = I()

    for i in range(2 ** N):
        a = []
        b = []
        # print("pattern {}: ".format(i), end="")
        for j in range(N):
            if ((i >> j) & 1):
                a.append(data[j])
            else:
                b.append(data[j])

        ans = min(ans, max(sum(a), sum(b)))

    print(ans)


if __name__ == '__main__':
    main()
