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
    N = I()
    A = LI()
    B = LI()
    ans = IINF

    for idxs in permutations([i for i in range(N)]):
        idxs = list(idxs)
        front = []
        v = []
        for pos in range(len(idxs)):
            idx = idxs[pos]
            if pos % 2 == 0 and idx % 2 == 0:
                front.append(A[idx])
                v.append('A' + str(idx))
            elif pos % 2 == 0 and idx % 2 == 1:
                front.append(B[idx])
                v.append('B' + str(idx))
            elif pos % 2 == 1 and idx % 2 == 0:
                front.append(B[idx])
                v.append('B' + str(idx))
            elif pos % 2 == 1 and idx % 2 == 1:
                front.append(A[idx])
                v.append('A' + str(idx))
        print(v)

        if all([front[i-1] <= front[i] for i in range(1, N)]):
            swap_count = sum([abs(pos - idxs[pos]) for pos in range(len(idxs))]) // 2
            ans = min(ans, swap_count)

    if ans == IINF:
        print(-1)
    else:
        print(ans)



if __name__ == '__main__':
    main()
