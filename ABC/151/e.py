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


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def factorization(n):
    """
    素因数分解
    :param int n:
    :rtype: list of int
    """
    if n <= 1:
        return []

    ret = []
    while n > 2 and n % 2 == 0:
        ret.append(2)
        n //= 2
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            ret.append(i)
            n //= i
        else:
            i += 2
    ret.append(n)
    return ret


def main():
    N, K = MI()
    A = LI()
    ans = 0
    A = sorted(A)
    ARR = list(accumulate([0] + A))

    # for i, d in enumerate(list(itertools.combinations(A, K))):
    #     print(i, d)
    #     ans += max(d) - min(d)

    for i in range(N-K+1):
        # print(i + 1, i + K - 1)
        start = i + K - 1
        a = ARR[N] - ARR[start]
        n = A[i] * (N - (i + K - 1))
        begin = A[start]
        end = A[N-1]
        print(A[i], 'b', begin, 'e', end, 'a', a, 'n', n)
        ans += a - n

    print(ans)


if __name__ == '__main__':
    main()
