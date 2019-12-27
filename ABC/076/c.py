
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
    T = input()
    canditates = []

    for i in range(len(S)):
        idx = 0
        for j in range(i, len(S)):
            if idx < len(T) and (S[j] == T[idx] or S[j] == '?'):
                idx += 1
            else:
                break

        # print(idx, S, len(T))
        if idx == len(T):
            canditates.append(S[:i] + T + S[i+len(T):])
            # print(S[:i], T, S[i+len(T):])
            # print(i, i+len(T))

    if len(canditates) > 0:
        # print(canditates)
        canditates = [c.replace("?", "a") for c in canditates]
        canditates.sort()
        print(canditates[0])
    else:
        print("UNRESTORABLE")


if __name__ == '__main__':
    main()
