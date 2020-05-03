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


def debug(table, *args):
    ret = []
    for name, val in table.items():
        if val in args:
            ret.append('{}: {}'.format(name, val))
    print(' | '.join(ret), file=sys.stderr)


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

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_n(a, n):
    ans = a[0]
    for i in range(1, n):
        ans = gcd(ans, a[i])
    return ans


def divisor(n):
    ret = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


def rec(i, arr, N, K):
    if len(arr) == N:
        ret = gcd_n(arr, N)
        print(arr, ret)
        return ret

    ans = 0
    for v in range(1, K+1):
        ans += rec(i+1, arr + [v], N, K)
        ans %= MOD

    return ans


def main():
    N, K = MI()
    ans = 0
    m = {}
    dp =

    # print(rec(0, [], N, K))
    ans = 0
    for i in range(N):
        dp_next = [-IINF] * (N//2+1)
        for j in range(1, 5):
            ans += 1
        dp = dp_next

    print(ans)



if __name__ == '__main__':
    main()
