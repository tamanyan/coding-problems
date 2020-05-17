from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, accumulate, product, combinations_with_replacement
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
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]

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

def bitstr(bit):
    return '{:03b}'.format(bit)


def main():
    N, M = MI()
    edge = [0] * N
    ans = IINF
    dp = [0] * (1 << N)
    dp[0] = 1

    for i in range(M):
        x, y = MI()
        x -= 1
        y -= 1
        edge[x] |= 1 << y

    print(list(map(bin, edge)))

    jbs = [(j, 1 << j) for j in range(N)]

    for bit in range(1 << N):
        for j, jb in jbs:
            # 集合bitの中にiはまだ存在しない and jの流出先ノードにbitの要素が含まれない
            if bit & jb and not (edge[j] & bit):
                dp[bit] += dp[bit ^ jb]
                print('bin', *[bitstr(j) for j in range(1 << N)])
                print(' dp', *['{: 3}'.format(j) for j in dp])
                print(bitstr(bit ^ jb), '->', bitstr(bit))
                print('=======================================')
            else:
                print('skip bit', bitstr(bit), 'i', bitstr(i), 'conn', bitstr(edge[i]))
                print('=======================================')



    # for bit in range(1 << N):
    #     for i in range(N):
    #         # i番目のbitが立ってない（＝ゴールしてない）ならとばす
    #         if not (bit & (1 << i)):
    #             continue
    #         # iは先にゴールしている、という証言があれば不適
    #         if not (edge[i] & bit):
    #             # delete bit
    #             dp[bit] += dp[bit^(1 << i)]
    #         #     print('bin', *[bitstr(j) for j in range(1 << N)])
    #         #     print(' dp', *['{: 3}'.format(j) for j in dp])
    #         #     print(bitstr(bit^(1 << i)), '->', bitstr(bit))
    #         #     print('=======================================')
    #         # else:
    #         #     print('skip bit', bitstr(bit), 'i', bitstr(i), 'conn', bitstr(edge[i]))
    #         #     print('=======================================')
    print(dp[-1])


if __name__ == '__main__':
    main()
