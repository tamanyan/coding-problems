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


def S(): return input()


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


YN = {False: 'No', True: 'Yes'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    t = I()
    lamps_case = [None] * t

    for i in range(t):
        lamps_case[i] = LI()

    for i in range(t):
        lamps = lamps_case[i]
        m = max(lamps)
        # print(lamps, m)
        for i in range(3):
            lamps[i] = lamps[i] - m
        # print(lamps)
        lamps = [i for i in lamps if i != 0]
        if len(lamps) == 2:
            # print(lamps[0], lamps[1])
            if abs(lamps[0] - lamps[1]) <= 1:
                print('Yes')
            else:
                print('No')
        elif len(lamps) < 2:
            print('Yes')


if __name__ == '__main__':
    main()