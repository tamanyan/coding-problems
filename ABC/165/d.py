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


def f(x, A, B):
    return (A * x) // B - A * (x // B)

def main():
    A, B, N = MI()
    ans = 0
    s = set()

    x = B - 1
    # print(f(x, A, B))

    if x >= N:
        # print(x, N)
        x = N

    # print('x', x)
    print(f(x, A, B))
    # print(3, f(3, A, B))
    # print(4, f(4, A, B))

    # for x in range(min(N+1, 10**6)):
    #     d = f(x, A, B)
    #     ans = max(ans, d)
    #     s.add(d)
    #     print(x, d)

    # print(s)
    # print(ans)


if __name__ == '__main__':
    main()
