
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    L = [0] * N
    R = [0] * N

    for i in range(N):
        L[i], R[i] = map(input(), int)


if __name__ == '__main__':
    main()
