from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
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
    X, Y = MI()
    a = deque()
    b = deque()
    tim = 0
    ans = 0

    for i in LI():
        a.append(i)

    for i in LI():
        b.append(i)

    while len(a) != 0 and len(b) != 0:
        d = a.popleft()
        while d < tim and len(a) != 0:
            d = a.popleft()

        # print('a', tim, d)
        if d < tim:
            break

        tim = d + X

        d = b.popleft()
        while d < tim and len(b) != 0:
            d = b.popleft()

        # print('b', tim, d)
        if d < tim:
            break

        tim = d + Y
        # print('tim', tim)

        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
