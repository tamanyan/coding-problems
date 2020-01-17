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


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # if self.parents[x] < 0:
        #     return x
        # else:
        #     ret = None
        #     stack = [(x, self.parents[x])]

        #     while True:
        #         caller, cur = stack[-1]
        #         nxt = self.parents[cur]
        #         if nxt < 0:
        #             ret = cur
        #             break
        #         stack.append((cur, nxt))

        #     while len(stack) > 0:
        #         caller, _ = stack.pop()
        #         self.parents[caller] = ret
        #         ret = self.parents[caller]

        #     return ret

        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N, Q = MI()
    # node_list = [UnionFindNode(i) for i in range(N+1)]
    P = [0] * Q
    A = [0] * Q
    B = [0] * Q
    uf = UnionFind(N+1)

    for i in range(Q):
        P[i], A[i], B[i] = MI()

    for i in range(Q):
        if P[i] == 0:
            uf.union(A[i], B[i])
        else:
            if uf.same(A[i], B[i]):
                print('Yes')
            else:
                print('No')


if __name__ == '__main__':
    main()
