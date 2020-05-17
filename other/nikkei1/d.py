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

def main():
    N, M = MI()
    edges = []

    for i in range(N-1+M):
        a, b = MI()
        edges.append((a-1, b-1))

    in_cnt = defaultdict(int)
    outs = defaultdict(list)
    for a, b in edges:
        in_cnt[b] += 1
        outs[a].append(b)

    res = [0] * N
    queue = deque([i for i in range(N) if in_cnt[i] == 0])
    while len(queue) > 0:
        v = queue.popleft()
        # print(v + 1)
        # res.append(v)
        for nxt_v in outs[v]:
            # print('v', v + 1, 'nxt_v', nxt_v + 1)
            in_cnt[nxt_v] -= 1
            if in_cnt[nxt_v] == 0:
                res[nxt_v] = v + 1
                # print(res, nxt_v + 1, 'p', v + 1)
                queue.append(nxt_v)
    print(*res)

if __name__ == '__main__':
    main()
