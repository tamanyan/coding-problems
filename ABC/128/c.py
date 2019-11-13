import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    N, M = map(int, input().split())
    s = []
    mod = []
    ans = 0

    for i in range(M):
        t = list(map(int, input().split()))
        s.append(t[1:])

    mod = list(map(int, input().split()))

    for i in range(0, 2**N):
        switch = [0] * N
        for j in range(N):
            if ((i >> j) & 1):
                switch[j] = 1

        all = 0
        for i in range(M):
            li = s[i]
            total = 0
            for item in li:
                total += switch[item-1]

            if mod[i] != total % 2:
                break
            else:
                all += 1

        if all == M:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
