import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = [0] * N
    S = sum(A)
    X[0] = S - 2 * sum([A[i] for i in range(N) if i % 2 == 1])
    A[0] -= X[0] // 2
    A[N-1] -= X[0] // 2

    for i in range(1, N):
        X[i] = A[i-1] * 2
        A[i-1] -= X[i] // 2
        A[i] -= X[i] // 2

    print(*X)
    # print(*A)


if __name__ == '__main__':
    main()
