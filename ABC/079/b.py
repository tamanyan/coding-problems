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


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat)


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    N = I()
    a = LI()
    S = sum(a)

    ans = S % N
    person = S // N

    if ans != 0:
        print(-1)
        return

    s = 0
    # prev_idx = 0
    idx = 0
    ans = []
    for i in range(N):
        s += a[i]
        idx += 1
        if s == idx * person:
            s = 0
            # prev_idx = idx
            # print(idx)
            ans.append(idx - 1)
            idx = 0

    print(sum(ans))


if __name__ == '__main__':
    main()
