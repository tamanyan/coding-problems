
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    v = list(map(int, input().split()))
    v = sorted(v)
    # print(v)

    s = (v[0] + v[1]) / 2
    for i in range(2, N):
        s += v[i]
        s /= 2

    print(s)




if __name__ == '__main__':
    main()
