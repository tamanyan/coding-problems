
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
    A, B = MI()
    S = input()

    if len(S) != A + B + 1:
        print('No')
        # print('1')
        return

    for i in range(len(S)):
        if i == A and S[i] != '-':
            print('No')
            # print('2')
            return
        elif i != A and S[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('No')
            # print('3', i, S[i])
            return

    print('Yes')


if __name__ == '__main__':
    main()
