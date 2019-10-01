
MOD = 10**9 + 7


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a0 = 0

    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                a0 += 1

    a1 = 0
    A2 = A * 2
    for i in range(N*2):
        for j in range(i+1, N*2):
            if A2[i] > A2[j]:
                a1 += 1

    a2 = 0
    A3 = A * 3
    for i in range(N*3):
        for j in range(i+1, N*3):
            if A3[i] > A3[j]:
                a2 += 1

    d = (a2 - a1) - (a1 - a0)
    # d * K + a0
    # print(d)
    print((a0 + d * ((K * (K - 1)) // 2) + (K - 1) * a0) % MOD)


if __name__ == '__main__':
    main()
