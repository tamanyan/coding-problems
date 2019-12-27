
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
    N, M = MI()
    ab = [None] * M

    for i in range(M):
        a, b = MI()
        ab[i] = (a, b)

    ab = sorted(ab, key=lambda x: x[1])
    print(ab)
    bridge = [(ab[0][1]-1, ab[0][1])]

    for i in range(1, len(ab)):
        # print(ab[i], bridge[-1])
        if ab[i][0] <= bridge[-1][0] and ab[i][1] >= bridge[-1][1]:
            pass
        else:
            bridge.append((ab[i][1]-1, ab[i][1]))

    print(len(bridge))


if __name__ == '__main__':
    main()
