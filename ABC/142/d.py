
from fractions import gcd
import itertools
import sys
input = sys.stdin.readline


# nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# nの約数列挙
def divisor(n):
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass


# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


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
