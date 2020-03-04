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


def print_matrix(d):
    for i in range(len(d)):
        print(d[i])


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
    s = S()
    stack1 = []
    stack2 = []
    ans = []

    for i in range(len(s)):
        if s[i] == '(':
            stack1.append((i+1, s[i]))
        else:
            stack2.append((i+1, s[i]))

    min_bracket = min(len(stack1), len(stack2))
    for i in range(min_bracket, 0, -1):
        flag = True
        a = []
        for j in range(i):
            b1 = stack1[j][0]
            b2 = stack2[len(stack2) - j - 1][0]
            a.append(b1)
            a.append(b2)
            flag = flag and (b1 < b2)
            if flag is False:
                break
        if flag:
            ans.append((len(a), sorted(a)))
            break

    print(len(ans))

    if len(ans) > 0:
        for i in range(len(ans)):
            print(ans[i][0])
            print(*ans[i][1])
            # print([s[j-1] for j in ans[i][1]])



if __name__ == '__main__':
    main()
