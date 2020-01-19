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


def get_ans(dic):
    ans = 0
    for j in range(0, 10):
        for k in range(0, 10):
            if 10 * j + k in dic:
                if 10 * j + k < 10:
                    ans += dic[10 * j + k] * dic[10 * j + k]
                else:
                    ans += dic[10 * j + k] * dic[10 * k + j]
    return ans


def main():
    N = I()
    NS = str(N)

    # m = {}
    # for j in range(1, 10):
    #     for k in range(1, 10):
    #         if j != k:
    #             m[10 * j + k] = 0
    #         else:
    #             m[j] = 0

    # for i in range(len(NS)):
    #     if i == 0:
    #         end = N if len(NS) == 1 else 9
    #         for j in range(1, end+1):
    #             m[j] += 1
    #     elif len(NS) - 1 != i:
    #         for j in range(1, 10):
    #             for k in range(1, 10):
    #                 if j != k:
    #                     m[10 * j + k] += 1 * (10 ** (i - 1))
    #                 else:
    #                     m[j] += 1 * (10 ** (i - 1))
    #     else:
    #         for j in range(1, 10):
    #             for k in range(1, 10):
    #                 b = int(NS[0])
    #                 e = int(NS[-1])
    #                 if j < b:
    #                     if j != k:
    #                         m[10 * j + k] += 1 * (10 ** (i - 1))
    #                     else:
    #                         m[j] += 1 * (10 ** (i - 1))
    #                 elif j == b:
    #                     PNS = ''
    #                     if e < k:
    #                         tmp = str((N - (N % 10)) - 1)
    #                         if tmp[0] != NS[0]:
    #                             continue
    #                         PNS = tmp[1:]
    #                     else:
    #                         PNS = NS[1:]
    #                     print(j, k, PNS)

    #                     if len(PNS) != len(NS) - 1:
    #                         break

    #                     cur = 1
    #                     for t in range(len(PNS)-1):
    #                         cur *= int(PNS[t]) + 1

    #                     if j != k:
    #                         m[10 * j + k] += cur
    #                     else:
    #                         m[j] += cur

    dic = {}

    for j in range(1, 10):
        for k in range(1, 10):
            if j != k:
                dic[10 * j + k] = 0
            else:
                dic[j] = 0

    for i in range(1, N+1):
        if i < 10:
            dic[i] += 1
        else:
            b = int(str(i)[0])
            e = int(str(i)[-1])
            if b == e:
                dic[b] += 1
            elif e != 0:
                dic[10 * b + e] += 1

    # for i in dic.keys():
    #     if m[i] != dic[i]:
    #         print(i, m[i], dic[i])
    # print(get_ans(m))
    print(get_ans(dic))


if __name__ == '__main__':
    main()
