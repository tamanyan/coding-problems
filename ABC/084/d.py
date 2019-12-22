
from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate
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


# show_flg = True
show_flg = False


# エラトステネスのふるい 素数の列挙
def primes(n):
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = 0
    return is_prime


def main():
    Q = I()
    l = [0] * Q
    r = [0] * Q

    for i in range(Q):
        l[i], r[i] = MI()

    prime_list = primes(10**5+1)
    arr = []
    for i in range(10**5+1):
        if i % 2 == 1:
            arr.append(int(prime_list[i] and prime_list[(i+1)//2]))
        else:
            arr.append(0)
    ARR = list(accumulate([0] + arr))

    for i in range(Q):
        # print(r[i]+1, l[i], ARR[r[i]+1], ARR[l[i]])
        # print(ARR[:r[i]+1])
        print(ARR[r[i]+1] - ARR[l[i]])


if __name__ == '__main__':
    main()
