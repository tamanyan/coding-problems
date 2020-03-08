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
IINF = 10**10
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10**6)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

show_flg = False
# show_flg = True


def main():
    N, P = MI()
    s = S()
    ans = 0
    dic = [0] * N
    dic2 = [0] * (N - 1)

    # for i in range(N):
    #     for j in range(i+1, N+1):
    #         # print(s[i:j])
    #         if int(s[i:j]) % P == 0:
    #             ans += 1

    tmp = 0
    for i in range(N + 1 - len(str(P))):
        if int(s[i:i+len(str(P))]) % P == 0:
            dic[i] = 1
            tmp += 1

    for i in range(N + 1 - len(str(P)) - 1):
        if s[i:i+1+len(str(P))][0] == '0':
            continue

        if int(s[i:i+1+len(str(P))]) % P == 0:
            dic2[i] = 1
            tmp += 1

    D = list(accumulate(dic))
    D2 = list(accumulate(dic2))
    # print(D, D2)
    # print((D[-1] + D2[-1]) * 2)

    # print(ans)
    tmp = 0
    tmp += (D[-1] * (D[-1] + 1)) // 2
    tmp += (D2[-1] * (D2[-1] + 1)) // 2
    print(tmp)
    # print(tmp, dic)


if __name__ == '__main__':
    main()
