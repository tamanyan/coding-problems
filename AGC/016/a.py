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


def S(): return input()


def MI(): return map(int, input().split())


def MS(): return map(str, input().split())


def LI(): return [int(i) for i in input().split()]


def LI_(): return [int(i)-1 for i in input().split()]


def StoI(): return [ord(i)-97 for i in input()]


def ItoS(nn): return chr(nn+97)


def input(): return sys.stdin.readline().rstrip()


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YNL = {False: 'No', True: 'Yes'}
YNU = {False: 'NO', True: 'YES'}
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
    s = S()
    c = Counter(s)
    mosts = c.most_common()
    ans = len(s)

    for most in mosts:
        t = [i for i in s]
        loop = 0
        while not all([i == most[0] for i in t]):
            cur = []
            for i in range(len(t)):
                if i < len(t) - 1 and t[i+1] == most[0]:
                    cur.append(t[i+1])
                else:
                    cur.append(t[i])
            cur.pop()
            t = cur
            loop += 1
        ans = min(ans, loop)

    print(ans)


if __name__ == '__main__':
    main()
