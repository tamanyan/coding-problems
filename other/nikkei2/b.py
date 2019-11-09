INF = float("inf")
IINF = 10 ** 18
MOD = 998244353


def main():
    N = int(input())
    d = list(map(int, input().split()))
    # d = sorted(d)

    distance = [0] * (max(d) + 1)

    for _d in d:
        distance[_d] += 1

    if d[0] != 0 or distance[0] != 1:
        print(0)
        return

    ans = 1
    for i in range(1, len(distance)):
        n = distance[i-1]
        r = distance[i]
        ans = ans * n ** r
        ans = ans % MOD
        # print(ans)

    print(ans % MOD)


if __name__ == '__main__':
    main()
