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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    N = I()
    F = LI()
    gifts_in = [0] * N
    gifts_out = [0] * N

    for i in range(N):
        F[i] -= 1
        if F[i] >= 0:
            gifts_in[F[i]] += 1
            gifts_out[i] += 1

    loops = []
    for i in range(N):
        if gifts_in[i] == 0 and gifts_out[i] == 0:
            loops.append(i)

    if len(loops) == 1:
        idx = loops[0]
        for i in range(N):
            if gifts_in[i] == 0 and i != idx:
                F[idx] = i
                gifts_in[i] += 1
                gifts_out[idx] += 1
                break
    elif len(loops) > 1:
        for i in range(len(loops)):
            cur = loops[i]
            nxt = loops[(i + 1) % (len(loops))]
            F[cur] = nxt
            gifts_in[nxt] += 1
            gifts_out[cur] += 1

    # print('in', gifts_in)
    # print('out', gifts_out)

    ins = []
    outs = []
    for i in range(N):
        if gifts_in[i] == 0:
            ins.append(i)
        if gifts_out[i] == 0:
            outs.append(i)

    if len(outs) == len(ins):
        for i in range(len(ins)):
            F[outs[i]] = ins[i]
        print(*[f+1 for f in F])
    else:
        print(-1)


if __name__ == '__main__':
    main()
