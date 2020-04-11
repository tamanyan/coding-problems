from math import factorial
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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True


def main():
    N, K = MI()
    A = LI()
    LEN = 61
    ans = 0

    for d in range(LEN, -2, -1):
        if d != -1 and (K & (1 << d)) == False:
            continue

        tmp = 0
        for e in range(LEN, -1, -1):
            mask = 1 << e
            num = 0
            for j in range(N):
                if A[j] & mask > 0:
                    num += 1

            if e > d:
                if K & mask > 0:
                    tmp += mask * (N - num)
                else:
                    tmp += mask * num
            elif e == d:
                tmp += mask * num;
            else:
                tmp += mask * max(num, N - num)

        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
