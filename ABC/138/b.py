
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))

    a = 0.0
    for i in range(N):
        a += 1 / float(A[i])
    print(1.0/a)


if __name__ == '__main__':
    main()
