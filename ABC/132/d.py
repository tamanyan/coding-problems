import sys
import math
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def main():
    N, K = map(int, input().split())
    red = N - K
    blue = K

    for i in range(1, K+1):
        if i > red + 1:
            print(0)
        else:
            ans = cmb(red + 1, i)
            ans *= cmb(blue - 1, i - 1)
            print(ans % MOD)


if __name__ == '__main__':
    main()
