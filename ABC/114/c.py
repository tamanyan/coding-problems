from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)


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
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


def main():
    N = int(input())
    number = str(N)
    L = len(number)
    dp = [[[[[0 for t in range(2)]
                for f in range(2)]
                for s in range(2)]
                for smaller in range(2)]
                for j in range(L + 1)]

    n = []
    for i in range(L):
        n.append(int(number[i]))

    # k,smaller,7,5,3
    dp[0][0][0][0][0] = 1

    for k in range(L):
        for smaller in range(2):
            for s in range(2):
                for f in range(2):
                    for t in range(2):
                        li = [0, 7, 5, 3] if smaller else [q for q in [0, 7, 5, 3] if q <= n[k]]
                        for m in li:
                            if k + 2 == L:
                                if s == 1 and f == 0 and t == 0 and m != 7:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                elif s == 0 and f == 1 and t == 0 and m != 5:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                elif s == 0 and f == 0 and t == 1 and m != 3:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                elif m != 0:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                # print('k+2', k)
                            elif k + 1 == L:
                                if s == 0 and f == 1 and t == 1 and m == 7:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                elif s == 1 and f == 0 and t == 1 and m == 5:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                elif s == 1 and f == 1 and t == 0 and m == 3:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                elif m != 0:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
                                # print('k+1', k)
                            else:
                                if s == 0 and f == 0 and t == 0 and m == 0:
                                    dp[k+1][1][0][0][0] += dp[k][smaller][s][f][t]
                                elif m != 0:
                                    dp[k+1][smaller or m < n[k]][s == 1 or m == 7][f == 1 or m == 5][t == 1 or m == 3] += dp[k][smaller][s][f][t]
        # print(k+1)
        # print('dp[k+1][0][0][0][0]', dp[k+1][0][0][0][0])
        # print('dp[k+1][0][0][0][1]', dp[k+1][0][0][0][1])
        # print('dp[k+1][0][0][1][0]', dp[k+1][0][0][1][0])
        # print('dp[k+1][0][0][1]11]', dp[k+1][0][0][1][1])
        # print('dp[k+1][0][1][0][0]', dp[k+1][0][1][0][0])
        # print('dp[k+1][0][1][0][1]', dp[k+1][0][1][0][1])
        # print('dp[k+1][0][1][1][0]', dp[k+1][0][1][1][0])
        # print('dp[k+1][0][1][1][1]', dp[k+1][0][1][1][1])
        # print('dp[k+1][1][0][0][0]', dp[k+1][1][0][0][0])
        # print('dp[k+1][1][0][0][1]', dp[k+1][1][0][0][1])
        # print('dp[k+1][1][0][1][0]', dp[k+1][1][0][1][0])
        # print('dp[k+1][1][0][1][1]', dp[k+1][1][0][1][1])
        # print('dp[k+1][1][1][0][0]', dp[k+1][1][1][0][0])
        # print('dp[k+1][1][1][0][1]', dp[k+1][1][1][0][1])
        # print('dp[k+1][1][1][1][0]', dp[k+1][1][1][1][0])
        # print('dp[k+1][1][1][1][1]', dp[k+1][1][1][1][1])
        # print('=========================')

    # print(dp[L][0][1][1][1])
    # print(dp[L][1][1][1][1])
    print(dp[L][0][1][1][1] + dp[L][1][1][1][1])


def sub():
    N = int(input())
    number = str(N)
    length = len(number)
    ans = 0

    stack = ['']
    while len(stack) > 0:
        s = stack.pop()

        if len(s) >= length:
            remain = set([s[i] for i in range(len(s))]) - set('0')
            if len(remain) == 3 and int(s) <= N:
                ans += 1
                # print(s)
            continue

        for i in ['0', '7', '5', '3']:
            if (i == '0' and len(s) == 0) or (len(s) > 0 and s[-1] == '0'):
                stack.append(s + i)
            elif i != '0':
                stack.append(s + i)

    print(ans)


if __name__ == '__main__':
    sub()
