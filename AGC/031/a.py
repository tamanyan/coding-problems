
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


def calc_next(N, S):
    dp = [[0 for i in range(26)] for i in range(N+1)]

    for i in range(N-1, -1, -1):
        for j in range(26):
            dp[i][j] = dp[i+1][j]
        dp[i][ord(S[i])-ord('a')] = i

    return dp


def main():
    N = int(input())
    S = input()
    a = [0 for i in range(26)]
    ans = 1

    for i in range(N):
        a[ord(S[i])-ord('a')] += 1

    for i in range(26):
        ans *= a[i] + 1
        ans %= MOD

    print(ans - 1)


if __name__ == '__main__':
    main()
