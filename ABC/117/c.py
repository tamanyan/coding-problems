IINF = 10 ** 18


def main():
    N, M = list(map(int, input().split()))
    X = list(map(int, input().split()))
    X = sorted(X)
    # left = -IINF
    # right = IINF

    # print(M, N)
    if M <= N:
        print(0)
        return
    else:
        L = []
        for i in range(M-1):
            L.append(X[i+1]-X[i])

        # print(L)

        L.sort()
        if N == 1:
            ans = sum(L)
            print(ans)
        else:
            ans = sum(L[0:-(N-1)])
            print(ans)

    # for i in range(N):
    #     if len(X) == 0:
    #         break
    #     elif i == 0:
    #         left = X[0]
    #         X.pop(0)
    #     elif i == 1:
    #         right = X[-1]
    #         X.pop(len(X)-1)
    #     else:
    #         if abs(X[1] - X[-1]) < abs(X[-2] - X[0]):
    #             left = X[0]
    #             X.pop(0)
    #         else:
    #             right = X[-1]
    #             X.pop(-1)

    # ans = 0
    # while len(X) > 0:
    #     # print(ans, X)
    #     if abs(left - X[0]) < abs(right - X[-1]):
    #         ans += abs(left - X[0])
    #         left = X[0]
    #         X.pop(0)
    #     else:
    #         ans += abs(right - X[-1])
    #         right = X[-1]
    #         X.pop(len(X)-1)
    #     # b = min(abs(left - X[0]), abs(right - X[-1]))
    #     # print(b, X)
    #     # print(abs(X[0] - X[-1]) + b)
    # print(ans)


if __name__ == '__main__':
    main()
