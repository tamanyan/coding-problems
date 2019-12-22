from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
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


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    N = I()
    a = LI()
    ans = 0
    temp = []

    for i in range(N):
        if len(temp) == 0 and a[i] == 1:
            temp.append(1)
        elif len(temp) != 0 and a[i] == temp[-1] + 1:
            temp.append(a[i])
        else:
            ans += 1

    # print(temp)
    if len(temp) == 0:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
