import sys
input = sys.stdin.readline


def distance(X1, X2):
    r = 0
    for i in range(len(X1)):
        r += (X1[i] - X2[i]) ** 2
    return r ** 0.5


def main():
    N, D = map(int, input().split())
    X = [None for i in range(N)]

    for i in range(N):
        X[i] = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            r = distance(X[i], X[j])
            if r.is_integer():
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
