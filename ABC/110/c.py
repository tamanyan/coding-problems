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
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def main():
    s = S()
    t = S()
    s_pos = {k: set() for k in l_alp}
    t_pos = {k: set() for k in l_alp}

    for i in range(len(s)):
        s_pos[s[i]].add(i)
        t_pos[t[i]].add(i)

    for c in l_alp:
        loc = s_pos[c]
        candidates = set()
        for i in loc:
            candidates.add(t[i])

        if len(candidates) > 1:
            print('No')
            return

    for c in l_alp:
        loc = t_pos[c]
        candidates = set()
        for i in loc:
            candidates.add(s[i])

        if len(candidates) > 1:
            # print(c, candidates)
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
