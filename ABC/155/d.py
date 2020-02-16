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
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main():
    N, K = MI()
    A = LI()
    minus = [-a for a in A if a < 0]
    zero = [a for a in A if a == 0]
    plus = [a for a in A if a > 0]

    minus_max_idx = len(minus) * len(plus)
    zero_max_idx = minus_max_idx + len(zero) * (len(plus) + len(minus)) + cmb(len(zero), 2)

    # print(minus_max_idx, zero_max_idx)

    if (K-1) <= minus_max_idx:
        plus.sort()
        minus.sort(reverse=True)
        high = 10 ** 19
        low = 0

        while high - low > 1:
            mid = (high + low) // 2
            r = 0
            ans = 0
            for l in range(len(minus)):
                while r < len(plus) and minus[l] * plus[r] < mid:
                    r += 1
                ans += len(plus) - r
            if ans < K:
                high = mid
            else:
                low = mid
        print(-low)
    elif (K-1) > minus_max_idx and (K-1) < zero_max_idx:
        print(0)
    else:
        high = 10 ** 19
        low = 0
        plus.sort()
        minus.sort()

        while high - low > 1:
            mid = (high + low) // 2
            r = 0
            ans = 0
            for num in minus[::-1]:
                if num * num <= mid:
                    ans -= 1
                while r < len(minus) and minus[r] * num <= mid:
                    r += 1
                ans += r
            r = 0
            for num in plus[::-1]:
                if num * num <= mid:
                    ans -= 1
                while r < len(plus) and plus[r] * num <= mid:
                    r += 1
                ans += r
            ans //= 2
            # print('ans', ans, 'mid', mid, 'low', low, 'high', high, K - zero_max_idx)

            if ans < K - zero_max_idx:
                low = mid
            else:
                high = mid
        print(high)


if __name__ == '__main__':
    main()
