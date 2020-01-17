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
    N, M = MI()
    ans = 0
    cur = -1.0
    cnt = 1
    correct = 0.5 ** M
    wrong = 1 - correct

    while cnt <= 10**4:
        cur = 0
        if cnt == 1:
            cur = (1900 * M + 100 * (N - M)) * correct
            # print(cur, cnt, (cnt * 1900 * M + cnt * 100 * (N - M)))
        # elif cnt == 2:
        #     cur = (cnt * 1900 * M + cnt * 100 * (N - M)) * \
        #         correct * (wrong ** (cnt - 1))
        #     print(cur, cnt, (cnt * 1900 * M + cnt * 100 * (N - M)))
        else:
            cur = (cnt * 1900 * M + cnt * 100 * (N - M)) * \
                correct * (wrong ** (cnt - 1))
            # cur = (cnt * 1900 * M + cnt * 100 * (N - M)) * \
            #     correct * (wrong ** (cnt - 1) ** M)
        ans += cur
        cnt += 1

    print(int(ans + 0.0001))


if __name__ == '__main__':
    main()
