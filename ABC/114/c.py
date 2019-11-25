
import sys

input = sys.stdin.readline

# input = sys.stdin.readline
sys.setrecursionlimit(2147483647)


def main():
    N = int(input())
    number = str(N)
    L = len(number)
    dp = [[0 for i in range(2)] for j in range(L + 1)]

    dp[0][3] = 1
    dp[0][7] = 1
    dp[0][5] = 1

    for k in range(L):
        for m in [3, 7, 5]:
            dp[k+1][m] += dp[k][m]
            print(dp[k][m])

    print(dp)


if __name__ == '__main__':
    main()
