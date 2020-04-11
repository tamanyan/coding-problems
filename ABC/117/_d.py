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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True

def bin_to_v(q):
    return int("".join(str(x) for x in q), 2)

import random

def main():
    # N, K = MI()
    # A = LI()
    N = random.randint(4, 5)
    K = random.randint(0, 100)
    A = [random.randint(0, 100) for i in range(N)]
    LEN = len(str(bin(K)))-2
    ans = 0
    q = []
    k = [int(d) for d in str(bin(K))[2:]]
    q_c = []

    for i in range(LEN):
        m = defaultdict(int)
        for j in range(N):
            m[(A[j] & (1 << i)) != 0] += 1
        if m[True] >= m[False]:
            q.append(0)
            q_c.append(m[True])
        else:
            q.append(1)
            q_c.append(m[False])

    q = q[::-1]
    q_c = q_c[::-1]

    p = 0
    v = bin_to_v(q)
    if v <= K:
        p = max(p, sum([v ^ a for a in A]))

    for i in range(len(q)):
        _q = q.copy()
        _q[i] = 0
        v = bin_to_v(_q)
        if v <= K:
            p = max(p, sum([v ^ a for a in A]))

    ans = 0
    ans_i = 0
    for i in range(K+1):
        out = sum([i ^ a for a in A])
        if ans < out:
            ans = out
            ans_i = i

    if p != ans:
        print(q)
        print(q_c)
        print(N, K)
        print(*A)
        for a in A:
            print(a, [int(d) for d in str(bin(a))[2:]])
        print(p, '=', ans, v, '=', ans_i)
        print('q', q)
        # print('o', o)
        print('i', [int(d) for d in str(bin(ans_i))[2:]])
        print('k', [int(d) for d in str(bin(K))[2:]])
        print('v', [int(d) for d in str(bin(v))[2:]])
        print('===========================')


if __name__ == '__main__':
    # main()
    for i in range(10):
        main()
# q [1, 1, 1, 0]
# i [0, 1, 1, 0]
# k [1, 0, 1, 0]
# v [1, 1, 1, 0]
