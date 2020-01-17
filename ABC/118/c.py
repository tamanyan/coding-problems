# N個の最大公約数
# ユークリッド互除法
# Check


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*b // gcd(a, b)


def good(A, N):
    # A = sorted(A)
    ans = A[0]
    # for i in range(1, N):
    #     ans = fractions.gcd(A[i], ans)
    for i in range(1, N):
        ans = lcm(ans, A[i])
    return ans


def my(A, N):
    A = sorted(A)

    while True:
        v = A[0]
        tmp = [v]
        for i in range(len(A)):
            if A[i] % v == 1:
                print(1)
                return
            if A[i] % v == 0:
                pass
            else:
                tmp.append(A[i] % v)

        if len(A) == 1:
            print(A[0])
            return

        A = sorted(tmp)
        # print(A)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    good(A, N)


if __name__ == '__main__':
    main()
