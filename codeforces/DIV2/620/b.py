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

show_flg = False
# show_flg = True


def main():
    n, m = MI()
    s = [None] * n
    pairs = []
    self_p = []
    n_pairs = []

    for i in range(n):
        s[i] = S()

    for i in range(n):
        for j in range(i, n):
            cnt = 0
            for k in range(m):
                if s[i][k] == s[j][(m-1)-k]:
                    cnt += 1

            if cnt == m:
                pairs.append((i, j))

    for i in range(len(pairs)):
        if pairs[i][0] == pairs[i][1]:
            self_p.append(pairs[i])
        else:
            n_pairs.append(pairs[i])

    # print(n_pairs, self_p)
    head = ''
    tail = ''
    for i in range(len(n_pairs)):
        head += s[n_pairs[i][0]]
        tail = s[n_pairs[i][1]] + tail

    middle = ''
    for i in range(len(self_p)):
        middle = s[self_p[i][0]]

    ans = head + middle + tail
    print(len(ans))
    print(ans)
    # print(head, middle, tail)


if __name__ == '__main__':
    main()
