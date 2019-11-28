
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


def MS(): return map(str, input().split())


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


# show_flg = False
show_flg = True


def main():
    N, L = MI()
    apples = [L + i - 1 for i in range(1, N+1)]
    apple_pie = sum(apples)
    apple_pie_n = []

    for i in range(N):
        tmp = 0
        for j in range(N):
            if j != i:
                tmp += apples[j]
        apple_pie_n.append((abs(apple_pie - tmp), i))

    apple_pie_n.sort()
    print(apple_pie - apples[apple_pie_n[0][1]])


if __name__ == '__main__':
    main()
