
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    a = int(input())
    s = input()

    if a >= 3200:
        print(s)
    else:
        print('red')


if __name__ == '__main__':
    main()
