import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N

    for i in range(N):
        if i == 0:
            # A[N-1] == A[0] == A[1]
            # ans[0], ans[1]
            A[0] == ans[0] // 2 + ans[1] // 2
            A[1] == ans[1] // 2 + ans[2] // 2
            A[3] == ans[2] // 2 + ans[3] // 2
            # rain = min(A[0]*2, A[N-1]*2)
            # ans[0] = rain
            # A[0] -= rain // 2
            # A[N-1] -= rain // 2
        else:
            ans[i] = min(A[i]*2, A[i-1]*2)
            if A[i] - rain >= 0 and A[i-1] - rain >= 0:
                ans[i] = rain
                A[i] -= rain // 2
                A[i-1] -= rain // 2

    print(*ans)
    print(*A)


if __name__ == '__main__':
    main()
