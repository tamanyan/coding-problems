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


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


def print_matrix(mat):
    for i in range(len(mat)):
        print(*mat[i])


yn = {False: 'No', True: 'Yes'}
YN = {False: 'NO', True: 'YES'}
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
    A = [[None] * N for i in range(N)]
    B = [[None] * M for i in range(M)]

    for i in range(N):
        s = S()
        for j in range(N):
            A[i][j] = s[j]

    for i in range(M):
        s = S()
        for j in range(M):
            B[i][j] = s[j]

    for i in range(N-M+1):
        for j in range(N-M+1):
            f = []
            for m in range(M):
                for n in range(M):
                    f.append(A[i+m][j+n] == B[m][n])

            if all(f):
                print('Yes')
                return

    print('No')


if __name__ == '__main__':
    main()
