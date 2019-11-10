import sys
from fractions import gcd
input = sys.stdin.readline

MOD = 10 ** 9 + 7


# a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    A, B, C, D = map(int, input().split())
    E = lcm(C, D)

    c_count = B // C - (A - 1) // C
    d_count = B // D - (A - 1) // D
    e_count = B // E - (A - 1) // E
    print((B - A + 1) - (c_count + d_count - e_count))


if __name__ == '__main__':
    main()
