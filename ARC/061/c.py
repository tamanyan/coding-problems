
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
    S = input()
    N = len(S) - 1

    total = 0
    for i in range(2 ** N):
        splits = []
        # print("pattern {}: ".format(i), end="")
        for j in range(N):
            if ((i >> j) & 1):
                splits.append(j)
        splits.append(len(S))

        for j in range(len(splits)):
            n = splits[j]
            if j == 0:
                total += int(S[:n+1])
                # print(S[:n+1])
            else:
                prev = splits[j-1]
                # print(prev, n, S[prev+1:n+1])
                total += int(S[prev+1:n+1])

    print(total)


if __name__ == '__main__':
    main()
