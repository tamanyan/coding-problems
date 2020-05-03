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


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    N, M = MI()
    dic = {k: {k} for k in range(1, N+1)}

    for i in range(M):
        x, y = MI()
        dic[x].add(y)
        dic[y].add(x)

    ans = 0
    for i in range(2 ** N):
        groups = set()
        for j in range(N):
            if ((i >> j) & 1):
                groups.add(j+1)

        if all([groups.issubset(dic[i]) for i in groups]):
            ans = max(ans, len(groups))

    print(ans)


if __name__ == '__main__':
    main()
