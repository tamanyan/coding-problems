
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


# show_flg = True
show_flg = False


def main():
    N = int(input())
    S = input()
    pos = [[] for i in range(10)]
    ans = 0

    for i in range(len(S)):
        pos[int(S[i])].append(i)

    show(pos)

    NUM = 10
    for i in range(NUM):
        for j in range(NUM):
            for k in range(NUM):
                cur = -1
                # print(pos[k])
                pos_i = [m for m in pos[i]]

                pos_j = [m for m in pos[j]]
                if j == i and len(pos_j) > 1:
                    pos_j.pop(0)

                pos_k = [m for m in pos[k]]
                if k == i and len(pos_k) > 1:
                    pos_k.pop(0)
                if k == j and len(pos_k) > 1:
                    pos_k.pop(0)

                if len(pos_i) == 0:
                    show('len(pos_i) == 0:')
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue

                cur = pos_i.pop(0)

                #################################

                if len(pos_j) == 0:
                    show('len(pos_j) == 0:')
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue

                # prev_cur = cur
                idx = bisect.bisect_right(pos_j, cur)
                # print(cur, idx, pos_j)
                if len(pos_j) <= idx:
                    show('pos_j', idx, cur, pos_j)
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue

                if cur > pos_j[idx]:
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue
                cur = pos_j[idx]
                # show('bisect', pos_j[test], prev_cur)
                # while len(pos_j) > 0:
                #     tmp = pos_j.pop(0)
                #     if tmp > cur:
                #         cur = tmp
                #         break
                # show('while', cur, prev_cur)

                # if prev_cur == cur:
                #     show('pos_j', tmp, cur)
                #     show(i, j, k, pos[i], pos[j], pos[k])
                #     continue

                #################################

                if len(pos_k) == 0:
                    show('len(pos_k) == 0:')
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue

                idx = bisect.bisect_right(pos_k, cur)
                # print(cur, idx, pos_j)
                if len(pos_k) <= idx:
                    show('pos_k', idx, cur, pos_k)
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue

                if cur > pos_k[idx]:
                    show(i, j, k, pos[i], pos[j], pos[k])
                    continue
                cur = pos_k[idx]
                # prev_cur = cur
                # while len(pos_k) > 0:
                #     tmp = pos_k.pop(0)
                #     if tmp > cur:
                #         cur = tmp
                #         break

                # if prev_cur == cur:
                #     show('pos_k', tmp, cur)
                #     show(i, j, k, pos[i], pos[j], pos[k])
                #     continue

                # show(i, j, k)
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
