
import sys
input = sys.stdin.readline


def main():
    INF = 10**9
    N, M = map(int, input().split())
    h = []
    dp = [INF for i in range(1 << N)]

    for i in range(M):
        a, b = map(int, input().split())
        s = 0
        for c in map(int, input().split()):
            c -= 1
            s |= 1 << c
        h.append((a, s))

    print(h)
    dp[0] = 0

    for s in range(1 << N):
        for i in range(M):
            t = s | h[i][1]
            cost = dp[s] + h[i][0]
            # print(bin(s), '->', bin(t), cost, h)
            dp[t] = min(dp[t], cost)

    print(dp[-1] if dp[-1] != INF else -1)


if __name__ == '__main__':
    main()
