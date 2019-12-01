
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
    N, K = MI()
    A = LI()
    print((N+K-3)//(K-1))
    # a = min(A)
    # count = []

    # tmp = 0
    # for i in range(len(A)):
    #     if A[i] != a:
    #         tmp += 1
    #     else:
    #         count.append(tmp)
    #         tmp = 0

    # if tmp != 0:
    #     count.append(tmp)

    # print(count)

    # ans = 0
    # for c in count:
    #     # print(c, (K-1), math.ceil(float(c) / (K-1)))
    #     ans += math.ceil(float(c) / (K-1))
    # print(ans)


if __name__ == '__main__':
    main()
