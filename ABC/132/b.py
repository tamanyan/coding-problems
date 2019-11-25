import sys
import math
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0

    for i in range(N-2):
        if (p[i+1] > p[i+2] and p[i+1] < p[i]) or (p[i+1] < p[i+2] and p[i+1] > p[i]):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
