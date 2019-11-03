import sys
input = sys.stdin.readline


def main():
    MOD = 2019
    L, R = map(int, input().split())
    # R = min(R, L+MOD*2)
    ans = MOD - 1

    if R - L >= 3000:
        print(0)
        return

    for i in range(L, R+1):
        for j in range(i+1, R+1):
            ans = min(ans, i*j % MOD)

    print(ans)


if __name__ == '__main__':
    main()
