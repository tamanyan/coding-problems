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

show_flg = False
# show_flg = True


def main():
    T = I()
    n = [0] * T
    x = [0] * T
    s = [''] * T

    for i in range(T):
        n[i], x[i] = MI()
        s[i] = S()

    for t in range(T):
        Q = s[t]
        X = x[t]
        one = 0
        zero = 0
        ans = 0
        a = [0] * (len(Q) + 1)
        for i in range(len(Q)):
            if Q[i] == '1':
                one += 1
            else:
                zero += 1
            a[i+1] += zero - one

        for i in range(len(a)):
            if a[i] == X:
                ans += 1
        end = a[-1]
        print(Q, X, a, end)

        if end == 0 and ans != 0:
            print(-1)
            continue

        if end == 0 and ans == 0:
            print(0)
            continue

        for i in range(1, len(a)):
            if end > 0 and a[i] < X and ((X - a[i]) % end) == 0:
                print(X, a[i])
                ans += 1
            elif end < 0 and a[i] > X and ((a[i] - X) % abs(end)) == 0:
                print(X, a[i])
                ans += 1

        print(ans)


if __name__ == '__main__':
    main()
