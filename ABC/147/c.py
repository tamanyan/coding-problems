
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


YN = ['No', 'Yes']
MOD = 10**9+7
inf = float('inf')
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = False
show_flg = True

p = None
XY = None
N = None


def dfs(XY, cur, ans_list):
    if cur == N:
        # show(ans_list, len([i for i in ans_list if i != 0]))
        return len([i for i in ans_list if i != 0])

    flag = True
    _ans_list = [i for i in ans_list]
    for xy in XY[cur]:
        if _ans_list[xy[0]-1] == -1 or _ans_list[xy[0]-1] == xy[1]:
            _ans_list[xy[0]-1] = xy[1]
        else:
            flag = False

    ret0 = 0
    ret1 = 0

    if flag:
        if _ans_list[cur] == -1 or _ans_list[cur] == 1:
            _ans_list[cur] = 1
            ret0 = dfs(XY, cur+1, _ans_list)

    _f_ans_list = [i for i in ans_list]
    # _f_ans_list[cur] = 0
    if _f_ans_list[cur] == -1 or _f_ans_list[cur] == 0:
        _f_ans_list[cur] = 0
        ret1 = dfs(XY, cur+1, _f_ans_list)

    return max(ret0, ret1)


def main():
    global p
    global XY
    global N
    N = I()
    XY = [[] for i in range(N)]
    p = [[] for i in range(N+1)]

    for i in range(N):
        a = I()
        for j in range(a):
            x, y = MI()
            XY[i].append((x, y))
            p[x].append(y)

    # print(XY)
    print(dfs(XY, 0, [-1] * N))
    # flag = True
    # for i in range(1, len(p)):
    #     if len(p[i]) == 1 and p[i][0] == 0:
    #         flag = flag and True
    #     else:
    #         flag = flag and False

    # if flag:
    #     print(1)
    #     return

    # ans = 0
    # for i in range(1, len(p)):
    #     # print(sum(p[i]), len(p[i]))
    #     if sum(p[i]) == len(p[i]):
    #         ans += 1

    # print(ans)


if __name__ == '__main__':
    main()
