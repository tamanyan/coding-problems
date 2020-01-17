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

show_flg = False
# show_flg = True

memo = {}

# 26.000000000000004
test = []

def call(distance, index, arr, selected, x, N, F):
    # global test
    if len(selected) == N-1:
        # test.append(distance)
        # print(distance, arr, distance / F)
        return distance / F

    # test = 0
    # if x != -1:
    #     test = 1

    sum_d = 0
    for i in range(N-1):
        if i not in selected:
            # bisect.insort(arr, i)
            last_index = i + 1
            for n in range(i + 1, N):
                if n not in selected:
                    last_index = n
                    break

            nd = x[last_index] - x[i]
            ns = selected.union(set([i]))
            # _arr = [a for a in arr]
            # print('index', i, last_index, selected)
            # _arr.append(i)
            _arr = []
            ret = call(distance + nd, index, _arr, ns, x, N, F)
            # memo[str(_arr)] = ret
            sum_d += ret

    return sum_d


def main():
    global test
    N = I()
    # x = LI()
    x = [i for i in range(N)]
    F = math.factorial(N-1)

    ans = call(0, -1, [], set(), x, N, F) * F

    print(ans)


if __name__ == '__main__':
    main()
