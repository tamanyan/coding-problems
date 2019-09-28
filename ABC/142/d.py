import math
import os
import sys
from fractions import gcd

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def divisor(n):
    """
    n の約数をリストで返す
    :param int n:
    :rtype: list of int
    """
    ret = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


def factorization(n):
    """
    素因数分解
    :param int n:
    :rtype: list of int
    """
    if n <= 1:
        return []

    ret = []
    while n > 2 and n % 2 == 0:
        ret.append(2)
        n //= 2
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            ret.append(i)
            n //= i
        else:
            i += 2
    ret.append(n)
    return ret


def is_prime(n):
    """
    nの素数判定
    :param int n:
    :rtype: Bool
    """
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def coprime(a, b):
    return gcd(a, b) == 1


def main():
    A, B = map(int, input().split())
    gcdab = gcd(A, B)
    cd = divisor(gcdab)
    # print(factorization(gcdab))
    # print(cd)
    # da = sorted(divisor(A))
    # db = sorted(divisor(B))
    # cd = []
    # for i in da:
    #     if i in db:
    #         cd.append(i)

    ans = 0

    for i in cd:
        if is_prime(i) or i == 1:
            ans += 1

    print(ans)

    # print(cd)
    # li = []
    # # c = itertools.combinations(cd, 2)
    # for i in cd:
    #     if i == 1:
    #         li.append(i)
    #         continue

    #     flg = True
    #     for c in li:
    #         if not coprime(i, c):
    #             flg = False

    #     if flg:
    #         li.append(i)

    # # print(li)
    # print(len(li))


if __name__ == '__main__':
    main()
