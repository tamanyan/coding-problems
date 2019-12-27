
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
    S = input()
    center = len(S) // 2

    if len(S) % 2 == 0:
        c = 1
        while True:
            if (center - 1 + c) < len(S) and S[center - c] == S[center - 1 + c] and S[center - c] == S[center]:
                c += 1
            else:
                break
        print(c + center - 1)
    else:
        c = 0
        while True:
            if (center + c) < len(S) and S[center - c] == S[center + c] and S[center] == S[center - c]:
                c += 1
            else:
                break
        print(c + center)


if __name__ == '__main__':
    main()
