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
    T = I()
    n = [0] * T
    digits = [None] * T

    for i in range(T):
        n[i] = I()
        digits[i] = S()

    for i in range(T):
        even = 0
        odd = 0
        _D = digits[i]
        D = ''
        N = n[i]
        result = 0

        for j in range(len(_D)):
            if int(_D[j]) % 2 != 0:
                D += _D[j]

        # while len(D) != 0:
        #     if int(D) % 2 == 0:
        #         D = D[:len(D)-1]
        #         if len(D) != 0 and int(D) % 2 != 0:
        #             break
        #     else:
        #         break
                # print(D)

        # print('Start', D)

        for j in range(len(D)):
            if int(D[j]) % 2 == 0:
                even += 1
            else:
                odd += 1
            result += int(D[j])

        ans = ''
        flag = False

        # print('odd', odd, 'even', even)

        if odd % 2 == 1:
            for j in range(len(D)):
                if int(D[j]) % 2 == 1 and flag is False:
                    flag = True
                    continue
                ans += D[j]
        else:
            ans = D

        # print('ans', ans)
        # print(D, even, odd)
        if len(ans) == 0 or ans == '0':
            print(-1)
        else:
            if int(ans) % 2 == 0:
                print(-1)
            else:
                print(ans)
            # print('result', result)


if __name__ == '__main__':
    main()
