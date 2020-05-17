from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
import sys
import bisect
import string
import math
import time
from decimal import Decimal
import decimal


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

def cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.87758256189
    >>> print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    decimal.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    decimal.getcontext().prec -= 2
    return +s


def main():
    A, B, H, M = MI()
    decimal.getcontext().prec = 20

    if M == 0 and H == 0:
        print(A - B)
        return

    if M == 0:
        m = Decimal(0)
    else:
        m = Decimal(M * 360 / 60)

    if H == 0:
        h = Decimal(0)
    else:
        h = Decimal(H * 360.0 / 12.0)
        # print(h, 360 / 12)
        h += Decimal(360.0 / 12.0) * (Decimal(M) / Decimal(60.0))

    if h > m:
        d = 0
        if abs(h - m) >= 180:
            d = 360 - abs(h - m)
        else:
            d = abs(h - m)
        r = Decimal(math.radians(d))
        A = Decimal(A)
        B = Decimal(B)
        ans = A**2 + B**2 - 2 * A * B * Decimal(cos(r))
        # print('A', A, 'B', B, 'm', m, 'h', h)
        # print(d, r)
        print(ans.sqrt())
    else:
        # print('ssssssss')
        d = 0
        if abs(m - h) >= 180:
            d = 360 - abs(h - m)
        else:
            d = abs(m - h)
        r = Decimal(math.radians(d))
        A = Decimal(A)
        B = Decimal(B)
        # ans = A**2 + B**2 - 2 * A * B * math.cos(r)
        ans = A**2 + B**2 - 2 * A * B * Decimal(cos(r))
        # print('A', A, 'B', B, 'm', m, 'h', h)
        # print(d, r)
        print(ans.sqrt())



if __name__ == '__main__':
    main()
