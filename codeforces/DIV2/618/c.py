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


def f(x, y):
    return x & ~y


def main():
    n = I()
    a = LI()
    a = sorted(a, reverse=True)
    x = 0
    # bin_a = sorted(bin_a, reverse=True)

    # 一つだけbitが立っている部分を先頭にする
    for i in range(30, -1, -1):
        c = 0
        for j in range(n):
            if (a[j] >> i) & 1 == 1:
                c += 1
                x = j

        if c == 1:
            break

    ans = [a.pop(x)] + a
    print(*ans)


if __name__ == '__main__':
    main()
