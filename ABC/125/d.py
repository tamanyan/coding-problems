import math

INF = float("inf")

# Check

def good(N, A):
    even = 0
    zero = 0
    c = 0

    ans = 0
    for i in A:
        if i < 0:
            c += 1
        elif i == 0:
            even = 0
            c = 0
        else:
            if c % 2 != 0:
                even += 1
            c = 0
        ans += abs(i)

    if c != 0 and c % 2 != 0:
        even += 1

    if even % 2 == 0:
        print(ans)
    else:
        print(ans - min([abs(i) for i in A if abs(i) > 0]) * 2)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0 for i in range(2)] for i in range(N+1)]

    dp[0][0] = 0
    dp[0][1] = -INF

    for i in range(N):
        dp[i+1][0] = max(dp[i][0] + A[i], dp[i][1] - A[i])
        dp[i+1][1] = max(dp[i][0] - A[i], dp[i][1] + A[i])

    print(dp[N][0])
    # good(N, A)


if __name__ == '__main__':
    main()
