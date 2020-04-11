from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product
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
    c = S()
    ans = 10**9

    for pair1 in product(['A', 'B', 'X', 'Y'], repeat=2):
        for pair2 in product(['A', 'B', 'X', 'Y'], repeat=2):
            if pair1 == pair2:
                continue
            L = ''.join(pair1)
            R = ''.join(pair2)
            dp = [i for i in range(N+1)]
            dp[0] = 0
            dp[1] = 1

            for i in range(2, N+1):
                dp[i] = min(dp[i], dp[i-1]+1)
                if c[i-2:i] == L or c[i-2:i] == R:
                    dp[i] = min(dp[i], dp[i-2]+1)

            ans = min(ans, dp[-1])

    print(ans)


if __name__ == '__main__':
    main()
