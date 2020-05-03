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


def S(): return input()


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
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True

import random

def solve(T):
    N = I()
    s = S()
    # s = [random.choice(['R', 'L', 'U', 'D']) for i in range(2 * 10**5)]
    # N = len(s)

    test3 = {'[0, 0]': [0]}
    pos = [0, 0]
    can = []
    for i in range(N):
        if s[i] == 'U':
            pos[1] += 1
        elif s[i] == 'D':
            pos[1] -= 1
        elif s[i] == 'R':
            pos[0] += 1
        elif s[i] == 'L':
            pos[0] -= 1

        str_pos = str(pos)
        if str_pos not in test3:
            test3[str_pos] = [i+1]
        else:
            can.append((i - test3[str_pos][-1], test3[str_pos][-1]))
            test3[str_pos] = []
            test3[str_pos].append(i+1)

    can = sorted(can)

    # print(loc1, loc2)
    if len(can) > 0:
        print(can[0][1] + 1, can[0][1] + 1 + can[0][0])
    else:
        print(-1)


def main():
    T = I()

    for i in range(T):
        solve(T)


if __name__ == '__main__':
    main()
