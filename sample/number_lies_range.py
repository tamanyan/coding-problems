from bisect import bisect_left as lower_bound
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
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


show_flg = True
show_flg = False


def answer_queries(a, n, queries, q):
    # container to store all range
    v = list()

    # hash the L and R
    mpp = dict()

    # Push the element to container
    # and hash the L and R
    for i in range(n):
        v.append(a[i][0])
        mpp[a[i][0]] = 1
        v.append(a[i][1])
        mpp[a[i][1]] = 2

    # sort the elements in container
    v.sort()
    for i in range(q):

        # each query
        num = queries[i]

        # get the number same or greater than integer
        ind = bisect.bisect_left(v, num)

        # if it lies
        if v[ind] == num:
            # print(ind, v[ind], v, num, mpp)
            print("Yes")
        else:

            # check if greater is hashed as 2
            if mpp[v[ind]] == 2:
                # print(ind, v[ind], v, num, mpp)
                print("Yes")
            # check if greater is hashed as 1
            else:
                print("No")


def main():
    a = [[5, 6], [1, 3], [8, 10]]
    n = 3
    queries = [1, 2, 3, 4, 7]
    q = len(queries)

    # function call to answer queries
    answer_queries(a, n, queries, q)


if __name__ == '__main__':
    main()
