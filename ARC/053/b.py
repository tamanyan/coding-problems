from heapq import heappush, heappop, heapify
import heapq
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
def print_matrix(mat):
    for i in range(len(mat)):
        print(*['IINF' if v == IINF else "{:0=4}".format(v) for v in mat[i]])


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
    s = S()
    c = Counter(s)
    odd_count = 0
    odd_total = 0
    even_total = 0

    for alpha, count in c.items():
        if count % 2 == 1:
            odd_total += count
            odd_count += 1
        else:
            even_total += count

    if odd_count == 0:
        print(even_total)
        return

    print(2 * ((len(s) - odd_count) // (2 * odd_count)) + 1)
    # v = odd_total // odd_count
    # if v % 2 == 0:
    #     v -= 1
    # remain = odd_total - v * odd_count
    # odd = [v] * odd_count
    # odd = [odd[i] + 1 if i < remain else odd[i] for i in range(len(odd))]
    # print(odd, odd_count, c)

    # # print(even_total)
    # while even_total > 0:
    #     mn = heappop(odd)
    #     mn += 2
    #     even_total -= 2
    #     heappush(odd, mn)

    # print(odd)
    # print(heappop(odd))


if __name__ == '__main__':
    main()
