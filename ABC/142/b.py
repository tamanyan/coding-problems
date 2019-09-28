def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        if A[i] >= K:
            ans += 1

    print(ans)

    # for i in range(N):
    #     A = list(map(int, input().split()))


if __name__ == '__main__':
    main()
