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
ts = time.time()
# sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def main():
    N = I()
    w = list(MS())
    dic = {
        'b': 1, 'c': 1,
        'd': 2, 'w': 2,
        't': 3, 'j': 3,
        'f': 4, 'q': 4,
        'l': 5, 'v': 5,
        's': 6, 'x': 6,
        'p': 7, 'm': 7,
        'h': 8, 'k': 8,
        'n': 9, 'g': 9,
        'z': 0, 'r': 0
    }

    ans = []

    for i in range(N):
        s = []
        for j in range(len(w[i])):
            c = w[i][j].lower()
            if c in dic:
                s.append(str(dic[c]))
        if len(s) > 0:
            ans.append(''.join(s))

    print(*ans)


if __name__ == '__main__':
    main()
