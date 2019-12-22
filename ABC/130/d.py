import sys
import bisect
from itertools import accumulate
input = sys.stdin.readline

# 累積和

def cumulative_sum(N, K, a):
    b = list(accumulate([0] + a))
    ans = 0

    for i in range(N, 0, -1):
        if b[i] >= K:
            s = b[i] - K
            x = bisect.bisect_right(b, s)
            ans += x

    print(ans)

# しゃくとり法

def two_pointer(N, K, a):
    ans = 0
    left = 0
    right = 0
    s = 0

    for left in range(0, N):
        while right < N and s + a[right] < K:
            s += a[right]
            right += 1
        ans += (N - 1) - right + 1
        s -= a[left]
        # print(left, right, ans)

    print(ans)


def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    two_pointer(N, K, a)


if __name__ == '__main__':
    main()
