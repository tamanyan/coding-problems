
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


def lcm(a, b):
    return a * b // gcd(a, b)


def coprime(a, b):
    return gcd(a, b) == 1


def main():
    N, M = MI()
    S = input()
    T = input()

    LMC = lcm(N, M)

    if S[0] != T[0]:
        print(-1)
    else:
        a = LMC / N
        b = LMC / M
        abl = lcm(a, b)
        cur = 1
        while True:
            i = int(cur * abl * N // LMC)
            j = int(cur * abl * M // LMC)

            # print(i, j)

            if i >= N or j >= M:
                break

            if S[i] != T[j]:
                print(-1)
                return
            cur += 1

        print(LMC)


if __name__ == '__main__':
    main()
