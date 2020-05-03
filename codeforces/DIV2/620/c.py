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
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def solve(n, m):
    TIME = 0
    LOW = 1
    HIGH = 2
    cus = []

    for i in range(n):
        t, l, h = MI()
        cus.append((t, l, h))

    if abs(m - cus[0][LOW]) > cus[0][TIME] and abs(m - cus[0][HIGH]) > cus[0][TIME]:
       print('NO')
       return

    for i in range(1, n):
        if cus[i][LOW] < cus[i+1][LOW] and cus[i][HIGH] < cus[i+1][HIGH]:
            pass
        # if abs(cus[i][LOW] - cus[i][LOW])

    # print(cus[0][TIME])
    # print(abs(m - cus[0][LOW]))
    # print(abs(m - cus[0][HIGH]))

    # l_range = 0
    # h_range = 0
    # if m < cus[0][LOW]:
    #     l_range = cus[0][LOW]
    #     h_range = min(cus[0][HIGH], cus[0][TIME] + m)
    # elif m > cus[0][HIGH]:
    #     l_range = max(cus[0][LOW], m - cus[0][TIME])
    #     h_range = cus[0][HIGH]
    # else:
    #     l_range = max(cus[0][LOW], m - cus[0][TIME])
    #     h_range = min(cus[0][HIGH], m + cus[0][TIME])

    # # print('l_range', 'h_range', l_range, h_range)

    # ranges = []
    # next_ranges = [(l_range, h_range)]

    # for i in range(1, n):
    #     can = False
    #     # print('next_ranges', next_ranges)
    #     ranges = next_ranges
    #     next_ranges = []
    #     TIME_LEN = cus[i][TIME] - cus[i-1][TIME]
    #     next_l_range = 10**19
    #     next_h_range = -10**19
    #     for (l_range, h_range) in ranges:
    #         # print('Start', 'i', i, '(', l_range, h_range, ')', TIME_LEN)
    #         for m in range(l_range, h_range+1):
    #             if abs(m - cus[i][LOW]) <= TIME_LEN or abs(m - cus[i][HIGH]) <= TIME_LEN or\
    #                  (m >= cus[i][LOW] and m <= cus[i][HIGH]):
    #                 can = True
    #                 _l_range = 0
    #                 _h_range = 0
    #                 if m < cus[i][LOW]:
    #                     _l_range = cus[i][LOW]
    #                     _h_range = min(cus[i][HIGH], TIME_LEN + m)
    #                 elif m > cus[i][HIGH]:
    #                     _l_range = max(cus[i][LOW], m - TIME_LEN)
    #                     _h_range = cus[i][HIGH]
    #                 else:
    #                     _l_range = max(cus[i][LOW], m - TIME_LEN)
    #                     _h_range = min(cus[i][HIGH], m + TIME_LEN)
    #                 next_l_range = min(next_l_range, _l_range)
    #                 next_h_range = max(next_h_range, _h_range)

    #     # if i+1 < n and cus[i+1][HIGH] < next_l_range:
    #     #     next_h_range = next_l_range
    #     # elif i+1 < n and cus[i+1][LOW] > next_h_range:
    #     #     next_l_range = next_h_range
    #     next_ranges.append((next_l_range, next_h_range))
    #     # print('l', 'r', next_ranges)

    #     if not can:
    #         print('NO')
    #         return
    #     # cus[n][LOWER]

    # print('YES')


def main():
    q = I()

    for i in range(q):
        n, m = MI()
        solve(n, m)


if __name__ == '__main__':
    main()
