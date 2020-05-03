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


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    S = input()
    N = len(S)
    r_counter = 0
    l_counter = 0
    ans = [0] * N

    for i in range(N):
        if S[i] == 'R':
            r_counter += 1
        else:
            if r_counter % 2 == 1:
                ans[i-1] += r_counter // 2 + 1
                ans[i] += r_counter // 2
            else:
                ans[i-1] += r_counter // 2
                ans[i] += r_counter // 2
            r_counter = 0

    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            l_counter += 1
        else:
            if l_counter % 2 == 1:
                ans[i+1] += l_counter // 2 + 1
                ans[i] += l_counter // 2
            else:
                ans[i+1] += l_counter // 2
                ans[i] += l_counter // 2
            l_counter = 0

    print(*ans)


if __name__ == '__main__':
    main()
