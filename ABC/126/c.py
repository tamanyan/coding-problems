import sys
import math
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    N, K = map(int, input().split())
    ans = 0.0

    for i in range(1, N+1):
        c = 0
        if i < K:
            c = math.ceil(math.log(K, 2) - math.log(i, 2))
        # print(i, c, (1.0 / (2 ** c)), 1.0/N)
        ans += (1.0 / (2 ** c)) * 1.0/N

    print(ans)


if __name__ == '__main__':
    main()
