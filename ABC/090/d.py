from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time
from fractions import gcd
#import random


def I(): return int(input())


def MI(): return map(int, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['Yes', 'No']
MOD = 10**9+7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True

def divisor(n):
    ret = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


def main():
    N, K = MI()
    arr = [[0] * N for i in range(N)]
    divisors = []

    for a in range(1, N+1):
        divisors.append(divisor(a))
        for b in range(1, N+1):
            if a % b >= K:
                arr[a-1][b-1] = a % b
                # print('t', a, b, K)
            else:
                arr[a-1][b-1] = a % b

    for i in range(len(arr)):
        print(i+1, arr[i])

if __name__ == '__main__':
    main()
