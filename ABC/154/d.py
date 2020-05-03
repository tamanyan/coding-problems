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
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# show_flg = True
show_flg = False


def main():
    N, K = MI()
    p = LI()

    ans = 0
    cur = 0
    right = 0
    ans_arr = []
    for left in range(N):

        while right < len(p) and right - left < K:
            cur += p[right]
            right += 1

        if ans <= cur:
            ans = cur
            ans_arr = p[left:right]
        cur -= p[left]
        # print(ans, cur, cur + p[left], left, right)

    # print(ans, ans_arr)
    p = 0

    for a in ans_arr:
        t = (a * (a + 1)) // 2
        # print(a, t)
        p += t / a

    print(p)



if __name__ == '__main__':
    main()
