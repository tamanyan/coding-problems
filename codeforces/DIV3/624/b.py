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


YN = {False: 'NO', True: 'YES'}
MOD = 10**9+7
inf = float('inf')
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def solve(T):
    n, m = MI()
    a = LI()
    p = LI()
    dic = {k: True for k in p}
    # print(dic)

    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                if j+1 not in dic:
                    # print(j)
                    print('NO')
                    return
                a[j], a[j+1] = a[j+1], a[j]

    # print(a)
    print('YES')


def main():
    T = I()

    for i in range(T):
        solve(T)


if __name__ == '__main__':
    main()
