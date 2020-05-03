from math import factorial
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


def MI(): return map(int, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True

p = None
XY = None
N = None


def main():
    N = I()
    P = LI()
    Q = LI()
    # start = 0
    # finish = 0
    data = sorted(list(itertools.permutations(P, N)))

    for index, arr in enumerate(data):
        tmpS = 0
        tmpE = 0
        for i in range(N):
            if P[i] == arr[i]:
                tmpS += 1
            if Q[i] == arr[i]:
                tmpE += 1

        if tmpS == N:
            start = index

        if tmpE == N:
            finish = index

    print(abs(finish - start))


if __name__ == '__main__':
    main()
