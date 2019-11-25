INF = float("inf")
IINF = 10 ** 18
MOD = 998244353


def main():
    M = int(input())
    N = 0
    S = 0

    for i in range(M):
        d, c = list(map(int, input().split()))

        if d == 0 and i == 0:
            continue

        S += d * c
        N += c

    print((N - 1) + (S - 1) // 9)


if __name__ == '__main__':
    main()
