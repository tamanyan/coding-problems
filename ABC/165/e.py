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
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]

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

    if N % 2 == 1:
        pairs = []
        for i in range(N//2):
            pairs.append((i+1, N-i))

        # print(pairs)
        for i in range(M):
            print(*pairs[i])
            # print((pairs[i][0] - pairs[i][1]) % N)
            # print((pairs[i][1] - pairs[i][0]) % N)
    else:
        pairs = []
        for i in range(N//2//2):
            pairs.append((i+1, N-i))

        for i in range(N//2//2+1, N//2):
            pairs.append((i+1, N-i+1))

        # print(pairs)
        for i in range(M):
            print(*pairs[i])
            # print((pairs[i][0] - pairs[i][1]) % N)
            # print((pairs[i][1] - pairs[i][0]) % N)


if __name__ == '__main__':
    main()
