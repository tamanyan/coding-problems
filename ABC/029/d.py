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
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True


def main():
    s = S()
    N = len(s)
    SIZE = N+2
    n = [int(s[i]) for i in range(N)]
    dp = [[0 for j in range(SIZE)]
                for smaller in range(2)]
    dp[0][0] = 1

    for i in range(N):
        dp_next = [[0 for j in range(SIZE)]
                    for smaller in range(2)]
        for smaller in range(2):
            for one in range(SIZE-1):
                for x in range(10 if smaller else n[i] + 1):
                    if x == 1:
                        dp_next[smaller or x < n[i]][one+1] += dp[smaller][one]
                    else:
                        dp_next[smaller or x < n[i]][one] += dp[smaller][one]
        dp = dp_next

    ans = 0
    for i in range(1, SIZE):
        ans += (dp[0][i] + dp[1][i]) * i
    print(ans)


if __name__ == '__main__':
    main()
