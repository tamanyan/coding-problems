
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
IINF = 10**19
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)


show_flg = False
# show_flg = True


def main():
    N = I()
    w = [0] * N
    stacks = [[] for i in range(N)]
    min_tops = [IINF] * N

    for i in range(N):
        w[i] = I()

    for i in range(N):
        min_index = min_tops.index(min(min_tops))
        if len(stacks[min_index]) == 0:
            stacks[min_index].append(w[i])
            min_tops[min_index] = w[i]
        elif stacks[min_index][-1] >= w[i]:
            stacks[min_index].append(w[i])
            min_tops[min_index] = w[i]
        else:
            for j in range(len(stacks)):
                if len(stacks[j]) == 0:
                    stacks[j].append(w[i])
                    min_tops[j] = w[i]
                    break
                elif stacks[j][-1] >= w[i]:
                    stacks[j].append(w[i])
                    min_tops[j] = w[i]
                    break

    # print(stacks)
    print(len([s for s in stacks if len(s) != 0]))


if __name__ == '__main__':
    main()
